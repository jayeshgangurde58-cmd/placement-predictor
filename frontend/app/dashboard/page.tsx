"use client";

import { useEffect, useState } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import { getPredictions, getSkillAnalyses, getBulkReports } from "@/lib/firestore";
import { motion } from "framer-motion";
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  BarChart, Bar, Cell, PieChart, Pie, Legend,
} from "recharts";
import { BrainCircuit, TrendingUp, Users, Search, ArrowRight } from "lucide-react";
import Link from "next/link";

const PURPLE = "#8b5cf6";
const VIOLET = "#818cf8";
const SUCCESS = "#4ade80";
const DANGER = "#f87171";

interface StatCardProps {
  label: string;
  value: string | number;
  sub?: string;
  icon: React.ReactNode;
  color: string;
  delay?: number;
}

function StatCard({ label, value, sub, icon, color, delay = 0 }: StatCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, duration: 0.4 }}
      className="stat-card"
    >
      <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between" }}>
        <div>
          <div style={{ fontSize: "0.78rem", fontWeight: 600, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 10 }}>
            {label}
          </div>
          <div style={{ fontSize: "2rem", fontWeight: 800, color: "#f1f5f9" }}>{value}</div>
          {sub && <div style={{ fontSize: "0.78rem", color: "#475569", marginTop: 4 }}>{sub}</div>}
        </div>
        <div style={{ width: 44, height: 44, borderRadius: 12, background: `${color}22`, border: `1px solid ${color}44`, display: "flex", alignItems: "center", justifyContent: "center", color }}>
          {icon}
        </div>
      </div>
    </motion.div>
  );
}

export default function DashboardPage() {
  const { user, profile } = useAuth();
  const [predictions, setPredictions] = useState<any[]>([]);
  const [skillAnalyses, setSkillAnalyses] = useState<any[]>([]);
  const [bulkReports, setBulkReports] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) return;
    Promise.all([
      getPredictions(user.uid, 30),
      getSkillAnalyses(user.uid, 10),
      getBulkReports(user.uid, 10),
    ]).then(([preds, skills, bulk]) => {
      setPredictions(preds);
      setSkillAnalyses(skills);
      setBulkReports(bulk);
      setLoading(false);
    });
  }, [user]);

  const avgProb = predictions.length
    ? Math.round(predictions.reduce((s, p) => s + p.result?.probability, 0) / predictions.length)
    : 0;

  const placedCount = predictions.filter(p => p.result?.placed).length;
  const latest5 = predictions.slice(0, 10).map((p, i) => ({
    name: `#${predictions.length - i}`,
    probability: p.result?.probability || 0,
  }));

  const skillRoleData = skillAnalyses.slice(0, 5).map(s => ({
    role: s.input?.target_role?.replace(" Developer", " Dev").replace("Scientist", "Sci.") || "?",
    matchRate: s.result?.match_rate || 0,
  }));

  const pieData = predictions.length
    ? [
        { name: "Likely Placed", value: placedCount, fill: SUCCESS },
        { name: "At Risk", value: predictions.length - placedCount, fill: DANGER },
      ]
    : [];

  return (
    <ProtectedRoute>
      <AppLayout>
        {/* Header */}
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }}>
          <div style={{ marginBottom: 32 }}>
            <h1 style={{ fontSize: "1.8rem", fontWeight: 800, margin: 0, color: "#f1f5f9" }}>
              Welcome back, <span className="gradient-text">{profile?.name?.split(" ")[0] || "User"}</span> 👋
            </h1>
            <p style={{ color: "#64748b", marginTop: 6 }}>
              Here&apos;s your placement performance overview
            </p>
          </div>
        </motion.div>

        {/* Stat Cards */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 20, marginBottom: 32 }}>
          <StatCard label="Total Predictions" value={predictions.length} icon={<BrainCircuit size={20} />} color={PURPLE} delay={0} />
          <StatCard label="Avg Probability" value={`${avgProb}%`} sub="across all predictions" icon={<TrendingUp size={20} />} color={VIOLET} delay={0.08} />
          <StatCard label="Likely Placed" value={placedCount} sub={`of ${predictions.length} analyzed`} icon={<Users size={20} />} color={SUCCESS} delay={0.16} />
          <StatCard label="Skill Analyses" value={skillAnalyses.length} icon={<Search size={20} />} color="#fb923c" delay={0.24} />
        </div>

        {/* Charts Row */}
        <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: 24, marginBottom: 28 }}>
          {/* Probability Trend */}
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.3 }} className="glass-card" style={{ padding: 24 }}>
            <h2 style={{ margin: "0 0 20px", fontSize: "1rem", fontWeight: 700, color: "#e2e8f0" }}>
              Placement Probability Trend
            </h2>
            {loading ? (
              <div style={{ height: 220 }} className="skeleton" />
            ) : latest5.length === 0 ? (
              <EmptyState label="Run a prediction to see your trend" href="/predict" />
            ) : (
              <ResponsiveContainer width="100%" height={220}>
                <AreaChart data={[...latest5].reverse()}>
                  <defs>
                    <linearGradient id="probGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor={PURPLE} stopOpacity={0.35} />
                      <stop offset="95%" stopColor={PURPLE} stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" tick={{ fontSize: 11 }} />
                  <YAxis domain={[0, 100]} tick={{ fontSize: 11 }} unit="%" />
                  <Tooltip formatter={(v: any) => [`${v}%`, "Probability"]} />
                  <Area type="monotone" dataKey="probability" stroke={PURPLE} strokeWidth={2.5} fill="url(#probGrad)" dot={{ fill: PURPLE, r: 4 }} />
                </AreaChart>
              </ResponsiveContainer>
            )}
          </motion.div>

          {/* Pie */}
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.35 }} className="glass-card" style={{ padding: 24 }}>
            <h2 style={{ margin: "0 0 20px", fontSize: "1rem", fontWeight: 700, color: "#e2e8f0" }}>
              Placement Outlook
            </h2>
            {loading ? (
              <div style={{ height: 180 }} className="skeleton" />
            ) : pieData.length === 0 ? (
              <EmptyState label="No data yet" href="/predict" />
            ) : (
              <ResponsiveContainer width="100%" height={180}>
                <PieChart>
                  <Pie data={pieData} cx="50%" cy="50%" innerRadius={50} outerRadius={80} dataKey="value" paddingAngle={3}>
                    {pieData.map((entry, i) => <Cell key={i} fill={entry.fill} />)}
                  </Pie>
                  <Tooltip />
                  <Legend iconType="circle" iconSize={10} />
                </PieChart>
              </ResponsiveContainer>
            )}
          </motion.div>
        </div>

        {/* Skill match bar */}
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.4 }} className="glass-card" style={{ padding: 24, marginBottom: 28 }}>
          <h2 style={{ margin: "0 0 20px", fontSize: "1rem", fontWeight: 700, color: "#e2e8f0" }}>
            Skill Match Rates by Role
          </h2>
          {loading ? (
            <div style={{ height: 180 }} className="skeleton" />
          ) : skillRoleData.length === 0 ? (
            <EmptyState label="Run a skill gap analysis to see results" href="/skill-gap" />
          ) : (
            <ResponsiveContainer width="100%" height={180}>
              <BarChart data={skillRoleData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="role" tick={{ fontSize: 11 }} />
                <YAxis domain={[0, 100]} tick={{ fontSize: 11 }} unit="%" />
                <Tooltip formatter={(v: any) => [`${v}%`, "Match Rate"]} />
                <Bar dataKey="matchRate" radius={[6, 6, 0, 0]}>
                  {skillRoleData.map((_, i) => (
                    <Cell key={i} fill={`hsl(${260 + i * 20}, 70%, 65%)`} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          )}
        </motion.div>

        {/* Quick Actions */}
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.45 }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 700, color: "#e2e8f0", marginBottom: 16 }}>Quick Actions</h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 16 }}>
            {[
              { href: "/predict", label: "Predict Placement", desc: "Analyse your profile", color: PURPLE },
              { href: "/skill-gap", label: "Skill Gap Analysis", desc: "Find missing skills", color: VIOLET },
              { href: "/bulk", label: "Bulk Analysis", desc: "Analyse multiple students", color: "#fb923c" },
              { href: "/history", label: "View History", desc: "All past reports", color: SUCCESS },
            ].map(({ href, label, desc, color }) => (
              <Link key={href} href={href} style={{ textDecoration: "none" }}>
                <motion.div whileHover={{ y: -3 }} className="glass-card glass-card-hover"
                  style={{ padding: 20, cursor: "pointer" }}>
                  <div style={{ fontSize: "0.9rem", fontWeight: 700, color: "#e2e8f0", marginBottom: 4 }}>{label}</div>
                  <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: 12 }}>{desc}</div>
                  <div style={{ display: "flex", alignItems: "center", gap: 4, fontSize: "0.8rem", fontWeight: 600, color }}>
                    Go <ArrowRight size={13} />
                  </div>
                </motion.div>
              </Link>
            ))}
          </div>
        </motion.div>
      </AppLayout>
    </ProtectedRoute>
  );
}

function EmptyState({ label, href }: { label: string; href: string }) {
  return (
    <div style={{ height: 180, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 10 }}>
      <p style={{ color: "#475569", fontSize: "0.85rem" }}>{label}</p>
      <Link href={href} className="btn-primary" style={{ fontSize: "0.8rem", padding: "8px 16px" }}>Get Started</Link>
    </div>
  );
}
