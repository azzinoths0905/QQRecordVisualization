from database.database import DataBase


class ChatLog(DataBase):
    def __init__(self, file):
        """
        Control the chat_log table
        """
        super().__init__(file)
        self.__log = {
            "id": "",
            "name": "",
            "qq": "",
            "content": "",
            "datetime": None,
            "from": file
        }

    @property
    def log(self) -> dict:
        return self.__log

    @log.setter
    def log(self, log_info):
        for item in ["id", "name", "qq", "content"]:
            if item in log_info:
                self.__log[item] = str(log_info[item])
        if "datetime" in log_info:
            self.__log["datetime"] = log_info["datetime"]

    def create(self) -> dict:
        if self.log["id"]:
            return {
                "affect": 0
            }

        for item in ["name", "qq", "content", "datetime"]:
            if not self.log[item]:
                return {
                    "affect": 0
                }

        with self._connection.cursor() as cursor:
            sql = "INSERT INTO `chat_log` (`name`, `qq`, `content`, `datetime`, `from`) " \
                  "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
                    self.log["name"],
                    self.log["qq"],
                    self.log["content"],
                    self.log["datetime"],
                    self.log["from"]
                    )
            try:
                aff_row = cursor.execute(sql)
            except Exception as e:
                print(e)
                aff_row = 0

        return {
            "affect": aff_row,
        }

    def read(self) -> dict:
        where = "WHERE `from` = {0},".format(self.log["from"])
        for key, value in self.log.items():
            if value:
                where += "`{0}` = '{1}',".format(key, value)
        where = where[:-1]

        with self._connection.cursor() as cursor:
            sql = "SELECT * FROM `chat_log` " + where
            aff_row = cursor.execute(sql)
            logs_info = cursor.fetchall()

        return {
            "affect": aff_row,
            "logs": logs_info
        }

    def update(self, log_id) -> dict:
        set_value = "SET "
        for key, value in self.log.items():
            if value:
                set_value += "t.`{0}` = '{1}',".format(key, value)
        set_value = set_value[:-1]

        with self._connection.cursor() as cursor:
            sql = "UPDATE `chat_log` t {0} WHERE t.`id` = {1}".format(set_value, log_id)
            aff_row = cursor.execute(sql)

        return {
            "affect": aff_row
        }

    def delete(self):
        where = "WHERE `from` = {0},".format(self.log["from"])
        for key, value in self.log.items():
            if value:
                where += "`{0}` = '{1}',".format(key, value)
        where = where[:-1]

        with self._connection.cursor() as cursor:
            sql = "DELETE FROM `{0}` ".format(self.__log) + where
            aff_row = cursor.execute(sql)

        return {
            "affect": aff_row
        }
