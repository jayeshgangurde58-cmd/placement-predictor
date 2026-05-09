"use client";

import { useState, useEffect } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import {
  getPredictions, getSkillAnalyses, getBulkReports, formatTimestamp,
  PredictionRecord, SkillAnalysisRecord, BulkReportRecord,
} from "@/lib/firestore";
import { motion } from "framer-motion";
import { History, BrainCircuit, Search, Users, Download } from "lucide-react";

type Tab = "predictions" | "skill_analyses" | "bulk_reports";

export default function HistoryPage() {
  const { user } = useAuth();
  const [tab, setTab] = useState<Tab>("predictions");
  const [predictions, setPredictions] = useState<PredictionRecord[]>([]);
  const [skillAnalyses, setSkillAnalyses] = useState<SkillAnalysisRecord[]>([]);
  const [bulkReports, setBulkReports] = useState<BulkReportRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState("");

  useEffect(() => {
    if (!user) return;
    Promise.all([
      getPredictions(user.uid),
      getSkillAnalyses(user.uid),
      getBulkReports(user.uid),
    ]).then(([p, s, b]) => {
      setPredictions(p);
      setSkillAnalyses(s);
      setBulkReports(b);
      setLoading(false);
    });
  }, [user]);

  const filteredPredictions = predictions.filter(p =>
    filter === "" || String(p.result?.probability).includes(filter) ||
    (p.result?.placed ? "placed" : "at risk").includes(filter.toLowerCase())
  );

  const exportPredictions = () => {
    const rows = filteredPredictions.map(p => ({
      timestamp: formatTimestamp(p.timestamp),
      cgpa: p.input?.cgpa,
      aptitude: p.input?.aptitude,
      programming: p.input?.programming,
      communication: p.input?.communication,
      projects: p.input?.projects,
      internships: p.input?.internships,
      probability: p.result?.probability,
      placed: p.result?.placed ? "Yes" : "No",
      confidence: p.result?.confidence,
    }));
    const headers = Object.keys(rows[0] || {});
    const csv = [headers, ...rows.map(r => Object.values(r))].map(r => r.join(",")).join("\n");
    const blob = new Blob([csv], { type: "text/csv" });
    const a = document.createElement("a"); a.href = URL.createObjectURL(blob);
    a.download = "predictions_history.csv"; a.click();
  };

  const TABS = [
    { key: "predictions" as Tab, label: "Predictions", icon: BrainCircuit, count: predictions.length },
    { key: "skill_analyses" as Tab, label: "Skill Analyses", icon: Search, count: skillAnalyses.length },
    { key: "bulk_reports" as Tab, label: "Bulk Reports", icon: Users, count: bulkReports.length },
  ];

  return (
    <ProtectedRoute>
      <AppLayout>
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }}>
          <div style={{ marginBottom: 32 }}>
            <h1 style={{ fontSize: "1.8rem", fontWeight: 800, margin: 0 }}>
              <span className="gradient-text">History & Reports</span>
            </h1>
            <p style={{ color: "#64748b", marginTop: 6 }}>
              All your past predictions, analyses and bulk uploads
            </p>
          </div>
        </motion.div>

        {/* Tabs */}
        <div style={{ display: "flex", gap: 8, marginBottom: 24, padding: "6px", background: "rgba(139,92,246,0.07)", borderRadius: 14, border: "1px solid rgba(139,92,246,0.12)", width: "fit-content" }}>
          {TABS.map(({ key, label, icon: Icon, count }) => (
            <button key={key} onClick={() => setTab(key)}
              id={`tab-${key}`}
              style={{
                display: "flex", alignItems: "center", gap: 8,
                padding: "10px 20px", borderRadius: 10,
                background: tab === key ? "rgba(124,58,237,0.25)" : "transparent",
                border: tab === key ? "1px solid rgba(124,58,237,0.4)" : "1px solid transparent",
                color: tab === key ? "#a78bfa" : "#64748b",
                fontWeight: 600, fontSize: "0.87rem", cursor: "pointer",
                transition: "all 0.2s",
              }}>
              <Icon size={16} />
              {label}
              <span style={{
                padding: "1px 8px", borderRadius: 12, fontSize: "0.72rem", fontWeight: 700,
                background: tab === key ? "rgba(167,139,250,0.2)" : "rgba(100,116,139,0.15)",
                color: tab === key ? "#a78bfa" : "#64748b",
              }}>{count}</span>
            </button>
          ))}
        </div>

        <div className="glass-card" style={{ padding: 28, overflowX: "auto" }}>
          {/* Filter + Export */}
          <div style={{ display: "flex", justifyContent: "space-between", gap: 12, marginBottom: 20 }}>
            <input id="history-filter" className="form-input" style={{ maxWidth: 280 }}
              placeholder="Filter results…"
              value={filter} onChange={e => setFilter(e.target.value)} />
            {tab === "predictions" && filteredPredictions.length > 0 && (
              <button onClick={exportPredictions} className="btn-secondary" style={{ fontSize: "0.82rem", padding: "8px 14px", flexShrink: 0 }}>
                <Download size={14} /> Export CSV
              </button>
            )}
          </div>

          {loading ? (
            <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              {[...Array(5)].map((_, i) => <div key={i} className="skeleton" style={{ height: 48 }} />)}
            </div>
          ) : (
            <>
              {/* Predictions Tab */}
              {tab === "predictions" && (
                filteredPredictions.length === 0
                  ? <EmptyState label="No predictions yet" />
                  : <table className="data-table">
                      <thead>
                        <tr>
                          <th>Timestamp</th>
                          <th>CGPA</th>
                          <th>Programming</th>
                          <th>Projects</th>
                          <th>Internships</th>
                          <th>Probability</th>
                          <th>Status</th>
                          <th>Confidence</th>
                        </tr>
                      </thead>
                      <tbody>
                        {filteredPredictions.map((p, i) => (
                          <motion.tr key={p.id || i} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.02 }}>
                            <td style={{ whiteSpace: "nowrap", fontSize: "0.8rem" }}>{formatTimestamp(p.timestamp)}</td>
                            <td>{p.input?.cgpa}</td>
                            <td>{p.input?.programming}%</td>
                            <td>{p.input?.projects}</td>
                            <td>{p.input?.internships}</td>
                            <td>
                              <span style={{ fontWeight: 700, color: (p.result?.probability || 0) >= 60 ? "#4ade80" : "#f87171" }}>
                                {p.result?.probability}%
                              </span>
                            </td>
                            <td><span className={`badge ${p.result?.placed ? "badge-success" : "badge-danger"}`}>
                              {p.result?.placed ? "Placed" : "At Risk"}
                            </span></td>
                            <td><span className="badge badge-purple">{p.result?.confidence}</span></td>
                          </motion.tr>
                        ))}
                      </tbody>
                    </table>
              )}

              {/* Skill Analyses Tab */}
              {tab === "skill_analyses" && (
                skillAnalyses.length === 0
                  ? <EmptyState label="No skill analyses yet" />
                  : <table className="data-table">
                      <thead>
                        <tr>
                          <th>Timestamp</th>
                          <th>Target Role</th>
                          <th>Match Rate</th>
                          <th>Skill Gap Index</th>
                          <th>Missing Skills</th>
                        </tr>
                      </thead>
                      <tbody>
                        {skillAnalyses.map((s, i) => (
                          <motion.tr key={s.id || i} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.02 }}>
                            <td style={{ fontSize: "0.8rem" }}>{formatTimestamp(s.timestamp)}</td>
                            <td style={{ fontWeight: 600, color: "#e2e8f0" }}>{s.input?.target_role}</td>
                            <td><span style={{ fontWeight: 700, color: (s.result?.match_rate || 0) >= 60 ? "#4ade80" : "#fb923c" }}>{s.result?.match_rate}%</span></td>
                            <td><span className="badge badge-purple">{s.result?.skill_gap_index?.toFixed(2)}</span></td>
                            <td style={{ maxWidth: 260 }}>
                              <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
                                {(s.result?.missing_skills || []).slice(0, 4).map(sk => (
                                  <span key={sk} className="badge badge-danger" style={{ fontSize: "0.68rem" }}>{sk}</span>
                                ))}
                                {(s.result?.missing_skills || []).length > 4 && (
                                  <span style={{ color: "#475569", fontSize: "0.75rem" }}>+{(s.result?.missing_skills || []).length - 4}</span>
                                )}
                              </div>
                            </td>
                          </motion.tr>
                        ))}
                      </tbody>
                    </table>
              )}

              {/* Bulk Reports Tab */}
              {tab === "bulk_reports" && (
                bulkReports.length === 0
                  ? <EmptyState label="No bulk reports yet" />
                  : <table className="data-table">
                      <thead>
                        <tr>
                          <th>Timestamp</th>
                          <th>File Name</th>
                          <th>Total Students</th>
                          <th>Placed</th>
                          <th>Avg Probability</th>
                          <th>Placement Rate</th>
                        </tr>
                      </thead>
                      <tbody>
                        {bulkReports.map((b, i) => (
                          <motion.tr key={b.id || i} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.02 }}>
                            <td style={{ fontSize: "0.8rem" }}>{formatTimestamp(b.timestamp)}</td>
                            <td style={{ fontWeight: 600, color: "#e2e8f0" }}>{b.fileName}</td>
                            <td>{b.total}</td>
                            <td>{b.placed}</td>
                            <td>{b.avg_probability}%</td>
                            <td><span className="badge badge-blue">{b.placement_rate}%</span></td>
                          </motion.tr>
                        ))}
                      </tbody>
                    </table>
              )}
            </>
          )}
        </div>
      </AppLayout>
    </ProtectedRoute>
  );
}

function EmptyState({ label }: { label: string }) {
  return (
    <div style={{ padding: "60px 24px", textAlign: "center" }}>
      <History size={40} color="#374151" style={{ margin: "0 auto 12px" }} />
      <p style={{ color: "#475569", fontSize: "0.9rem" }}>{label}</p>
    </div>
  );
}
