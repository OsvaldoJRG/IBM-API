import requests
import pytest
import datetime as date

### TEST DATA ###
# Expected error message from API
errorMsg = "No valid parameter received, type 'help' for more information"
slash = "/"
# API main adrress
mainAddress = "http://127.0.0.1:5000"
# Functionalities implemented in API
funtionalities = ["datetime","calculator"]

### DATETIME FUNCTIONALITY ###
# Valid commands
validDatetimeCmds = ["year","month","day","hour","minute","second","complete"]
# Invalid commands
invalidDatetimeCmds = ["Year","Mpnth","Dayu","houR","test","int(8)","str"]

# CALCULATOR FUNCTIONALITY
# Valid commands
validCalculatorCmds = ["ADD","SUB","MUL","DIV","MOD","EXP","FLO"]
# Valid numbers
validCalculatorNum = ["_5_10","_78_5","_8_13","_24_78"]
# Invalid commands
invalidCalculatorCmds = ["Add","sUb","a_B_","DeV","__45","1__","iuQ"]
# Invalid numbers
invalidCalculatorNum = ["_5s10_","_a_4","2s_2","__478","ADD_7_8"]

# Method to create datetime url for GET information from API
def buildDatetimeCmds(main = "", func = "", cmds = []):
    # Method to create a string with the main address of API
    url = buildUrl(main,func)
    resList = []
    #print(f"URL: {url}")
    # Completes the url and make a request to get the information, the results are appended to a list
    for cmd in cmds:
        tempUrl = url + cmd
        #print(f"URL: {tempUrl}")
        response = requests.get(tempUrl)
        resList.append(response.text)
    return resList

# Method to create calculator url for GET information from API
def buildCalculatorCmds(main = "", func = "", cmds = [], numCmds = {}):
    # Method to create a string with the main address of API
    url = buildUrl(main,func)
    resList = []
    #print(f"URL: {url}")
    # Completes the url and make a request to get the information, the results are appended to a list
    for cmd in cmds:
        tempUrl = url + cmd
        #print(f"URL: {tempUrl}")
        for numCmd in numCmds:
            tempUrl2 = tempUrl + numCmd
            #print(f"URL: {tempUrl2}")
            response = requests.get(tempUrl2)
            #print(response.text)
            resList.append(response.text)
    return resList

def buildUrl(main,func):
    return "" + main + slash + func + slash

# Method to generate the expected results of datetime from the API in order to compare the results
def createDatetimeResults(cmds = []):
    resList = []
    currentTime = date.datetime.now()
    for cmd in cmds:
        if cmd == cmds[0]:
            resList.append(str(currentTime.year))
        if cmd == cmds[1]:
            resList.append(str(currentTime.month))
        if cmd == cmds[2]:
            resList.append(str(currentTime.day))
        if cmd == cmds[3]:
            resList.append(str(currentTime.hour))
        if cmd == cmds[4]:
            resList.append(str(currentTime.minute))
        if cmd == cmds[5]:
            resList.append(str(currentTime.second))
        if cmd == cmds[6]:
            resList.append(str(str(currentTime.year) + " "
                     + str(currentTime.month) + " "
                     + str(currentTime.day) + " "
                     + str(currentTime.hour) + " "
                     + str(currentTime.minute) + " "
                     + str(currentTime.second)))
    return resList

# Method to generate the expected results of calculator from the API in order to compare the results
def createCalculatorResults(cmds = [], nums = []):
    resList = []
    for cmd in cmds:
        for num in nums:
            tempNum = num.replace("_", " ")
            numList = tempNum.split()
            if cmd == cmds[0]:
                resList.append(float(numList[0]) + float(numList[1]))
            if cmd == cmds[1]:
                resList.append(float(numList[0]) - float(numList[1]))
            if cmd == cmds[2]:
                resList.append(float(numList[0]) * float(numList[1]))
            if cmd == cmds[3]:
                resList.append(float(numList[0]) / float(numList[1]))
            if cmd == cmds[4]:
                resList.append(float(numList[0]) % float(numList[1]))
            if cmd == cmds[5]:
                resList.append(float(numList[0]) ** float(numList[1]))
            if cmd == cmds[6]:
                resList.append(float(numList[0]) // float(numList[1]))
    return resList

#DEBUG
#print(buildDatetimeCmds(mainAddress,funtionalities[0],validDatetimeCmds))
#print(createDatetimeResults(validDatetimeCmds))

### TEST CASES DATETIME ###
# Testing datetime functionality with valid commands
def test_DatetimeValidCmds():
    listGet = buildDatetimeCmds(mainAddress,funtionalities[0],validDatetimeCmds)
    listExp = createDatetimeResults(validDatetimeCmds)
    for i in range(len(listExp)):
        assert listGet[i] == listExp[i]

# Testing datetime functionality with invalid commands
def test_DatetimeInvalidCmds():
    listGet = buildDatetimeCmds(mainAddress,funtionalities[0],invalidDatetimeCmds)
    for i in range(len(listGet)):
        assert listGet[i] == errorMsg

### TEST CASES CALCULATOR ###
# Testing Calculator functionality with valid calculator commands and numbers
def test_CalculatorValidCmdsNums():
    listGet = buildCalculatorCmds(mainAddress,funtionalities[1],validCalculatorCmds,validCalculatorNum)
    listExp = createCalculatorResults(validCalculatorCmds, validCalculatorNum)
    for i in range(len(listExp)):
        assert float(listGet[i]) == listExp[i]

# Testing Calculator functionality with valid calculator commands and invalid numbers
def test_CalculatorValidCmdsInvalidNums():
    listGet = buildCalculatorCmds(mainAddress,funtionalities[1],validCalculatorCmds,invalidCalculatorNum)
    for i in range(len(listGet)):
        assert listGet[i] == errorMsg

# Testing Calculator functionality with invalid calculator commands and valid numbers
def test_CalculatorInvalidCmdsValidNums():
    listGet = buildCalculatorCmds(mainAddress,funtionalities[1],invalidCalculatorCmds,validCalculatorNum)
    for i in range(len(listGet)):
        assert listGet[i] == errorMsg

# Testing Calculator functionality with invalid calculator commands and invalid numbers
def test_CalculatorInvalidCmdsInvalidNums():
    listGet = buildCalculatorCmds(mainAddress,funtionalities[1],invalidCalculatorCmds,invalidCalculatorNum)
    for i in range(len(listGet)):
        assert listGet[i] == errorMsg