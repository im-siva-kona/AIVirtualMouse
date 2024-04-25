// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCZNL6JnrJhOpWHFjSD_r_pqXonvt1YCZI",
  authDomain: "a2zdukhan.firebaseapp.com",
  projectId: "a2zdukhan",
  storageBucket: "a2zdukhan.appspot.com",
  messagingSenderId: "747128117331",
  appId: "1:747128117331:web:c8e7728d979a4f9958cea6",
  measurementId: "G-RQRT2H78FM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);