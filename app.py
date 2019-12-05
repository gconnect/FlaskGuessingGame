from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/contact')
def contacts():
    my_file = {
        "name": "Glory",
        "dept": "python",
        "class": "beginner",
        "phones": [
            {
                "contact": 123456,
                "second_contact": 2435446
            },
            {
                "contact": 123456,
                "second_contact": 2435446
            }

        ]
    }
    return jsonify(my_file)

@app.route('/add', methods =['POST'])
def add_numbers():
    data_dic = request.get_json()
    if "y" or "x" not in data_dic:
        return "Error", 305

    x = data_dic["x"]
    y = data_dic["y"]
    z = x + y
    retJson = {
        "z" : z
    }
    return jsonify(retJson), 200

class Add(Resource):
    def post(self):
        data_dic = request.get_json()
        if "y" or "x" not in data_dic:
            return "Error", 305

        x = data_dic["x"]
        y = data_dic["y"]
        z = x + y
        retJson = {
            "z" : z
        }
        return jsonify(retJson), 200

api.add_resource(Add, "/add")

if __name__ == "__main__":
    app.run(debug=True)
