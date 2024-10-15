import { useState } from "react";
import "../assets/styles/signupPage.css";
import SignupForm from "../components/SignupForm";
import ButtonAndError from "../components/ButtonAndError";
import GoogleSignIn from "../components/GoogleSignIn";
import LinkedInSignIn from "../components/LinkedInSignIn";
import { Link } from "react-router-dom";

function SignupPage() {
  const [loading, setLoading] = useState(false);
  const [signedUp, setSignedUp] = useState(false);
  const [error, setError] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  return (
    <div className="signupPage">
      <main className="signupPage_main">
        <h1>eeek!</h1>
        <h2>Create your account</h2>
        <div className="signupPage_content">
          <SignupForm
            setLoading={setLoading}
            setSignedUp={setSignedUp}
            setError={setError}
            setErrorMsg={setErrorMsg}
            error={error}
            errorMsg={errorMsg}
            loading={loading}
          />
          <ButtonAndError loading={loading} />
          <div className="ssoServices">
            <GoogleSignIn setSignedUp={setSignedUp} />
            <LinkedInSignIn setSignedUp={setSignedUp} />
          </div>
          <p className="alreadySignedUp">
            Already have an account?{" "}
            <Link className="login_redirect" to={"/login"}>
              Log in
            </Link>
          </p>
        </div>
      </main>
      <footer className="signupPage_footer">
        <p className="termsAndConditions">
          By clicking 'Sign Up', you acknowledge you have read and agreed to our{" "}
          <span>Terms of Use</span> and <span>Privacy Policy</span>.
        </p>
        <article className="footer_content">
          <p>Give feedback</p>
          <p>&copy; eeek!-inc {new Date().getFullYear()}</p>
          <p>
            <img src="/src/assets/privacy.png" height="10px" alt="" /> Your
            Privacy Rights
          </p>
        </article>
      </footer>
    </div>
  );
}

export default SignupPage;
