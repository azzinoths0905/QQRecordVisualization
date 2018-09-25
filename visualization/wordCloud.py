from visualization.visualization import Visualization


class WordCloud(Visualization):
    def __init__(self, file):
        super().__init__(file)

    def _get_data(self) -> dict:
        # TODO(Ron): The output name is not the latest name
        sql = "SELECT COUNT(*), `name` FROM `chat_log` WHERE `from` = '{0}' GROUP BY `qq` ORDER BY COUNT(*) DESC".format(
            self._file,
        )
        resp = self._cl.exc_sql(sql)
        if not resp["error"]:
            self._data = resp["logs"]
        return {
            "error": resp["error"]
        }

    def process(self) -> dict:
        err = self._get_data()["error"]
        data = []
        for member in self._data:
            data.append(
                {
                    "name": member["name"],
                    "value": member["COUNT(*)"]
                }
            )
        self._opt = {
            "series": [
                {
                    "type": "wordCloud",
                    "data": data
                }
            ]
        }
        return {
            "option": self._opt,
            "error": err
        }

