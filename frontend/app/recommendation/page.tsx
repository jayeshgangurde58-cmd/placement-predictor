"use client";

import { useEffect, useState } from "react";
import { useAuth } from "@/context/AuthContext";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";
import CourseCard from "@/components/CourseCard";
import { getAllCourses, CourseItem } from "@/lib/api";
import { motion } from "framer-motion";
import { Search, Filter, BookOpen, Briefcase, TrendingUp, Loader2 } from "lucide-react";

const PURPLE = "#8b5cf6";
const VIOLET = "#818cf8";
const SUCCESS = "#4ade80";

export default function RecommendationPage() {
  const { user } = useAuth();
  const [searchTerm, setSearchTerm] = useState("");
  const [filterType, setFilterType] = useState<"all" | "course" | "internship">("all");
  const [filterCategory, setFilterCategory] = useState<string>("all");
  const [allData, setAllData] = useState<CourseItem[]>([]);
  const [filteredData, setFilteredData] = useState<CourseItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [stats, setStats] = useState({ total: 0, courses: 0, internships: 0 });

  useEffect(() => {
    async function loadCourses() {
      try {
        setLoading(true);
        const data = await getAllCourses();
        setAllData(data.items);
        setFilteredData(data.items);
        setStats({ total: data.total, courses: data.courses, internships: data.internships });
        setError(null);
      } catch (err: any) {
        setError(err.message || "Failed to load courses");
      } finally {
        setLoading(false);
      }
    }
    loadCourses();
  }, []);

  useEffect(() => {
    let result = allData;

    if (searchTerm) {
      const term = searchTerm.toLowerCase();
      result = result.filter(
        (item) =>
          item.title.toLowerCase().includes(term) ||
          item.provider.toLowerCase().includes(term) ||
          item.skills.some((skill) => skill.toLowerCase().includes(term))
      );
    }

    if (filterType !== "all") {
      result = result.filter((item) => item.type === filterType);
    }

    if (filterCategory !== "all") {
      result = result.filter((item) => item.category === filterCategory);
    }

    setFilteredData(result);
  }, [searchTerm, filterType, filterCategory, allData]);

  const categories = Array.from(new Set(allData.map((c) => c.category))).sort();

  return (
    <ProtectedRoute>
      <AppLayout>
        {/* Header */}
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} style={{ marginBottom: 32 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 16, marginBottom: 24 }}>
            <div
              style={{
                width: 56,
                height: 56,
                borderRadius: 16,
                background: `linear-gradient(135deg, ${PURPLE} 0%, ${VIOLET} 100%)`,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                boxShadow: `0 8px 32px rgba(139, 92, 246, 0.3)`,
              }}
            >
              <BookOpen size={28} color="white" />
            </div>
            <div>
              <h1 style={{ fontSize: "2rem", fontWeight: 800, margin: 0, color: "#f1f5f9" }}>
                Learning <span style={{ background: "linear-gradient(135deg, #a78bfa 0%, #818cf8 100%)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>Opportunities</span>
              </h1>
              <p style={{ color: "#64748b", margin: "8px 0 0", fontSize: "0.95rem" }}>
                Explore curated courses and internships to boost your career prospects.
              </p>
            </div>
          </div>

          {/* Stats */}
          <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <div style={{ width: 40, height: 40, borderRadius: 10, background: "rgba(139, 92, 246, 0.15)", display: "flex", alignItems: "center", justifyContent: "center", color: PURPLE }}>
                <BookOpen size={20} />
              </div>
              <div>
                <div style={{ fontSize: "0.75rem", color: "#64748b", fontWeight: 600, textTransform: "uppercase" }}>Total Courses</div>
                <div style={{ fontSize: "1.3rem", fontWeight: 700, color: "#f1f5f9" }}>{stats.courses}</div>
              </div>
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <div style={{ width: 40, height: 40, borderRadius: 10, background: "rgba(139, 92, 246, 0.15)", display: "flex", alignItems: "center", justifyContent: "center", color: PURPLE }}>
                <Briefcase size={20} />
              </div>
              <div>
                <div style={{ fontSize: "0.75rem", color: "#64748b", fontWeight: 600, textTransform: "uppercase" }}>Internships</div>
                <div style={{ fontSize: "1.3rem", fontWeight: 700, color: "#f1f5f9" }}>{stats.internships}</div>
              </div>
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <div style={{ width: 40, height: 40, borderRadius: 10, background: "rgba(74, 222, 128, 0.15)", display: "flex", alignItems: "center", justifyContent: "center", color: SUCCESS }}>
                <TrendingUp size={20} />
              </div>
              <div>
                <div style={{ fontSize: "0.75rem", color: "#64748b", fontWeight: 600, textTransform: "uppercase" }}>Total Resources</div>
                <div style={{ fontSize: "1.3rem", fontWeight: 700, color: "#f1f5f9" }}>{stats.total}</div>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Search and Filters */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          style={{ marginBottom: 32, display: "flex", gap: 16, flexWrap: "wrap", alignItems: "flex-end" }}
        >
          {/* Search Bar */}
          <div style={{ flex: 1, minWidth: 250 }}>
            <label style={{ fontSize: "0.8rem", color: "#64748b", fontWeight: 600, textTransform: "uppercase", display: "block", marginBottom: 8 }}>
              Search
            </label>
            <div
              style={{
                position: "relative",
                background: "rgba(15, 23, 42, 0.6)",
                backdropFilter: "blur(12px)",
                border: "1px solid rgba(139, 92, 246, 0.2)",
                borderRadius: 12,
                overflow: "hidden",
                display: "flex",
                alignItems: "center",
              }}
            >
              <div style={{ padding: "0 16px", color: "#64748b" }}>
                <Search size={18} />
              </div>
              <input
                type="text"
                placeholder="Search courses, internships, skills..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                style={{
                  flex: 1,
                  background: "transparent",
                  border: "none",
                  padding: "14px 16px 14px 0",
                  color: "#f1f5f9",
                  fontSize: "0.95rem",
                  outline: "none",
                }}
              />
            </div>
          </div>

          {/* Filter Type */}
          <div>
            <label style={{ fontSize: "0.8rem", color: "#64748b", fontWeight: 600, textTransform: "uppercase", display: "block", marginBottom: 8 }}>
              Type
            </label>
            <select
              value={filterType}
              onChange={(e) => setFilterType(e.target.value as any)}
              style={{
                background: "rgba(15, 23, 42, 0.6)",
                backdropFilter: "blur(12px)",
                border: "1px solid rgba(139, 92, 246, 0.2)",
                borderRadius: 12,
                color: "#f1f5f9",
                padding: "12px 16px",
                fontSize: "0.95rem",
                cursor: "pointer",
                outline: "none",
              }}
            >
              <option value="all">All</option>
              <option value="course">Courses</option>
              <option value="internship">Internships</option>
            </select>
          </div>

          {/* Filter Category */}
          <div>
            <label style={{ fontSize: "0.8rem", color: "#64748b", fontWeight: 600, textTransform: "uppercase", display: "block", marginBottom: 8 }}>
              Category
            </label>
            <select
              value={filterCategory}
              onChange={(e) => setFilterCategory(e.target.value)}
              style={{
                background: "rgba(15, 23, 42, 0.6)",
                backdropFilter: "blur(12px)",
                border: "1px solid rgba(139, 92, 246, 0.2)",
                borderRadius: 12,
                color: "#f1f5f9",
                padding: "12px 16px",
                fontSize: "0.95rem",
                cursor: "pointer",
                outline: "none",
              }}
            >
              <option value="all">All Categories</option>
              {categories.map((cat) => (
                <option key={cat} value={cat}>
                  {cat}
                </option>
              ))}
            </select>
          </div>
        </motion.div>

        {/* Results Count */}
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.15 }} style={{ marginBottom: 24 }}>
          <p style={{ color: "#64748b", fontSize: "0.9rem" }}>
            Showing <span style={{ color: "#a78bfa", fontWeight: 600 }}>{filteredData.length}</span> of {stats.total} results
          </p>
        </motion.div>

        {/* Loading State */}
        {loading && (
          <div style={{ textAlign: "center", padding: "80px 20px" }}>
            <Loader2 size={48} color={PURPLE} style={{ animation: "spin 1s linear infinite" }} />
            <p style={{ color: "#64748b", marginTop: 16 }}>Loading courses and internships...</p>
          </div>
        )}

        {/* Error State */}
        {error && !loading && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            style={{
              textAlign: "center",
              padding: "60px 20px",
              background: "rgba(239, 68, 68, 0.1)",
              borderRadius: 16,
              border: "1px solid rgba(239, 68, 68, 0.2)",
            }}
          >
            <div style={{ fontSize: "2rem", marginBottom: 12 }}>⚠️</div>
            <h3 style={{ fontSize: "1.2rem", fontWeight: 600, color: "#f87171", margin: "0 0 8px 0" }}>
              Failed to load data
            </h3>
            <p style={{ color: "#64748b", margin: 0 }}>{error}</p>
          </motion.div>
        )}

        {/* Courses and Internships Grid */}
        {!loading && !error && filteredData.length > 0 ? (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2, staggerChildren: 0.05 }}
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))",
              gap: 24,
              paddingBottom: 40,
            }}
          >
            {filteredData.map((item, idx) => (
              <CourseCard
                key={item.id}
                title={item.title}
                provider={item.provider}
                skills={item.skills}
                rating={4.5}
                reviews={0}
                duration={item.type === "course" ? "Online Course" : "Internship Opportunity"}
                level={"All Levels"}
                image={item.image}
                logo={item.logo}
                badge={item.type === "course" ? "Course" : "Internship"}
                url={item.url}
                type={item.type as any}
                delay={idx * 0.02}
              />
            ))}
          </motion.div>
        ) : !loading && !error ? (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            style={{
              textAlign: "center",
              padding: "80px 20px",
              background: "rgba(15, 23, 42, 0.3)",
              borderRadius: 16,
              border: "1px solid rgba(139, 92, 246, 0.1)",
            }}
          >
            <div style={{ fontSize: "3rem", marginBottom: 16 }}>🔍</div>
            <h3 style={{ fontSize: "1.3rem", fontWeight: 600, color: "#f1f5f9", margin: "0 0 8px 0" }}>
              No results found
            </h3>
            <p style={{ color: "#64748b", margin: 0, fontSize: "0.95rem" }}>
              Try adjusting your search or filter criteria to find relevant courses and internships.
            </p>
          </motion.div>
        ) : null}
      </AppLayout>
    </ProtectedRoute>
  );
}

