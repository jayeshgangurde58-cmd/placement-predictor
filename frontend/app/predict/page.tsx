"use client";

import { useState, useCallback } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import { predictPlacement, PredictResponse, parseResume } from "@/lib/api";
import { savePrediction } from "@/lib/firestore";
import { motion, AnimatePresence } from "framer-motion";
import toast from "react-hot-toast";
import { useDropzone } from "react-dropzone";
import {
  RadialBarChart, RadialBar, ResponsiveContainer,
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Cell,
} from "recharts";
import { BrainCircuit, CheckCircle, XCircle, Info, Sparkles, Upload, FileText } from "lucide-react";

interface SliderFieldProps {
  id: string;
  label: string;
  value: number;
  min: number; max: number; step: number;
  unit?: string;
  onChange: (v: number) => void;
  description: string;
}

function SliderField({ id, label, value, min, max, step, unit = "", onChange, description }: SliderFieldProps) {
  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 10 }}>
        <label htmlFor={id} className="form-label" style={{ marginBottom: 0 }}>{label}</label>
        <span style={{ fontWeight: 700, color: "#a78bfa", fontSize: "1rem" }}>{value}{unit}</span>
      </div>
      <input id={id} type="range" min={min} max={max} step={step}
        value={value} onChange={e => onChange(Number(e.target.value))} />
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 4, fontSize: "0.72rem", color: "#475569" }}>
        <span>{min}{unit}</span>
        <span style={{ color: "#64748b" }}>{description}</span>
        <span>{max}{unit}</span>
      </div>
    </div>
  );
}

function GaugeChart({ value }: { value: number }) {
  const color = value >= 70 ? "#4ade80" : value >= 45 ? "#fbbf24" : "#f87171";
  const data = [{ value: 100, fill: "rgba(139,92,246,0.1)" }, { value, fill: color }];
  return (
    <div style={{ position: "relative", width: 200, height: 200 }}>
      <ResponsiveContainer width="100%" height="100%">
        <RadialBarChart innerRadius="55%" outerRadius="100%" data={data} startAngle={225} endAngle={-45}>
          <RadialBar dataKey="value" cornerRadius={8} background={false} />
        </RadialBarChart>
      </ResponsiveContainer>
      <div style={{
        position: "absolute", inset: 0, display: "flex", flexDirection: "column",
        alignItems: "center", justifyContent: "center",
      }}>
        <span style={{ fontSize: "2.4rem", fontWeight: 900, color }}>{value}%</span>
        <span style={{ fontSize: "0.75rem", color: "#64748b", fontWeight: 600 }}>Probability</span>
      </div>
    </div>
  );
}

export default function PredictPage() {
  const { user } = useAuth();
  const [formData, setFormData] = useState({
    cgpa: 7.0, aptitude: 65, programming: 60,
    communication: 60, tenth_percentage: 85, twelfth_percentage: 88,
    projects: 2, internships: 1,
  });
  const [result, setResult] = useState<PredictResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [resumeLoading, setResumeLoading] = useState(false);
  const [extractedSkills, setExtractedSkills] = useState<string[]>([]);
  const [activeTab, setActiveTab] = useState<"form" | "resume">("form");

  const set = (key: keyof typeof formData) => (v: number) =>
    setFormData(prev => ({ ...prev, [key]: v }));

  // Resume parsing
  const onDrop = useCallback(async (files: File[]) => {
    const file = files[0];
    if (!file) return;
    setResumeLoading(true);
    try {
      const r = await parseResume(file);
      setExtractedSkills(r.extracted_skills);
      toast.success(`Extracted ${r.count} skills from resume!`);
    } catch {
      toast.error("Resume parsing failed. Is the backend running?");
    } finally { setResumeLoading(false); }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "application/pdf": [".pdf"] },
    maxFiles: 1,
  });

  // Estimate scores from skills
  const estimateScoresFromSkills = () => {
    const skillsLower = extractedSkills.map(s => s.toLowerCase());
    
    const programmingKeywords = ["python", "java", "javascript", "c++", "c#", "go", "rust", "typescript", "react", "angular", "vue", "node", "express", "django", "flask", "sql", "database"];
    const communicationKeywords = ["presentation", "communication", "leadership", "management", "collaboration", "teamwork"];
    const projectKeywords = ["project", "github", "gitlab", "repository", "developed", "built", "created"];
    const internshipKeywords = ["internship", "intern", "experience", "worked", "employed", "job", "company"];
    
    const programmingCount = skillsLower.filter(s => programmingKeywords.some(k => s.includes(k))).length;
    const communicationCount = skillsLower.filter(s => communicationKeywords.some(k => s.includes(k))).length;
    const projectCount = skillsLower.filter(s => projectKeywords.some(k => s.includes(k))).length;
    const internshipCount = skillsLower.filter(s => internshipKeywords.some(k => s.includes(k))).length;
    
    return {
      cgpa: Math.min(10, 6.5 + (extractedSkills.length / 20)),
      aptitude: Math.min(100, 50 + (extractedSkills.length * 1.5)),
      programming: Math.min(100, 40 + (programmingCount * 10)),
      communication: Math.min(100, 50 + (communicationCount * 15)),
      tenth_percentage: Math.min(100, 65 + (extractedSkills.length * 1.2)),
      twelfth_percentage: Math.min(100, 68 + (extractedSkills.length * 1.1)),
      projects: Math.min(15, Math.max(1, projectCount)),
      internships: Math.min(5, Math.max(1, internshipCount)),
    };
  };

  const handleResumePredict = async () => {
    if (extractedSkills.length === 0) { toast.error("Upload a resume first"); return; }
    const estimatedScores = estimateScoresFromSkills();
    setFormData(estimatedScores);
    setLoading(true);
    try {
      const res = await predictPlacement(estimatedScores);
      setResult(res);
      if (user) {
        await savePrediction(user.uid, { input: estimatedScores, result: res, source: "resume" });
      }
      toast.success("Resume-based prediction complete!");
    } catch (err: any) {
      toast.error(err.message || "Prediction failed. Is the backend running?");
    } finally { setLoading(false); }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await predictPlacement(formData);
      setResult(res);
      if (user) {
        await savePrediction(user.uid, { input: formData, result: res });
      }
      toast.success("Prediction complete!");
    } catch (err: any) {
      toast.error(err.message || "Prediction failed. Is the backend running?");
    } finally { setLoading(false); }
  };

  const fiColors = ["#8b5cf6", "#818cf8", "#38bdf8", "#4ade80", "#fbbf24", "#fb923c"];

  return (
    <ProtectedRoute>
      <AppLayout>
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }}>
          <div style={{ marginBottom: 32 }}>
            <h1 style={{ fontSize: "1.8rem", fontWeight: 800, margin: 0 }}>
              <span className="gradient-text">Placement Predictor</span>
            </h1>
            <p style={{ color: "#64748b", marginTop: 6 }}>
              Fill in your profile details and get an AI-powered placement probability score
            </p>
          </div>
        </motion.div>

        {/* Tab Buttons */}
        <div style={{ display: "flex", gap: 12, marginBottom: 24, borderBottom: "1px solid rgba(139,92,246,0.2)", paddingBottom: 16 }}>
          <button onClick={() => { setActiveTab("form"); setResult(null); }}
            style={{
              padding: "8px 16px", background: activeTab === "form" ? "rgba(139,92,246,0.2)" : "transparent",
              border: "1px solid " + (activeTab === "form" ? "rgba(139,92,246,0.4)" : "transparent"),
              borderRadius: 8, color: activeTab === "form" ? "#a78bfa" : "#64748b", cursor: "pointer", fontWeight: 600, fontSize: "0.9rem",
            }}>
            Manual Input
          </button>
          <button onClick={() => { setActiveTab("resume"); setResult(null); }}
            style={{
              padding: "8px 16px", background: activeTab === "resume" ? "rgba(139,92,246,0.2)" : "transparent",
              border: "1px solid " + (activeTab === "resume" ? "rgba(139,92,246,0.4)" : "transparent"),
              borderRadius: 8, color: activeTab === "resume" ? "#a78bfa" : "#64748b", cursor: "pointer", fontWeight: 600, fontSize: "0.9rem",
            }}>
            Upload Resume
          </button>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: result ? "1fr 1fr" : "1fr", gap: 28, transition: "all 0.4s" }}>
          {/* Form */}
          {activeTab === "form" && (
          <motion.div layout className="glass-card" style={{ padding: 32 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 28 }}>
              <BrainCircuit size={22} color="#a78bfa" />
              <h2 style={{ margin: 0, fontSize: "1.1rem", fontWeight: 700, color: "#e2e8f0" }}>Your Profile</h2>
            </div>
            <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 28 }}>
              <SliderField id="pred-cgpa" label="CGPA" value={formData.cgpa} min={4} max={10} step={0.1}
                onChange={set("cgpa")} description="Your current GPA" />
              <SliderField id="pred-aptitude" label="Aptitude Score" value={formData.aptitude} min={0} max={100} step={1}
                unit="%" onChange={set("aptitude")} description="Logical & quantitative" />
              <SliderField id="pred-programming" label="Programming Skills" value={formData.programming} min={0} max={100} step={1}
                unit="%" onChange={set("programming")} description="Coding proficiency" />
              <SliderField id="pred-communication" label="Communication Skills" value={formData.communication} min={0} max={100} step={1}
                unit="%" onChange={set("communication")} description="Verbal & written" />
              <SliderField id="pred-10th" label="10th Percentage" value={formData.tenth_percentage} min={0} max={100} step={1}
                unit="%" onChange={set("tenth_percentage")} description="Board exam score" />
              <SliderField id="pred-12th" label="12th Percentage" value={formData.twelfth_percentage} min={0} max={100} step={1}
                unit="%" onChange={set("twelfth_percentage")} description="Board exam score" />
              <SliderField id="pred-projects" label="Projects Completed" value={formData.projects} min={0} max={15} step={1}
                onChange={set("projects")} description="GitHub / academic" />
              <SliderField id="pred-internships" label="Internships" value={formData.internships} min={0} max={5} step={1}
                onChange={set("internships")} description="Industrial experience" />

              <button id="predict-submit" type="submit" className="btn-primary" disabled={loading} style={{ marginTop: 8 }}>
                {loading
                  ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Analyzing...</>
                  : <><Sparkles size={17} /> Predict My Placement</>
                }
              </button>
            </form>
          </motion.div>
          )}

          {/* Resume Upload */}
          {activeTab === "resume" && (
          <motion.div layout className="glass-card" style={{ padding: 32 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 28 }}>
              <FileText size={22} color="#a78bfa" />
              <h2 style={{ margin: 0, fontSize: "1.1rem", fontWeight: 700, color: "#e2e8f0" }}>Resume-Based Prediction</h2>
            </div>

            {/* Resume Upload Area */}
            <div style={{ marginBottom: 28 }}>
              <div {...getRootProps()} className={`drop-zone ${isDragActive ? "active" : ""}`}>
                <input {...getInputProps()} id="resume-upload" />
                {resumeLoading
                  ? <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 8 }}>
                      <span className="spinner" style={{ width: 20, height: 20, borderWidth: 2 }} />
                      <span style={{ color: "#64748b", fontSize: "0.85rem" }}>Extracting skills…</span>
                    </div>
                  : <>
                      <Upload size={32} color="#475569" style={{ margin: "0 auto 12px" }} />
                      <p style={{ color: "#64748b", fontSize: "0.9rem", margin: 0, fontWeight: 600 }}>
                        {isDragActive ? "Drop your PDF here" : "Drag & drop or click to upload PDF"}
                      </p>
                      <p style={{ color: "#374151", fontSize: "0.8rem", marginTop: 6 }}>
                        Skills extracted automatically via NLP
                      </p>
                    </>
                }
              </div>
            </div>

            {/* Extracted Skills */}
            {extractedSkills.length > 0 && (
              <div style={{ marginBottom: 24 }}>
                <h3 style={{ fontSize: "0.95rem", fontWeight: 700, color: "#e2e8f0", marginBottom: 12 }}>
                  Extracted Skills ({extractedSkills.length})
                </h3>
                <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                  {extractedSkills.map(skill => (
                    <span key={skill} className="badge badge-purple" style={{ fontSize: "0.8rem", padding: "6px 12px" }}>
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Estimated Scores Preview */}
            {extractedSkills.length > 0 && (
              <div style={{ background: "rgba(139,92,246,0.08)", border: "1px solid rgba(139,92,246,0.2)", borderRadius: 12, padding: 16, marginBottom: 24 }}>
                <h4 style={{ fontSize: "0.85rem", fontWeight: 700, color: "#a78bfa", margin: "0 0 12px" }}>
                  📊 Estimated Profile (based on skills)
                </h4>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 12, fontSize: "0.8rem" }}>
                  <div><span style={{ color: "#94a3b8" }}>CGPA</span><br /><span style={{ color: "#4ade80", fontWeight: 700 }}>{estimateScoresFromSkills().cgpa.toFixed(2)}</span></div>
                  <div><span style={{ color: "#94a3b8" }}>Programming</span><br /><span style={{ color: "#4ade80", fontWeight: 700 }}>{Math.round(estimateScoresFromSkills().programming)}%</span></div>
                  <div><span style={{ color: "#94a3b8" }}>Communication</span><br /><span style={{ color: "#4ade80", fontWeight: 700 }}>{Math.round(estimateScoresFromSkills().communication)}%</span></div>
                </div>
              </div>
            )}

            <button id="predict-resume-submit" onClick={handleResumePredict} className="btn-primary"
              disabled={loading || extractedSkills.length === 0} style={{ width: "100%" }}>
              {loading
                ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Analyzing…</>
                : <><Sparkles size={17} /> Predict from Resume</>
              }
            </button>
          </motion.div>
          )}

          {/* Results */}
          <AnimatePresence>
            {result && (
              <motion.div
                key="result"
                initial={{ opacity: 0, x: 30 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 30 }}
                transition={{ duration: 0.4 }}
                style={{ display: "flex", flexDirection: "column", gap: 20 }}
              >
                {/* Gauge */}
                <div className="glass-card animate-pulse-glow" style={{ padding: 32, textAlign: "center" }}>
                  <h2 style={{ margin: "0 0 20px", fontSize: "1.05rem", fontWeight: 700, color: "#e2e8f0" }}>
                    Placement Probability
                  </h2>
                  <div style={{ display: "flex", justifyContent: "center", marginBottom: 20 }}>
                    <GaugeChart value={Math.round(result.probability)} />
                  </div>
                  <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 8 }}>
                    {result.placed
                      ? <><CheckCircle size={18} color="#4ade80" /><span style={{ color: "#4ade80", fontWeight: 700 }}>Likely to be Placed!</span></>
                      : <><XCircle size={18} color="#f87171" /><span style={{ color: "#f87171", fontWeight: 700 }}>Needs Improvement</span></>
                    }
                  </div>
                  <div style={{ marginTop: 12 }}>
                    <span className="badge badge-purple">Confidence: {result.confidence}</span>
                  </div>
                </div>

                {/* Minimum Requirements Warning */}
                {result.explanation && (
                  <div className="glass-card" style={{ padding: 20, border: "1px solid rgba(248, 113, 113, 0.3)", background: "rgba(248, 113, 113, 0.08)" }}>
                    <div style={{ display: "flex", alignItems: "flex-start", gap: 12 }}>
                      <XCircle size={18} color="#f87171" style={{ marginTop: 2, flexShrink: 0 }} />
                      <div>
                        <h4 style={{ margin: "0 0 8px", fontSize: "0.9rem", fontWeight: 700, color: "#f87171" }}>
                          Minimum Requirements Not Met
                        </h4>
                        <p style={{ margin: "0 0 12px", fontSize: "0.85rem", color: "#fb7185" }}>
                          {result.explanation}
                        </p>
                        <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: 10, fontSize: "0.8rem" }}>
                          {result.min_requirements && (
                            <>
                              <div style={{ background: "rgba(248, 113, 113, 0.1)", padding: 8, borderRadius: 6 }}>
                                <span style={{ color: "#94a3b8" }}>Min CGPA:</span>
                                <br />
                                <span style={{ color: "#f87171", fontWeight: 700 }}>{result.min_requirements.cgpa}</span>
                              </div>
                              <div style={{ background: "rgba(248, 113, 113, 0.1)", padding: 8, borderRadius: 6 }}>
                                <span style={{ color: "#94a3b8" }}>Min Aptitude:</span>
                                <br />
                                <span style={{ color: "#f87171", fontWeight: 700 }}>{result.min_requirements.aptitude}%</span>
                              </div>
                              <div style={{ background: "rgba(248, 113, 113, 0.1)", padding: 8, borderRadius: 6 }}>
                                <span style={{ color: "#94a3b8" }}>Min Programming:</span>
                                <br />
                                <span style={{ color: "#f87171", fontWeight: 700 }}>{result.min_requirements.programming}%</span>
                              </div>
                              <div style={{ background: "rgba(248, 113, 113, 0.1)", padding: 8, borderRadius: 6 }}>
                                <span style={{ color: "#94a3b8" }}>Min Communication:</span>
                                <br />
                                <span style={{ color: "#f87171", fontWeight: 700 }}>{result.min_requirements.communication}%</span>
                              </div>
                              <div style={{ background: "rgba(248, 113, 113, 0.1)", padding: 8, borderRadius: 6 }}>
                                <span style={{ color: "#94a3b8" }}>Min 10th %:</span>
                                <br />
                                <span style={{ color: "#f87171", fontWeight: 700 }}>{result.min_requirements.tenth_percentage}%</span>
                              </div>
                              <div style={{ background: "rgba(248, 113, 113, 0.1)", padding: 8, borderRadius: 6 }}>
                                <span style={{ color: "#94a3b8" }}>Min 12th %:</span>
                                <br />
                                <span style={{ color: "#f87171", fontWeight: 700 }}>{result.min_requirements.twelfth_percentage}%</span>
                              </div>
                            </>
                          )}
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* Minimum Requirements Info (for qualified candidates) */}
                {!result.explanation && result.min_requirements && (
                  <div className="glass-card" style={{ padding: 16, border: "1px solid rgba(74, 222, 128, 0.2)", background: "rgba(74, 222, 128, 0.05)" }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 12 }}>
                      <CheckCircle size={16} color="#4ade80" />
                      <h4 style={{ margin: 0, fontSize: "0.85rem", fontWeight: 700, color: "#4ade80" }}>
                        ✓ Meets All Minimum Requirements
                      </h4>
                    </div>
                    <div style={{ display: "grid", gridTemplateColumns: "repeat(3, minmax(0, 1fr))", gap: 8, fontSize: "0.75rem" }}>
                      <div><span style={{ color: "#94a3b8" }}>CGPA</span><br /><span style={{ color: "#a78bfa", fontWeight: 700 }}>≥ {result.min_requirements.cgpa}</span></div>
                      <div><span style={{ color: "#94a3b8" }}>Aptitude</span><br /><span style={{ color: "#a78bfa", fontWeight: 700 }}>≥ {result.min_requirements.aptitude}%</span></div>
                      <div><span style={{ color: "#94a3b8" }}>Programming</span><br /><span style={{ color: "#a78bfa", fontWeight: 700 }}>≥ {result.min_requirements.programming}%</span></div>
                      <div><span style={{ color: "#94a3b8" }}>Communication</span><br /><span style={{ color: "#a78bfa", fontWeight: 700 }}>≥ {result.min_requirements.communication}%</span></div>
                      <div><span style={{ color: "#94a3b8" }}>10th %</span><br /><span style={{ color: "#a78bfa", fontWeight: 700 }}>≥ {result.min_requirements.tenth_percentage}%</span></div>
                      <div><span style={{ color: "#94a3b8" }}>12th %</span><br /><span style={{ color: "#a78bfa", fontWeight: 700 }}>≥ {result.min_requirements.twelfth_percentage}%</span></div>
                    </div>
                  </div>
                )}

                {/* Feature Importance */}
                <div className="glass-card" style={{ padding: 24 }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 18 }}>
                    <Info size={17} color="#a78bfa" />
                    <h3 style={{ margin: 0, fontSize: "0.95rem", fontWeight: 700, color: "#e2e8f0" }}>
                      What Drives Your Score
                    </h3>
                  </div>
                  <ResponsiveContainer width="100%" height={220}>
                    <BarChart data={result.feature_importance} layout="vertical" margin={{ left: 10 }}>
                      <CartesianGrid strokeDasharray="3 3" horizontal={false} />
                      <XAxis type="number" domain={[0, 40]} tick={{ fontSize: 11 }} unit="%" />
                      <YAxis type="category" dataKey="factor" tick={{ fontSize: 11 }} width={110} />
                      <Tooltip formatter={(v: any) => [`${v}%`, "Contribution"]} />
                      <Bar dataKey="contribution" radius={[0, 6, 6, 0]}>
                        {result.feature_importance.map((_, i) => (
                          <Cell key={i} fill={fiColors[i % fiColors.length]} />
                        ))}
                      </Bar>
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                {/* Tips */}
                <div className="glass-card" style={{ padding: 20 }}>
                  <h3 style={{ margin: "0 0 12px", fontSize: "0.9rem", fontWeight: 700, color: "#e2e8f0" }}>
                    💡 Improvement Tips
                  </h3>
                  {result.probability < 70 && (
                    <ul style={{ margin: 0, paddingLeft: 18, color: "#94a3b8", fontSize: "0.85rem", lineHeight: 1.8 }}>
                      {result.probability < 50 && <li>Focus on increasing your programming score through daily coding practice</li>}
                      {formData.projects < 3 && <li>Build 2–3 more projects to demonstrate practical skills</li>}
                      {formData.internships === 0 && <li>Apply for internships — even short ones significantly boost placement odds</li>}
                      {formData.communication < 60 && <li>Work on communication skills through mock interviews and GD practice</li>}
                    </ul>
                  )}
                  {result.probability >= 70 && (
                    <p style={{ color: "#4ade80", fontSize: "0.87rem", margin: 0 }}>
                      🎉 Great profile! Keep it up and target top companies. Consider premium certifications to stand out further.
                    </p>
                  )}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </AppLayout>
    </ProtectedRoute>
  );
}
