const colors = require('tailwindcss/colors')
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  purge: { content: ['./public/**/*.html', './src/**/*.vue'] },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      width: {
        '1/7': '14.2857143%',
      },
      height: theme => ({
        "screen-real": `calc(100vh - ${theme('spacing.16')})`,
      }),
      colors: { 
        gray: colors.trueGray,
        purple: {
          '100': '#ff00ff',
          '200': '#e600e6',
          '300': '#cc00cc',
          '400': '#b300b3',
          '500': '#990099',
          '600': '#800080',
          '700': '#660066',
          '800': '#4d004d',
          '900': '#330033',
          '1000': '#1a001a',
        },
        'main': {
          '100': '#FFF9F5',
          '200': '#FFF6F0',
          '300': '#FFEBDB',
          '400': '#76390a',
          '500': '#552907',
          '600': '#452208',
          '700': '#341C09',
          '800': '#2f1704',
          '900': '#180b02',
        }
      },
      inset: {
        '110px': '110px',
      },
      spacing: {
        '13': '3.25rem',
        '15': '3.75rem',
        '128': '32rem',
        '144': '36rem',
        '168': '42rem',
        '728px': '728px'
      },
      fontFamily: {
        'quicksand': ['Quicksand', 'sans-serif'],
        'fira': ['Fira Sans', 'sans-serif'],
      },
      gridTemplateRows: {
       '7': 'repeat(7, minmax(0, 1fr))',
      },
      backgroundPosition: {
        'center-center': 'center center',
        'center-left': '70% 100%',
        'top-1': '100% 20%'
      },
    },
    // objectPosition: {
    //  'center-20': 'center 20%',
    // },
    container: {
      screens: {
         sm: "100%",
         md: "768px",
         lg: "1024px",
         xl: "1280px"
      }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
