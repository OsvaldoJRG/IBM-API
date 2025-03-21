import subprocess
import requests
import os
import signal
import time

endpointAPIFile = "IBMAplication"
APITestFile = "APITest"
interpreter = "py -3"

def runSubPythonFile(interpreter = "", file = ""):
    sub = subprocess.Popen(interpreter + " " + file + ".py", stdout=True, text=True)
    return sub

def runSubPytestFile(file = ""):
    sub = subprocess.Popen("pytest " + file + ".py" + " --html=testSuiteReport.html", stdout=True, text=True)
    return sub

serverSub = runSubPythonFile(interpreter,endpointAPIFile)
time.sleep(1)
pytestSub = runSubPytestFile(APITestFile)
pytestSub.wait()

if pytestSub.returncode == 0:
    print("Pytest subprocess finished...")
    print("Turning off Flask server...")
    serverPID = requests.get("http://127.0.0.1:5000/getpid/")
    os.kill(int(serverPID.text), signal.SIGINT)