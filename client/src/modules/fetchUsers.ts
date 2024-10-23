import axios from "axios";

const instance = axios.create({
  baseURL: import.meta.env.VITE_USERS_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export async function initUsers(): Promise<string> {
  try {
    const response = await instance.get("/init/");
    console.log(response.data?.status);
    return response.data?.status;
  } catch (error) {
    console.error("Error initializing users:", error);
  }
}

export async function getUsers(name: string): Promise<boolean> {
  console.log(name);
  try {
    const response = await instance.post("/check_username/", { content: name });
    console.dir(response.data.found);
    return response.data?.found;
  } catch (error) {
    console.error("Error fetching users:", error);
  }
}
