/// <reference types="vitest/config" />
import { defineConfig } from "vite";

export default defineConfig({
  test: {
    include: ["**/tests/**"],
    setupFiles: ["vitest-localstorage-mock"],
   
  },
});
