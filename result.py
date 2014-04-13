__author__ = 'dylan'
import datetime
infoArray = []
security=""
ticker =""
date = ""
last_price=""
open_price=""

with open('example.txt') as f:

    for line in f.readlines():
        infoElement = dict()

        if "security" in line:
            # print line[line.rfind("security = ")+10:line.rfind('"')+1]
            ticker = line[line.rfind('security = "')+10:line.rfind('"')+1]
            # infoElement.update({"ticker": ticker})

        if "date =" in line:
            date = line[line.rfind('date =')+7:line.rfind('date =')+17]
            # print date
            print datetime.datetime.strptime(date,"%Y-%m-%d")

        if "PX_LAST =" in line:
            last_price=line[line.rfind('PX_LAST =')+10:line.rfind('PX_LAST =')+15]
            print type(float(last_price))
            # infoElement.update({"last_price":line[line.rfind('PX_LAST =')+10:line.rfind('PX_LAST =')+15]})

        if "OPEN =" in line:
            open_price = line[line.rfind('OPEN =')+6:line.rfind('OPEN =')+12]
        infoElement.update({"ticker":ticker,"date":date,"last_price":last_price,"open_price":open_price})
        if "fieldData =" in line:
            infoArray.append(infoElement)

infoArray.pop(0)

print infoArray



