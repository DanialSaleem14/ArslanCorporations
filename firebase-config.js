// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDH5sTGeuxtaq4DcOhHBmZ2FHsZcjm4p7s",
  authDomain: "arslancorportations.firebaseapp.com",
  projectId: "arslancorportations",
  storageBucket: "arslancorportations.firebasestorage.app",
  messagingSenderId: "239611139235",
  appId: "1:239611139235:web:bd495e02aec80cf6b91b16",
  measurementId: "G-H6EG9YF9JH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { app, analytics };
