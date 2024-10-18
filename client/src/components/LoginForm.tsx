import { useState } from "react";
import { userLogIn } from "../modules/submitNewUser";
import Error from "./ErrorMessage";

const LoginForm = ({
  setLoading,
  setLoggedIn,
  setError,
  setErrorMsg,
  error,
  errorMsg,
  loading,
}: any) => {
  const [credential, setCredential] = useState("");
  const [password, setPassword] = useState("");

  return (
    <>
      <form
        id="loginUserForm"
        action=""
        name="Login"
        onSubmit={async (e) => {
          e.preventDefault();
          setLoading(true);
          const response = await userLogIn(credential, password);
          setLoading(false);
          if (response.status === 200) {
            setLoggedIn(true);
            setTimeout(() => {
              window.location.reload();
            }, 3000);
          } else {
            setError(true);
            setErrorMsg(`${response.data.detail}`);
          }
        }}
      >
        <div className="credentials_div">
          <label htmlFor="credential">Email or Username: </label>
          <div>
            <input
              className="credential"
              type="text"
              name="credential"
              id="credential"
              value={credential}
              maxLength={256}
              onChange={(e) => {
                setCredential(e.target.value);
              }}
              required
            />
          </div>
        </div>
        <div className="password_div">
          <label htmlFor="password">Password: </label>
          <div>
            <input
              type="password"
              name="password"
              id="password"
              value={password}
              minLength={8}
              pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
              maxLength={64}
              onChange={(e) => {
                setPassword(e.target.value);
              }}
              required
            />
          </div>
        </div>
      </form>
      <div className="forgotPassword">
        <a href="/forgot-password">Forgot password?</a>
      </div>
      <div className="error_div">
        <div
          className="errorMsg"
          style={{ display: error && loading === false ? "contents" : "none" }}
        >
          <Error errorMsg={errorMsg} />
        </div>
      </div>
    </>
  );
};

export default LoginForm;
