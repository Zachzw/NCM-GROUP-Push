import requests
import csv
import json
import logging

#Import API keys from CSV and assigns them variables

end = 'Press Enter to exit'

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

  # Imports the payload from Load.txt and verifys it's in a valid JSON format

  try:
    with open('Load.txt', 'r') as f:
      payload=f.read()
      payload_json = json.loads(payload) 
  except: 
    print(f'Invalid JSON, {end}')     
    input()     
  else:
    print('Valid JSON')        
        
    # Pulls payload from .txt and assigns it a variable.

  r = requests.put(NCMendpoint,json=payload_json,headers =headers)
  r.status_code
 
  # Prints status codes from the API call
 
  if r.status_code == 202:
    print(f'Status Code: {r.status_code} Successfully PUT config to NCM')
  elif r.status_code == 401:
    print(f'Status Code: {r.status_code} Authorization Failed: Verify your API keys')
  elif r.status_code == 403:
    print(f'Status Code: {r.status_code} Verify your Group ID') 
      

  print(end)
  input()


if __name__ == "__main__":
    main()




