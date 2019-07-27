from flask import Flask, escape, request, render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def home_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
