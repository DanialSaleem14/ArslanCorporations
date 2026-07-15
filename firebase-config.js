// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCW0xnsyfLy1a7KtqnLsQUWD6fALBptp-Q",
  authDomain: "arslancorporation.firebaseapp.com",
  projectId: "arslancorporation",
  storageBucket: "arslancorporation.firebasestorage.app",
  messagingSenderId: "812939195224",
  appId: "1:812939195224:web:05e48679a75fb64f75ab2d",
  measurementId: "G-YT1EZECKNE"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { app, analytics };
