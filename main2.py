import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
import math
from clean_and_convert import clean


driver=webdriver.Chrome(service=Service(executable_path="./chromedriver"))
driver.implicitly_wait(15)
print("Location : The Stamford, Raffles City Robinsons, 2 Stamford Rd")
driver.get("https://food.grab.com/sg/en/restaurants?search=The%20Stamford%2C%20Raffles%20City%20Robinsons%2C%202%20Stamford%20Rd&lng=en")
time.sleep(15)
print("\n\n")
print("Please ignore connection warning and errors.")
print("\n\n")
print("If script fails to run please run the script again")
print("\n\n")
print("Please wait while I load all of the restaurants...")
print("This may take few minutes...")
print("\n\n")
while True:
    try:
        load_more=driver.find_element(By.CSS_SELECTOR,"button[type='button']")
        load_more.click()
        time.sleep(15)
    except Exception as e:
        print ("All restraunts are now loaded on the web page ...")
        break
print("\n\n")
print("Getting the restaurants...")
list_restraunt_info=driver.find_elements(By.CSS_SELECTOR,"div[class='ant-col-24 RestaurantListCol___1FZ8V  ant-col-md-12 ant-col-lg-6']")
print("\n\n")
print("Got the restaurants....")
print("\n\n")
#print(list_restraunt_info)
# getting the info from each restraunt 
full_info_data=[]
counter=1
for i in list_restraunt_info:
    info_restraunt=[]
    print(f"getting info for {counter} restraunt.....")
    name=i.find_element(By.CSS_SELECTOR,"h6[class='name___2epcT']").text
    #time.sleep(3)
    info_restraunt.append(name)
    distan=i.find_elements(By.CSS_SELECTOR,"div[class='numbersChild___2qKMV']")
    if len(distan)==2:
        distan=distan[1].text
    else:
        distan=distan[0].text
    #time.sleep(3)
    info_restraunt.append(distan)
    full_info_data.append(info_restraunt)
    print(f"got info for {counter} restraunt ....")
    counter+=1
print("\n\n")
print("Quiting driver...")
print("\n\n\n")
driver.quit()
print("Driver Exited successfully...")
print("\n\n")
#print(full_info_data)
df = pd.DataFrame(full_info_data, columns=['Name', 'Distance'])
#df.to_csv(r"C:\Users\ASUS\Desktop\Arpit jha Anakin intern assignment\scrapped_data\sample_Data.csv", index = False, header=True)
#df.to_csv(r"./scrapped_data/final_dataset.csv", index = False, header=True)
print(" Cleaning the scrapped data...")
print("\n\n")
clean(df)
df.to_csv(r"./scrapped_data/final_dataset.csv", index = False, header=True)
print(" Data file saved in the scrapped_data folder ...")
print("\n\n")
print(" !!!!! Scrapping Complete !!!!!!")
print("\n\n")
print("It might be possible all of the restaurants have not being loaded due to slow internet connection.")
print("So try running the script again.")






