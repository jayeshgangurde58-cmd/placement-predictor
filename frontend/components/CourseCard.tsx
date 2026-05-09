"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Star, ExternalLink } from "lucide-react";

interface CourseCardProps {
  title: string;
  provider: string;
  skills: string[];
  rating: number;
  reviews: number;
  duration: string;
  level: string;
  image?: string;
  logo?: string;
  badge?: string;
  url?: string;
  delay?: number;
  type?: "course" | "internship";
}

export default function CourseCard({
  title,
  provider,
  skills,
  rating,
  reviews,
  duration,
  level,
  image,
  logo,
  badge,
  url,
  delay = 0,
  type = "course",
}: CourseCardProps) {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [logoLoaded, setLogoLoaded] = useState(false);
  const [imageError, setImageError] = useState(false);
  const [logoError, setLogoError] = useState(false);
  const PURPLE = "#8b5cf6";

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, duration: 0.4 }}
      className="glass-card-hover"
      style={{
        position: "relative",
        borderRadius: 16,
        overflow: "hidden",
        cursor: "pointer",
        maxWidth: "100%",
        background: "rgba(15, 23, 42, 0.4)",
        border: "1px solid rgba(139, 92, 246, 0.1)",
      }}
    >
      <a
        href={url || "#"}
        target="_blank"
        rel="noopener noreferrer"
        style={{ textDecoration: "none", color: "inherit", display: "block" }}
      >
        {/* Image/Header Section */}
        <div
          style={{
            width: "100%",
            height: 180,
            background: `linear-gradient(135deg, ${PURPLE}44, #818cf866)`,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            position: "relative",
            overflow: "hidden",
          }}
        >
          {/* Main Background Image */}
          {image && !imageError && (
            <img
              src={image}
              alt={title}
              onLoad={() => setImageLoaded(true)}
              onError={() => setImageError(true)}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
                position: "absolute",
                top: 0,
                left: 0,
                opacity: imageLoaded ? 0.7 : 0,
                transition: "opacity 0.5s ease",
              }}
            />
          )}

          {/* Dark Overlay for contrast */}
          <div style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "linear-gradient(to bottom, rgba(15, 23, 42, 0.2), rgba(15, 23, 42, 0.6))",
            zIndex: 1,
          }} />

          {/* Logo Container Overlay */}
          <div style={{
            width: 72,
            height: 72,
            borderRadius: 20,
            background: "rgba(255, 255, 255, 0.1)",
            backdropFilter: "blur(12px)",
            border: "1px solid rgba(255, 255, 255, 0.2)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            boxShadow: "0 8px 32px rgba(0, 0, 0, 0.4)",
            position: "relative",
            zIndex: 2,
            transition: "transform 0.3s ease",
          }}>
            {logo && !logoError ? (
              <img
                src={logo}
                alt={provider}
                onLoad={() => setLogoLoaded(true)}
                onError={() => setLogoError(true)}
                style={{
                  width: 40,
                  height: 40,
                  objectFit: "contain",
                  display: logoLoaded ? "block" : "none",
                }}
              />
            ) : (
              <div style={{ fontSize: "1.5rem" }}>
                {type === "internship" ? "🏢" : "📚"}
              </div>
            )}
            {!logoLoaded && logo && !logoError && (
              <div style={{ fontSize: "1.2rem", fontWeight: 700, color: "white" }}>
                {provider.charAt(0)}
              </div>
            )}
          </div>

          {/* Badge */}
          {badge && (
            <div
              style={{
                position: "absolute",
                top: 12,
                right: 12,
                background: "rgba(139, 92, 246, 0.9)",
                color: "white",
                padding: "4px 14px",
                borderRadius: 20,
                fontSize: "0.65rem",
                fontWeight: 700,
                backdropFilter: "blur(10px)",
                zIndex: 3,
                textTransform: "uppercase",
                letterSpacing: "0.05em",
                boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
              }}
            >
              {badge}
            </div>
          )}
        </div>

        {/* Content Section */}
        <div style={{ padding: 20 }}>
          {/* Provider */}
          <div style={{ fontSize: "0.8rem", color: "#64748b", marginBottom: 8, textTransform: "uppercase", letterSpacing: "0.06em", fontWeight: 600 }}>
            {provider}
          </div>

          {/* Title */}
          <h3
            style={{
              fontSize: "1.1rem",
              fontWeight: 700,
              color: "#f1f5f9",
              margin: "0 0 12px 0",
              lineHeight: 1.4,
              display: "-webkit-box",
              WebkitLineClamp: 2,
              WebkitBoxOrient: "vertical",
              overflow: "hidden",
            }}
          >
            {title}
          </h3>

          {/* Skills */}
          <div style={{ marginBottom: 16 }}>
            <div style={{ fontSize: "0.7rem", color: "#64748b", marginBottom: 8, fontWeight: 600, textTransform: "uppercase" }}>
              Skills you'll gain:
            </div>
            <div
              style={{
                display: "flex",
                gap: 6,
                flexWrap: "wrap",
              }}
            >
              {skills.slice(0, 4).map((skill, idx) => (
                <span
                  key={idx}
                  style={{
                    fontSize: "0.75rem",
                    background: "rgba(139, 92, 246, 0.15)",
                    color: "#a78bfa",
                    padding: "4px 12px",
                    borderRadius: 12,
                    border: "1px solid rgba(139, 92, 246, 0.3)",
                    whiteSpace: "nowrap",
                  }}
                >
                  {skill}
                </span>
              ))}
              {skills.length > 4 && (
                <span
                  style={{
                    fontSize: "0.75rem",
                    color: "#64748b",
                    padding: "4px 8px",
                  }}
                >
                  +{skills.length - 4}
                </span>
              )}
            </div>
          </div>

          {/* Rating and Reviews */}
          <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 16 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 4 }}>
              <Star size={14} fill={PURPLE} color={PURPLE} />
              <span style={{ fontSize: "0.9rem", fontWeight: 600, color: "#f1f5f9" }}>{rating}</span>
            </div>
            <span style={{ fontSize: "0.8rem", color: "#64748b" }}>
              {reviews.toLocaleString()} reviews
            </span>
          </div>

          {/* Duration and Level */}
          <div style={{ fontSize: "0.8rem", color: "#94a3b8", lineHeight: 1.6 }}>
            <div>{level}</div>
            <div>{duration}</div>
          </div>
        </div>
      </a>
    </motion.div>
  );
}
