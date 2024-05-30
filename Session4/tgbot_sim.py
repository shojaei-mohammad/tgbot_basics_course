import time

import requests

MAX_COUNTER = 100

TEXT = "یک آپدیت بدون متن دریافت شد"
BASE_API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "7337372286:AAGLhdGcu-UuOTCFDDtPALXwU_oUYRWP1wQ"

counter = 0

chat_id: int
offset = -2
timeout = 30


def send_message(chat_id: int, text: str):
    requests.get(f"{BASE_API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}")


while counter < MAX_COUNTER:
    print("attempt: " + str(counter))
    start_time = time.time()
    updates: dict = requests.get(
        f"{BASE_API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}"
    ).json()
    if updates.get("result"):
        for result in updates["result"]:
            offset = result.get("update_id")
            chat_id = result.get("message").get("from").get("id")
            print(result)
            user_text = result.get("message").get("text")

            if user_text:
                send_message(chat_id, user_text)
            else:
                send_message(chat_id, TEXT)

    end_time = time.time()
    print(f"time btween updates: {end_time - start_time}")
    counter += 1
