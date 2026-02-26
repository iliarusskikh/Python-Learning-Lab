from flask import Flask , request
from ui import stylish_ui

app = Flask(__name__)

@app.route("/")
def hello_world():
    content = """
    <form action="/login" method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    """
    return stylish_ui(content)

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    return stylish_ui(f"successfully logged in as <b>{user}</b>.")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port =80)
    
# run with localhost
