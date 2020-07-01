import requests
import csv
import json
import logging

#Import API keys from CSV and assigns them variables

def main():

  with open('API_keys.csv', 'r') as f:
    reader = csv.reader(f)
    API_list = list(reader)

  a, b, c, d = API_list

#JSON Headers for NCM
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

  print('Your group ID is ' + group_ID)
  NCMendpoint = f'https://www.cradlepointecm.com/api/v2/groups/{group_ID}/' 
  print(NCMendpoint)

  # Pulls payload from .txt and assigns it a variable.

  try:
    with open('Load.txt', 'r') as f:
      payload=f.read()
      payload_json = json.loads(payload) 
  except: 
    print('Invalid JSON')      
  else:
    print('Valid JSON')        
        
    
  r = requests.put(NCMendpoint,json=payload_json,headers =headers)
  r.status_code
  print(f'Status Code: {r.status_code}')
  
 
  if r.status_code == 202:
    print('Successfully PUT config to NCM')
  elif r.status_code == 401:
    print('Authorization Failed: Verify your API keys')
  elif r.status_code == 403:
    print('Access Forbidden: Verify your Group ID')
  elif r.status_code == 400:
    file = open("JSON_Error.txt","w")
    file.write(r.status_code)  
    file.close()
  

  print('Press Enter to close')
  input()


if __name__ == "__main__":
    main()




