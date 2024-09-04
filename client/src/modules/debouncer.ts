import { getUsers } from "./fetchUsers";

const usernameDebouncer = (callback: Function, delay: number) => {
  let debounceTimer: NodeJS.Timeout;

  return function (...args: [string]) {
    return new Promise<any>((resolve) => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(async () => {
        const found = await callback(...args);
        resolve(found);
      }, delay);
    });
  };
};

export const debounce = usernameDebouncer(getUsers, 500);
