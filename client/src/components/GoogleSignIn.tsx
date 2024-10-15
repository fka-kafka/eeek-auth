/* eslint-disable react-hooks/exhaustive-deps */
import React, { useEffect, useRef } from "react";
import { userSSOSignUp } from "../modules/submitNewUser";

const GoogleSignIn = ({ setSignedUp }: any) => {
  const buttonRef = useRef(null);

  useEffect(() => {
    const loadGoogleScript = () => {
      const script = document.createElement("script");
      script.src = "https://accounts.google.com/gsi/client";
      script.async = true;
      script.defer = true;
      script.onload = initializeGoogleSignIn;
      document.body.appendChild(script);
    };

    const initializeGoogleSignIn = () => {
      if (window.google && window.google.accounts) {
        window.google.accounts.id.initialize({
          client_id: import.meta.env.VITE_GSI_CLIENT_ID,
          callback: handleCredentialResponse,
        });

        window.google.accounts.id.renderButton(buttonRef.current, {
          theme: "outline",
          size: "large",
          type: "icon",
          shape: "square",
          text: "signup_with",
        });
      }
    };

    loadGoogleScript();

    return () => {
      // Cleanup function to remove the script when component unmounts
      const script = document.querySelector(
        'script[src="https://accounts.google.com/gsi/client"]'
      );
      if (script) {
        document.body.removeChild(script);
      }
    };
  }, []);

  const handleCredentialResponse = async (data: any) => {
    console.dir(data.credential);
    let response = await userSSOSignUp(data.credential, "google");
    if (response === 201) {
      setSignedUp(true);
    }
  };

  return (
    <div style={{ maxWidth: "140px" }}>
      <div className="gsi" ref={buttonRef}></div>
    </div>
  );
};

export default GoogleSignIn;
