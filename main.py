from flask import Flask, redirect
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def entry1():
    myName = "David"
    heading = "Blog entry 1"
    date = "4th April 2024"
    text = "This is my first blog entry, and it's all about Replit. Replit's awesome! I definitely want to join core soon."

    with open("template/blog.html", "r") as f:
        page = f.read()

    page = page.replace("{name}", myName)
    page = page.replace("{title}", heading)
    page = page.replace("{date}", date)  # Convert date to string
    page = page.replace("{text}", text)

    return page

@app.route('/blog')  # Changed route name
def altlink():
    return redirect('/')

app.run(host='0.0.0.0', port=81)

