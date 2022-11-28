import tkinter as tk
from tkinter import messagebox
import requests
import time
from tkinter import *

api_key = 'd686fdc2b94f32899779452b1a635eef'


def weatherFind(city):
    final = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        f_temperature = json_file["main"]['temp']
        feels_temperature = json_file["main"]['feels_like']
        h_temperature = json_file["main"]['temp_max']
        l_temperature = json_file["main"]['temp_min']
        weather_display = json_file['weather'][0]["main"]
        weather_description = json_file['weather'][0]['description']
        pressure = json_file['main']['pressure']
        humidity = json_file['main']['humidity']
        wind = json_file['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_file['sys']['sunrise'] - 14400))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_file['sys']['sunset'] - 14400))
        result = (city, country_name, feels_temperature, f_temperature, weather_display, h_temperature, l_temperature,
                  weather_description, pressure, humidity, wind, sunset, sunrise)
        return result
    else:
        return None


def print_weather():
    city = search_city.get()
    weather = weatherFind(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0], weather[1])
        temperature_entry2['text'] = '{:.2f}°'.format(weather[3])
        mm_temperature['text'] = 'H:{:.2f}°, L:{:.2f}°'.format(weather[5], weather[6])
        weather_entry['text'] = weather[4]
    else:
        messagebox.showerror('Error', 'Please enter valid city name')


def print_weather2():
    city = search_city.get()
    weather = weatherFind(city)
    if weather:
        temperature_entry['text'] = 'feels like: {:.2f}°'.format(weather[2])
        weather_desc['text'] = weather[7]
        rs_weather['text'] = 'Sunrise:{}AM, Sunset:{}PM'.format(weather[12], weather[11])
        phw_entry['text'] = 'Pressure: {} inHg  Humidity: {}% Wind: {} mph'.format(weather[8], weather[9], weather[10])
    else:
        messagebox.showerror('Error', 'Please enter valid city name')


is_on = True
canvas = Tk()
canvas.geometry("600x500")

canvas.configure(bg='gray')

label1 = Label(canvas, text="Enter City")
label1.pack()
search_city = StringVar()
search_box = Entry(canvas, textvariable=search_city)
search_box.pack()

s_button = Button(canvas, text="Submit", command=print_weather)
s_button.pack()

location_entry = Label(canvas, text='')
location_entry.pack()

temperature_entry2 = Label(canvas, text='')
temperature_entry2.pack()

weather_entry = Label(canvas, text='')
weather_entry.pack()

mm_temperature = Label(canvas, text='')
mm_temperature.pack()

s_button = Button(canvas, text="See more", command=print_weather2)
s_button.pack()

temperature_entry = Label(canvas, text='')
temperature_entry.pack()

weather_desc = Label(canvas, text='')
weather_desc.pack()

rs_weather = Label(canvas, text='')
rs_weather.pack()

phw_entry = Label(canvas, text='')
phw_entry.pack()

canvas.mainloop()
