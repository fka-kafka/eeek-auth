import React from "react";
import { useEffect } from "react";

const Welcome = () => {
    useEffect(() => {
      if (window.location.href.includes('code')) {
          window.location.href = window.location.origin + window.location.pathname
      }

      return
    }, [])    

  return (
    <main
      style={{
        backgroundColor: "#034694",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div >
        <h1
          style={{
            textAlign: "center",
            color: "#fff",
            textShadow: '0 4px 4px 0 #00000040'
          }}
        >
          Welcome to eeek!
        </h1>
      </div>
    </main>
  );
};

export default Welcome;
