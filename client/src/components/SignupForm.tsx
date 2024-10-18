import { useEffect, useState } from "react";
import users from "../../MOCK_DATA.json" assert { type: "json" };
import { userSignUp } from "../modules/submitNewUser";
import { NewUserType } from "../modules/submitNewUser";
import { initUsers } from "../modules/fetchUsers";
import { debounce } from "../modules/debouncer";
import Error from "../components/ErrorMessage";

const SignupForm = ({
  setLoading,
  setSignedUp,
  setError,
  setErrorMsg,
  error,
  loading,
  errorMsg,
}: any) => {
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");
  const [foundUser, setFoundUser] = useState<boolean | null>(null);
  const [passwordRules, setPasswordRules] = useState<boolean>(false);

  useEffect(() => {
    initUsers();
  }, []);

  useEffect(() => {
    if (username) {
      debounce(username).then((found: boolean) => {
        setFoundUser(found);
      });
    }
  }, [username]);

  let newUser: NewUserType = {
    firstname,
    lastname,
    username,
    email,
    password,
  };

  let userArray: string[] = [];
  users.forEach((user) => {
    userArray.push(user.username);
    return userArray;
  });

  return (
    <div className="signupForm">
      <form
        id="newUserForm"
        action=""
        name="Signup"
        onSubmit={async (e) => {
          e.preventDefault();
          setLoading(true);
          const response = await userSignUp(newUser);
          setError(false);
          setLoading(false);
          if (response === 201) {
            setSignedUp(true);
            setTimeout(() => {
              window.location.reload();
            }, 3000);
          } else {
            setError(true);
            setErrorMsg(`${response.data.detail}`);
          }
        }}
      >
        <section className="newUserForm_names">
          <div className="newUserForm_input">
            <label htmlFor="firstname">Firstname: </label>
            <div>
              <input
                type="text"
                name="firstname"
                id="firstname"
                value={firstname}
                maxLength={32}
                onChange={(e) => {
                  setFirstname(e.target.value);
                }}
                required
              />
            </div>
          </div>
          <div className="newUserForm_input">
            <label htmlFor="lastname">Lastname: </label>
            <div>
              <input
                type="text"
                name="lastname"
                id="lastname"
                value={lastname}
                maxLength={32}
                onChange={(e) => {
                  setLastname(e.target.value);
                }}
                required
              />
            </div>
          </div>
        </section>
        <section className="newUserForm_credentials">
          <div className="newUserForm_input">
            <div className="isUsernameValid">
              <label htmlFor="username">Username: </label>
              <div
                style={{
                  visibility:
                    foundUser === null || username === ""
                      ? "hidden"
                      : "visible",
                }}
              >
                {foundUser ? (
                  <span aria-hidden="true" className="invalidUsername">
                    <svg
                      aria-hidden="true"
                      focusable="false"
                      className="invalidSvg"
                      viewBox="0 0 12 12"
                      width="12"
                      height="12"
                      fill={"#da3633"}
                    >
                      <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
                    </svg>
                  </span>
                ) : (
                  <span aria-hidden="true" className="validUsername">
                    <svg
                      aria-hidden="true"
                      focusable="false"
                      className="validSvg"
                      viewBox="0 0 12 12"
                      width="12"
                      height="12"
                      fill="green"
                    >
                      <path d="M6 0a6 6 0 1 1 0 12A6 6 0 0 1 6 0Zm-.705 8.737L9.63 4.403 8.392 3.166 5.295 6.263l-1.7-1.702L2.356 5.8l2.938 2.938Z"></path>
                    </svg>
                  </span>
                )}
              </div>
            </div>
            <div>
              <input
                type="text"
                name="username"
                id="username"
                className="username"
                value={username}
                maxLength={32}
                onInput={(e) => {
                  setUsername(e.currentTarget.value);
                  //usernameChecker(e.currentTarget.value);
                }}
                required
                style={
                  username === ""
                    ? { border: ".1px solid hsla(0, 0%, 0%, 0.4)" }
                    : foundUser
                      ? { border: "2px solid #da3633" }
                      : { border: "2px solid green" }
                }
              />
            </div>
          </div>
          <div className="newUserForm_input">
            <label htmlFor="email">Email: </label>
            <div>
              <input
                className="email"
                type="email"
                name="email"
                id="email"
                value={email}
                maxLength={256}
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
                required
              />
            </div>
          </div>
        </section>
        <section className="newUserForm_secrets">
          <div className="newUserForm_input">
            <label htmlFor="password">Password: </label>
            <div>
              <input
                type="password"
                name="password"
                id="password"
                value={password}
                minLength={8}
                pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$"
                maxLength={64}
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
                onFocus={() => setPasswordRules(true)}
                required
                title="See the password rules below. Characters allowed: @$!%*?&"
              />
            </div>
          </div>
          <div className="newUserForm_input">
            <label htmlFor="password_assert">Password confirmation: </label>
            <div className=".password_assert_div">
              <input
                type="password"
                name="password_assert"
                id="password_assert"
                value={passwordConfirmation}
                minLength={8}
                pattern={password}
                maxLength={64}
                onChange={(e) => {
                  setPasswordConfirmation(e.target.value);
                }}
                required
                style={
                  passwordConfirmation === ""
                    ? { border: ".1px solid hsla(0, 0%, 0%, 0.4)" }
                    : password === passwordConfirmation
                      ? { border: "2px solid green" }
                      : { border: "2px solid #da3633" }
                }
              />
            </div>
          </div>
        </section>
      </form>
      <section style={{ display: passwordRules ? "contents" : "none" }}>
        <div className="rulesAndErrors">
          <article className="rules_article">
            <p className="passwordRules">
              Your password must include the following:
            </p>
            <p className="passwordInstructions">
              Be at least <strong>12 characters</strong> long
              <br />
              At least one <strong>Upper</strong> & <strong>lower</strong> case
              letter
              <br />
              At least <strong>one number</strong> and <strong>special</strong>{" "}
              character
            </p>
          </article>
          <div className="error_div">
            <div
              className="errorMsg"
              style={{ display: error && !loading ? "contents" : "none" }}
            >
              <Error errorMsg={errorMsg} />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default SignupForm;

//http://localhost:5173/?code=AQTHrJqedZmPOeR59na6d0LSQ4YgZEJapywmwy_4_eomG973HkTa79k50fFEt-eKb5kTWSkxFA5a3pWgJNCCX099gryoBBJxuiUErY31f8jf46JFy642SND-SlVlOwAM2bwkW2blG9X3oVCUPD75HZlLantgRuufHH0XyjGxwg6v2kWV1h2mjRH5gEUKnhLBDMdIi4mKJ6h3Nk_F_pA
