  ##################################################################
  #  Section 001H
  #  Computer Project #12
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################

#note: python 3.2.4 was used to create this program

import pylab

def average(file):
    junk = file.readline()
    junk = file.readline()

    #the first 2 lines are not needed
    
    mydict = {}
    highestdict = {}
    lowestdict = {}
    highest = 0
    lowest = 1000
    for line in file:
        line = line.split()
        if (int(line[0]),int(line[1])) in mydict:
            mydict[(int(line[0]),int(line[1]))].add(float(line[4]))
        else:
            mydict[(int(line[0]),int(line[1]))] = set()
            mydict[(int(line[0]),int(line[1]))].add(float(line[4]))

    #all of the temperatures are added with the day/month to the dictionary

    for key in mydict:
        for i in mydict[key]:
            if i > highest:
                highest = i
            if i < lowest:
                lowest = i
        highestdict[key] = highest
        lowestdict[key] = lowest
        highest = 0
        lowest = 1000

    #the highest and lowest for each day are added to a special dictionary

    janhigh = 0
    febhigh = 0
    marhigh = 0
    aprilhigh = 0
    mayhigh = 0
    junehigh = 0
    julyhigh = 0
    aughigh = 0
    septhigh = 0
    octhigh = 0
    novhigh = 0
    dechigh = 0
    
    for key in highestdict:
        if key[0] == 1:
            janhigh += highestdict[key]
        if key[0] == 2:
            febhigh += highestdict[key]
        if key[0] == 3:
            marhigh += highestdict[key]
        if key[0] == 4:
            aprilhigh += highestdict[key]
        if key[0] == 5:
            mayhigh += highestdict[key]
        if key[0] == 6:
            junehigh += highestdict[key]
        if key[0] == 7:
            julyhigh += highestdict[key]
        if key[0] == 8:
            aughigh += highestdict[key]
        if key[0] == 9:
            septhigh += highestdict[key]
        if key[0] == 10:
            octhigh += highestdict[key]
        if key[0] == 11:
            novhigh += highestdict[key]
        if key[0] == 12:
            dechigh += highestdict[key]

    #the highest for each day in a month is added
            
    janhigh = (janhigh/31)
    febhigh = (febhigh/29)
    marhigh = (marhigh/31)
    aprilhigh = (aprilhigh/30)
    mayhigh = (mayhigh/31)
    junehigh = (junehigh/30)
    julyhigh = (julyhigh/31)
    aughigh = (aughigh/31)
    septhigh = (septhigh/30)
    octhigh = (octhigh/31)
    novhigh = (novhigh/30)
    dechigh = (dechigh/31)

    #we then divide as necessary

    janlow = 0
    feblow = 0
    marlow = 0
    aprillow = 0
    maylow = 0
    junelow = 0
    julylow = 0
    auglow = 0
    septlow = 0
    octlow = 0
    novlow = 0
    declow = 0


    for key in lowestdict:
        if key[0] == 1:
            janlow += lowestdict[key]
        if key[0] == 2:
            feblow += lowestdict[key]
        if key[0] == 3:
            marlow += lowestdict[key]
        if key[0] == 4:
            aprillow += lowestdict[key]
        if key[0] == 5:
            maylow += lowestdict[key]
        if key[0] == 6:
            junelow += lowestdict[key]
        if key[0] == 7:
            julylow += lowestdict[key]
        if key[0] == 8:
            auglow += lowestdict[key]
        if key[0] == 9:
            septlow += lowestdict[key]
        if key[0] == 10:
            octlow += lowestdict[key]
        if key[0] == 11:
            novlow += lowestdict[key]
        if key[0] == 12:
            declow += lowestdict[key]
            
    janlow = (janlow/31)
    feblow = (feblow/29)
    marlow = (marlow/31)
    aprillow = (aprillow/30)
    maylow = (maylow/31)
    junelow = (junelow/30)
    julylow = (julylow/31)
    auglow = (auglow/31)
    septlow = (septlow/30)
    octlow = (octlow/31)
    novlow = (novlow/30)
    declow = (declow/31)

    #the same is done for the lowest of each month as above

    return janhigh,febhigh,marhigh,aprilhigh,mayhigh,junehigh,julyhigh,aughigh,septhigh,octhigh,novhigh,dechigh,janlow,feblow,marlow,aprillow,maylow,junelow,julylow,auglow,septlow,octlow,novlow,declow

def radiation(file1,file2):
    mydict = {}
    junk = file1.readline()
    junk = file1.readline()
    
    junk = file2.readline()
    junk = file2.readline()

    
    for line in file1:
        line = line.split()
        if line[0] == '6':
            mydict[(int(line[1]),int(line[3]))] = float(line[4])

        #we only care about the 6th month, june
        #the radiation for each hour is added to a dict

    rhour1 = 0
    rhour2 = 0
    rhour3 = 0
    rhour4 = 0
    rhour5 = 0
    rhour6 = 0
    rhour7 = 0
    rhour8 = 0
    rhour9 = 0
    rhour10 = 0
    rhour11 = 0
    rhour12 = 0
    rhour13 = 0
    rhour14 = 0
    rhour15 = 0
    rhour16 = 0
    rhour17 = 0
    rhour18 = 0
    rhour19 = 0
    rhour20 = 0
    rhour21 = 0
    rhour22 = 0
    rhour23 = 0
    rhour24 = 0


    for key in mydict:
        if key[1] == 100:
            rhour1 += mydict[key]
        if key[1] == 200:
            rhour2 += mydict[key]
        if key[1] == 300:
            rhour3 += mydict[key]
        if key[1] == 400:
            rhour4 += mydict[key]
        if key[1] == 500:
            rhour5 += mydict[key]
        if key[1] == 600:
            rhour6 += mydict[key]
        if key[1] == 700:
            rhour7 += mydict[key]
        if key[1] == 800:
            rhour8 += mydict[key]
        if key[1] == 900:
            rhour9 += mydict[key]
        if key[1] == 1000:
            rhour10 += mydict[key]
        if key[1] == 1100:
            rhour11 += mydict[key]
        if key[1] == 1200:
            rhour12 += mydict[key]
        if key[1] == 1300:
            rhour13 += mydict[key]
        if key[1] == 1400:
            rhour14 += mydict[key]
        if key[1] == 1500:
            rhour15 += mydict[key]
        if key[1] == 1600:
            rhour16 += mydict[key]
        if key[1] == 1700:
            rhour17 += mydict[key]
        if key[1] == 1800:
            rhour18 += mydict[key]
        if key[1] == 1900:
            rhour19 += mydict[key]
        if key[1] == 2000:
            rhour20 += mydict[key]
        if key[1] == 2100:
            rhour21 += mydict[key]
        if key[1] == 2200:
            rhour22 += mydict[key]
        if key[1] == 2300:
            rhour23 += mydict[key]
        if key[1] == 2400:
            rhour24 += mydict[key]

        #the radiation for each hour is added up

    rhour1 = (rhour1/30)
    rhour2 = (rhour2/30)
    rhour3 = (rhour3/30)
    rhour4 = (rhour4/30)
    rhour5 = (rhour5/30)
    rhour6 = (rhour6/30)
    rhour7 = (rhour7/30)
    rhour8 = (rhour8/30)
    rhour9 = (rhour9/30)
    rhour10 = (rhour10/30)
    rhour11 = (rhour11/30)
    rhour12 = (rhour12/30)
    rhour13 = (rhour13/30)
    rhour14 = (rhour14/30)
    rhour15 = (rhour15/30)
    rhour16 = (rhour16/30)
    rhour17 = (rhour17/30)
    rhour18 = (rhour18/30)
    rhour19 = (rhour19/30)
    rhour20 = (rhour20/30)
    rhour21 = (rhour21/30)
    rhour22 = (rhour22/30)
    rhour23 = (rhour23/30)
    rhour24 = (rhour24/30)

    for line in file2:
        line = line.split()
        if line[0] == '6':
            mydict[(int(line[1]),int(line[3]))] = float(line[4])

        #now we add the temperature the same way we did radiation above

    thour1 = 0
    thour2 = 0
    thour3 = 0
    thour4 = 0
    thour5 = 0
    thour6 = 0
    thour7 = 0
    thour8 = 0
    thour9 = 0
    thour10 = 0
    thour11 = 0
    thour12 = 0
    thour13 = 0
    thour14 = 0
    thour15 = 0
    thour16 = 0
    thour17 = 0
    thour18 = 0
    thour19 = 0
    thour20 = 0
    thour21 = 0
    thour22 = 0
    thour23 = 0
    thour24 = 0


    for key in mydict:
        if key[1] == 100:
            thour1 += mydict[key]
        if key[1] == 200:
            thour2 += mydict[key]
        if key[1] == 300:
            thour3 += mydict[key]
        if key[1] == 400:
            thour4 += mydict[key]
        if key[1] == 500:
            thour5 += mydict[key]
        if key[1] == 600:
            thour6 += mydict[key]
        if key[1] == 700:
            thour7 += mydict[key]
        if key[1] == 800:
            thour8 += mydict[key]
        if key[1] == 900:
            thour9 += mydict[key]
        if key[1] == 1000:
            thour10 += mydict[key]
        if key[1] == 1100:
            thour11 += mydict[key]
        if key[1] == 1200:
            thour12 += mydict[key]
        if key[1] == 1300:
            thour13 += mydict[key]
        if key[1] == 1400:
            thour14 += mydict[key]
        if key[1] == 1500:
            thour15 += mydict[key]
        if key[1] == 1600:
            thour16 += mydict[key]
        if key[1] == 1700:
            thour17 += mydict[key]
        if key[1] == 1800:
            thour18 += mydict[key]
        if key[1] == 1900:
            thour19 += mydict[key]
        if key[1] == 2000:
            thour20 += mydict[key]
        if key[1] == 2100:
            thour21 += mydict[key]
        if key[1] == 2200:
            thour22 += mydict[key]
        if key[1] == 2300:
            thour23 += mydict[key]
        if key[1] == 2400:
            thour24 += mydict[key]

    thour1 = (thour1/30)
    thour2 = (thour2/30)
    thour3 = (thour3/30)
    thour4 = (thour4/30)
    thour5 = (thour5/30)
    thour6 = (thour6/30)
    thour7 = (thour7/30)
    thour8 = (thour8/30)
    thour9 = (thour9/30)
    thour10 = (thour10/30)
    thour11 = (thour11/30)
    thour12 = (thour12/30)
    thour13 = (thour13/30)
    thour14 = (thour14/30)
    thour15 = (thour15/30)
    thour16 = (thour16/30)
    thour17 = (thour17/30)
    thour18 = (thour18/30)
    thour19 = (thour19/30)
    thour20 = (thour20/30)
    thour21 = (thour21/30)
    thour22 = (thour22/30)
    thour23 = (thour23/30)
    thour24 = (thour24/30)
    thour25 = 0

    rlist = [rhour1,rhour2,rhour3,rhour4,rhour5,rhour6,rhour7,rhour8,rhour9,rhour10,rhour11,rhour12,rhour13,rhour14,rhour15,rhour16,rhour17,rhour18,rhour19,rhour20,rhour21,rhour22,rhour23,rhour24]             
    tlist = [thour1,thour2,thour3,thour4,thour5,thour6,thour7,thour8,thour9,thour10,thour11,thour12,thour13,thour14,thour15,thour16,thour17,thour18,thour19,thour20,thour21,thour22,thour23,thour24]             
    #the radiation and temperatures are made into a list we can use later
    return rlist,tlist

def main():
    temperature_file = open('temperature.txt')
    radiation_file = open('solar_radition.txt')

    #the necessary files are opened, the function is called below
    
    rlist,tlist = radiation(radiation_file,temperature_file)

    pylab.title("Charleston, MO - June, 2012")
    pylab.ylabel("Average Temperature",color='b')
    pylab.yticks(color='b')
    pylab.xlabel("Hour")
    pylab.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],tlist,color='b',marker='o')
    otheraxis = pylab.twinx()
    otheraxis.set_ylabel("Average Solar Radiation",color='r')
    pylab.yticks(color='r')
    otheraxis.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],rlist,color='r',marker='o')
    pylab.savefig('radiation.png')
    pylab.close()

    #the figure is created and we save it
    
def main1():
    temperature_file = open('temperature.txt')

    janhigh,febhigh,marhigh,aprilhigh,mayhigh,junehigh,julyhigh,aughigh,septhigh,octhigh,novhigh,dechigh,janlow,feblow,marlow,aprillow,maylow,junelow,julylow,auglow,septlow,octlow,novlow,declow = average(temperature_file)
    pylab.title("Charleston, MO - 2012")
    pylab.ylabel("Average Temperature")
    pylab.xticks([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5], ['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.'])
    pylab.bar([1,2,3,4,5,6,7,8,9,10,11,12], [janhigh-janlow,febhigh-feblow,marhigh-marlow,aprilhigh-aprillow,mayhigh-maylow,junehigh-junelow,julyhigh-julylow,aughigh-auglow,septhigh-septlow,octhigh-octlow,novhigh-novlow,dechigh-declow], bottom=[janlow,feblow,marlow,aprillow,maylow,junelow,julylow,auglow,septlow,octlow,novlow,declow])
    pylab.savefig('temperature.png')
    pylab.close()

#this is the same thing as the original main function.
#a second one had to be created because the second figure would show otherwise


main()
main1()
