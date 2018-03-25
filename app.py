from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://interesting:123456@localhost/interesting'
app.testing = True
db = SQLAlchemy(app)

@app.route("/api/v1/index")
def index():
    return "Testing"

@app.route("/api/v1/users/register", methods=["POST"])
def users_register():
    data = request.get_json(force=True)
    response = jsonify({"message":data.get("first_name")})
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(debug=True)
