from flask import (
    Flask,
    jsonify,
    request
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from flask_cors import CORS

from datetime import timedelta

class BasicConfig:
    """basic configuration for application"""
    BASIC_HEADER="jaibhawani"
    JSON_SORT_KEY=False,
    JWT_SECRET_KEY="mysecret_key",
    JWT_ALGORITHM="SHA256"
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=5)

CONFIG=BasicConfig

app=Flask(__name__)
app.config.from_object(CONFIG)
jwt_object=JWTManager()
jwt_object.init_app(app)

CORS(app, resources={r"/*": {"origins": "*"}})

app.app_context().push()



user={
    "shudhanshu":"casper"
}

def check_headers(func):
    def wrap_function():
        if request.get_json:
            headers=dict(request.headers)
            if headers.get("Casper")!="ghost":
                return jsonify(
                    {
                    "status":False,
                    "message":"Invalid headers"
                    }
                ),400
            return  func()
    return wrap_function
                






@app.get("/checker")
@check_headers
def checker():
    print(request.headers)
    return jsonify(
        {
        "status":True,
        "message":"app checker route working"
        }
    )
@app.route("/login",methods=["POST"])
def check_login():
    payload=request.get_json()
    header=request.headers
    if user.get(payload.get("id"))==payload.get("pw"):
        return jsonify(
            {
            "status":True,
            "message":"user logged in"
            }),200
    return jsonify(
        {
        "status":False,
        "message":"user does not exist"
        }),400
        



if __name__=="__main__":
    app.run(debug=True,port=5020)


