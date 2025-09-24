from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from CI/CD! V3 Super-puper</h1><p>This site runs on port 9999 🚀</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
