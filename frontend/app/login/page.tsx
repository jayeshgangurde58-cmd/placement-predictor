"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "@/context/AuthContext";
import { motion } from "framer-motion";
import toast from "react-hot-toast";
import { Eye, EyeOff, Zap, Mail, Lock, Globe } from "lucide-react";

export default function LoginPage() {
  const { login, loginWithGoogle } = useAuth();
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPass, setShowPass] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password) { toast.error("Please fill all fields"); return; }
    setLoading(true);
    try {
      await login(email, password);
      toast.success("Welcome back!");
      router.push("/dashboard");
    } catch (err: any) {
      toast.error(err.message?.replace("Firebase: ", "") || "Login failed");
    } finally { setLoading(false); }
  };

  const handleGoogle = async () => {
    setLoading(true);
    try {
      await loginWithGoogle();
      router.push("/dashboard");
    } catch (err: any) {
      toast.error(err.message?.replace("Firebase: ", "") || "Google login failed");
    } finally { setLoading(false); }
  };

  return (
    <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", padding: "24px" }}>
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="glass-card"
        style={{ width: "100%", maxWidth: 420, padding: "40px 36px" }}
      >
        {/* Logo */}
        <div style={{ textAlign: "center", marginBottom: 32 }}>
          <div style={{ display: "inline-flex", alignItems: "center", justifyContent: "center", width: 56, height: 56, borderRadius: 16, background: "linear-gradient(135deg,#7c3aed,#4f46e5)", boxShadow: "0 8px 24px rgba(124,58,237,0.4)", marginBottom: 16 }}>
            <Zap size={26} color="white" />
          </div>
          <h1 style={{ fontSize: "1.6rem", fontWeight: 800, margin: 0 }} className="gradient-text">
            PlaceAI
          </h1>
          <p style={{ color: "#64748b", marginTop: 6, fontSize: "0.9rem" }}>
            Sign in to your account
          </p>
        </div>

        <form onSubmit={handleLogin} style={{ display: "flex", flexDirection: "column", gap: 18 }}>
          <div>
            <label className="form-label">Email Address</label>
            <div style={{ position: "relative" }}>
              <Mail size={16} style={{ position: "absolute", left: 14, top: "50%", transform: "translateY(-50%)", color: "#475569" }} />
              <input id="login-email" type="email" className="form-input" style={{ paddingLeft: 42 }}
                placeholder="you@example.com" value={email} onChange={e => setEmail(e.target.value)} required />
            </div>
          </div>

          <div>
            <label className="form-label">Password</label>
            <div style={{ position: "relative" }}>
              <Lock size={16} style={{ position: "absolute", left: 14, top: "50%", transform: "translateY(-50%)", color: "#475569" }} />
              <input id="login-password" type={showPass ? "text" : "password"} className="form-input"
                style={{ paddingLeft: 42, paddingRight: 42 }} placeholder="••••••••"
                value={password} onChange={e => setPassword(e.target.value)} required />
              <button type="button" onClick={() => setShowPass(!showPass)}
                style={{ position: "absolute", right: 14, top: "50%", transform: "translateY(-50%)", background: "none", border: "none", cursor: "pointer", color: "#475569", display: "flex" }}>
                {showPass ? <EyeOff size={16} /> : <Eye size={16} />}
              </button>
            </div>
          </div>

          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <Link href="/forgot-password" style={{ color: "#a78bfa", fontSize: "0.85rem", textDecoration: "none", fontWeight: 500 }}>
              Forgot Password?
            </Link>
          </div>

          <button id="login-submit" type="submit" className="btn-primary" disabled={loading} style={{ marginTop: 4 }}>
            {loading ? <span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> : "Sign In"}
          </button>
        </form>

        <div style={{ margin: "20px 0", display: "flex", alignItems: "center", gap: 12 }}>
          <div style={{ flex: 1, height: 1, background: "rgba(139,92,246,0.2)" }} />
          <span style={{ color: "#475569", fontSize: "0.8rem" }}>or</span>
          <div style={{ flex: 1, height: 1, background: "rgba(139,92,246,0.2)" }} />
        </div>

        <button id="google-login" onClick={handleGoogle} className="btn-secondary" style={{ width: "100%" }} disabled={loading}>
          <Globe size={17} />
          Continue with Google
        </button>

        <p style={{ textAlign: "center", marginTop: 24, color: "#475569", fontSize: "0.87rem" }}>
          Don&apos;t have an account?{" "}
          <Link href="/register" style={{ color: "#a78bfa", fontWeight: 600, textDecoration: "none" }}>
            Sign up free
          </Link>
        </p>
      </motion.div>
    </div>
  );
}
