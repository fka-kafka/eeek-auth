import axios from "axios";

const instance = axios.create({
  baseURL: import.meta.env.VITE_USERS_URL, //process.env.USERNAME_URL
  headers: {
    "Content-Type": "application/json",
  },
});

export async function initUsers(): Promise<any> {
  try {
    const response = await instance.get("/init/");
    console.log(response.data);
    return response;
  } catch (error) {
    console.error("Error initializing users:", error);
  }
}

export async function getUsers(name: string): Promise<any> {
  console.log(name);
  try {
    const response = await instance.post("/check_username/", { username: name });
    console.dir(response.data.found);
    return response.data.found;
  } catch (error) {
    console.error("Error fetching users:", error);
  }
}
