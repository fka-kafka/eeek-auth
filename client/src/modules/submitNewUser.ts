import axios from "axios";

interface NewUserType {
  firstname: string;
  lastname: string;
  username: string;
  email: string;
  password: string;
}

const instance = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function userSignUp(user: NewUserType) {
  try {
    const response = await instance.post("/signup/", user);
    console.log(response);
    return response.status;
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
    console.log(response);
    return response.status;
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export async function userLogIn(username: string, password: string) {
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);
  const thisInstance = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  try {
    const response = await thisInstance.post("/login/", formData);
    console.log(response);
    return response;
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export async function userSSOLogIn(payload: string, provider: string) {
  try {
    const response = await instance.post(`/signup-sso/${provider}`, {
      content: payload,
    });
    console.log(response);
    return response.data;
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export type { NewUserType };
