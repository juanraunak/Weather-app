from flask import Flask, render_template, request
import json
import requests 
import urllib.request

app = Flask(__name__) #creating the Flask class object   

@app.route('/', methods = ['POST','GET']) #decorator   


def home():  

    if request.method == 'POST':
        city = request.form['city']
        print(city)
    else:
        city = 'bangalore'


    url = f" https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5396a21d4a839c7acb27a1c9412de39b&units=metric"

    location = "bangalore"

    r =  requests.get(url=url)
    data = r.json()
    temp = data['main']['temp'] 
    print(temp)
    temp_data =  {"temp" : data['main']['temp']} 
    what_data =  data['weather'][0]['main'] 
    print(what_data)
    
    return render_template("index.html", data = temp_data, city = city, what = what_data )

@app.route('/log_in') #log in 
def log_in():
    return "log inn"

if __name__ =='__main__':  
    app.run(debug = True)   