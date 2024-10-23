import React from "react";
import Throbber from "./Throbber";
import "../assets/styles/submit.css";

const ButtonAndError = ({ loading, signedUp, loggedIn }: any) => {
  let page = window.location.href;

  return (
    <>
      <div
        className="buttonAndError"
        style={{
          margin: "2vh 0",
        }}
      >
        <div
          className="button_div"
          style={{ display: loading ? "none" : "contents" }}
        >
          {page.includes("login") ? (
            <button className="loginUser" type="submit" form="loginUserForm" disabled={loggedIn ? true : false}>
              Log In
            </button>
          ) : (
            <button
              className="submitNewUser"
              type="submit"
              form="newUserForm"
              disabled={signedUp ? true : false}
            >
              Sign Up
            </button>
          )}
        </div>
        <div>{loading ? <Throbber /> : ""}</div>
      </div>
    </>
  );
};

export default ButtonAndError;
