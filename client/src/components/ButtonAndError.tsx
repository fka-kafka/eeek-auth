import React from "react";
import Throbber from "./Throbber";
import Error from "./ErrorMessage";

const ButtonAndError = ({ loading, error, errorMsg }: any) => {
  return (
    <>
      <div>
        <div>
          {loading ? (
            ""
          ) : (
            <button
              style={{
                margin: "4px 0",
              }}
              type="submit"
              form="newUserForm"
            >
              Sign Up
            </button>
          )}
        </div>
        <div>
          {loading ? <Throbber /> : error ? <Error errorMsg={errorMsg} /> : ""}
        </div>
      </div>
    </>
  );
};

export default ButtonAndError;
