"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "@/context/AuthContext";
import { motion } from "framer-motion";
import toast from "react-hot-toast";
import { Eye, EyeOff, Zap, Mail, Lock } from "lucide-react";

export default function ForgotPasswordPage() {
  const { resetPasswordWithSecurity } = useAuth();
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [securityAnswer, setSecurityAnswer] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [showPass, setShowPass] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleReset = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !securityAnswer || !newPassword) { toast.error("Please fill all fields"); return; }
    if (newPassword.length < 6) { toast.error("New password must be at least 6 characters"); return; }
    setLoading(true);
    try {
      await resetPasswordWithSecurity(email, securityAnswer, newPassword);
      toast.success("Password reset simulated successfully!");
      router.push("/login");
    } catch (err: any) {
      toast.error(err.message?.replace("Firebase: ", "") || "Password reset failed");
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
        <div style={{ textAlign: "center", marginBottom: 32 }}>
          <div style={{ display: "inline-flex", alignItems: "center", justifyContent: "center", width: 56, height: 56, borderRadius: 16, background: "linear-gradient(135deg,#7c3aed,#4f46e5)", boxShadow: "0 8px 24px rgba(124,58,237,0.4)", marginBottom: 16 }}>
            <Zap size={26} color="white" />
          </div>
          <h1 style={{ fontSize: "1.6rem", fontWeight: 800, margin: 0 }} className="gradient-text">
            Reset Password
          </h1>
          <p style={{ color: "#64748b", marginTop: 6, fontSize: "0.9rem" }}>
            Answer your security question to continue
          </p>
        </div>

        <form onSubmit={handleReset} style={{ display: "flex", flexDirection: "column", gap: 18 }}>
          <div>
            <label className="form-label">Email Address</label>
            <div style={{ position: "relative" }}>
              <Mail size={16} style={{ position: "absolute", left: 14, top: "50%", transform: "translateY(-50%)", color: "#475569" }} />
              <input id="reset-email" type="email" className="form-input" style={{ paddingLeft: 42 }}
                placeholder="you@example.com" value={email} onChange={e => setEmail(e.target.value)} required />
            </div>
          </div>

          <div>
            <label className="form-label">Security Question: What is your favourite programming language?</label>
            <div style={{ position: "relative" }}>
              <Lock size={16} style={{ position: "absolute", left: 14, top: "50%", transform: "translateY(-50%)", color: "#475569" }} />
              <input id="reset-security" type="text" className="form-input" style={{ paddingLeft: 42 }}
                placeholder="e.g. Python" value={securityAnswer} onChange={e => setSecurityAnswer(e.target.value)} required />
            </div>
          </div>

          <div>
            <label className="form-label">New Password</label>
            <div style={{ position: "relative" }}>
              <Lock size={16} style={{ position: "absolute", left: 14, top: "50%", transform: "translateY(-50%)", color: "#475569" }} />
              <input id="reset-password" type={showPass ? "text" : "password"} className="form-input"
                style={{ paddingLeft: 42, paddingRight: 42 }} placeholder="Min 6 characters"
                value={newPassword} onChange={e => setNewPassword(e.target.value)} required />
              <button type="button" onClick={() => setShowPass(!showPass)}
                style={{ position: "absolute", right: 14, top: "50%", transform: "translateY(-50%)", background: "none", border: "none", cursor: "pointer", color: "#475569", display: "flex" }}>
                {showPass ? <EyeOff size={16} /> : <Eye size={16} />}
              </button>
            </div>
          </div>

          <button id="reset-submit" type="submit" className="btn-primary" disabled={loading} style={{ marginTop: 4 }}>
            {loading ? <span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> : "Reset Password"}
          </button>
        </form>

        <p style={{ textAlign: "center", marginTop: 24, color: "#475569", fontSize: "0.87rem" }}>
          Remember your password?{" "}
          <Link href="/login" style={{ color: "#a78bfa", fontWeight: 600, textDecoration: "none" }}>
            Sign in
          </Link>
        </p>
      </motion.div>
    </div>
  );
}
