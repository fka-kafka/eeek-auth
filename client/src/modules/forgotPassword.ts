import axios from "axios";
import { URL } from "url";

const instance = axios.create({
  baseURL: import.meta.env.VITE_SERVER_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function sendOTP(email: string) {
  const response = await instance.post("/forgot-password/request-reset", {
    content: email,
  });
  console.log(response);
  return response;
}

export async function verifyOTP(OTP: string) {
  const response = await instance.post("/forgot-password/verify-reset", {
    content: OTP,
  });
  console.log(response);
  return response;
}

export async function resetPassword(resetURL: URL, password: string) {
  const response = await instance.post(
    `${resetURL.pathname}${resetURL.search}`,
    { content: password }
  );
  console.log(response);
  return response;
}
