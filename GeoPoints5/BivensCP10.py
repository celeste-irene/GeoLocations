
import math

class GeoPoint:
    def __init__(self, lat=0, lon=0, description ="TBD"):
        self.lat = lat
        self.lon = lon
        self.description = description

    def setPoint(self, point): 
        self.lat = point[0]
        self.lon = point[1]
    def getPoint(self):
        return self.lat, self.lon
    point = property(getPoint,setPoint)

    def setDescription(self, description ):
        self.description = description
    def getDescription (self):
        return self.description.rstrip()
    description = (getDescription, setDescription)

    def calcDistance(self, point):

        r= 6371.0
        lat1 = math.radians(self.lat)
        long1 = math.radians(self.lon)
        lat2 = math.radians(point.lat)
        long2 = math.radians(point.lon)
        a = math.sin((lat2-lat1)/2.0)**2 + math.cos(lat1)*math.cos(lat2)* math.sin((long2-long1)/2.0)**2
        c = 2.0*math.atan2(math.sqrt(a), math.sqrt(1.0-a))
        d = r*c
        return d

#function for reading the txt file and seperating line. 
def OpenPointsList(Points):
    f = open(Points)
    lines = f.readlines()
    #Empty list that gets filled with each item after an iteration. 
    pointList = []
    for line in lines:
        #Splits the line of text into three seperate items which have the comma and assigns variables to them.
        x = line.split(',')
    
        lat = float(x[0])
        lon = float(x[1])
        description = x[2]
        coordinateTuple = (lat, lon, description)
        #Appends the list so that each item for the 5 lines can go into the empty list. 
        pointList.append(coordinateTuple)
    
    return pointList

#Header for the program.
def header():
    print('Welcome to the ultimate and supreme geography point calculater number 5!')
    print('In this program, I utilized text files in order to provide a list of different locations')
    print("Please enter your location's latitude and longitude coordinates(in degrees).")
    print("You'll see whether you're closer to 1 out of 5 locations!")

#Goodbye message.
def goodbyeMessage():
    print('Thank you for using my program!')

#Function that prompts user if they want to do the program again. 
def doanother():
    usrResponse = input('Would you like to calculate again? (yes/no): ')
    another = usrResponse.strip()[0].lower() == 'y'
    return another


#Main part of the program. 
if __name__ == "__main__":
    #Assigns a variable to the filename 
    fileName = 'Points.txt'
    #Assigns variable to the calling of the OpenPointsList function. 
    pointList = OpenPointsList(fileName)

    #Empty GeoPoint list
    geoPointList = []
    for point in pointList:
        #Constructor that creates an instance of the points from the txt file into the GeoPoint class.
        geoPoint = GeoPoint(point[0], point[1], point[2])
        geoPointList.append(geoPoint)
    
    print()
    header()
    print()

    doAnother ='y'
    while doAnother =='y':
        try:
            userLat = float(input('Please enter the latitude of your location(in degrees): '))
            userLon = float(input('Please enter the longitude of your location(in degrees): '))
            print()

            pointUser = GeoPoint(userLat, userLon, 'User Location')
            
            #Empty list for each item to be contained in after each iteration in the for loop. 
            distanceToGeoPointList = []
            for point in geoPointList:
                #Calculates the distance between the user's points and all of the 5 locations points 
                distance = point.calcDistance(pointUser)
                #Assigns variable to the distance found in line 71 and the points of the locations. 
                distToGeoP = (distance, point)
                #Appends the list and iterates each item. 
                distanceToGeoPointList.append(distToGeoP)

            #Sorts the new list by ascending order starting from the smallest number tuple for the distance. 
            sortedList = sorted(distanceToGeoPointList)
            #Isolates the first tuple in the ascended order in the sorted list. 
            closestPointTuple = sortedList[0] 
            #Assignes variable to tuple in line 80.
            closestGeoPoint = closestPointTuple[1]
            print(f'Closest point is {closestGeoPoint.getDescription()} which is located {closestGeoPoint.getPoint()}')
         #Displays error message when a type error isn't attributed right.
        except TypeError:
            print('Wrong type of input!')
        #Displays message when the value that was the input wasn't a number. 
        except ValueError:
            print('Not a number. Try again please.')
        #Displays this message when any exception other than a TypeError or ValueError occurs.
        except Exception as e:
            print(f'Something went wrong:',e)
        print()
        if not doanother():
            break

    
    goodbyeMessage()
    print()