import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AuthProvider } from "@/context/AuthContext";
import { Toaster } from "react-hot-toast";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "Smart Placement Predictor & Skill Gap Analyzer",
  description:
    "AI-powered placement prediction and skill gap analysis for students. Get personalized recommendations to boost your career.",
  keywords: ["placement predictor", "skill gap analyzer", "AI career tool", "placement probability"],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.variable} font-sans antialiased`}>
        <AuthProvider>
          {children}
          <Toaster
            position="top-right"
            toastOptions={{
              style: {
                background: "#1e1b4b",
                color: "#e2e8f0",
                border: "1px solid rgba(139,92,246,0.3)",
                borderRadius: "12px",
              },
              success: { iconTheme: { primary: "#a78bfa", secondary: "#0f0a2a" } },
              error: { iconTheme: { primary: "#f87171", secondary: "#0f0a2a" } },
            }}
          />
        </AuthProvider>
      </body>
    </html>
  );
}
