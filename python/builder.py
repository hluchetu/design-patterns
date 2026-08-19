class HTMLDocument:
    def __init__(self):
        self.title = ""
        self.body = ""
        self.footer = ""

    def __str__(self):
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{self.title}</title>
</head>
<body>
    <main>{self.body}</main>
    <footer>{self.footer}</footer>
</body>
</html>"""


class HTMLBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.document = HTMLDocument()
        return self

    def add_title(self, title):
        self.document.title = title
        return self

    def add_body(self, body):
        self.document.body = body
        return self

    def add_footer(self, footer):
        self.document.footer = footer
        return self

    def build(self):
        result = self.document
        self.reset()
        return result


page = (
    HTMLBuilder()
    .add_title("Builder Pattern")
    .add_body("<h1>Hello, world!</h1><p>My first HTML page.</p>")
    .add_footer("<p>Copyright 2026</p>")
    .build()
)

print(page)
