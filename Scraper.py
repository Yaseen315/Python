
# Importing functions which allows data to be extracted
from lxml import html
import requests
import numpy as np 
import pandas as pd
# import matplotlib.pyplot as plt 

# graph = plt.figure()
# plt.show()

def weather_report(URL):
# Chosen website
    page = requests.get(URL)
   
    # Extracting HTML
    data = html.fromstring(page.content)

    # Extacting data from BBC weather for days, min & max temp
    day = data.xpath('//*[@id="blq-content"]/div[7]/div[2]/ul/li/a/div/h3/span/text()')
    max_temp = data.xpath('//*[@id="blq-content"]/div[7]/div[2]/ul/li/a/span[2]/span/span[1]/text()')
    min_temp = data.xpath('//*[@id="blq-content"]/div[7]/div[2]/ul/li/a/span[3]/span/span[1]/text()')
    location = data.xpath('//*[@id="blq-content"]/div[1]/h1/span/text()')
    print (location[0])

    # Inputting figues into a chart
    a=np.zeros((5,3),dtype='object')
    a[:,0] = day
    a[0:,1] = min_temp
    a[0:,2] = max_temp
    a[:,1] = a[:,1].astype(int)
    a[:,2] = a[:,2].astype(int)
    print (a)
    a = pd.DataFrame(a) 
    a.to_csv(location[0] + ".csv")


weather_report('http://www.bbc.co.uk/weather/2650430')
weather_report('http://www.bbc.co.uk/weather/2639842')
weather_report('http://www.bbc.co.uk/weather/2636979')

