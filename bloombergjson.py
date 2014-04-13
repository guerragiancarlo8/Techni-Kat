__author__ = 'dylan'
import requests
import json
import os
import datetime

class bloombergjson(object):
    def __init__(self):
        pass
    def getJson(self):
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
                    ticker = line[line.rfind('security = "')+10:line.rfind('"')+1]

                if "date =" in line:
                    dateStr = line[line.rfind('date =')+7:line.rfind('date =')+17]
                    date = datetime.datetime.strptime(dateStr,"%Y-%m-%d")

                if "PX_LAST =" in line:
                    last_price=float(line[line.rfind('PX_LAST =')+10:line.rfind('PX_LAST =')+15])

                if "OPEN =" in line:
                    open_price = float(line[line.rfind('OPEN =')+6:line.rfind('OPEN =')+12])

                infoElement.update({"ticker":ticker,"date":date,"last_price":last_price,"open_price":open_price})
                if "fieldData =" in line:
                    infoArray.append(infoElement)
            infoArray.pop(0)

        return infoArray



