import requests
import hashlib
from termcolor import colored


def send_massage(loc, checklist):
    """send a massage to channel by telegram bot"""
    event = loc[3]
    actual = loc[4]
    forecast = loc[5]
    previous = loc[6]
    base_url = "https://api.telegram.org/7293544363:AAHpbMO7PhVOtZ-Dj8ncrhUPALoWjR7kDmI/sendMessage"
    parameters = {
        "chat_id": "@economics_calendar",
        "text": f"""
{event}📅

✅ Actual ----> {actual} 
✅ Forecast ----> {forecast} 
✅ previous ----> {previous} 

"""
    }
    hash_massage = hashlib.sha256(parameters["text"].encode("utf-8")).hexdigest()
    if not hash_massage in checklist:
        try:
            resp = requests.get(url=base_url, data=parameters)
            print(parameters["text"])
            print(colored("the massage was sent to bot", "green"))
        except Exception as e:
            print(e)
    return hash_massage
