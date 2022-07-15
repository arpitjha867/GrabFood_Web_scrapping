import pandas as pd
import math
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


def clean(df):
    names = df["Name"]
    for i in range(len(names)):
        names[i] = names[i].split("-")[0]
    distance = df['Distance']
    for i in range(len(distance)):
        distance[i] = distance[i].split("•")[1].strip()
        distance[i] = distance[i].split(" ")[0]
        distance[i] = float(distance[i])
    print("Data cleaned successfuly...")
    print("\n\n")
    print("Converting the distance into latitude and longitude range")
    print("\n\n")
    getLatLong(df)
def getLatLong(df):
    orginal_location_latitude=float(1.2931)
    orginal_location_longitude=float(103.8535)
    distance=df['Distance']
    latitude_range=[]
    for i in range(len(distance)):
        new_latitude_1st=float(orginal_location_latitude+distance[i]*(1/111))
        new_latitude_2nd=float(orginal_location_latitude-distance[i]*(1/111))
        lat=str(f"{new_latitude_1st} to {new_latitude_2nd}")
        latitude_range.append(lat)
    df['Latitude_Range']=latitude_range  
    longitude_list=[]
    for i in range(len(distance)):
        new_long_1st=orginal_location_longitude+(distance[i]*(1/(math.cos(orginal_location_latitude)*111.32)))
        new_long_2nd=orginal_location_longitude-(distance[i]*(1/(math.cos(orginal_location_latitude)*111.32)))
        long=str(f"{new_long_1st} to {new_long_2nd}")
        longitude_list.append(long)
    df['Longitude_Range']=longitude_list 
    print("Converted the distance from original address position to range of possible Latitude and Longitude...")
    print("\n\n")
    
