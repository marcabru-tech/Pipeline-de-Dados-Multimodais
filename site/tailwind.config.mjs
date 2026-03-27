/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    fontFamily: {
      sans: ['"Space Grotesk"', "Inter", "system-ui", "sans-serif"],
    },
    extend: {
      colors: {
        bg: "#0a0a0f",
        panel: "#0f111a",
        accent: "#4DF4F1",
        accent2: "#9B5CF6",
        text: "#e5e7eb",
        muted: "#9ca3af",
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
      boxShadow: {
        glass: "0 20px 60px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.04)",
      },
      backdropBlur: {
        xl: "20px",
      },
    },
  },
  plugins: [],
};

