# Todo:
# Read the encoded GPS files
# Split by lines
# Convert to coordinate
# Store in .CSV file
# Plot them



# -------- Read the encoded GPS files ---------
with open("message.txt",'r') as file:
    coords = file.readline()
coords = coords.split('$')
del coords[0] # remove the first element, since it's just '$' due to nature of spli('$') giving residuals
organized_coords = ['$' + pos for pos in coords]

# -------- Save it in a organized way, ONLY NEED TO RUN ONES -------------
# with open("organized_message.txt",'a') as file:
#     for pos in organized_coords:
#         file.write(pos + '\n')
    
# -------- Convert to coordinate ---------------
from pynmeagps import NMEAReader # https://pypi.org/project/pynmeagps/, https://github.com/Knio/pynmea2
import pynmea2

lat_list = []
lon_list = []

for pos in organized_coords:
    try:
        # pynmea 1 version
        msg = NMEAReader.parse(pos)
        # print(msg.lat, msg.lon)
        lat_list.append(msg.lat)
        lon_list.append(msg.lon)
    except:
        try:
            # pynmea 2 version
            msg = pynmea2.parse(pos)
            # print(msg.latitude, msg.longitude)
            lat_list.append(msg.latitude)
            lon_list.append(msg.longitude)
        except:
            print("Can't be formatted:",msg)

# --------- Plotting into Google Map-----------
# https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/
import gmplot
# Plot method Draw a line in
# between given coordinates
gmap1 = gmplot.GoogleMapPlotter(lat_list[0], lon_list[0], 17) #Last digit in this function is for Zooming in, lower = farther
# scatter method of map object 
# scatter points on the google map
gmap1.scatter(lat_list, lon_list, '#FF0000', size = 2, marker = False )
#drawline
gmap1.plot(lat_list, lon_list, 'cornflowerblue', edge_width = 1)
#output file
gmap1.draw("GPS_tracking.html")

# if __name__ == "__main__":
#     pass