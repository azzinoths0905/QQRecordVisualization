from unittest import TestCase
from chatLog import ChatLog
import datetime


class TestChatLog(TestCase):
    def test_create(self):
        cl = ChatLog()
        log = {
            "name": "Ron Test",
            "qq": "11111111",
            "content": "asdasdsdasdsadas",
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        cl.log = log
        print(cl.create())

    def test_read(self):
        cl = ChatLog()
        log = {
            "id": 4
        }
        cl.log = log
        print(cl.read())

    def test_update(self):
        cl = ChatLog()
        log = {
            "name": "Ron Test 2222",
            "qq": "11111111",
            "content": "asdasdsdasdsadas",
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        cl.log = log
        print(cl.update("2"))

    def test_delete(self):
        cl = ChatLog()
        log = {
            "id": "3",
        }
        cl.log = log
        print(cl.delete())