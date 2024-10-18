import React, { useState } from "react";
import { Link } from "react-router-dom";
import "/src/assets/styles/otpVerification.css";
import { verifyOTP } from "../modules/forgotPassword";

const OTPVerification = () => {
  const [sentOTP, setSentOTP] = useState<boolean>(false);
  const [oTP, setOTP] = useState<string>("");

  const handleOTPRequest = async (oTP: string) => {
    setSentOTP(true);
    console.log(oTP);
    let response = await verifyOTP(oTP);
    return response;
  };

  return (
    <>
      <main className="otpVerification_main">
        <h1>eeek!</h1>
        <h2>We emailed you a code</h2>
        <article className="otpVerification_main_article">
          <p>Enter the verification code sent to your email address.</p>
        </article>
        <section className="otpVerification_section">
          {!sentOTP ? (
            <div className="otpVerification_div">
              <label htmlFor="otpVerification_div_label">Enter code:</label>
              <input
                value={oTP}
                id="OTP"
                type="text"
                name="OTP"
                onChange={(e) => setOTP(e.target.value)}
              />
              <button type="button" onClick={() => handleOTPRequest(oTP)}>
                Verify OTP{" "}
              </button>
            </div>
          ) : (
            <div className="otpVerification_div">
              <p style={{ maxWidth: "30vw" }}>
                An <b>email reset link</b> has been sent to the mailbox of the
                email provided. It expires in <strong>15 minutes</strong>.
              </p>
            </div>
          )}
          <span>
            <strong>&lt;-</strong>
          </span>{" "}
          <Link to={"/login"}> Try logging in</Link>
        </section>
      </main>
      <footer className="otpVerification_footer">
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

export default OTPVerification;
