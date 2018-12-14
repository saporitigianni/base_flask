from flask import FLask, request
import json

app = FLask(__name__)

@app.route("/test-get/<sample_prop>", methods=['GET'])
def test_get(sample_prop):
    print(request.headers)
    print(request.args['xyz']) # to get arguments from the url string
    return json.dumps({"error": 123, "this": 234})

@app.route("/test-post/<sample_prop>", methods=['POST'])
def test_post(sample_prop):
    print(request.get_json())
