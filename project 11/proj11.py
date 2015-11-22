  ##################################################################
  #  Section 001H
  #  Computer Project #11
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################


import urllib.request

class Tour(object):
    def __init__(self,*city):
        self.city = city
        self.citylist = list(self.city)
        
#this defines the tour and uses *city so you can use as many cities as you like

    def distance(self,mode='driving'):
        try:
            driving_str = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins='     
            count = 0
            distance_combined = []
            while (count+1) < len(self.citylist):
                origin = self.citylist[count].split(', ')
                if ' ' in origin[0]:
                    origin[0] = origin[0].replace(' ','')
                if ' ' in origin[0]:
                    origin[0] = origin[0].replace(' ','')
                destination = self.citylist[(count+1)].split(', ')
                if ' ' in destination[0]:
                    destination[0] = origin[0].replace(' ','')
                if ' ' in destination[0]:
                    destination[0] = origin[0].replace(' ','')

#we split the citylist into each of the origin cities and destination cities

                driving_str2 = driving_str + origin[0]
                driving_str2 += '+'
                driving_str2 += origin[1]
                driving_str2 += '&destinations='
                driving_str2 += destination[0]
                driving_str2 += '+'
                driving_str2 += destination[1]
                driving_str2 += '&mode='
                driving_str2 += mode
                driving_str2 += '&sensor=false'
                web_obj = urllib.request.urlopen(driving_str2)
                results_str = str(web_obj.read())
                web_obj.close()
                results_list = results_str.split()

#for each of the origin/destination sets, the url is opened and read
                
                try:
                    distance_list = list(results_list[32])
                    distance_stuff = ''.join(distance_list[0:-2])
                    int(distance_stuff)
                except ValueError:
                    try:
                        distance_list = list(results_list[33])
                        distance_stuff = ''.join(distance_list[0:-2])
                        int(distance_stuff)
                    except ValueError:
                        distance_list = list(results_list[34])
                        distance_stuff = ''.join(distance_list[0:-2])

#the distances are all added to a list                    
                    
                distance_stuff = ''.join(distance_list[0:-2])
                distance_combined.append(distance_stuff)
                count += 1

            count = 0
            distance = 0
            for i in distance_combined:
                distance = distance + int(distance_combined[count])
                count += 1

#every distance is added together and becomes the total distance that is returned

            return distance

        except IndexError:
            raise ValueError ('No distance value.')

        except ValueError:
            return "No distance could be calculated"

    def __str__(self):
        size = "%s; "*(len(self.city)-1) + "%s"
        return size % (self.city)

#the amount of cities is calculated and then each city is printed with formatting

    def __repr__(self):
        return self.__str__()

    def __add__(self,newTour):
        t3 = Tour()
        t3.citylist = self.citylist + newTour.citylist
        t3.city = tuple(t3.citylist)
        return t3

#a new tour is returned with the city list of both cities that were added

    def __mul__(self,int1):
        if int1 < 0:
            raise ValueError ("Integer is negative.")
        if type(int1) != int:
            raise TypeError ("Integer must be integer")
        t4 = Tour()
        t4.citylist = self.citylist * int1
        t4.city = tuple(t4.citylist)
        return t4

#the new tour is returned as the list of the cities from the original tour multiplied by the integer
        
    def __rmul__(self,rhs):
        return self.__mul__(rhs)

    def __gt__(self,other):
        selfdistance = self.distance()
        otherdistance = other.distance()
        if selfdistance > otherdistance:
            return True
        else:
            return False

#if the distance of self is more than other, True is returned

    def __lt__(self,other):
        selfdistance = self.distance()
        otherdistance = other.distance()
        if selfdistance < otherdistance:
            return True
        else:
            return False

#if the distance of self is less than other, True is returned

    def __eq__(self,other):
        if self.citylist == other.citylist:
            return True
        else:
            return False

#if the two tours go to the same exact cities in the same order, True is returned

        
def main():
    t1 = Tour("New York, NY", "Lansing, MI", "Sacramento, CA")
    t2 = Tour("Oakland, CA")
    t3 = Tour("Sacramento, CA", "Oakland, CA")
    print("t1: {}\nt2: {}\nt3: {}".format(t1,t2,t3))
    print("t1 distances: driving-{} km; biking-{} km; walking-{} km".format(round(t1.distance()/1000), round(t1.distance('bicycling')/1000),round(t1.distance('walking')/1000)))
    print("Using driving distances from here on.")
    t4 = t1 + t2
    print("t4 (t1 + t2):", t4)
    print("t4 driving distance:", round(t4.distance()/1000),"km")
    t5 = t1 * 2
    print("t5 (t1 * 2):",t5)
    t6 = 3 * t3
    print("t6 (3 * t3):",t6)
    print("t1 > t2:", t1 > t2)
    print("t1 < t2:", t1 < t2)
    print("t4 == t1 + t2:", t4 == t1 + t2)
    print("t4 == t1 + t3:", t4 == t1 + t3)

#all methods are tested.

main()

