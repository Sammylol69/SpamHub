import pyautogui
import time
import webbrowser as wb
import requests
import fade

def dc():
   dc = "▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄ \n▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌\n░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌\n░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌\n░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓ \n ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ \n░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ \n  ░     ░        ░  ░ ░          ░ ░     ░        ░    "
   faded_text = fade.water(dc)
   print(faded_text)
def logo():
  logo = "  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓    ██░ ██  █    ██  ▄▄▄▄   \n▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒   ▓██░ ██▒ ██  ▓██▒▓█████▄ \n░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░   ▒██▀▀██░▓██  ▒██░▒██▒ ▄██\n  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██    ░▓█ ░██ ▓▓█  ░██░▒██░█▀  \n▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒   ░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓\n▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░    ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒\n░  ░  ░  ░░         ░   ▒   ░      ░       ░  ░░ ░ ░░░ ░ ░  ░    ░ \n      ░                 ░  ░       ░       ░  ░  ░   ░      ░      "
  faded_text = fade.purplepink(logo)
  print(faded_text)

def menu():
  menu = "[01] Discord Webhook"
  faded_text = fade.purplepink(menu)
  print(faded_text)


logo()
menu()

number = int(input("Enter a number: "))
print("")

if number == 1:
  for x in range(100):
    print("\n")
  dc()
  webhook_url = str(input("Webhook Url: "))
  print("")
  username = str(input("Webhook Name: "))
  print("")
  title = str(input("Webhook Message: "))
  print("")

embed = {
    "title": title,
    "description": "This is a webhook spamer",
    "color": 0xffffff, 
    "footer": {"text": "by SHO"}
}


payload = {
  "username": username,
    "embeds": [embed]
}


for x in range(int(input("How much messages: "))):
   response = requests.post(webhook_url, json=payload)
   suc = "Webhook sent successfully!"
   faded_text = fade.water(suc)
   print(faded_text)
   time.sleep(0.01)