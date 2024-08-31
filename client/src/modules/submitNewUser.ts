import axios from "axios";

interface NewUserType {
  firstname: string;
  lastname: string;
  username: string;
  email: string;
  password: string;
}

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function submitNewUser(user: NewUserType) {
  try {
    const response = await instance.post("/signup/", user);
    console.log(response);
    return response.status;
  } catch (errorStack: any) {
    console.error(errorStack.response);
    return errorStack.response;
  }
}

export type { NewUserType };
