/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect } from "react";
import { userSSOSignUp } from "../modules/submitNewUser";

const LinkedInSignIn = ({ setSignedUp }: any) => {
  const linkedInLogin = `https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=${
    import.meta.env.VITE_LINKEIN_CLIENT_ID
  }&redirect_uri=${encodeURIComponent(
    import.meta.env.VITE_LINKEIN_REDIRECT_URI
  )}&scope=profile%20email%20openid`;

  const handleLinkedInCallback = async () => {
    const provider: string = "linkedin";
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const code = urlParams.get("code");
    if (code) {
      let response = await userSSOSignUp(code, provider);
      if (response === 201) {
        setSignedUp(true);
      }
    }
  };

  useEffect(() => {
    handleLinkedInCallback();
  }, []);

  return (
    <>
      <a href={linkedInLogin}>Continue with LinkedIn</a>
    </>
  );
};

export default LinkedInSignIn;
