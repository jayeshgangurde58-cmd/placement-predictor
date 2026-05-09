"use client";

import { ReactNode } from "react";
import Sidebar from "./Sidebar";

export default function AppLayout({ children }: { children: ReactNode }) {
  return (
    <div style={{ display: "flex" }}>
      <Sidebar />
      <main
        style={{
          flex: 1,
          marginLeft: 260,
          minHeight: "100vh",
          padding: "32px 40px",
          maxWidth: "calc(100vw - 260px)",
        }}
      >
        {children}
      </main>
    </div>
  );
}
