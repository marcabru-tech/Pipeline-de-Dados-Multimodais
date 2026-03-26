/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Space Grotesk", "sans-serif"],
      },
      colors: {
        cyan: {
          400: "#22d3ee",
          500: "#06b6d4",
        },
        magenta: {
          400: "#f0abfc",
          500: "#e879f9",
          600: "#d946ef",
        },
      },
    },
  },
  plugins: [],
};
