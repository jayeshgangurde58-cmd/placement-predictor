# Smart Placement Predictor & Skill Gap Analyzer — Implementation Plan

## Overview

A production-ready, full-stack AI web application that predicts student placement probability and analyzes skill gaps. Built with **Next.js + Tailwind CSS** on the frontend, **Python FastAPI** as the ML backend, and **Firebase** for auth, database, and storage.

The app is designed with a modern SaaS dashboard aesthetic, modular architecture, and scalable deployment strategy.

---

## User Review Required

> [!IMPORTANT]
> **No Firebase credentials yet.** You'll need to create a Firebase project and provide credentials before the Auth/DB/Storage features can be tested live. I'll wire everything up so you only need to paste your config.

> [!IMPORTANT]
> **ML Model Strategy**: For the prediction engine, I'll use a **logistic regression / random forest model** trained on a synthetic placement dataset (realistic distributions). This is embedded directly in the FastAPI backend — no external API calls needed. You can swap in a real trained model later.

> [!WARNING]
> **Local-first build**: I'll build both the Next.js frontend and the FastAPI backend to run locally first for development. The architecture will be fully deployable to Vercel + Render with minimal config changes.

---

## Proposed Changes

### 📁 Project Structure

```
c:\Users\jayes\Placement\
├── frontend/                    # Next.js App
│   ├── app/
│   │   ├── (auth)/
│   │   │   ├── login/
│   │   │   └── register/
│   │   ├── dashboard/
│   │   ├── predict/
│   │   ├── skill-gap/
│   │   ├── bulk/
│   │   ├── history/
│   │   └── admin/
│   ├── components/              # Reusable UI components
│   ├── lib/                     # Firebase config, API helpers
│   ├── hooks/                   # Custom React hooks
│   └── public/
│
└── backend/                     # Python FastAPI ML API
    ├── main.py                  # FastAPI app + all routes
    ├── model/
    │   ├── train_model.py       # Model training script
    │   └── placement_model.pkl  # Trained model artifact
    ├── services/
    │   ├── predictor.py         # Placement prediction logic
    │   ├── skill_gap.py         # Skill gap analysis logic
    │   └── bulk_processor.py   # CSV batch processing
    └── requirements.txt
```

---

### 🖥️ Frontend — Next.js 14 (App Router)

#### [NEW] `frontend/` — Next.js Application

**Pages & Routes:**

| Route | Description |
|---|---|
| `/login` | Firebase email + Google auth |
| `/register` | New user signup |
| `/dashboard` | Main analytics dashboard |
| `/predict` | Single student placement prediction |
| `/skill-gap` | Skill gap analyzer (manual + resume upload) |
| `/bulk` | CSV bulk upload & batch analysis |
| `/history` | Past predictions & reports |
| `/admin` | Admin panel (user management, analytics) |

**Key Components:**
- `Navbar` — Glassmorphism sidebar nav with user avatar
- `PredictionForm` — 6-input form with animated results card
- `ProbabilityGauge` — Animated radial gauge (0–100%)
- `SkillGapChart` — Radar chart of skills vs. job role requirements
- `BulkUploader` — Drag-and-drop CSV with progress bar
- `HistoryTable` — Filterable, exportable table of past predictions
- `DashboardCharts` — Recharts line/bar charts for trends
- `FeatureImportanceBar` — Horizontal bar chart showing CGPA %, skills %, etc.
- `AdminTable` — User analytics management view

**Design System:**
- Dark mode SaaS aesthetic (deep navy + purple/violet accents)
- Glassmorphism cards with backdrop blur
- Smooth Framer Motion animations on result reveals
- Google Font: **Inter**
- Recharts for all data visualizations

---

### 🐍 Backend — Python FastAPI

#### [NEW] `backend/main.py`

Three core API endpoints:

```
POST /predict          → Single student ML prediction
POST /skill-gap        → Skill gap analysis for a profile
POST /bulk-analysis    → Process CSV, return per-student results
GET  /health           → Health check
```

#### [NEW] `backend/services/predictor.py`
- Loads trained `placement_model.pkl`
- Feature engineering (normalize inputs)
- Returns: `{ probability, confidence, feature_importance }`

#### [NEW] `backend/services/skill_gap.py`
- Job role → required skills mapping database
- Computes Skill Gap Index (SGI) = 1 − (matched/required)
- Returns: `{ missing_skills, sgi, match_rate, recommendations }`

#### [NEW] `backend/services/bulk_processor.py`
- Reads CSV rows
- Runs predictor + skill_gap per row
- Returns structured JSON array

#### [NEW] `backend/model/train_model.py`
- Generates synthetic training data (realistic distributions)
- Trains Random Forest classifier
- Saves `placement_model.pkl` with feature importance

---

### 🔥 Firebase Integration

#### [NEW] `frontend/lib/firebase.ts`
- Firebase app initialization
- Auth, Firestore, Storage exports

#### Firestore Schema:

```
users/{userId}
  - email, name, role (user/admin), createdAt

users/{userId}/predictions/{predictionId}
  - input: { cgpa, aptitude, programming, communication, projects, internships }
  - result: { probability, confidence, feature_importance }
  - timestamp

users/{userId}/skill_analyses/{analysisId}
  - input: { skills[], targetRole }
  - result: { missing_skills[], sgi, match_rate, recommendations[] }
  - timestamp

users/{userId}/bulk_reports/{reportId}
  - fileName, uploadedAt
  - resultsUrl (Firebase Storage link)
  - summary: { total, avgProbability, topSkillGaps[] }
```

---

### ⚙️ Configuration Files

#### [NEW] `frontend/.env.local`
```env
NEXT_PUBLIC_FIREBASE_API_KEY=...
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=...
NEXT_PUBLIC_FIREBASE_PROJECT_ID=...
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=...
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=...
NEXT_PUBLIC_FIREBASE_APP_ID=...
NEXT_PUBLIC_ML_API_URL=http://localhost:8000
```

#### [NEW] `backend/.env`
```env
CORS_ORIGINS=http://localhost:3000
```

---

## Open Questions

> [!IMPORTANT]
> **Do you have Firebase credentials?** If yes, share them (or just the Project ID) and I'll pre-fill the config. If not, I'll leave placeholders and document the setup step clearly.

> [!IMPORTANT]
> **Resume parsing scope**: For the Skill Gap page, should resume upload (PDF) extract skills automatically via NLP, or is manual skill input sufficient for the initial build? NLP parsing requires an additional library (`pdfplumber` + skill extraction logic) that I can include.

> [!NOTE]
> **Admin panel**: I'll build a basic admin panel that shows all users and analytics. It will use a Firestore `role` field to gate access. Do you want this included in the initial build?

---

## Verification Plan

### Automated / Local Testing
1. `cd backend && uvicorn main:app --reload` → test all 3 API endpoints via `/docs` (FastAPI Swagger)
2. `cd frontend && npm run dev` → verify all pages load
3. Test full prediction flow: fill form → see gauge + feature importance
4. Test skill gap: input skills + select role → see radar chart + recommendations
5. Test bulk upload: upload a sample CSV → see per-student results table
6. Test history: verify Firestore writes + history page reads

### Browser Validation
- Open the running app in a browser subagent and capture a recording of the full flow

### Manual Verification
- User to verify Firebase auth (login/register) with their own Firebase project credentials
