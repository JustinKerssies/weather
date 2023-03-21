from tkinter import ttk
from tkinter import *
from weerstation_datafile import Settings
from weerstation_locatie import Location
from weerstation_export import create_word_export
import tkintermapview
import sys


class Window:

    def __init__(self):
        # Creating the window
        self.ws = Settings()
        self.tab1 = None
        self.window = Tk()
        self.window.title('City weather')

        # Retrieve from the datafile whether full screen is needed or not
        if self.ws.fullscreen:
            width = self.window.winfo_screenwidth()
            height = self.window.winfo_screenheight()
        else:
            width = self.ws.screen_width
            height = self.ws.screen_height
        self.window.geometry('%dx%d' % (width, height))

        # Creating a search portion for the window
        start = ttk.Frame(self.window)
        start.grid(column=0, row=0)
        lbl = Label(start, text='Type city here')
        lbl.grid(column=0, row=0)
        self.txt = Entry(start, width=20, justify='center')
        self.txt.grid(column=1, row=0)
        self.txt.focus()
        btn = Button(start, text='start search', command=self.clicked, justify='right')
        btn.grid(column=3, row=0)

        # Create tabs for both the information and the eventual map
        self.tab = Frame(self.window)
        self.tab.grid(row=1, column=0)
        self.map_tab = Frame(self.window)
        self.map_tab.grid(row=1, column=2)

        # Creating a control notebook for the tabs
        self.txt.bind('<Return>', (lambda event: self.clicked()))
        self.txt.bind('<*>', (lambda event: sys.exit()))

        # Start main loop
        self.window.mainloop()

        """Defining the function of the search button"""

    def clicked(self):
        s = self.ws
        input_location = self.txt.get().title()
        loc = Location(s, input_location)

        # Delete all the info in the tabs, if it already has content
        for widgets in self.tab.grid_slaves():
            widgets.destroy()
        for widgets in self.map_tab.grid_slaves():
            widgets.destroy()

        # Create text based on the content saved within the Loc class
        # "items" are the questions, while "loc.data[items]" are the variables returned by the API
        i = 0
        for items in loc.data:
            question = Label(self.tab, text=items)
            question.grid(row=i, column=1)
            response = Label(self.tab, text=loc.data[items])
            response.grid(row=i, column=2)
            i += 1

        # Create a map based on the latitude and longitude
        self.create_map(loc.lat, loc.lon)

        # Create a Word document with all the information as well
        create_word_export(loc, input_location)
        print(loc.time)

    """Creating a map to show in the app"""

    def create_map(self, latitude, longitude):
        # Set up the widget in the map_tab and retrieve the height and with from the datafile
        map_widget = tkintermapview.TkinterMapView(self.map_tab, height=self.ws.map_height, width=self.ws.map_width)
        map_widget.grid(row=2, column=2)

        # Set the position on the latitude and longitude that was retrieved from the API response
        map_widget.set_position(latitude, longitude)

        # Set the zoom based on the zoom in the datafile
        map_widget.set_zoom(self.ws.zoom)


w = Window()
