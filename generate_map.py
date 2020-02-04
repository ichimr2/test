import folium
from locations_jinja import*
"""
-Uses john's way of pulling data out of a database file using locations_jinja object
-Folium is a library to plot data on a map
"""
# create object instance of folium with parameters of coventry location,size and zoom
m = folium.Map(width=500,height=500,location= [52.4051, -1.5133], zoom_start = 12)

# message displayed on map icon
tooltip = "Click here for info"
locations_object = LocationsWebsite()
# locations is a list with lat,long and all data from database
locations = locations_object.get_locations()

# separated lists each with latitude and longitudes
locations_list_latitudes = locations["LATITUDES"]
location_list_longitudes = locations["LONGITUDES"]
# run loop and place a marker at locations. round(float( is magic fuckery because .Marker takes only 4 digits? and our data is too long.
for i in range(len(locations_list_latitudes)):
	folium.Marker([round(float(locations_list_latitudes[i]),4),round(float(location_list_longitudes[i]),4)], popup='<strong>Location</strong>',tooltip=tooltip).add_to(m)
#folium.Marker([round(float(locations_list[i]),4),round(float(location_list2[i]),4)], popup='<strong>Location</strong>',tooltip=tooltip).add_to(m) 






# saves the generate map with data above. This is cool but...you generate a new html file each time you update data on map??
# it's fine like this but somehow we need to create a website and make the website pull the map.html and display it.
# if map.html changes fine the main.html will display the updated one.
# this is alright...but not very nice for cs student -_-
m.save('map.html')

