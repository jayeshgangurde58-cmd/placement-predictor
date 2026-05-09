const API_BASE = process.env.NEXT_PUBLIC_ML_API_URL || "http://localhost:8000";

async function apiFetch(path: string, options?: RequestInit) {
  const res = await fetch(`${API_BASE}${path}`, options);
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: "Unknown error" }));
    throw new Error(err.detail || "API request failed");
  }
  return res.json();
}

export interface PredictRequest {
  cgpa: number;
  aptitude: number;
  programming: number;
  communication: number;
  tenth_percentage: number;
  twelfth_percentage: number;
  projects: number;
  internships: number;
}

export interface FeatureImportance {
  factor: string;
  contribution: number;
}

export interface PredictResponse {
  probability: number;
  confidence: string;
  placed: boolean;
  feature_importance: FeatureImportance[];
  min_requirements?: {
    cgpa: number;
    aptitude: number;
    programming: number;
    communication: number;
  };
  explanation?: string;
}

export interface SkillGapRequest {
  skills: string[];
  target_role: string;
}

interface CourseRecommendation {
  course: string;
  platform: string;
  url: string;
}

interface InternshipRecommendation {
  company: string;
  role: string;
  location: string;
  url: string;
}

export interface SkillGapRecommendation {
  skill: string;
  courses: CourseRecommendation[];
  internships: InternshipRecommendation[];
}

export interface SkillGapResponse {
  target_role: string;
  required_skills: string[];
  matched_skills: string[];
  missing_skills: string[];
  match_rate: number;
  skill_gap_index: number;
  recommendations: SkillGapRecommendation[];
  radar_data: { skill: string; has: number }[];
  total_required: number;
  total_matched: number;
  total_missing: number;
}

export interface CourseItem {
  id: number;
  title: string;
  provider: string;
  type: "course" | "internship";
  category: string;
  skills: string[];
  url: string;
  image: string;
  logo: string;
}

export interface CoursesResponse {
  total: number;
  courses: number;
  internships: number;
  items: CourseItem[];
}

export async function getAvailableRoles(): Promise<{ roles: string[] }> {
  return apiFetch("/roles");
}

export async function predictPlacement(data: PredictRequest): Promise<PredictResponse> {
  return apiFetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}

export async function analyzeSkillGap(data: SkillGapRequest): Promise<SkillGapResponse> {
  return apiFetch("/skill-gap", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}

export async function bulkAnalysis(file: File): Promise<any> {
  const form = new FormData();
  form.append("file", file);
  return apiFetch("/bulk-analysis", { method: "POST", body: form });
}

export async function parseResume(file: File): Promise<{ extracted_skills: string[]; count: number }> {
  const form = new FormData();
  form.append("file", file);
  return apiFetch("/parse-resume", { method: "POST", body: form });
}

export async function getAllCourses(): Promise<CoursesResponse> {
  return apiFetch("/courses");
}
