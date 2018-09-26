from database.chatLog import ChatLog


class Visualization(object):
    def __init__(self, file):
        """
        Generate Echarts options
        """
        self._opt = {}
        self._data = []
        self._file = file
        self._cl = ChatLog(file)

    def _get_data(self) -> dict:
        """
        Get data from db
        :return: Error message
        """
        raise PermissionError

    def process(self) -> dict:
        """
        Generate the option
        :return: Option and error message
        """
        raise PermissionError
