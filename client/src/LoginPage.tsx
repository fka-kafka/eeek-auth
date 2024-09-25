import { useState } from "react";
import Welcome from "./components/Welcome";
import ButtonAndError from "./components/ButtonAndError";
import GoogleSignIn from "./components/GoogleSignIn";
import LinkedInSignIn from "./components/LinkedInSignIn";
import LoginForm from "./components/LoginForm";

function LoginPage() {
  const [loading, setLoading] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);
  const [error, setError] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  return (
    <>
      <main>
        <div>
          {!loggedIn ? (
            <>
              <LoginForm
                setLoading={setLoading}
                setLoggedIn={setLoggedIn}
                setError={setError}
                setErrorMsg={setErrorMsg}
              />
              <ButtonAndError
                loading={loading}
                errorMsg={errorMsg}
                error={error}
              />
              <GoogleSignIn setLoggedIn={setLoggedIn}/>
              <LinkedInSignIn setLoggedIn={setLoggedIn} />
            </>
          ) : (
            <Welcome />
          )}
        </div>
      </main>
    </>
  );
}

export default LoginPage;
