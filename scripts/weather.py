#!/bin/python
# -*- coding: utf-8 -*-

# Procedure
# Surf to https://openweathermap.org/city
# Fill in your CITY
# e.g. Antwerp Belgium
# Check url
# https://openweathermap.org/city/2803138
# you will the city code at the end
# create an account on this website
# create an api key (free)
# LANG included thanks to krive001 on discord
# slightly edited by axklen

# INFO: create a file named openweatherAPI.py with your API_KEY in it
# API_KEY = "your_key_here"
from openweatherAPI import API_KEY
import requests

CITY = "2950159"
UNITS = "Metric"
UNIT_KEY = "C"
LANG = "de"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))
        print(" {}°{}".format(TEMP, UNIT_KEY))
    else:
        print("No Data ")
except (ValueError, IOError):
    print("Error: ")
