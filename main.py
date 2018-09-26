from flask import Flask, request, Response
from flask_restful import Api
from reader import Reader
from visualization.wordCloudApi import WordCloudApi
import time


app = Flask(__name__)
api = Api(app)

api.add_resource(WordCloudApi, "/api/qqrv/v1/word_cloud")


@app.route("/upload", methods=["POST"])
def upload_file():
    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    try:
        f = request.files["log_file"]
        f_name = f.filename.rstrip(".txt") + str(int(time.time())) + ".txt"
        f.save("resource/" + f_name)
        reader = Reader("resource/" + f_name)
        reader.parse()
        result = reader.commit(f_name)
        if result["import"] > 0:
            resp.response = f_name
        else:
            resp.response = "Error: No log can be found."
    except Exception as e:
        resp.response = "Error: " + str(e)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
