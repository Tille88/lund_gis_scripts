import arcpy
import re

#infc = "C:\Users\Jonas\Desktop\E12\own_polygon.shp"
#If shapefile placed in same directory:
infc = "own_polygon.shp"


# Enter for loop for each feature (only once)
#Following ArcPy documentation
desc = arcpy.Describe(infc)
shapefieldname = desc.ShapeFieldName
rows = arcpy.SearchCursor(infc)
for row in rows:
    feat = row.getValue(shapefieldname)
#Since only one feature, no need to work inside the loop
#Extracting the WKT
polygon_own = feat.WKT

#Splitting into list based on spaces
polygon_split = polygon_own.split(" ")

#initiate x and y coord lists
x_cor = []
y_cor = []

#append coordinate lists
for i in range(1,len(polygon_split)):
	if i%2 != 0:
		x_cor.append(float(re.sub('[(),]','',polygon_split[i])))
	else:
		y_cor.append(float(re.sub('[(),]','',polygon_split[i])))
	
#After looking at ex. 3, the coordinates were in separate tuples, 
#so zipping these to make sure compatible input is ensured
zipped_pol = zip(x_cor, y_cor)

#Using the exact same code from ex. 3 below
temp=0
for i in range(0, len(zipped_pol)):
	if i < len(zipped_pol)-1:            
        	temp += zipped_pol[i][0]*zipped_pol[i+1][1] - zipped_pol[i][1]*zipped_pol[i+1][0]
	else:
        	temp += zipped_pol[i][0]*zipped_pol[0][1] - zipped_pol[i][1]*zipped_pol[0][0]
#print(float(temp)/float(2))
print("Area: {}".format((float(temp)/float(2))))
#Gives exactly the same output as the area calculation as seen from screenshots
#2.21800425671e+23




