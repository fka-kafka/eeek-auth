import { useState } from "react";
import SignupForm from "./components/SignupForm";
import Welcome from "./components/Welcome";
import ButtonAndError from "./components/ButtonAndError";
import GoogleSignIn from "./components/GoogleSignIn";
import LinkedInSignIn from "./components/LinkedInSignIn";

function SignupPage() {
  const [loading, setLoading] = useState(false);
  const [signedUp, setSignedUp] = useState(false);
  const [error, setError] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  return (
    <>
      <main>
        <div>
          {!signedUp ? (
            <>
              <SignupForm
                setLoading={setLoading}
                setSignedUp={setSignedUp}
                setError={setError}
                setErrorMsg={setErrorMsg}
              />
              <ButtonAndError
                loading={loading}
                errorMsg={errorMsg}
                error={error}
              />
              <GoogleSignIn setSignedUp={setSignedUp}/>
              <LinkedInSignIn setSignedUp={setSignedUp} />
            </>
          ) : (
            <Welcome />
          )}
        </div>
      </main>
    </>
  );
}

export default SignupPage;
