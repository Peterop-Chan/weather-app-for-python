from bs4 import BeautifulSoup
import requests
import warnings

class Weather:
    def __init__(self):
        self.url = "https://rthk9.rthk.hk/weather/index.htm"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'}

    def time_title(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
            response = requests.get(self.url , headers=self.headers)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find_all("div",class_="updateinfo")
        return title[0].text        

    def temperature_weather_forecast(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
            response = requests.get(self.url , headers=self.headers)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
        temperature_area = soup.find_all("div", class_="item")
        return temperature_area[0].text

    def temperature_ShamShuiPo(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
            response = requests.get(self.url , headers=self.headers)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
        temperature_area2 = soup.find_all("div", class_="item")
        return temperature_area2[22].text
    def weather_conditions(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
            response = requests.get(self.url , headers=self.headers)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
        weather_conditions = soup.find_all("div", class_="desc")
        return weather_conditions[0].text

    