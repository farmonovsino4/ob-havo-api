import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

class WeatherNotFoundError(Exception):
    """
    Weather not found, make sure you write the city name correctly, use Weather().help()
    """

class Weather:
    def __init__(self, place):
        self.place: str = place

    def help(self):
        return """Siz mana bu shaharlarni ob havo malumotlarini ko'rishingiz mumkin:
    toshkent, andijon, buxoro, guliston, jizzax, zarafshon, qarshi, navoiy, namangan, nukus, samarqand, termiz, urganch, farg'ona, xiva
        """
    def today(self):
        if self.place.lower() == "toshkent":
            response = requests.get(f"https://obhavo.uz/tashkent", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "andijon":
            response = requests.get(f"https://obhavo.uz/andijan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "buxoro":
            response = requests.get(f"https://obhavo.uz/bukhara", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "guliston":
            response = requests.get(f"https://obhavo.uz/gulistan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "jizzax":
            response = requests.get(f"https://obhavo.uz/jizzakh", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "zarafshon":
            response = requests.get(f"https://obhavo.uz/zarafshan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "qarshi":
            response = requests.get(f"https://obhavo.uz/karshi", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "navoiy":
            response = requests.get(f"https://obhavo.uz/navoi", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "namangan":
            response = requests.get(f"https://obhavo.uz/namangan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "nukus":
            response = requests.get(f"https://obhavo.uz/nukus", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "samarqand":
            response = requests.get(f"https://obhavo.uz/samarkand", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "termiz":
            response = requests.get(f"https://obhavo.uz/termez", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "urganch":
            response = requests.get(f"https://obhavo.uz/urgench", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "farg'ona":
            response = requests.get(f"https://obhavo.uz/ferghana", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "xiva":
            response = requests.get(f"https://obhavo.uz/khiva", proxies={'http': 'http://proxy.server:3128/'})
        else:
            raise WeatherNotFoundError("Ob Havo malumoti topilmadi, shahar nomini to'g'ri yozganingiznga ishonch hosil qiling, yoki Weather().help() dan foydalaning")
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.find_all("span")
        return {'min': data[2].text, 'max': data[3].text}

    def one_week(self):
        global data
        if self.place.lower() == "toshkent":
            response = requests.get(f"https://obhavo.uz/tashkent", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "andijon":
            response = requests.get(f"https://obhavo.uz/andijan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "buxoro":
            response = requests.get(f"https://obhavo.uz/bukhara", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "guliston":
            response = requests.get(f"https://obhavo.uz/gulistan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "jizzax":
            response = requests.get(f"https://obhavo.uz/jizzakh", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "zarafshon":
            response = requests.get(f"https://obhavo.uz/zarafshan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "qarshi":
            response = requests.get(f"https://obhavo.uz/karshi", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "navoiy":
            response = requests.get(f"https://obhavo.uz/navoi", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "namangan":
            response = requests.get(f"https://obhavo.uz/namangan", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "nukus":
            response = requests.get(f"https://obhavo.uz/nukus", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "samarqand":
            response = requests.get(f"https://obhavo.uz/samarkand", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "termiz":
            response = requests.get(f"https://obhavo.uz/termez", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "urganch":
            response = requests.get(f"https://obhavo.uz/urgench", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "farg'ona":
            response = requests.get(f"https://obhavo.uz/ferghana", proxies={'http': 'http://proxy.server:3128/'})
        elif self.place.lower() == "xiva":
            response = requests.get(f"https://obhavo.uz/khiva", proxies={'http': 'http://proxy.server:3128/'})
        else:
            raise WeatherNotFoundError("Ob Havo malumoti topilmadi, shahar nomini to'g'ri yozganingiznga ishonch hosil qiling, yoki Weather().help() dan foydalaning")
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.find_all("tr")
        data2 = soup.find_all("span")
        return [{'dushanba': {'min': data2[2].text, 'max': data2[3].text}, 'seshanba': {'min': data[1].text.split()[6], 'max': data[1].text.split()[7]}, data[2].text.split()[0]: {'min': data[2].text.split()[6], 'max': data[2].text.split()[7]}, data[3].text.split()[0]: {'min': data[3].text.split()[6], 'max': data[3].text.split()[7]}, data[4].text.split()[0]: {'min': data[3].text.split()[6], 'max': data[3].text.split()[7]}, data[5].text.split()[0]: {'min': data[3].text.split()[6], 'max': data[3].text.split()[7]}, data[6].text.split()[0]: {'min': data[3].text.split()[6], 'max': data[3].text.split()[7]}}]

@app.route('/')
def mainpage():
    return "Hello world"

@app.route("/api")
def hello():
    return "Salom ob havo malumotlarini olivchi apiga xush kelibsiz<br>apidan foydalanish uchun quyidagicha yozing: http://127.0.0.1:5000/api/v1/bugun/[viloyat nomi] masalan:<br> <a href='api/v1/bugun/toshkent'>http://127.0.0.1:5000/api/v1/bugun/toshkent</a>"

@app.route("/api/v1/bugun/<city>")
def api(city):
    return Weather(city).today()

@app.route("/api/v1/1_haftalik/<city>")
def bir_haftalik_obhavo(city):
    return Weather(city).one_week()


app.run()