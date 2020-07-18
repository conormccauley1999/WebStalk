CONFIG_PATH = "config.ini"

SMTP_SERVER = "smtp.gmail.com"
EMAIL_TEXT = """\
From: %s
To: %s
Subject: WebStalk Monitor: Recent change to webpage: %s

The following webpage was recently changed: %s.
"""
SMS_TEXT = "WebStalk Monitor: Recent change to webpage: %s"

LOG_FORMAT_STRING = "[%s] - (%s) - %s\n"
LOG_DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
LOG_PREFIX_INFO = "INFO"
LOG_PREFIX_FAIL = "FAIL"
LOG_PREFIX_SUCC = "PASS"
