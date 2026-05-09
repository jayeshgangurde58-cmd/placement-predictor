"use client";

import { useEffect, useState } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import { collection, getDocs, query, orderBy, limit } from "firebase/firestore";
import { db } from "@/lib/firebase";
import { motion } from "framer-motion";
import { Shield, Users, TrendingUp, Database } from "lucide-react";

export default function AdminPage() {
  const { profile } = useAuth();
  const [users, setUsers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (profile?.role !== "admin") { setLoading(false); return; }
    getDocs(query(collection(db, "users"), orderBy("createdAt", "desc"), limit(50)))
      .then(snap => {
        setUsers(snap.docs.map(d => ({ id: d.id, ...d.data() })));
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [profile]);

  if (profile?.role !== "admin") {
    return (
      <ProtectedRoute>
        <AppLayout>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "60vh", gap: 16 }}>
            <Shield size={48} color="#f87171" />
            <h2 style={{ color: "#f87171", margin: 0 }}>Access Denied</h2>
            <p style={{ color: "#64748b" }}>You need admin privileges to access this page.</p>
          </div>
        </AppLayout>
      </ProtectedRoute>
    );
  }

  return (
    <ProtectedRoute>
      <AppLayout>
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }}>
          <div style={{ marginBottom: 32 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 8 }}>
              <Shield size={24} color="#f87171" />
              <h1 style={{ fontSize: "1.8rem", fontWeight: 800, margin: 0 }}>
                <span style={{ background: "linear-gradient(135deg,#f87171,#fb923c)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
                  Admin Panel
                </span>
              </h1>
            </div>
            <p style={{ color: "#64748b", marginTop: 0 }}>
              Manage users and view platform analytics
            </p>
          </div>
        </motion.div>

        {/* Stats */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: 20, marginBottom: 32 }}>
          {[
            { label: "Total Users", value: users.length, icon: <Users size={20} />, color: "#a78bfa" },
            { label: "Admin Users", value: users.filter(u => u.role === "admin").length, icon: <Shield size={20} />, color: "#f87171" },
            { label: "Regular Users", value: users.filter(u => u.role === "user").length, icon: <TrendingUp size={20} />, color: "#4ade80" },
            { label: "DB Collections", value: 4, icon: <Database size={20} />, color: "#fb923c" },
          ].map(({ label, value, icon, color }, i) => (
            <motion.div key={label} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.07 }}
              className="stat-card">
              <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
                <div>
                  <div style={{ fontSize: "0.72rem", fontWeight: 700, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 8 }}>{label}</div>
                  <div style={{ fontSize: "2rem", fontWeight: 800, color: "#f1f5f9" }}>{value}</div>
                </div>
                <div style={{ width: 40, height: 40, borderRadius: 10, background: `${color}22`, border: `1px solid ${color}44`, display: "flex", alignItems: "center", justifyContent: "center", color }}>
                  {icon}
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Users Table */}
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.3 }}
          className="glass-card" style={{ padding: 28, overflowX: "auto" }}>
          <h2 style={{ margin: "0 0 20px", fontSize: "1rem", fontWeight: 700, color: "#e2e8f0" }}>
            Registered Users
          </h2>
          {loading ? (
            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              {[...Array(5)].map((_, i) => <div key={i} className="skeleton" style={{ height: 44 }} />)}
            </div>
          ) : (
            <table className="data-table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Role</th>
                  <th>User ID</th>
                </tr>
              </thead>
              <tbody>
                {users.map((u, i) => (
                  <motion.tr key={u.id} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.03 }}>
                    <td style={{ fontWeight: 600, color: "#e2e8f0" }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                        <div style={{
                          width: 28, height: 28, borderRadius: "50%",
                          background: "linear-gradient(135deg,#7c3aed,#818cf8)",
                          display: "flex", alignItems: "center", justifyContent: "center",
                          fontSize: "0.75rem", fontWeight: 700, color: "white", flexShrink: 0,
                        }}>
                          {u.name?.[0]?.toUpperCase() || "U"}
                        </div>
                        {u.name || "—"}
                      </div>
                    </td>
                    <td>{u.email}</td>
                    <td>
                      <span className={`badge ${u.role === "admin" ? "badge-danger" : "badge-purple"}`}>
                        {u.role || "user"}
                      </span>
                    </td>
                    <td style={{ fontSize: "0.72rem", color: "#374151", fontFamily: "monospace" }}>
                      {u.id}
                    </td>
                  </motion.tr>
                ))}
              </tbody>
            </table>
          )}
        </motion.div>
      </AppLayout>
    </ProtectedRoute>
  );
}
