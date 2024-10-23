import React from "react";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { userSignUp } from "../modules/submitNewUser";
import { NewUserType } from "../modules/submitNewUser";
import { initUsers } from "../modules/fetchUsers";
import { debounce } from "../modules/debouncer";
import "../form.css";

const Form = ({ setLoading, setSignedUp, setError, setErrorMsg }: any) => {
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");
  const [foundUser, setFoundUser] = useState<boolean | null>(null);
  const navigate = useNavigate()

  useEffect(() => {
    initUsers();
  }, []);

  useEffect(() => {
    if (username) {
      debounce(username).then((found: boolean) => {
        setFoundUser(found);
      });
    }
  }, [username]);

  let newUser: NewUserType = {
    firstname,
    lastname,
    username,
    email,
    password,
  };

  return (
    <>
      <h1>eeek!</h1>
      <form
        id="newUserForm"
        action=""
        name="Signup"
        onSubmit={async (e) => {
          e.preventDefault();
          setLoading(true);
          const response = await userSignUp(newUser);
          setLoading(false);
          if (response === 201) {
            setSignedUp(true);
            setTimeout(() => {
              navigate('/login')
            }, 3000);
          } else {
            setError(true);
            setErrorMsg(
              `${response.status} ${response.statusText}: ${response.data.detail}`
            );
          }
        }}
      >
        <section className="names">
          <div>
            <label htmlFor="firstname">Firstname: </label>
            <div>
              <input
                type="text"
                name="firstname"
                id="firstname"
                value={firstname}
                maxLength={32}
                onChange={(e) => {
                  setFirstname(e.target.value);
                }}
                required
              />
            </div>
          </div>
          <div>
            <label htmlFor="lastname">Lastname: </label>
            <div>
              <input
                type="text"
                name="lastname"
                id="lastname"
                value={lastname}
                maxLength={32}
                onChange={(e) => {
                  setLastname(e.target.value);
                }}
                required
              />
            </div>
          </div>
        </section>
        <section className="credentials">
          <div>
            <label htmlFor="username">Username: </label>
            <div>
              <input
                type="text"
                name="username"
                id="username"
                value={username}
                maxLength={32}
                onInput={(e) => {
                  setUsername(e.currentTarget.value);
                  //usernameChecker(e.currentTarget.value);
                }}
                required
              />
              <div>
                <button>
                  {username !== "" ? (
                    foundUser ? (
                      <svg
                        width="18"
                        height="18"
                        viewBox="0 0 24 24"
                        fill="none"
                      >
                        <path
                          d="M10.9997 8.24997V11.9166M10.9997 15.5833H11.0089M9.7304 3.56738L2.19092 16.5901C1.77274 17.3124 1.56364 17.6736 1.59455 17.97C1.6215 18.2286 1.75696 18.4635 1.9672 18.6164C2.20825 18.7916 2.62557 18.7916 3.46022 18.7916H18.5392C19.3738 18.7916 19.7911 18.7916 20.0322 18.6164C20.2424 18.4635 20.3779 18.2286 20.4048 17.97C20.4357 17.6736 20.2267 17.3124 19.8085 16.5901L12.269 3.56738C11.8523 2.84764 11.644 2.48778 11.3721 2.36691C11.135 2.26148 10.8644 2.26148 10.6273 2.36691C10.3554 2.48778 10.1471 2.84765 9.7304 3.56738Z"
                          stroke="#8C0020"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        ></path>
                      </svg>
                    ) : (
                      <svg
                        width="18"
                        height="18"
                        viewBox="0 0 24 24"
                        fill="none"
                      >
                        <path
                          d="M10.9999 7.33325V10.9999M10.9999 14.6666H11.0091M20.1666 10.9999C20.1666 16.0625 16.0625 20.1666 10.9999 20.1666C5.93731 20.1666 1.83325 16.0625 1.83325 10.9999C1.83325 5.93731 5.93731 1.83325 10.9999 1.83325C16.0625 1.83325 20.1666 5.93731 20.1666 10.9999Z"
                          stroke="#002570"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        ></path>
                      </svg>
                    )
                  ) : (
                    ""
                  )}
                </button>
              </div>
            </div>
          </div>
          <div>
            <label htmlFor="email">Email: </label>
            <div>
              <input
                className="email"
                type="email"
                name="email"
                id="email"
                value={email}
                maxLength={256}
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
                required
              />
            </div>
          </div>
        </section>
        <section>
          <div>
            <label htmlFor="password">Password: </label>
            <div>
              <input
                type="password"
                name="password"
                id="password"
                value={password}
                minLength={8}
                pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
                maxLength={64}
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
                required
              />
            </div>
          </div>
          <div>
            <label htmlFor="password_assert">Password confirmation: </label>
            <div>
              <input
                type="password"
                name="password_assert"
                id="password_assert"
                value={passwordConfirmation}
                minLength={8}
                pattern={password}
                maxLength={64}
                onChange={(e) => {
                  setPasswordConfirmation(e.target.value);
                }}
                required
              />
            </div>
          </div>
        </section>
      </form>
    </>
  );
};

export default Form;
