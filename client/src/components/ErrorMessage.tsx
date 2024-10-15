import React from "react";

const Error = ({ errorMsg }: any) => {
  return (
    <>
      <p style={{ marginLeft: "10px" }}>
        <span style={{ color: "#da3633", fontSize: "12px" }}>
          <strong>
            <span >{errorMsg}</span>
          </strong>
        </span>
      </p>
    </>
  );
};

export default Error;
