"use client";

import { useState, useCallback } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import { bulkAnalysis } from "@/lib/api";
import { saveBulkReport } from "@/lib/firestore";
import { motion, AnimatePresence } from "framer-motion";
import toast from "react-hot-toast";
import { useDropzone } from "react-dropzone";
import { Upload, Download, Users, CheckCircle, XCircle, FileText, AlertTriangle } from "lucide-react";

interface StudentResult {
  row: number;
  name: string;
  cgpa: number;
  aptitude: number;
  programming: number;
  communication: number;
  tenth_percentage?: number;
  twelfth_percentage?: number;
  projects: number;
  internships: number;
  probability: number;
  placed: boolean;
  confidence: string;
  skill_gap?: { target_role: string; match_rate: number; skill_gap_index: number; missing_skills: string[] };
}

interface BulkResult {
  filename: string;
  total_students: number;
  placed_count: number;
  not_placed_count: number;
  avg_probability: number;
  placement_rate: number;
  results: StudentResult[];
  errors: { row: number; error: string }[];
}

function downloadCSV(results: StudentResult[], filename: string) {
  const headers = ["Row", "Name", "CGPA", "Aptitude", "Programming", "Communication", "10th Percentage", "12th Percentage", "Projects", "Internships", "Probability (%)", "Placed", "Confidence"];
  const rows = results.map(r => [
    r.row, r.name, r.cgpa, r.aptitude, r.programming, r.communication,
    r.tenth_percentage ?? "", r.twelfth_percentage ?? "",
    r.projects, r.internships, r.probability, r.placed ? "Yes" : "No", r.confidence,
  ]);
  const csv = [headers, ...rows].map(row => row.join(",")).join("\n");
  const blob = new Blob([csv], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `bulk_results_${filename}`;
  a.click();
  URL.revokeObjectURL(url);
}

const SAMPLE_CSV = `name,cgpa,aptitude,programming,communication,10th_percentage,12th_percentage,projects,internships
Alice Johnson,8.5,85,80,75,92,90,4,2
Bob Smith,6.2,55,45,60,68,65,1,0
Catherine Lee,9.1,92,95,88,96,94,6,3
David Kumar,7.4,72,68,70,78,80,3,1
Emma Wilson,5.8,48,42,55,54,58,0,0
Frank Patel,7.8,78,82,72,88,85,4,2
Grace Chen,8.9,88,91,85,95,93,5,3
Henry Brown,6.5,58,52,62,72,74,2,1`;

export default function BulkPage() {
  const { user } = useAuth();
  const [result, setResult] = useState<BulkResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [fileName, setFileName] = useState("");

  const onDrop = useCallback(async (files: File[]) => {
    const file = files[0];
    if (!file) return;
    setFileName(file.name);
    setLoading(true);
    try {
      const res = await bulkAnalysis(file);
      setResult(res);
      if (user) {
        await saveBulkReport(user.uid, {
          fileName: file.name,
          total: res.total_students,
          placed: res.placed_count,
          avg_probability: res.avg_probability,
          placement_rate: res.placement_rate,
          results: res.results,
          errors: res.errors,
        });
      }
      toast.success(`Processed ${res.total_students} students!`);
    } catch (err: any) {
      toast.error(err.message || "Bulk analysis failed. Is the backend running?");
    } finally { setLoading(false); }
  }, [user]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "text/csv": [".csv"] },
    maxFiles: 1,
  });

  const downloadSample = () => {
    const blob = new Blob([SAMPLE_CSV], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url; a.download = "sample_students.csv"; a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <ProtectedRoute>
      <AppLayout>
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }}>
          <div style={{ marginBottom: 32 }}>
            <h1 style={{ fontSize: "1.8rem", fontWeight: 800, margin: 0 }}>
              <span className="gradient-text">Bulk Analysis</span>
            </h1>
            <p style={{ color: "#64748b", marginTop: 6 }}>
              Upload a CSV file to analyse multiple students at once
            </p>
          </div>
        </motion.div>

        {/* Upload Section */}
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.1 }}
          className="glass-card" style={{ padding: 32, marginBottom: 28 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 24 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <Upload size={20} color="#a78bfa" />
              <h2 style={{ margin: 0, fontSize: "1.05rem", fontWeight: 700, color: "#e2e8f0" }}>Upload CSV File</h2>
            </div>
            <button onClick={downloadSample} className="btn-secondary" style={{ fontSize: "0.82rem", padding: "8px 14px" }}>
              <Download size={14} /> Download Sample CSV
            </button>
          </div>

          <div {...getRootProps()} className={`drop-zone ${isDragActive ? "active" : ""}`}
            style={{ marginBottom: 16 }}>
            <input {...getInputProps()} id="bulk-upload" />
            {loading
              ? <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 12 }}>
                  <div className="spinner" style={{ width: 36, height: 36 }} />
                  <span style={{ color: "#64748b", fontSize: "0.9rem" }}>Processing students…</span>
                </div>
              : <>
                  <FileText size={36} color="#475569" style={{ margin: "0 auto 12px" }} />
                  <p style={{ color: "#64748b", fontSize: "0.9rem", margin: "0 0 6px" }}>
                    {isDragActive ? "Drop CSV here" : "Drag & drop a CSV file here, or click to browse"}
                  </p>
                  <p style={{ color: "#374151", fontSize: "0.78rem", margin: 0 }}>
                    Required columns: name, cgpa, aptitude, programming, communication, projects, internships
                  </p>
                  <p style={{ color: "#374151", fontSize: "0.78rem", margin: 0 }}>
                    Optional: 10th_percentage, 12th_percentage, skills, target_role
                  </p>
                </>
            }
          </div>

          {/* CSV Format Info */}
          <div style={{ background: "rgba(139,92,246,0.07)", border: "1px solid rgba(139,92,246,0.15)", borderRadius: 10, padding: 14, fontSize: "0.78rem", color: "#64748b" }}>
            <strong style={{ color: "#a78bfa" }}>Optional columns:</strong> skills (semicolon-separated) · target_role
          </div>
        </motion.div>

        {/* Results */}
        <AnimatePresence>
          {result && (
            <motion.div key="results" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
              {/* Summary Cards */}
              <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))", gap: 16, marginBottom: 24 }}>
                {[
                  { label: "Total Students", value: result.total_students, icon: <Users size={18} />, color: "#a78bfa" },
                  { label: "Likely Placed", value: result.placed_count, icon: <CheckCircle size={18} />, color: "#4ade80" },
                  { label: "At Risk", value: result.not_placed_count, icon: <XCircle size={18} />, color: "#f87171" },
                  { label: "Avg Probability", value: `${result.avg_probability}%`, icon: <AlertTriangle size={18} />, color: "#fb923c" },
                  { label: "Placement Rate", value: `${result.placement_rate}%`, icon: <CheckCircle size={18} />, color: "#38bdf8" },
                ].map(({ label, value, icon, color }) => (
                  <div key={label} className="stat-card" style={{ padding: 18 }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                      <span style={{ color }}>{icon}</span>
                      <span style={{ fontSize: "0.72rem", fontWeight: 700, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.05em" }}>{label}</span>
                    </div>
                    <div style={{ fontSize: "1.6rem", fontWeight: 800, color: "#f1f5f9" }}>{value}</div>
                  </div>
                ))}
              </div>

              {/* Table */}
              <div className="glass-card" style={{ padding: 24, overflowX: "auto" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
                  <h2 style={{ margin: 0, fontSize: "1rem", fontWeight: 700, color: "#e2e8f0" }}>
                    Student Results — {result.filename}
                  </h2>
                  <button onClick={() => downloadCSV(result.results, result.filename)}
                    className="btn-secondary" style={{ fontSize: "0.82rem", padding: "8px 14px" }}>
                    <Download size={14} /> Export Results
                  </button>
                </div>
                <table className="data-table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Name</th>
                      <th>CGPA</th>
                      <th>Aptitude</th>
                      <th>Programming</th>
                      <th>Communication</th>
                      <th>10th %</th>
                      <th>12th %</th>
                      <th>Projects</th>
                      <th>Internships</th>
                      <th>Probability</th>
                      <th>Status</th>
                      <th>Confidence</th>
                    </tr>
                  </thead>
                  <tbody>
                    {result.results.map((r, i) => (
                      <motion.tr key={r.row} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.03 }}>
                        <td style={{ color: "#475569" }}>{r.row}</td>
                        <td style={{ fontWeight: 600, color: "#e2e8f0" }}>{r.name}</td>
                        <td>{r.cgpa}</td>
                        <td>{r.aptitude}</td>
                        <td>{r.programming}%</td>
                        <td>{r.communication}%</td>
                        <td>{r.tenth_percentage ?? "—"}%</td>
                        <td>{r.twelfth_percentage ?? "—"}%</td>
                        <td>{r.projects}</td>
                        <td>{r.internships}</td>
                        <td>
                          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                            <div className="progress-bar-track" style={{ width: 60, height: 6 }}>
                              <div className="progress-bar-fill"
                                style={{ width: `${r.probability}%`, background: r.probability >= 60 ? "#4ade80" : "#f87171" }} />
                            </div>
                            <span style={{ fontWeight: 700, color: r.probability >= 60 ? "#4ade80" : "#f87171" }}>
                              {r.probability}%
                            </span>
                          </div>
                        </td>
                        <td>
                          <span className={`badge ${r.placed ? "badge-success" : "badge-danger"}`}>
                            {r.placed ? "Placed" : "At Risk"}
                          </span>
                        </td>
                        <td><span className="badge badge-purple">{r.confidence}</span></td>
                      </motion.tr>
                    ))}
                  </tbody>
                </table>

                {result.errors.length > 0 && (
                  <div style={{ marginTop: 16, padding: 12, background: "rgba(248,113,113,0.08)", border: "1px solid rgba(248,113,113,0.2)", borderRadius: 10 }}>
                    <p style={{ color: "#f87171", fontSize: "0.82rem", margin: "0 0 6px", fontWeight: 600 }}>
                      {result.errors.length} row(s) had errors:
                    </p>
                    {result.errors.map(e => (
                      <p key={e.row} style={{ color: "#64748b", fontSize: "0.78rem", margin: 0 }}>
                        Row {e.row}: {e.error}
                      </p>
                    ))}
                  </div>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </AppLayout>
    </ProtectedRoute>
  );
}
