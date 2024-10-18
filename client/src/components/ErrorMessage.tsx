import React from "react";

const Error = ({ errorMsg }: any) => {
  return (
    <>
      <p style={{ marginLeft: "10px", textAlign: "center" }}>
        <span style={{ color: "#da3633", fontSize: "12px" }}>
          <b>{errorMsg}</b>
        </span>
      </p>
    </>
  );
};

export default Error;
