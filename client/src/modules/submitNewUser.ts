import axios from "axios";
import { AxiosResponse } from "axios";

interface NewUserType {
  firstname: string;
  lastname: string;
  username: string;
  email: string;
  password: string;
}

const instance = axios.create({
  baseURL: import.meta.env.VITE_SERVER_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function userSignUp(user: NewUserType) {
  try {
    const response = await instance.post("/signup/", user);
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export async function userSSOSignUp(
  payload: string,
  provider: string,
): Promise<number> {
  try {
    const response = await instance.post(`/signup-sso/${provider}`, {
      content: payload,
    });
    return response.status;
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export async function userLogIn(username: string, password: string): Promise<AxiosResponse<any, string>> {
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);
  const thisInstance = axios.create({
    baseURL: import.meta.env.VITE_SERVER_URL,
    headers: {
      "Content-Type": "multipart/form-data",
    },
    withCredentials: true
  });

  try {
    const response = await thisInstance.post("/login/", formData);
    return response;
  } catch (errorStack: any) {
    console.error(errorStack);
    return errorStack.response;
  }
}

export async function userSSOLogIn(payload: string, provider: string): Promeise<number> {
  try {
    const response = await instance.post(`/login-sso/${provider}`, {
      content: payload,
    });
    return response.status;
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export type { NewUserType };
