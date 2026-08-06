// Firebase configuration shared by every page that needs Auth / Firestore.
// Loaded as an ES module: <script type="module" src="firebase-config.js"></script>
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAnalytics, isSupported as analyticsIsSupported } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-analytics.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyAbWkROth8A9pyKdeOrduwWAZ15xfhi-KQ",
  authDomain: "arslancorporation-ca6ad.firebaseapp.com",
  projectId: "arslancorporation-ca6ad",
  storageBucket: "arslancorporation-ca6ad.firebasestorage.app",
  messagingSenderId: "79477537175",
  appId: "1:79477537175:web:bd4a5e852f0562a2f12cd2",
  measurementId: "G-532XTLT884"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Analytics only works over https/localhost, never in a file:// preview.
analyticsIsSupported().then((supported) => {
  if (supported) getAnalytics(app);
}).catch(() => {});

export { app, auth, db };
