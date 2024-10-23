import React from "react";

const Welcome = () => {
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
