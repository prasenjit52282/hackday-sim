import gmplot
from datetime import datetime

def getLabel(label_filename):
    label_file = open(label_filename,"r")
    text = label_file.readlines()
    labels=[]
    for line in text:
        mydict={}
        label = line.split(",")
        mydict["start"]=label[0]
        mydict["end"]=label[1]
        mydict["condition"] = label[2].replace('\n','')
        labels.append(mydict)
    return labels

def getCoOrdinates(gps_filename):
    gps_file = open(gps_filename,"r")
    text = gps_file.readlines()
    ordinates = []
    for line in text:
        mydict={}
        crd = line.split(",")
        mydict["lat"]=crd[0]
        mydict["long"]=crd[1]
        mydict["speed"]=crd[2]
        mydict["altitude"]=crd[3]
        mydict["date"]=crd[4].split(" ")[0]
        mydict["time"]=crd[4].split(" ")[1]
        ordinates.append(mydict)
    return ordinates

def getCoOrdinate(gps_data,start,current,last):
    start = datetime.strptime(start,'%H:%M:%S')
    current = datetime.strptime(current,"%M:%S")
    zero = datetime.strptime('00:00:00','%H:%M:%S')
    now = (start - zero + current).time()
    for i in range(last+1,len(gps_data)):
        if gps_data[i]['time']==str(now):
            print(now)
            return i
    return ""

def getLatitudes(gps_data):
    lat=[]
    for i in gps_data:
        lat.append(float(i['lat']))
    return lat

def getLongitudes(gps_data):
    long=[]
    for i in gps_data:
        long.append(float(i['long']))
    return long
    

def mapPlot():
    lat=[23.49445753,23.49441251,23.49430737]
    long=[87.31693473,87.31694955,87.31714791]
    gmapOne = gmplot.GoogleMapPlotter(23.49445753,87.31693473,18)
    gmapOne.plot(lat,long,"blue",edge_width=2.5)
    gmapOne.draw("map.html")

def driver():
    label_filename="label.txt"
    gps_filename="gps.txt"
    labels = getLabel(label_filename)
    coordinates = getCoOrdinates(gps_filename)
    start_time = coordinates[0]['time']
    lat=getLatitudes(coordinates)
    long=getLongitudes(coordinates)
    gmapOne = gmplot.GoogleMapPlotter(lat[0],long[0],18)
    color={'-1':'blue','1':'green','2':'yellow','3':'#FF0000'}
    c=0
    for label in labels:
        i = getCoOrdinate(coordinates,start_time,label['end'],0)
        print(i,label['condition'])
        condition = label['condition']
        gmapOne.scatter(lat[c:i+1],long[c:i+1],color[condition],size=1,marker=False)
        gmapOne.plot(lat[c:i+1],long[c:i+1],color[condition],edge_width=2.5)
        c+=i+1
    gmapOne.draw("map.html")

if __name__ == "__main__":
    driver()
    # mapPlot()
    
    