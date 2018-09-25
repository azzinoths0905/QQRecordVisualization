from flask import Flask, request
from flask_restful import Api
from reader import Reader
from visualization.wordCloudApi import WordCloudApi
import time


app = Flask(__name__)
api = Api(app)

api.add_resource(WordCloudApi, "/api/qqrv/v1/word_cloud")


@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        f = request.files["log_file"]
        f_name = f.filename.rstrip(".txt") + str(int(time.time())) + ".txt"
        f.save("resource/" + f_name)
        reader = Reader("resource/" + f_name)
        reader.parse()
        result = reader.commit(f_name)
    except Exception as e:
        return "Error: " + str(e)
    if result["import"] > 0:
        return f_name
    else:
        return "Error: No log can be found."


if __name__ == '__main__':
    app.run(debug=True)
