
# InventoryManager (Online nut shop)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A django project that manages inventories of a nut shop across the country, their products and customers orders.


## Demo

https://inventorymanager.pythonanywhere.com/

### Test Accounts:
| Description        | Username           | Password  |
| ------------- |:-------------:| -----:|
| Admin account      | admin | admin |
| Customer account located in Tehran      | tehran      |   test@1234 |
| Customer account located in Mashhad | mashhad      |    test@1234 |

## Features

- Admin panel for controlling inventories, products and orders
- loading purchasable products for users based on their city
- tracking order processing for customers



## Run locally

Make sure you have python installed.

-  Clone the project:

```bash
  > git clone https://github.com/Moein-HDi/InventoryManager
```

- Make a virtual enviroment with desired name and active it:

```bash
  > py -m venv venv_name
  > venv_name\Scripts\activate
```
- Install requirements:
```bash
  > pip install -r requirements.txt
```
- Thats it! run the project:
```bash
  > py manage.py runserver
```
project should be accessible locally at http://127.0.0.1:8000
## Frontend

Project templates are styled using [TailwindCSS](https://tailwindcss.com/) framework.

I'm also using a tailwind plugin called [DaisyUI](https://daisyui.com) on top of that.

If you need to change the styles or templates. considering that you have node.js on your machine first install Tailwindcss then install daisyUI 

tailwind.config.js file should be configured like this:
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}'
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["autumn"], // true: all themes | false: only light + dark | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: "dark", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    rtl: true, // rotate style direction from left-to-right to right-to-left. You also need to add dir="rtl" to your html tag and install `tailwindcss-flip` plugin for Tailwind CSS.
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
  },
}


```


## License

[MIT](https://choosealicense.com/licenses/mit/)

