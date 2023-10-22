from flask import Flask, render_template, request
import json
import requests
app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        key = "9288b78765826bdf5ad120777112ab8e"
        city = request.form.get('city')
        api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
        weather = "weather"
        temp = 30
        location = "London"
        windSpeed = "WindSpeed"
        response = requests.get(url=api)
        if response.status_code == 200:
            data = response.json()
            #time, precipitaction, icon
            weather = data["weather"][0]['description']
            icon = data["weather"][0]['icon']
            temp = int(data["main"]["temp"])
            location = data['name']
            windSpeed = data['wind']['speed']
            print(data)
            icon_src = f"https://openweathermap.org/img/wn/{icon}@2x.png"
            #print(f'{weather}, {temp}, {location}, {windSpeed}')
            return render_template("index.html", weather=weather, temp=temp, location=location, windSpeed=windSpeed,
                                   icon=icon_src)
        else:
            return render_template("index.html", weather, temp, location, windSpeed, icon = "")

if __name__ == '__main__':
    app.run(debug=True)