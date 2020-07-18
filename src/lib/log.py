from datetime import datetime
from lib.constants import *


class Log:

    def __init__(self, log_file):
        self.log_file = log_file

    def __log(self, prefix, timestamp, message):
        formatted_string = LOG_FORMAT_STRING % (prefix, timestamp, message)
        print(formatted_string)
        try:
            with open(self.log_file, "a+") as f:
                f.write(formatted_string)
        except Exception as e:
            print(str(e))

    def info(self, message):
        timestamp = datetime.now().strftime(LOG_DATE_FORMAT)
        self.__log(LOG_PREFIX_INFO, timestamp, message)

    def succ(self, message):
        timestamp = datetime.now().strftime(LOG_DATE_FORMAT)
        self.__log(LOG_PREFIX_SUCC, timestamp, message)

    def fail(self, message):
        timestamp = datetime.now().strftime(LOG_DATE_FORMAT)
        self.__log(LOG_PREFIX_FAIL, timestamp, message)
