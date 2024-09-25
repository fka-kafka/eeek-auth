import { useState } from "react";
import { userLogIn } from "../modules/submitNewUser";

const LoginForm = ({ setLoading, setLoggedIn, setError, setErrorMsg }: any) => {
  const [credential, setCredential] = useState("");
  const [password, setPassword] = useState("");

  return (
    <>
      <h1>eeek!</h1>
      <form
        id="newUserForm"
        action=""
        name="Signup"
        onSubmit={async (e) => {
          e.preventDefault();
          setLoading(true);
          const response = await userLogIn({
            credential: credential,
            secret: password,
          });
          setLoading(false);
          if (response === 201) {
            setLoggedIn(true);
            setTimeout(() => {
              window.location.reload();
            }, 3000);
          } else {
            setError(true);
            setErrorMsg(
              `${response.status} ${response.statusText}: ${response.data.detail}`
            );
          }
        }}
      >
        <div>
          <label htmlFor="email">Email: </label>
          <div>
            <input
              className="email"
              type="email"
              name="email"
              id="email"
              value={credential}
              maxLength={256}
              onChange={(e) => {
                setCredential(e.target.value);
              }}
              required
            />
          </div>
        </div>
        <div>
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
    </>
  );
};

export default LoginForm;
