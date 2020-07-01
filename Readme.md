# Prerequisites

1. Have `Set-ExecutionPolicy -ExecutionPolicy Unrestricted` ran on your Windows machine

1. [Python 3.8.x](https://www.python.org/downloads/) installed on machine

2. Python library [virtualenv](https://virtualenv.pypa.io/en/stable/) installed on machine


# Installation (Manual) in Powershell or CMD window

1. Create virtual environment in main directory

        virtualenv venv

1. Activate virtual environment

        ./venv/Scripts/activate

1. Install python requests library

        pip3 install requests

# Installation (Automatic)

1. Run Install_Env.ps1


# User Guide

1. Add API keys to API_keys.csv in the following format
    
        X-CP-API-ID
        X-CP-API-KEY
        X-ECM-API-ID
        X-ECM-API-KEY
    
    ### Example API_keys file:
    
        not547r1
        8125bd72135dacme697566234673
        f6afak38d-d67a-4b66-b958-a2435299992d21
        10c53659jgkafoob4rsaedfffeb7sc00bs00995

1. Set your NCM Group ID in the `Group_ID.txt` file

        193340

1. Put Configuration payload in Load.txt with the JSON Wrapper

    ### NCM JSON Wrapper

        "configuration": [{<DATA GOES HERE>},[]]}


1. Run the script (manually)

        cd %USERPROFILE%\~\Python_NCM_Group_Push

        ./venv/Scripts/activate
        
        python .\GroupPush.py

1. OR run the `run.ps1` to activate and run the Group_ID_Prompt.py & GroupPush.py files

1. Response 202  is a successful PUT



