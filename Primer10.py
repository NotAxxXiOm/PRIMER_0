import html
user_input = input("Введите свой комментарий:")
comment = "<p>" + html.escape(user_input) + "</p>"
html = """
    <html>
        <head>
            <title>Моя страница</title>
        </head>
        <body>
            <h1>Мой комментарий:</h1>
            {}
        </body>
    </html>
""".format(comment)
print(html)
