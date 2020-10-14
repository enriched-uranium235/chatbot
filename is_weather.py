import requests
import json

def is_weather(place):
    city_name = place
    app_id = "212d7e7121a90a8c7f5436dace35878b"
    #&units=metricで摂氏温度を求める
    URL = "https://api.openweathermap.org/data/2.5/weather?q={0},jp&units=metric&lang=ja&appid={1}".format(city_name, app_id)

    response = requests.get(URL)
    data =  response.json()
     #天気情報
    weather = data["weather"][0]["description"] #最高気温
    temp_max = data["main"]["temp_max"] #最低気温
    temp_min = data["main"]["temp_min"] #寒暖差
    diff_temp = temp_max - temp_min #湿度
    humidity = data["main"]["humidity"]

    answer = "天気：" + weather + "\n最高気温：" + str(temp_max) + "℃\n最低気温：" + str(temp_min) + "℃\n寒暖差：" + str(diff_temp) + "℃\n湿度：" + str(humidity) + "%"
    return answer

def next_weather(place):
    city_name = place
    app_id = "212d7e7121a90a8c7f5436dace35878b"
    # &units=metricで摂氏温度を求める
    url = "https://api.openweathermap.org/data/2.5/forecast?q={0},jp&units=metric&lang=ja&appid={1}".format(city_name, app_id)

    response = requests.get(url)
    data = response.json()

    #天気情報
    weather1 = data["list"][0]["weather"][0]["description"]
    weather2 = data["list"][8]["weather"][0]["description"]
    weather3 = data["list"][16]["weather"][0]["description"]
    weather4 = data["list"][24]["weather"][0]["description"]

    answer = "現在の天気：" + weather1 + "\n明日の天気：" + weather2 + "\n明後日の天気：" + weather3 + "\n明々後日の天気：" + weather4
    return answer
