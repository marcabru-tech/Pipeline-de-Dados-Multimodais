/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx}'],
  theme: {
    fontFamily: {
      sans: ['"Space Grotesk"', 'Inter', 'system-ui', 'sans-serif'],
    },
    extend: {
      colors: {
        bg: '#0a0a0f',
        panel: '#0f111a',
        accent: '#4DF4F1',
        accent2: '#9B5CF6',
        text: '#e5e7eb',
        muted: '#9ca3af',
      },
      boxShadow: {
        glass: '0 20px 60px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.04)',
      },
      backdropBlur: {
        xl: '20px',
      },
    },
  },
  plugins: [],
};
