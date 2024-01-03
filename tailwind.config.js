/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "webshelf/books/templates/**/*.html",
        "webshelf/desk/templates/**/*.html",
        "webshelf/door/templates/**/*.html",
        "webshelf/shelf/templates/**/*.html",
        "webshelf/templates/**/*.html"],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}

