from flask import Flask

app = Flask(__name__)

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

@app.route('/<error>')
def error(error):
    return f"\"{error}\" page not found"


app.run()