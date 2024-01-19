from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image, ImageTk
import requests
import pytz
from geopy.exc import GeocoderInsufficientPrivileges

app = Tk()
app.title("Weather App")
app.geometry("900x500+300+200")
app.configure(bg='#ffffff')
app.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        locator = Nominatim(user_agent="geoapiExercises")
        location = locator.geocode(city)

        if location is None:
            messagebox.showerror("Erreur", "Ville non trouvée.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather
        api_key = "e0f276a9abe0200adc5a39f7583dcadf"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
        
        try:
            json_data = requests.get(api).json()

            if 'weather' in json_data and 'main' in json_data and 'wind' in json_data:
                condition = json_data['weather'][0]['main']
                description = json_data['weather'][0]['description']
                temp = int(json_data['main']['temp'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
            else:
                messagebox.showerror("Erreur", "Structure de réponse API incorrecte.")
                return

            t.config(text=f"{temp}°")
            c.config(text=f"{condition} | FEELS {temp}°")
            label1.config(text=f"{wind} m/s")
            label2.config(text=f"{humidity}%")
            label3.config(text=f"{description}")
            label4.config(text=f"{pressure} hPa")

        except requests.RequestException as e:
            messagebox.showerror("Erreur", f"Erreur de requête API : {str(e)}")

    except GeocoderInsufficientPrivileges:
        messagebox.showerror("Erreur", "Accès refusé. Veuillez réduire l'utilisation ou obtenir une clé API.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")



# Search box
search_image = Image.open("photo3.jpg")
image_tk = ImageTk.PhotoImage(search_image)
myimage = tk.Label(app, image=image_tk)
myimage.place(x=20, y=20)

textfield = tk.Entry(app, justify="center", width=17, font=("poppins", 15, "bold"), bg="#0e1f1e", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="photo.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", height=48, bg="#0e1f1e", command=getWeather)
myimage_icon.place(x=272, y=22)

# Logo
logo_image = PhotoImage(file="logo_weather.png")
logo = Label(image=logo_image, borderwidth=0)
logo.place(x=90, y=128)

#Bottom box
frame_image = PhotoImage(file="bilow2.png")
frame_myimage = Label(image=frame_image, height=60)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(app, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(app, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(app, text="WIND", font=("Helvetica", 15, 'bold'), fg="#4da7c9", bg="#ffffff", borderwidth=0)
label1.place(x=150, y=440)

label2 = Label(app, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="#4da7c9", bg="#ffffff", borderwidth=0)
label2.place(x=265, y=440)

label3 = Label(app, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="#4da7c9", bg="#ffffff", borderwidth=0)
label3.place(x=430, y=440)

label4 = Label(app, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="#4da7c9", bg="#ffffff", borderwidth=0)
label4.place(x=650, y=440)

t = Label(app, font=("arial", 70, "bold"))
t.place(x=400, y=150)

c = Label(app, font=("arial", 15, "bold"))
c.place(x=400, y=250)

app.mainloop()
#2814ada80898faf1881093871f9b9163