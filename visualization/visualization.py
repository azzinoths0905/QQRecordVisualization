from database.chatLog import ChatLog


class Visualization(object):
    def __init__(self, file):
        self._opt = {}
        self._data = []
        self._file = file
        self._cl = ChatLog(file)

    def _get_data(self) -> dict:
        raise PermissionError

    def process(self) -> dict:
        raise PermissionError
