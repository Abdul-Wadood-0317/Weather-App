import requests
import json
import os
import win32com.client as wincom

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=19b456ca3a4c4321acf205911230612&q={city}"
r = requests.get(url)
# print(r.text)
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]
print(weatherdic["current"]["temp_c"])
speak = wincom.Dispatch("SAPI.SpVoice")

# os.system(f"say'The current waether in {city} is {w} degrees.'")
text = (f"'The current waether in {city} is {w} degrees.'")
speak.Speak(text)

