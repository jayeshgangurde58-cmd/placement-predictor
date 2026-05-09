"use client";

import { useState, useEffect, useCallback } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import { analyzeSkillGap, getAvailableRoles, parseResume, SkillGapResponse } from "@/lib/api";
import { saveSkillAnalysis } from "@/lib/firestore";
import { motion, AnimatePresence } from "framer-motion";
import toast from "react-hot-toast";
import { useDropzone } from "react-dropzone";
import {
  RadarChart, Radar, PolarGrid, PolarAngleAxis, ResponsiveContainer,
} from "recharts";
import { Search, Upload, Plus, X, BookOpen, ExternalLink, Target, AlertTriangle, CheckCircle, Book, Briefcase } from "lucide-react";
import CourseCard from "@/components/CourseCard";

export default function SkillGapPage() {
  const { user } = useAuth();
  const [roles, setRoles] = useState<string[]>([]);
  const [targetRole, setTargetRole] = useState("Web Developer");
  const [skills, setSkills] = useState<string[]>([]);
  const [inputSkill, setInputSkill] = useState("");
  const [result, setResult] = useState<SkillGapResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [resumeLoading, setResumeLoading] = useState(false);

  useEffect(() => {
    getAvailableRoles().then(r => setRoles(r.roles)).catch(() => {});
  }, []);

  const addSkill = () => {
    const s = inputSkill.trim();
    if (s && !skills.includes(s)) {
      setSkills(prev => [...prev, s]);
    }
    setInputSkill("");
  };

  const removeSkill = (s: string) => setSkills(prev => prev.filter(x => x !== s));

  const onDrop = useCallback(async (files: File[]) => {
    const file = files[0];
    if (!file) return;
    setResumeLoading(true);
    try {
      const r = await parseResume(file);
      setSkills(prev => Array.from(new Set([...prev, ...r.extracted_skills])));
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

  const handleAnalyze = async () => {
    if (skills.length === 0) { toast.error("Add at least one skill"); return; }
    setLoading(true);
    try {
      const res = await analyzeSkillGap({ skills, target_role: targetRole });
      setResult(res);
      if (user) {
        await saveSkillAnalysis(user.uid, {
          input: { skills, target_role: targetRole },
          result: res,
        });
      }
      toast.success("Skill gap analysis complete!");
    } catch (err: any) {
      toast.error(err.message || "Analysis failed. Is the backend running?");
    } finally { setLoading(false); }
  };

  const radarData = result?.radar_data?.slice(0, 8).map(d => ({
    skill: d.skill.length > 10 ? d.skill.slice(0, 10) + "…" : d.skill,
    You: d.has * 100,
    Required: 100,
  })) || [];

  return (
    <ProtectedRoute>
      <AppLayout>
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }}>
          <div style={{ marginBottom: 32 }}>
            <h1 style={{ fontSize: "1.8rem", fontWeight: 800, margin: 0 }}>
              <span className="gradient-text">Skill Gap Analyzer</span>
            </h1>
            <p style={{ color: "#64748b", marginTop: 6 }}>
              Compare your skills against job roles and get personalized learning recommendations
            </p>
          </div>
        </motion.div>

        <div style={{ display: "grid", gridTemplateColumns: "420px 1fr", gap: 28, alignItems: "start" }}>
          {/* Left Panel */}
          <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
            {/* Role Select */}
            <div className="glass-card" style={{ padding: 24 }}>
              <label className="form-label" htmlFor="role-select">Target Job Role</label>
              <select id="role-select" className="form-input" value={targetRole}
                onChange={e => setTargetRole(e.target.value)}>
                {roles.length > 0
                  ? roles.map(r => <option key={r} value={r}>{r}</option>)
                  : [
                      "Software Engineer",
                      "Web Developer",
                      "Data Scientist",
                      "DevOps Engineer",
                      "Machine Learning Engineer",
                      "Cloud Engineer",
                      "Cybersecurity Analyst",
                      "Embedded Systems Engineer",
                      "Mechanical Engineer",
                      "Electrical Engineer",
                      "Civil Engineer",
                      "Industrial Engineer"
                    ].map(r => <option key={r} value={r}>{r}</option>)
                }
              </select>
            </div>

            {/* Resume Upload */}
            <div className="glass-card" style={{ padding: 24 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 16 }}>
                <Upload size={17} color="#a78bfa" />
                <h3 style={{ margin: 0, fontSize: "0.95rem", fontWeight: 700, color: "#e2e8f0" }}>
                  Upload Resume (PDF)
                </h3>
              </div>
              <div {...getRootProps()} className={`drop-zone ${isDragActive ? "active" : ""}`}>
                <input {...getInputProps()} id="resume-upload" />
                {resumeLoading
                  ? <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 8 }}>
                      <span className="spinner" style={{ width: 20, height: 20, borderWidth: 2 }} />
                      <span style={{ color: "#64748b", fontSize: "0.85rem" }}>Extracting skills…</span>
                    </div>
                  : <>
                      <Upload size={28} color="#475569" style={{ margin: "0 auto 10px" }} />
                      <p style={{ color: "#64748b", fontSize: "0.85rem", margin: 0 }}>
                        {isDragActive ? "Drop your PDF here" : "Drag & drop or click to upload PDF"}
                      </p>
                      <p style={{ color: "#374151", fontSize: "0.75rem", marginTop: 4 }}>
                        Skills extracted automatically via NLP
                      </p>
                    </>
                }
              </div>
            </div>

            {/* Manual Skills */}
            <div className="glass-card" style={{ padding: 24 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 16 }}>
                <Plus size={17} color="#a78bfa" />
                <h3 style={{ margin: 0, fontSize: "0.95rem", fontWeight: 700, color: "#e2e8f0" }}>
                  Add Skills Manually
                </h3>
              </div>
              <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
                <input id="skill-input" className="form-input" style={{ flex: 1 }}
                  placeholder="e.g. Python, React, SQL…"
                  value={inputSkill}
                  onChange={e => setInputSkill(e.target.value)}
                  onKeyDown={e => { if (e.key === "Enter") { e.preventDefault(); addSkill(); } }}
                />
                <button onClick={addSkill} className="btn-secondary" style={{ padding: "10px 16px", flexShrink: 0 }}>
                  <Plus size={16} />
                </button>
              </div>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8, minHeight: 40 }}>
                {skills.map(s => (
                  <motion.div key={s} initial={{ scale: 0.7 }} animate={{ scale: 1 }}
                    style={{
                      display: "flex", alignItems: "center", gap: 6, padding: "5px 12px",
                      background: "rgba(139,92,246,0.15)", border: "1px solid rgba(139,92,246,0.3)",
                      borderRadius: 20, fontSize: "0.8rem", color: "#a78bfa", fontWeight: 600,
                    }}
                  >
                    {s}
                    <button onClick={() => removeSkill(s)}
                      style={{ background: "none", border: "none", cursor: "pointer", color: "#6b7280", display: "flex", padding: 0 }}>
                      <X size={13} />
                    </button>
                  </motion.div>
                ))}
                {skills.length === 0 && (
                  <span style={{ color: "#374151", fontSize: "0.8rem" }}>No skills added yet</span>
                )}
              </div>

              <button id="analyze-gap" onClick={handleAnalyze} className="btn-primary"
                disabled={loading || skills.length === 0} style={{ width: "100%", marginTop: 20 }}>
                {loading
                  ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Analyzing…</>
                  : <><Search size={17} /> Analyze Skill Gap</>
                }
              </button>
            </div>
          </div>

          {/* Results Panel */}
          <AnimatePresence>
            {result ? (
              <motion.div key="result" initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }}
                style={{ display: "flex", flexDirection: "column", gap: 20 }}>

                {/* Summary */}
                <div className="glass-card" style={{ padding: 24 }}>
                  <h2 style={{ margin: "0 0 20px", fontSize: "1.05rem", fontWeight: 700, color: "#e2e8f0" }}>
                    Analysis for <span style={{ color: "#a78bfa" }}>{result.target_role}</span>
                  </h2>
                  <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 16, marginBottom: 20 }}>
                    {[
                      { label: "Match Rate", value: `${result.match_rate}%`, color: result.match_rate >= 70 ? "#4ade80" : result.match_rate >= 40 ? "#fbbf24" : "#f87171" },
                      { label: "Skill Gap Index", value: result.skill_gap_index.toFixed(2), color: "#a78bfa" },
                      { label: "Missing Skills", value: result.total_missing, color: "#fb923c" },
                    ].map(({ label, value, color }) => (
                      <div key={label} style={{ textAlign: "center", padding: "16px 8px", background: "rgba(139,92,246,0.07)", borderRadius: 12, border: "1px solid rgba(139,92,246,0.12)" }}>
                        <div style={{ fontSize: "1.6rem", fontWeight: 800, color }}>{value}</div>
                        <div style={{ fontSize: "0.73rem", color: "#64748b", marginTop: 4, fontWeight: 600, textTransform: "uppercase", letterSpacing: "0.04em" }}>{label}</div>
                      </div>
                    ))}
                  </div>
                  {/* Progress bar */}
                  <div style={{ marginBottom: 6, display: "flex", justifyContent: "space-between", fontSize: "0.8rem", color: "#64748b" }}>
                    <span>Skills matched: {result.total_matched}/{result.total_required}</span>
                    <span>{result.match_rate}%</span>
                  </div>
                  <div className="progress-bar-track">
                    <motion.div className="progress-bar-fill"
                      initial={{ width: 0 }} animate={{ width: `${result.match_rate}%` }}
                      transition={{ duration: 0.8, ease: "easeOut" }} />
                  </div>
                </div>

                {/* Radar + Skills */}
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
                  {/* Radar Chart */}
                  {radarData.length > 0 && (
                    <div className="glass-card" style={{ padding: 24 }}>
                      <h3 style={{ margin: "0 0 16px", fontSize: "0.9rem", fontWeight: 700, color: "#e2e8f0" }}>Skill Radar</h3>
                      <ResponsiveContainer width="100%" height={220}>
                        <RadarChart data={radarData}>
                          <PolarGrid stroke="rgba(139,92,246,0.2)" />
                          <PolarAngleAxis dataKey="skill" tick={{ fontSize: 10, fill: "#94a3b8" }} />
                          <Radar name="Required" dataKey="Required" stroke="rgba(139,92,246,0.3)" fill="rgba(139,92,246,0.08)" />
                          <Radar name="You" dataKey="You" stroke="#4ade80" fill="rgba(74,222,128,0.15)" strokeWidth={2} />
                        </RadarChart>
                      </ResponsiveContainer>
                    </div>
                  )}

                  {/* Matched / Missing */}
                  <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
                    <div className="glass-card" style={{ padding: 20 }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 12 }}>
                        <CheckCircle size={16} color="#4ade80" />
                        <h3 style={{ margin: 0, fontSize: "0.88rem", fontWeight: 700, color: "#4ade80" }}>You Have</h3>
                      </div>
                      <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                        {result.matched_skills.map(s => (
                          <span key={s} className="badge badge-success">{s}</span>
                        ))}
                        {result.matched_skills.length === 0 && <span style={{ color: "#475569", fontSize: "0.8rem" }}>None matched</span>}
                      </div>
                    </div>
                    <div className="glass-card" style={{ padding: 20 }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 12 }}>
                        <AlertTriangle size={16} color="#f87171" />
                        <h3 style={{ margin: 0, fontSize: "0.88rem", fontWeight: 700, color: "#f87171" }}>Missing Skills</h3>
                      </div>
                      <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
                        {result.missing_skills.map(s => (
                          <span key={s} className="badge badge-danger">{s}</span>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>

                {/* Recommendations */}
                  <div className="glass-card" style={{ padding: 24 }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 18 }}>
                      <BookOpen size={17} color="#a78bfa" />
                      <h3 style={{ margin: 0, fontSize: "0.95rem", fontWeight: 700, color: "#e2e8f0" }}>
                        Skill Gap Recommendations
                      </h3>
                    </div>
                    <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
                      {result.recommendations.slice(0, 6).map((rec, recIdx) => (
                        <div key={recIdx}>
                          <h4 style={{ fontSize: "0.9rem", fontWeight: 700, color: "#a78bfa", marginBottom: 12 }}>
                            {rec.skill}
                          </h4>
                          <div style={{ display: "flex", gap: 12 }}>
                            <div style={{ flex: 1 }}>
                              <h5 style={{ fontSize: "0.8rem", color: "#94a3b8", margin: "0 0 8px 0", fontWeight: 600 }}>
                                Courses ({rec.courses.length})
                              </h5>
                              <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                                {rec.courses.slice(0,4).map((c, i) => (
                                  <a key={i} href={c.url} target="_blank" rel="noopener noreferrer" style={{
                                    display: "flex", alignItems: "center", gap: 8, padding: "8px 12px", background: "rgba(139,92,246,0.07)", borderRadius: 8, textDecoration: "none"
                                  }}>
                                    <div style={{ width: 32, height: 32, background: "#4f46e5", borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.8rem", color: "white" }}>
                                      📚
                                    </div>
                                    <div>
                                      <div style={{ fontSize: "0.8rem", fontWeight: 600 }}>{c.course}</div>
                                      <div style={{ fontSize: "0.7rem", color: "#64748b" }}>{c.platform}</div>
                                    </div>
                                  </a>
                                ))}
                              </div>
                            </div>
                            <div style={{ flex: 1 }}>
                              <h5 style={{ fontSize: "0.8rem", color: "#94a3b8", margin: "0 0 8px 0", fontWeight: 600 }}>
                                Internships ({rec.internships.length})
                              </h5>
                              <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                                {rec.internships.slice(0,4).map((intern, i) => (
                                  <a key={i} href={intern.url} target="_blank" rel="noopener noreferrer" style={{
                                    display: "flex", alignItems: "center", gap: 8, padding: "8px 12px", background: "rgba(34,197,94,0.07)", borderRadius: 8, textDecoration: "none"
                                  }}>
                                    <div style={{ width: 32, height: 32, background: "#059669", borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "center", fontSize: "0.8rem", color: "white" }}>
                                      🏢
                                    </div>
                                    <div>
                                      <div style={{ fontSize: "0.8rem", fontWeight: 600 }}>{intern.role} at {intern.company}</div>
                                      <div style={{ fontSize: "0.7rem", color: "#64748b" }}>{intern.location}</div>
                                    </div>
                                  </a>
                                ))}
                              </div>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
              </motion.div>
            ) : (
              <motion.div key="empty" initial={{ opacity: 0 }} animate={{ opacity: 1 }}
                className="glass-card"
                style={{ minHeight: 400, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 12 }}>
                <Target size={48} color="#374151" />
                <p style={{ color: "#475569", fontSize: "0.9rem", textAlign: "center", maxWidth: 300 }}>
                  Add your skills and select a job role, then click &quot;Analyze Skill Gap&quot; to see personalized results
                </p>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </AppLayout>
    </ProtectedRoute>
  );
}
