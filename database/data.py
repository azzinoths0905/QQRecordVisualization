import pymysql
import config


class Data(object):
    def __init__(self, file):
        """
        control the data model
        connect to the database
        """
        self._connection = pymysql.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            db=config.DB,
            port=config.PORT,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self._file = file

    def create(self) -> dict:
        # TODO(Ron): Add Exception
        raise PermissionError

    def read(self) -> dict:
        # TODO(Ron): Add Exception
        raise PermissionError

    def update(self, log_id: str) -> dict:
        # TODO(Ron): Add Exception
        raise PermissionError

    def delete(self) -> dict:
        # TODO(Ron): Add Exception
        raise PermissionError

    def delete_all(self) -> dict:
        with self._connection.cursor() as cursor:
            sql = "TRUNCATE TABLE `chat_log`"
            aff_row = cursor.execute(sql)

        return {
            "affect": aff_row
        }

    def exc_sql(self, sql):
        with self._connection.cursor() as cursor:
            aff_row = 0
            logs_info = []
            err = ""
            try:
                aff_row = cursor.execute(sql)
                logs_info = cursor.fetchall()
            except Exception as e:
                err = str(e)

        return {
            "affect": aff_row,
            "logs": logs_info,
            "error": err
        }
