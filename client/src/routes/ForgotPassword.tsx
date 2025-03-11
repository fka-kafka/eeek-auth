import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "/src/assets/styles/forgotPassword.css";
import { sendOTP } from "../modules/forgotPassword";
import { Link } from "react-router-dom";
import Throbber from "../components/Throbber";

const ForgotPassword = () => {
  const [sentOTP, setSentOTP] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [email, setEmail] = useState<string>("");
  const navigate = useNavigate();

  const handleOTPRequest = async (email: string) => {
    setSentOTP(true);
    setLoading(true)

    let response = await sendOTP(email);
    setLoading(false)
    console.log(response);
    if (response.status === 202) {
      setTimeout(() => {
        navigate("/forgot-password/verify-reset");
      }, 3000);
    }
  };

  return (
    <>
      <main className="forgotPassword_main">
        <h1>eeek!</h1>
        <h2>Forgot Password?</h2>
        <article className="forgotPassword_main_article">
          <p>
            No worries. Enter the <span>email address</span> registered to your
            account and we will send you an OTP to confirm the reset attempt
          </p>
        </article>
        <section className="forgotPassword_section">
          {!sentOTP ? (
            <div className="forgotPassword_div">
              <label htmlFor="recoveryEmail">Enter email address:</label>
              <input
                value={email}
                id="recoveryEmail"
                type="email"
                name="email"
                onChange={(e) => setEmail(e.target.value)}
              />
              <button type="button" onClick={() => handleOTPRequest(email)}>
                Send OTP{" "}
              </button>
            </div>
          ) : !loading ? (
            <div className="forgotPasswordInfo_div">
              <svg
                width="50px"
                height="50px"
                viewBox="0 0 48 48"
                version="1"
                xmlns="http://www.w3.org/2000/svg"
                enableBackground="new 0 0 48 48"
              >
                <polygon
                  fill="#43A047"
                  points="40.6,12.1 17,35.7 7.4,26.1 4.6,29 17,41.3 43.4,14.9"
                />
              </svg>
              <p style={{ maxWidth: "30vw" }}>
                An OTP has been sent to the mailbox of the email provided. It
                expires in <strong>15 minutes</strong>. You will be redirected to the Verify OTP page.
              </p>
            </div>
          ) : <div className="forgotPasswordInfo_div"><Throbber /> </div>}
          <span>
            <strong>&lt;-</strong>
          </span>{" "}
          <Link to={"/login"}> Return to login</Link>
        </section>
      </main>
      <footer className="forgotPassword_footer">
        <article className="footer_content">
          <p>Give feedback</p>
          <p>&copy; eeek!-inc {new Date().getFullYear()}</p>
          <p>
            <img src="/src/assets/images/privacy.png" height="10px" alt="" /> Your
            Privacy Rights
          </p>
        </article>
      </footer>
    </>
  );
};

export default ForgotPassword;
