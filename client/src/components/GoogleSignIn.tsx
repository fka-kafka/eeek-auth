/* eslint-disable react-hooks/exhaustive-deps */
import React, { useEffect, useRef } from "react";
import { userSSOSignUp, userSSOLogIn } from "../modules/submitNewUser";
import {useNavigate} from 'react-router-dom';

const GoogleSignIn = ({ setSignedUp, setLoggedIn }: any) => {
  const buttonRef = useRef(null);
  const navigate = useNavigate()

  useEffect(() => {
    const loadGoogleScript = () => {
      const script = document.createElement("script");
      script.src = import.meta.env.VITE_GSI_SCRIPT_SRC;
      script.async = true;
      script.defer = true;
      script.onload = initializeGoogleSignIn;
      document.body.appendChild(script);
    };

    const initializeGoogleSignIn = () => {
      if (window.google && window.google.accounts && buttonRef.current) {
        window.google.accounts.id.initialize({
          client_id: import.meta.env.VITE_GSI_CLIENT_ID,
          callback: handleCredentialResponse,
        });

        window.google.accounts.id.renderButton(buttonRef.current!, {
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
        'script[src="https://accounts.google.com/gsi/client"]',
      );
      if (script) {
        document.body.removeChild(script);
      }
    };
  }, []);

  const handleCredentialResponse = async (data: any) => {
    console.dir(data.credential);
    let response = window.location.href.includes("login")
      ? await userSSOLogIn(data.credential, "google")
      : await userSSOSignUp(data.credential, "google");
    if (response === 201) {
      setSignedUp(true);
      setTimeout(() => {
        navigate("/home")
      }, 2000);
    } else if (response === 200) {
        setLoggedIn(true)
        setTimeout(() => {
          navigate('/home')
        }, 2000);
    }
  };

  return (
    <div style={{ maxWidth: "140px" }}>
      <div className="gsi" ref={buttonRef}></div>
    </div>
  );
};

export default GoogleSignIn;
