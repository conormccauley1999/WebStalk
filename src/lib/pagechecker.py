import requests


class PageChecker:

    def __init__(self, webpage, log):
        self.webpage = webpage
        self.log = log
        self.content = ""

    def check(self):
        new_content = requests.get(self.webpage).content
        if self.content == "":
            self.content = new_content
            return False
        changed = self.content != new_content
        self.content = new_content
        return changed
