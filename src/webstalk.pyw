import configparser
import sched
import time
from lib.log import *
from lib.notifier import *
from lib.pagechecker import *


schedule = sched.scheduler(time.time, time.sleep)


def webstalk():

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    log_file = config.get("logging", "log_file")
    webpage = config.get("monitor", "webpage")
    wait = int(config.get("monitor", "wait"))
    email = config.get("notify", "email")
    mobile = config.get("notify", "mobile")
    gmail_user = config.get("gmail", "gmail_user")
    gmail_pass = config.get("gmail", "gmail_pass")
    twilio_number = config.get("twilio", "twilio_number")
    twilio_asid = config.get("twilio", "twilio_asid")
    twilio_token = config.get("twilio", "twilio_token")

    log = Log(log_file)
    page_checker = PageChecker(webpage, log)
    notifier = Notifier(email, mobile, log, gmail_user, gmail_pass, twilio_number, twilio_asid, twilio_token)

    log.info("Starting WebStalk")
    schedule.enter(wait, 1, check_and_notify, (log, page_checker, notifier, wait,))
    schedule.run()


def check_and_notify(log, page_checker, notifier, wait):
    try:
        log.info("Checking for changes to webpage")
        changed = page_checker.check()
        if changed:
            log.info("Changes were found - notifying the user")
            notifier.notify(page_checker.webpage)
        else:
            log.info("No changes were found")
        log.succ("Finished checking for changes")
    except Exception as e:
        log.fail("An error occurred: " + str(e))
    try:
        schedule.enter(wait, 1, check_and_notify, (log, page_checker, notifier, wait,))
    except Exception as e:
        log.fail("A fatal error occurred: " + str(e))


if __name__ == "__main__":
    webstalk()
