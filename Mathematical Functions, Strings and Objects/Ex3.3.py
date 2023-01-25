# Below is the programming exercise
# (Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
# Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
# www.gps-data-team.com/map/ and compute the estimated area enclosed by these
# four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
# distance between two cities. Divide the polygon into two triangles and use the formula
# in Programming Exercise 2.14 to compute the area of a triangle.)

import math

ATlat=33.75         # Atlanta's Latitude
ATlong=-84.38       # Atlanta's Longitude
ORlat=28.53         # Orlando's Latitude
ORlong=-81.38       # Orlando's Longitude
SVlat=32.08         # Savanna's Latitude
SVlong=-81.09       # Savanna's Longitude
CHlat=35.23         # Charlotte's Latitude
CHlong=-80.84       # Charlotte's Longitude

# Below is the formula of getting the distance between points
distOrSav=6371.01 * math.acos(math.sin(math.radians(ORlat)) * math.sin(math.radians(SVlat)) + math.cos(math.radians(ORlat)) * math.cos(math.radians(SVlat)) * math.cos(math.radians(ORlong - SVlong)))
distOrAt=6371.01 * math.acos(math.sin(math.radians(ORlat)) * math.sin(math.radians(ATlat)) + math.cos(math.radians(ORlat)) * math.cos(math.radians(ATlat)) * math.cos(math.radians(ORlong - ATlong)))
distSavAt=6371.01 * math.acos(math.sin(math.radians(SVlat)) * math.sin(math.radians(ATlat)) + math.cos(math.radians(SVlat)) * math.cos(math.radians(ATlat)) * math.cos(math.radians(SVlong - ATlong)))
distSavChar=6371.01 * math.acos(math.sin(math.radians(SVlat)) * math.sin(math.radians(CHlat)) + math.cos(math.radians(SVlat)) * math.cos(math.radians(CHlat)) * math.cos(math.radians(SVlong - CHlong)))
distAtChar=6371.01 * math.acos(math.sin(math.radians(ATlat)) * math.sin(math.radians(CHlat)) + math.cos(math.radians(ATlat)) * math.cos(math.radians(CHlat)) * math.cos(math.radians(ATlong - CHlong)))

