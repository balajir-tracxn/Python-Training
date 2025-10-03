import requests
import json
import csv

def callApi(url,headers,payload):
  try:
    print("API call Initiated. URL:",url)
    url =url
    response = requests.post(url=url,headers=headers,json=payload)

    if response.status_code == 200:
        print("Response Data Sent")
        return response.json()
    else:
        return f'Error: {response.status_code}'
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def writeJson(fileName,Jsondata):
    try:
        json_str = json.dumps(Jsondata,indent=2)
        with open(fileName, "w") as f:
            f.write(json_str)
            f.close()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def readJsonFile(fileName):
    try:
        with open(fileName, "r") as f:
            data =json.load(f)
            f.close()
        return data
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    
def createCSV(twoDimArr):
    try:
        with open('output_dict.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(twoDimArr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

companyCSVHeaders ={
        "name":"Company Name",
        "domain":"Domain",
        "tracxnScore":"Tracxn Score",
        "foundedYear":"Founded Year",
        "shortDescription":"Short Description",
        "xcorn":"X Corn Status",
        "editorRating":"Editor's Rating",
        "location":"Locations",
        "stage":"Company Stage",
        "totalEquityFunding":"Total Equity Funding",
        "latestEmployeeCount":"Latest Employee Count",
    }

def csvColoumIndexing(dataKeys,arrHeaders):
    temp ={}
    for i in arrHeaders:
        temp[i]=dataKeys.index(i)
    return temp

        