import { useState } from "react";
import Form from "./components/Form";
import Welcome from "./components/Welcome";
import ButtonAndError from "./components/ButtonAndError";

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
              <Form
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
