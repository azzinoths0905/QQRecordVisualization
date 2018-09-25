import re
from database.chatLog import ChatLog


class Reader(object):
    def __init__(self, file):
        self.__f = open(file, "r", encoding="UTF-8")
        self.__lines = self.__f.readlines()
        self.__logs = []
        self.__failed_logs = []

    def parse(self):
        i = 0
        while i < len(self.__lines):
            line = self.__lines[i]
            dt = re.match(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})", line)
            if not dt:
                i += 1
                continue
            log = {
                "datetime": dt.group()
            }
            line = line[dt.end()+1:].rstrip("\n")[::-1]
            qq_flag = line.find("(")
            log["qq"] = line[qq_flag-1:0:-1]
            log["name"] = line[:qq_flag:-1].strip(" ")
            i += 1
            log["content"] = self.__lines[i].rstrip("\n")
            while self.__lines[i+1] != "\n":
                i += 1
                log["content"] += " " + self.__lines[i].rstrip("\n")
            self.__logs.append(log)
            i += 2

    def commit(self, table) -> dict:
        cl = ChatLog(table)
        for log in self.__logs:
            cl.log = log
            result = cl.create()
            if result["affect"] != 1:
                self.__failed_logs.append(log)
        return {
            "import": len(self.__logs) - len(self.__failed_logs),
            "failed": len(self.__failed_logs)
        }
