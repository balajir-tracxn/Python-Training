import json
from utils import callApi,writeJson,readJsonFile,createCSV,csvColoumIndexing,companyCSVHeaders
from dotenv import load_dotenv
import os

load_dotenv()   

headers = {
      "X-Request-Source": os.getenv("URL_SOURCE"),
      "accessToken": os.getenv("URL_ACCESS_TOKEN"),
    }

def companyData():
    print("Fetching Company data")

    payLoad ={
    "dataset": "query",
    "size":100,
    "from":0,
    "filter": {
        "isFunded": True,
        "companyStage": [
            "Series E"
            ]
        }
    }
    url=os.getenv("COMPANY_URL")

    data = callApi(url=url,headers=headers,payload=payLoad)

    if isinstance(data,str):
        print("No data found:",data)
    else:


        total_count = data["total_count"]
        data_count =len(data['result'])


        while data_count<total_count:
            payLoad["from"]=data_count
            tempData= callApi(url=url,payload=payLoad,headers=headers)
            data['result'].extend(tempData['result'])
            data_count=data_count+len(tempData['result'])
        
        
        writeJson("CompanyData.json",data)
        print("Finished Writing")


    print("Total Results Count:",len(data['result']))
    print("Payload Total Count:",data['total_count'])


# def fundingRoundsData():
#     print("Fetching Funding Rounds data by company Funding")

#     payLoad ={
#     "dataset": "query",
#     "filter": {
#         "fundingRoundId" : []
#         }
#     }
#     url=os.getenv("FUNDING_ROUND_URL")

#     data =readJsonFile("CompanyData.json")
#     if(data==False):
#         print("No data Found in CompanyData.json")
#         return
    
#     print(data['total_count'])



# def createCompanyCSV():
#     data =readJsonFile("CompanyData.json")
#     if(data==False):
#         print("No data Found in CompanyData.json")
#         return

    

#     indexedRange =csvColoumIndexing(dataKeys=list(data['result'][0].keys()),arrHeaders=companyCSVHeaders.keys())

#     arr =[]
#     arr.append(list(companyCSVHeaders.values()))

#     for i in data['result']:
#         for key,val in indexedRange.items():
#             if i[key]:
#                 temparr =[]
#                 temparr.insert(val,i[key])
#                 arr.append(temparr)

#     # for key,val in indexedRange.items():
#     #     temparr =[]
#     #     temparr.insert(val,data.result[][key])
#     #     arr.append(temparr)
    
#     print(arr)

#     # createCSV(data)

companyData()
# fundingRoundsData()
# createCompanyCSV()