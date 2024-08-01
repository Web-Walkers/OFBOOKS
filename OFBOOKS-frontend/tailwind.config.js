/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./src/**/*.{html,js,css}",
  ],
  theme: {
    extend: {
      boxShadow:{
          'glass':'inset 0 2px 22px 0 rgba(255,255,255,0.6);',
          'bth2': '0 4px 20px -4px #074643', 
          'bth': '0 1px 20px -10px #074643', 
          'bth1': 'rgba(50, 235, 230, 0.1) 0px 4px 6px -1px, rgba(50, 235, 230, 0.06) 0px 2px 4px -1px',
        },
        colors: {
          'maincolor': '#074643',
          'footercolor': '#010707',
          'background': '#6A417D',
          'gradstart': '#B3A7B7',
          'actionbtn': '#DC8AFF',
        },
        dropShadow: {
          'glow': [
            '0 0 1px #0007', 
            '0 0 5px #000'
          ]
        },
        animation: {
          'glow': 'xglow 3s ease-in-out infinite',
          'fade-down': 'fade-down 500ms ease-in-out',
          'shimmer': 'shimmer 8s infinite ease-in-out',
        },
        keyframes: {
          'xglow': {
          '0%, 100%': { inset: '10px' },
          '50%, 25%': { inset: '-0.25rem' }
          },
          'fade-down': {
            '0%': { transform: 'translateY(-25%) ', opacity: '0;',  },
            '100%': { transform: 'translateY(0) ', opacity: '100;',  },
          },
          'shimmer': {
            '0%': { 'background-position': '100%'},
            '50%': { 'background-position': '0%'},
            '100%': { 'background-position': '100%'},
          },
        },
      }
    },
  plugins: [
      require('@tailwindcss/aspect-ratio'),
      require('flowbite/plugin')({
        charts: true,
      }),
  ],
}