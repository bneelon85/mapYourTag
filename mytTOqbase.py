import requests
import json
import pandas as pd
import math

#CONSTANTS
resTypeID = '5a72215fc46e6a164632296c'
headers = {'Authorization': 'Md34bPCxKi2VCuPznLYx'}
baseUrl = 'https://www.mapyourtag.com/api/v1/clients/5a7220e9c46e6a1646322961'

#CREATE DATAFRAME FOR ALL ASSETS!!!
allAssetsUrl = baseUrl+'/resourcetypes/'+resTypeID+'/resources'
allAssets = json.loads(requests.get(allAssetsUrl, headers = headers).text)
assetsDict = []


for i in range(1, (math.ceil(allAssets['total']/100)+1)):
    x = json.loads(requests.get(allAssetsUrl+'?page='+str(i),headers = headers).text)['resources']
    for n in range(0,len(x)):
        assetsDict.append(x[n])

allAssetsDF = pd.DataFrame.from_records(assetsDict)
allAssetsDF.to_csv('assets.csv')
print(allAssetsDF.head())

#CREATE DATAFRAME FOR ALL TAGS!!!
tagURL = baseUrl+'/tags'
tags = json.loads(requests.get(tagURL, headers = headers).text)
tagsDict = []

for i in range(1, (math.ceil(tags['total']/100)+1)):
    x = json.loads(requests.get(tagURL+'?page='+str(i),headers = headers).text)['tags']
    for n in range(0,len(x)):
        tagsDict.append(x[n])

tagsDF = pd.DataFrame.from_records(tagsDict)
tagsDF.to_csv('tags.csv')
print(tagsDF.head())

#CREATE DATAFRAME FOR ALL Users!!!
usersURL = baseUrl+'/clientroles.json'
users = json.loads(requests.get(usersURL, headers = headers).text)
usersDF = pd.DataFrame.from_dict(users['clientroles'])
usersDF.to_csv('users.csv')
print(usersDF.head())

#CREAT DATAFRAME FOR LOCATIONS
assetIDs = []

for i in assetsDict:
    assetIDs.append(i['id'])

locationsDict = []

for i in assetIDs:
    x = json.loads(requests.get(baseUrl+'/resourcetypes/'+resTypeID+'/resources/'+i+'/locations',headers = headers).text)['locations']
    for i in x:
        locationsDict.append(i)



locationsDF = pd.DataFrame.from_records(locationsDict)
locationsDF.to_csv('locations.csv')
print(locationsDF.head())
















#resourceTypesUrl = baseUrl+'/resourcetypes.json'
#AssetsUrl = baseUrl+'/resourcetypes/'+resTypeID+'/resources/5adce945dc4b24001c436622.json'
#locationUrl = baseUrl+'/resourcetypes/'+resTypeID+'/resources/asdgasd/locations.json'

#resourceTypes = json.loads(requests.get(resourceTypesUrl, headers = headers).text)
#Asset = json.loads(requests.get(AssetsUrl, headers = headers).text)

#location = json.loads(requests.get(locationUrl, headers = headers).text)
#print(location)
#print(Asset.text)
#print(resourceTypes.text)
#print(allAssets)
#print(requests.get(allAssetsUrl, headers = headers).text)
#print(location['locations'][0])
#print(requests.get(tagURL, headers = headers).text)
#print(requests.get(locationUrl, headers = headers).text)
#print(requests.get(usersURL, headers = headers).text)

#tagsDF = pd.DataFrame.from_dict(tags['tags'])