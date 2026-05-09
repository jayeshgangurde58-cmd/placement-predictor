import {
  collection,
  addDoc,
  getDocs,
  query,
  orderBy,
  limit,
  serverTimestamp,
} from "firebase/firestore";
import { db } from "@/lib/firebase";

// ─── Demo mode: active when Firebase API key is not yet configured ───────────
const IS_DEMO =
  !process.env.NEXT_PUBLIC_FIREBASE_API_KEY ||
  process.env.NEXT_PUBLIC_FIREBASE_API_KEY === "your-firebase-api-key";

export interface PredictionRecord {
  id?: string;
  input: {
    cgpa: number;
    aptitude: number;
    programming: number;
    communication: number;
    tenth_percentage: number;
    twelfth_percentage: number;
    projects: number;
    internships: number;
  };
  result: {
    probability: number;
    confidence: string;
    placed: boolean;
    feature_importance: { factor: string; contribution: number }[];
  };
  timestamp?: any;
}

export interface SkillAnalysisRecord {
  id?: string;
  input: { skills: string[]; target_role: string };
  result: {
    target_role: string;
    required_skills: string[];
    matched_skills: string[];
    missing_skills: string[];
    match_rate: number;
    skill_gap_index: number;
    recommendations: { skill: string; course: string; platform: string; url: string }[];
    radar_data: { skill: string; has: number }[];
    total_required: number;
    total_matched: number;
    total_missing: number;
  };
  timestamp?: any;
}

export interface BulkReportRecord {
  id?: string;
  fileName: string;
  total: number;
  placed: number;
  avg_probability: number;
  placement_rate: number;
  results?: any[];
  errors?: { row: number; error: string }[];
  timestamp?: any;
}

export async function savePrediction(userId: string, record: PredictionRecord) {
  if (IS_DEMO) {
    console.log("Demo Mode: Skipping Firestore write for prediction");
    return { id: "demo-id-" + Date.now() };
  }
  return addDoc(
    collection(db, "users", userId, "predictions"),
    { ...record, timestamp: serverTimestamp() }
  );
}

export async function getPredictions(userId: string, maxCount = 50): Promise<PredictionRecord[]> {
  if (IS_DEMO) {
    return [
      {
        id: "demo-1",
        input: { cgpa: 8.5, aptitude: 80, programming: 85, communication: 75, tenth_percentage: 92, twelfth_percentage: 88, projects: 3, internships: 1 },
        result: { probability: 88, confidence: "High", placed: true, feature_importance: [] },
        timestamp: { toDate: () => new Date() }
      }
    ];
  }
  const q = query(
    collection(db, "users", userId, "predictions"),
    orderBy("timestamp", "desc"),
    limit(maxCount)
  );
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() } as PredictionRecord));
}

export async function saveSkillAnalysis(userId: string, record: SkillAnalysisRecord) {
  if (IS_DEMO) {
    console.log("Demo Mode: Skipping Firestore write for skill analysis");
    return { id: "demo-id-" + Date.now() };
  }
  return addDoc(
    collection(db, "users", userId, "skill_analyses"),
    { ...record, timestamp: serverTimestamp() }
  );
}

export async function getSkillAnalyses(userId: string, maxCount = 50): Promise<SkillAnalysisRecord[]> {
  if (IS_DEMO) {
    return [
      {
        id: "demo-s1",
        input: { skills: ["React", "Node", "Python"], target_role: "Web Developer" },
        result: {
          target_role: "Web Developer",
          required_skills: ["React", "Node", "JavaScript", "HTML", "CSS"],
          matched_skills: ["React", "Node"],
          missing_skills: ["JavaScript", "HTML", "CSS"],
          match_rate: 75,
          skill_gap_index: 0.25,
          recommendations: [
            { skill: "JavaScript", course: "Modern JavaScript", platform: "Udemy", url: "https://udemy.com/js" },
            { skill: "CSS", course: "CSS Flexbox and Grid", platform: "YouTube", url: "https://youtube.com/css" }
          ],
          radar_data: [
            { skill: "React", has: 0.8 },
            { skill: "Node", has: 0.7 },
            { skill: "JavaScript", has: 0.4 }
          ],
          total_required: 5,
          total_matched: 2,
          total_missing: 3,
        },
        timestamp: { toDate: () => new Date() }
      }
    ];
  }
  const q = query(
    collection(db, "users", userId, "skill_analyses"),
    orderBy("timestamp", "desc"),
    limit(maxCount)
  );
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() } as SkillAnalysisRecord));
}

export async function saveBulkReport(userId: string, record: BulkReportRecord) {
  if (IS_DEMO) {
    console.log("Demo Mode: Skipping Firestore write for bulk report");
    return { id: "demo-id-" + Date.now() };
  }
  return addDoc(
    collection(db, "users", userId, "bulk_reports"),
    { ...record, timestamp: serverTimestamp() }
  );
}

export async function getBulkReports(userId: string, maxCount = 20): Promise<BulkReportRecord[]> {
  if (IS_DEMO) {
    return [
      {
        id: "demo-b1",
        fileName: "students_june_2024.csv",
        total: 50,
        placed: 35,
        avg_probability: 72,
        placement_rate: 70,
        timestamp: { toDate: () => new Date() }
      }
    ];
  }
  const q = query(
    collection(db, "users", userId, "bulk_reports"),
    orderBy("timestamp", "desc"),
    limit(maxCount)
  );
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() } as BulkReportRecord));
}

export function formatTimestamp(ts: any): string {
  if (!ts) return "—";
  const date = ts.toDate ? ts.toDate() : new Date(ts);
  return date.toLocaleString("en-IN", {
    day: "2-digit", month: "short", year: "numeric",
    hour: "2-digit", minute: "2-digit",
  });
}
