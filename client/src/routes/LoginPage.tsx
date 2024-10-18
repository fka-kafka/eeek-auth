import { useState } from "react";
import ButtonAndError from "../components/ButtonAndError";
import GoogleSignIn from "../components/GoogleSignIn";
import LinkedInSignIn from "../components/LinkedInSignIn";
import LoginForm from "../components/LoginForm";
import { Link } from "react-router-dom";
import "../assets/styles/loginPage.css";

function LoginPage() {
  const [loading, setLoading] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);
  const [error, setError] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  return (
    <div className="loginPage">
      <section className="loginPage_image"></section>
      <div className="loginPage_content">
        <main className="loginPage_main">
          <h1>eeek!</h1>
          <h2>Log into your account</h2>
          <LoginForm
            className="loginForm"
            setLoading={setLoading}
            setLoggedIn={setLoggedIn}
            setError={setError}
            setErrorMsg={setErrorMsg}
            error={error}
            errorMsg={errorMsg}
            loading={loading}
          />
          <ButtonAndError loading={loading} errorMsg={errorMsg} error={error} />
          <div className="ssoServices">
            <GoogleSignIn setLoggedIn={setLoggedIn} />
            <LinkedInSignIn setLoggedIn={setLoggedIn} />
          </div>
          <p className="notSignedUp">
            Are you new here?{" "}
            <Link className="signup_redirect" to={"/signup"}>
              Sign Up
            </Link>
          </p>
        </main>
        <footer className="loginPage_footer" style={{}}>
          <p className="termsAndConditions">
            By clicking 'Sign Up', you acknowledge you have read and agreed to
            our <span>Terms of Use</span> and <span>Privacy Policy</span>.
          </p>
          <article className="footer_content">
            <p>Give feedback</p>
            <p>&copy; eeek!-inc {new Date().getFullYear()}</p>
            <p>
              <img src="/src/assets/images/privacy.png" height="10px" alt="" />{" "}
              Your Privacy Rights
            </p>
          </article>
        </footer>
      </div>
    </div>
  );
}

export default LoginPage;
