from flask_restful import Resource, reqparse
from data.data import Data


class DataApi(Resource):
    @staticmethod
    def post():
        result = {"error": ""}
        try:
            param = reqparse.request.json()
            reader = Data(param["file"])
            reader.parse()
            result.update(reader.commit(param["table"]))
        except Exception as e:
            result["error"] = str(e)
        return result
