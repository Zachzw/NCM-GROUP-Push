import requests
import csv
import json
import logging
import Group_ID_Prompt


def end_prompt():
  print('Press Enter to exit')
  input()

# Import API keys from CSV and assigns them variables
def main():

  with open('API_keys.csv', 'r') as f:
    reader = csv.reader(f)
    API_list = list(reader)

  a, b, c, d = API_list

 # JSON Headers for NCM
  headers = {
      'X-CP-API-ID': f'{a[0]}',
      'X-CP-API-KEY': f'{b[0]}',
      'X-ECM-API-ID': f'{c[0]}',
      'X-ECM-API-KEY': f'{d[0]}',
      'Content-Type': 'application/json' 
  }
 # Pulls Group ID from Group_ID.txt, injects it into the NCM Group endpoint, then assigns that endpoint to a variable

  with open('Group_ID.txt', 'r') as f:
    group_ID=f.read()    

  print(f'You entered the group ID: {group_ID}')
  NCMendpoint = f'https://www.cradlepointecm.com/api/v2/groups/{group_ID}/' 
  print(f'Your API endpoint is {NCMendpoint}')

 # Imports the payload from Load.txt and verifys it's in a valid JSON format

  try:
    with open('Load.txt', 'r') as f:
      payload=f.read()
      payload_json = json.loads(payload) 
  except: 
    print('Invalid JSON file')     
    end_prompt()    
  else:
    print('Valid JSON file')        
             
 # API call to NCM

  r = requests.put(NCMendpoint,json=payload_json,headers =headers)
  r.status_code
 
 # Prints status codes from the API call
 
  if r.status_code == 202:
    print(f'Status Code: {r.status_code}\nSuccessfully PUT config to NCM')
  elif r.status_code == 401:
    print(f'Status Code: {r.status_code}\n***Authorization Failed: Verify your API keys***')     
  elif r.status_code == 403:
    print(f'Status Code: {r.status_code}\n***Verify your Group ID***') 
      

  end_prompt()


if __name__ == "__main__":
     main()




