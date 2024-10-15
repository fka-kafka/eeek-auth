import { useState } from "react";
import Throbber from "./Throbber";
import "../assets/styles/resetPassword.css";
import { resetPassword } from "../modules/forgotPassword";

const ResetPassword = () => {
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");
  const [resetting, setResetting] = useState(false);

  const handleReset = async (password: string) => {
    const resetUrl = new URL(window.location.href);
    setResetting(true);
    let response = await resetPassword(resetUrl, password);
    console.log(response);
    setResetting(false);
  };

  return (
    <div className="resetPassword_wrapper">
      <main className="resetPassword_main">
        <h1>eeek!</h1>
        <h2>Reset password</h2>
        <section className="resetPassword_section">
          <form
            action=""
            className="resetPasswordForm"
            id="resetPasswordForm"
            name="Reset"
            onSubmit={async (e) => {
              e.preventDefault();
              handleReset(password);
            }}
          >
            <section className="resetPasswordForm_secrets">
              <div className="resetPasswordForm_input">
                <label htmlFor="password">Password: </label>
                <div>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    value={password}
                    minLength={12}
                    pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$"
                    maxLength={64}
                    onChange={(e) => {
                      setPassword(e.target.value);
                    }}
                    required
                    title="See the password rules below. Characters allowed: @$!%*?&"
                  />
                </div>
              </div>
              <div className="resetPasswordForm_input">
                <label htmlFor="password_assert">Password confirmation: </label>
                <div className=".password_assert_div">
                  <input
                    type="password"
                    name="password_assert"
                    id="password_assert"
                    value={passwordConfirmation}
                    minLength={12}
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
        </section>
        <div className="buttonDiv">
          {resetting ? (
            <Throbber />
          ) : (
            <button
              className="resetPassword"
              type="submit"
              form="resetPasswordForm"
            >
              Reset
            </button>
          )}
        </div>
      </main>
      <footer className="resetPassword_footer">
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
};

export default ResetPassword;
