
"""
Author: Parashar Bhatt
Date 9-Nov-2020

This application gives you weather information for the given City
City can be entered in format : City, Country_code
eg: Mumbai,IN  
    Toronto,CA

Note: You need to register on :  openweathermap.org  to get your API_KEY.

API_KEY: is to be set in your environment variable and is accessed in program.


"""

import sys
import os
import requests
from datetime import datetime
from tkinter import font
import tkinter as tk
from PIL import Image, ImageTk


#print(os.environ.get('MY_OWM_API_KEY'))  

"""
units parameter is	optional.
  Values can be:	standard, metric, imperial. 
    When you do not use the units parameter, format is standard by default.

"""

# initial window size for the app
HEIGHT = 600
WIDTH = 600

#weather_image = os.path.join( str( os.getcwd()) ,'weather.jpg')
weather_image = os.path.join( str( os.path.dirname(sys.argv[0])) ,'weather.png')

root = tk.Tk()

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title('City Weather Application')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open(weather_image)
        self.image = ImageTk.PhotoImage(self.original)
        self.display = tk.Canvas(self  , height=HEIGHT, width=WIDTH     , bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")
        self.display.grid(row=0, sticky="wens")
        self.pack(fill=tk.BOTH, expand=1)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class Empty_City(Error):
    """Raised when the input value is not provided"""
    pass


###########################

def exit_app():
    """ Exiting Application"""
    quit()

def search_weather(city_val):
    try:
        #mcity = input("Enter your city:")
        mcity=city_val
        """
         Note : 'MY_OWM_API_KEY' is environment variable which holds API_KEY for openweathermap.org
                 you can change it as per your setting

        """
        url= 'http://api.openweathermap.org/data/2.5/weather?appid='+os.environ.get('MY_OWM_API_KEY')
        url = url+'&q=' + mcity +'&units=metric'
        if len(mcity.strip()) ==0:
            raise Empty_City
        else:
            res = requests.get(url)
            if res.status_code <400:
                data=res.json()
                #print(res)
                #print(data)
                temp_d=data['main']
                #curdt=datetime.fromtimestamp(data['dt']).strftime("%Y-%m-%d %I:%M:%S")
                text  = 'Current weather for City :'  +mcity +'\n'
                text += 'Location (Lon,Lat) : ('+ str(data['coord']['lon']) +' , '+ str(data['coord']['lat']) +')\n'
                text += 'Country :' + data['sys']['country'] + ' Timezone : ' +  str( data['timezone']) +'\n'
                text += 'Temperature : ' + str(temp_d['temp']) + ' in Metric Unit \n'
                text += 'Feels like : '+ str(temp_d['feels_like'] ) +'\n'
                text += 'Pressure : '+ str(temp_d['pressure'] ) +'\n'
                text += 'Humidity : '+ str(temp_d['humidity'] ) +'\n'
                text += 'Visibility : ' + str( data['visibility'] ) +'\n'
                text += 'Wind speed : '+ str(data['wind']['speed'] ) +' at Degree : '+ str(data['wind']['deg'] ) +'\n'

            else:
                text = f"Error in input city or detail not found error, status {res.status_code}"
        

    except Empty_City:
        text="Please provide appropriate value for city, aborting program."
    label = tk.Label(lower_frame , font=('Courier',12), anchor='nw', justify='left', bd=4, wraplength=400)
    label.place(relwidth=1, relheight=1)
    label['text']=text
    



###############################

app = App(root)

"""
Defining Layout for application GUI

"""


frame =tk.Frame(app, bg='#80c1ff' ,bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#label = tk.Label(frame , text='City,CountryCode',font=('Courier',12), anchor='nw', justify='left', bd=4)
#label.place(relwidth=.1,relheight=.1)

entry=tk.Entry(frame, font=('Courier',12))
entry.place(relwidth=0.65 , relheight=1)


button = tk.Button(frame, text='Find Weather' , font=('Courier',12) , command= lambda:search_weather(entry.get()))
button.place(relx=.7, relwidth=0.3, relheight=1)

lower_frame =tk.Frame(app, bg='#80c1ff' ,bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.45 , anchor='n')

exit_frame =tk.Frame(app, bg='#80c1ff' ,bd=5)
exit_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')
exit_button = tk.Button(exit_frame, text='QUIT' , font=('Courier',12) , command=exit_app)
exit_button.place( relx=.25, relwidth=0.5, relheight=1)

# Main Loop for the application

app.mainloop()
#root.destroy()
