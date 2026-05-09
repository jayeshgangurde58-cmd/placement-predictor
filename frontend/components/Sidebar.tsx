"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useAuth } from "@/context/AuthContext";
import {
  LayoutDashboard,
  BrainCircuit,
  Search,
  Users,
  History,
  Shield,
  LogOut,
  ChevronRight,
  BookOpen,
} from "lucide-react";
import { motion } from "framer-motion";
import toast from "react-hot-toast";

const NAV_ITEMS = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/predict", label: "Predict Placement", icon: BrainCircuit },
  { href: "/skill-gap", label: "Skill Gap", icon: Search },
  { href: "/bulk", label: "Bulk Analysis", icon: Users },
  { href: "/recommendation", label: "Recommendations", icon: BookOpen },
  { href: "/history", label: "History", icon: History },
];

const ADMIN_ITEMS = [
  { href: "/admin", label: "Admin Panel", icon: Shield },
];

export default function Sidebar() {
  const { profile, logout } = useAuth();
  const pathname = usePathname();

  const handleLogout = async () => {
    await logout();
    toast.success("Logged out successfully");
  };

  return (
    <aside
      className="sidebar flex flex-col"
      style={{
        background: "rgba(10,6,21,0.9)",
        backdropFilter: "blur(20px)",
        borderRight: "1px solid rgba(139,92,246,0.15)",
        position: "fixed",
        top: 0,
        left: 0,
        height: "100vh",
        zIndex: 50,
        padding: "0",
      }}
    >
      {/* Nav */}
      <nav style={{ flex: 1, padding: "16px 12px", overflowY: "auto" }}>
        <div style={{ fontSize: "0.68rem", fontWeight: 700, color: "#475569", letterSpacing: "0.1em", padding: "8px 8px 10px", textTransform: "uppercase" }}>
          Main Menu
        </div>
        {NAV_ITEMS.map(({ href, label, icon: Icon }) => {
          const active = pathname === href || pathname.startsWith(href + "/");
          return (
            <Link key={href} href={href} style={{ textDecoration: "none" }}>
              <motion.div
                whileHover={{ x: 3 }}
                style={{
                  display: "flex", alignItems: "center", gap: 10,
                  padding: "11px 12px", borderRadius: 10, marginBottom: 4,
                  background: active ? "rgba(124,58,237,0.2)" : "transparent",
                  border: active ? "1px solid rgba(124,58,237,0.3)" : "1px solid transparent",
                  color: active ? "#a78bfa" : "#64748b",
                  fontWeight: active ? 600 : 500,
                  fontSize: "0.88rem",
                  cursor: "pointer",
                  transition: "color 0.2s, background 0.2s",
                }}
              >
                <Icon size={17} />
                <span style={{ flex: 1 }}>{label}</span>
                {active && <ChevronRight size={13} />}
              </motion.div>
            </Link>
          );
        })}

        {profile?.role === "admin" && (
          <>
            <div style={{ fontSize: "0.68rem", fontWeight: 700, color: "#475569", letterSpacing: "0.1em", padding: "16px 8px 10px", textTransform: "uppercase" }}>
              Admin
            </div>
            {ADMIN_ITEMS.map(({ href, label, icon: Icon }) => {
              const active = pathname === href;
              return (
                <Link key={href} href={href} style={{ textDecoration: "none" }}>
                  <motion.div
                    whileHover={{ x: 3 }}
                    style={{
                      display: "flex", alignItems: "center", gap: 10,
                      padding: "11px 12px", borderRadius: 10, marginBottom: 4,
                      background: active ? "rgba(248,113,113,0.15)" : "transparent",
                      border: active ? "1px solid rgba(248,113,113,0.3)" : "1px solid transparent",
                      color: active ? "#f87171" : "#64748b",
                      fontWeight: active ? 600 : 500,
                      fontSize: "0.88rem",
                      cursor: "pointer",
                    }}
                  >
                    <Icon size={17} />
                    <span>{label}</span>
                  </motion.div>
                </Link>
              );
            })}
          </>
        )}
      </nav>

      {/* User + Logout */}
      <div style={{ padding: "16px 12px", borderTop: "1px solid rgba(139,92,246,0.12)" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 12, padding: "8px 10px" }}>
          <div
            style={{
              width: 34, height: 34, borderRadius: "50%",
              background: "linear-gradient(135deg,#7c3aed,#818cf8)",
              display: "flex", alignItems: "center", justifyContent: "center",
              fontSize: "0.85rem", fontWeight: 700, color: "white", flexShrink: 0,
            }}
          >
            {profile?.name?.[0]?.toUpperCase() || "U"}
          </div>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontSize: "0.85rem", fontWeight: 600, color: "#e2e8f0", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>
              {profile?.name || "User"}
            </div>
            <div style={{ fontSize: "0.7rem", color: "#475569", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>
              {profile?.email || ""}
            </div>
          </div>
        </div>
        <button
          onClick={handleLogout}
          style={{
            display: "flex", alignItems: "center", gap: 8,
            width: "100%", padding: "10px 12px", borderRadius: 10,
            background: "rgba(248,113,113,0.08)",
            border: "1px solid rgba(248,113,113,0.2)",
            color: "#f87171", fontSize: "0.85rem", fontWeight: 600,
            cursor: "pointer", transition: "background 0.2s",
          }}
          onMouseEnter={e => (e.currentTarget.style.background = "rgba(248,113,113,0.16)")}
          onMouseLeave={e => (e.currentTarget.style.background = "rgba(248,113,113,0.08)")}
        >
          <LogOut size={15} />
          Sign Out
        </button>
      </div>
    </aside>
  );
}
