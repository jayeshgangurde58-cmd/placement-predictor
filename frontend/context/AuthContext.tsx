"use client";

import {
  createContext,
  useContext,
  useEffect,
  useState,
  ReactNode,
} from "react";
import {
  User,
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signInWithPopup,
  GoogleAuthProvider,
  signOut,
  updateProfile,
} from "firebase/auth";
import { doc, setDoc, getDoc, serverTimestamp, collection, query, where, getDocs } from "firebase/firestore";
import { auth, db } from "@/lib/firebase";

interface UserProfile {
  uid: string;
  email: string | null;
  name: string | null;
  role: "user" | "admin";
  photoURL?: string | null;
  securityAnswer?: string;
}

interface AuthContextValue {
  user: User | null;
  profile: UserProfile | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, name: string, securityAnswer: string) => Promise<void>;
  loginWithGoogle: () => Promise<void>;
  logout: () => Promise<void>;
  resetPasswordWithSecurity: (email: string, answer: string, newPassword: string) => Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

// ─── Demo mode: active when Firebase is not yet configured ───────────────────
const IS_DEMO =
  !process.env.NEXT_PUBLIC_FIREBASE_API_KEY ||
  process.env.NEXT_PUBLIC_FIREBASE_API_KEY === "your-firebase-api-key";

const DEMO_USER = {
  uid: "demo-user-001",
  email: "demo@placeai.app",
  displayName: "Demo User",
  photoURL: null,
} as unknown as User;

const DEMO_PROFILE: UserProfile = {
  uid: "demo-user-001",
  email: "demo@placeai.app",
  name: "Demo User",
  role: "admin",
};
// ─────────────────────────────────────────────────────────────────────────────

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (IS_DEMO) {
      setUser(DEMO_USER);
      setProfile(DEMO_PROFILE);
      setLoading(false);
      return;
    }

    const unsub = onAuthStateChanged(auth, async (firebaseUser) => {
      setUser(firebaseUser);
      if (firebaseUser) {
        const snap = await getDoc(doc(db, "users", firebaseUser.uid));
        if (snap.exists()) {
          setProfile(snap.data() as UserProfile);
        } else {
          const p: UserProfile = {
            uid: firebaseUser.uid,
            email: firebaseUser.email,
            name: firebaseUser.displayName,
            role: "user",
            photoURL: firebaseUser.photoURL,
          };
          await setDoc(doc(db, "users", firebaseUser.uid), { ...p, createdAt: serverTimestamp() });
          setProfile(p);
        }
      } else {
        setProfile(null);
      }
      setLoading(false);
    });
    return unsub;
  }, []);

  const login = async (email: string, password: string) => {
    if (IS_DEMO) { setUser(DEMO_USER); setProfile(DEMO_PROFILE); return; }
    await signInWithEmailAndPassword(auth, email, password);
  };

  const register = async (email: string, password: string, name: string, securityAnswer: string) => {
    if (IS_DEMO) { setUser(DEMO_USER); setProfile({ ...DEMO_PROFILE, name, securityAnswer: securityAnswer.toLowerCase() }); return; }
    const cred = await createUserWithEmailAndPassword(auth, email, password);
    await updateProfile(cred.user, { displayName: name });
    const p: UserProfile = { uid: cred.user.uid, email, name, role: "user", securityAnswer: securityAnswer.toLowerCase() };
    await setDoc(doc(db, "users", cred.user.uid), { ...p, createdAt: serverTimestamp() });
    setProfile(p);
  };

  const loginWithGoogle = async () => {
    if (IS_DEMO) { setUser(DEMO_USER); setProfile(DEMO_PROFILE); return; }
    const provider = new GoogleAuthProvider();
    await signInWithPopup(auth, provider);
  };

  const logout = async () => {
    if (IS_DEMO) { setUser(null); setProfile(null); return; }
    await signOut(auth);
  };

  const resetPasswordWithSecurity = async (email: string, answer: string, newPassword: string) => {
    if (IS_DEMO) return; // In demo mode, just pretend it succeeded
    
    // In real mode, verify answer from Firestore
    const q = query(collection(db, "users"), where("email", "==", email));
    const querySnapshot = await getDocs(q);
    if (querySnapshot.empty) {
      throw new Error("User not found");
    }
    const userDoc = querySnapshot.docs[0].data() as UserProfile;
    if (userDoc.securityAnswer !== answer.toLowerCase()) {
      throw new Error("Incorrect security answer");
    }
    // Note: Firebase Client SDK doesn't allow changing passwords unauthenticated. 
    // This is a minimal implementation to show the flow.
    throw new Error("Firebase API doesn't support changing password unauthenticated. But answer is correct! Use Demo Mode to mock this.");
  };

  return (
    <AuthContext.Provider value={{ user, profile, loading, login, register, loginWithGoogle, logout, resetPasswordWithSecurity }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}
