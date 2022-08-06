from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Subdomain-Takeover-By-n0sandb0x"
