import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LandingPage from "./routes/LandingPage";
import LoginPage from "./routes/LoginPage";
import SignupPage from "./routes/SignupPage";
import ForgotPassword from "./routes/ForgotPassword";
import OTPVerification from "./components/OTPVerification";
import ResetPassword from "./components/ResetPassword";
import Welcome from "./components/Welcome";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
  },
  {
    path: "/home",
    element: <Welcome />,
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
  {
    path: "/signup",
    element: <SignupPage />,
  },
  {
    path: "/forgot-password",
    element: <ForgotPassword />,
  },
  {
    path: "/forgot-password/verify-reset",
    element: <OTPVerification />,
  },
  {
    path: "/forgot-password/reset/:resetPIN",
    element: <ResetPassword />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <>
    <RouterProvider router={router} />
  </>
);
