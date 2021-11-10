#Watipaso Mulwafu
#https://github.com/thewati
#https://medium.com/@watipasomulwafu

#import all librabries
import csv
import folium
import io
from PIL import Image

#open csv file containing latitudes and longitudes to read through
reader = csv.reader(open('coordinates.csv', 'r'), delimiter=',')

#set your access token obtained from your mapbox account. See instructions on GitHub for more
mapboxAccessToken = '###'
#set tile set
mapboxTilesetId = 'mapbox.satellite'

#loop through all coordinates in csv file
for row in reader:
    #extracting each cell in row individually
    key = (row[0], row[1], row[2])
    print(key)

    m = folium.Map(
        location=[row[0], row[1]],
        zoom_start=20,
        tiles='https://api.tiles.mapbox.com/v4/' + mapboxTilesetId + '/{z}/{x}/{y}.png?access_token=' + mapboxAccessToken,
        attr='mapbox.com')
    m.save(row[2] + '.html') #save as html file
    # take screenshot of html page and save as .png file
    img_data = m._to_png(4)
    img = Image.open(io.BytesIO(img_data))
    img.save(row[2] + '.png')