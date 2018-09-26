from flask_restful import Resource, reqparse
from wordCloud import WordCloud


class WordCloudApi(Resource):
    @staticmethod
    def get():
        param = reqparse.request.args
        wc = WordCloud(param["file"])
        return wc.process(), 200, {"Access-Control-Allow-Origin": "*"}
