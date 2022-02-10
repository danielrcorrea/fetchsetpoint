import requests, json, time

def writeToFile(payload:str):
    '''Writes payload (string) to setpoint.json file
    
    Parameters:
    payload (str): data to be written to file

    Returns:
    None

    '''
    try:
        f = open('setpoint.json','w')
        f.write(payload)
        f.close()
    
    except Exception as e:
        print(f'Error writing to setpoint.json file ({e})')

def requestDataFromAPI(url:str):
    '''Request setpoint data from given API.
    
    Parameters:
    url (str): url which will be requested

    Returns:
    bool: succesfull / unsuccesfull
    str: data 

    '''
    dataAvailable = False
    getData = ''

    try:
        getData = requests.get(url)
        dataAvailable = True
    except Exception as e:
        #log error? put a default value to json file?
        print(f"Error requesting data from API ({e})")
        return False, NULL_PAYLOAD

    if dataAvailable:
        dataDict = getData.json()
        setpointVal = dataDict['elements'][uuid]['control']['ports']['top']['voltage']
        jsonPayload = {'setpoint': setpointVal}
        return True, json.dumps(jsonPayload)

url = 'http://188.166.104.86/actions/dcops/device/exercise'
uuid = '7d520da4-3283-45bf-98c2-02b371e63a4a'
NULL_PAYLOAD = ''


while True:
    ''' Main loop
    Requests data from API and write to a JSON file.
    This logic can be replaced with thread concept to avoid blocking due time.sleep function,
    allowing other logics to be implemented.
    '''
    success, payload = requestDataFromAPI(url)
    if success:
        writeToFile(payload)

    time.sleep(1)


    

    


