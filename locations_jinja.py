import cherrypy
import jinja2
import sqlite3 as sql
import math, os


DB = 'locations.db'
class LocationsWebsite(object):
    def get_locations(self):
        locationkey = {}
        i = 0
        latitudes = self.get_latitudes()
        longitudes = self.get_longitudes()
        #dates = self.get_date()
        #times = self.get_time()
        for i in range(len(latitudes)):
            #locationkey.append([latitudes[i]],dates[i])  #make list of lists to enable jinja render as column
            locationkey.update({"LATITUDES":latitudes,"LONGITUDES":longitudes})
        return locationkey
    def get_latitudes(self):
        latitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT latitude FROM Location;''')
            for latitude, in results:
                latitudes.append(str(latitude))
        return latitudes

    def get_longitudes(self):
        longitudes = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT longitude FROM Location;''')
            for longitude, in results:
                longitudes.append(str(longitude))
        return longitudes
    
    def get_date(self):
        dates = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT date FROM Location;''')
            for date, in results:
                dates.append(str(date))
        return dates
    
    def get_time(self):
        times = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT time FROM Location;''')
            for time, in results:
                times.append(str(time))
        return times

