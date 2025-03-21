# Datetime and Calculator
This endpoint API was created to request information regarding datetime and results of basic arithmetic operations.
Using [Flask](https://flask.palletsprojects.com/en/stable/) as lightweight WSGI web application framework to run the application on a local development server you can use HTTP GET methods to request information to the API.
This API includes a file to perform the basic tests using [Pytest](https://docs.pytest.org/en/stable/).

### Datetime information:
Return datetime information of the computer that runs the server in route: ``` http://127.0.0.1:5000/datetime/```, you can request the next information:
1. help > ```help```
2. Year > ```year```
3. Month > ```month```
4. Day > ```day```
5. Hour > ```hour```
6. Minute > ```minute```
7. Second > ```second```
8. Complete > ```complete```

e.g. 
``` bash
http://127.0.0.1:5000/datetime/year
```
Return:
2025

e.g. 
``` bash
http://127.0.0.1:5000/datetime/complete
```
Return:
2025 3 20 22 10 6


### Calculator information:
Return the result of a basic arithmetic operation of two numbers, implemented in route: ``` http://127.0.0.1:5000/calculator/```, you can request the result of the next operations:
1. help > ```help```
2. ADD > ```ADD_NUM1_NUM2```
3. SUB > ```SUB_NUM1_NUM2```
4. MUL > ```MUL_NUM1_NUM2```
5. DIV > ```DIV_NUM1_NUM2```
6. MOD > ```MOD_NUM1_NUM2```
7. EXP > ```EXP_NUM1_NUM2```
8. FLO > ```FLO_NUM1_NUM2```

The operation command and the first number should be followed by at least one "_" if the request doesn't have this format an error message should be returned.

e.g.
``` bash
http://127.0.0.1:5000/calculator/SUB_48.4_52.8
```
Return: -4.39

e.g.
``` bash
http://127.0.0.1:5000/calculator/MUL_5_5
```
Return: 25.0

e.g.
``` bash
http://127.0.0.1:5000/calculator/Sub_48.4_52.8
```
Return: "No valid parameter received, type "help" for more information"

e.g.
``` bash
http://127.0.0.1:5000/calculator/DIV_48.4__52.8
```
Return: 0.91

e.g.
``` bash
http://127.0.0.1:5000/calculator/DIV48.4__52.8
```
Return: "No valid parameter received, type "help" for more information"

## Installation
Ubuntu: 
1. Download the files from GitHub [repository](https://github.com/OsvaldoJRG/IBM-API) and save them in a desired folder. (Choose the folder according to your operating system)
2. Open a terminal in the folder and use [apt](https://help.ubuntu.com/kubuntu/desktopguide/es/apt-get.html) to install Flask (sudo password could be requested).
``` bash
sudo apt install python3-flask
```
3. You can use ``` flask --version ``` to check to correct installation.
4. Use [apt](https://help.ubuntu.com/kubuntu/desktopguide/es/apt-get.html) to install Pytest (sudo password could be requested).
``` bash
sudo apt install python3-pytest
```
5. You can use ``` pytest --version ``` to check to correct installation.
6. Use [apt](https://help.ubuntu.com/kubuntu/desktopguide/es/apt-get.html) to install [Curl](https://manpages.ubuntu.com/manpages/focal/man1/curl.1.html) (sudo password could be requested).
``` bash
sudo apt install curl
```
7. You can use ``` curl --version ``` to check to correct installation.

## Running endpoint API
1. First you need to run the API on your local computer executing the file ``` IBMAplication.py  ``` in terminal write:
``` bash
python3 IBMAplication.py
```
2. Server should start in ```localhost:5000/``` or ```http://127.0.0.1:5000/``` a confirmation message should be displayed.
   
![Flask](https://github.com/user-attachments/assets/00a794fb-c667-4bf0-a2ce-8e0eabf0f140)

3. Now you can send a HTTP GET method to check if API is running correctly, you can use your navigator or Curl to interact with the API, to use Curl open another terminal and sent some of the next example request:

#### Home page:
``` bash
curl http://127.0.0.1:5000/
```

#### Return:
"Welcome to API Tools, functionalities implemented: /datetime and /calculator, type command 'help' for more information."


#### Calculator, sum 5 and 15.5:
``` bash
curl http://127.0.0.1:5000/calculator/ADD_5_15.5
```
#### Return:
20.5

#### Datetime information, current year:
``` bash
curl http://127.0.0.1:5000/datetime/year
```
#### Return:
2025

## Running test suite
1. Once the endpoint API is running you can execute the test suite file ``` APITest.py  ``` in terminal type:
``` bash
pytest APITest.py --junitxml=testSuiteReport.xml
```
2. Pytest should start executing the test cases found in ``` APITest.py  ``` at the end, a XML report is generated in the root folder and a message with the results should be displayed:

![Pytest](https://github.com/user-attachments/assets/7075fe33-6850-4ed2-bc48-f5f32ffd3085)

## Running endpoint API and test suite with subprocess
A python script was implemented to run both process using one script that use subprocess to run ``` APITest.py  ``` in terminal type:
``` bash
python3 APITestSub.py
```
First the endpoint API should be executed in one subprocess, after that the test suite should start, once the test suite subprocess finish the endpoint API subprocess will finished too.
You can look for the results in the XML report generated in the root folder.

## Modifying test inputs
The test suite was created to be able to modify easily their input values in order to test the endpoint API, follow the next steps if you want to modified them.

1. You can use [nano](https://www.nano-editor.org/) to modified the test suite ``` APITest.py  ``` in terminal type:
``` bash
nano APITest.py
```
2. The test suite file ``` APITest.py  ``` should open, to modified the inputs locate the lists:

#### Datetime functionality:
``` validDatetimeCmds[]  ```
``` invalidDatetimeCmds[]  ```

#### Calculator functionality:
``` validCalculatorCmds[]  ```
``` validCalculatorNum[]  ```
``` invalidCalculatorCmds[]  ```
``` invalidCalculatorNum[]  ```

![TSInputs](https://github.com/user-attachments/assets/f53cac41-974c-4159-ae29-18186f271d08)

#### If you modify valid parameters the test suite should fail.
e.g. year > yearr:

![TSInputsF](https://github.com/user-attachments/assets/9b8bc794-72ea-490e-9487-cb70177381d7)

#### Test suite result:

![FailTest](https://github.com/user-attachments/assets/4410c6e2-430e-4a05-a27b-7ae2ea93e270)

#### If you add/delete invalid parameters the test suite should passed.

![TSNewP](https://github.com/user-attachments/assets/d505d70c-01ee-46e6-9d0a-1c2b2d41a994)

#### Test suite result:

![TSNewPR](https://github.com/user-attachments/assets/a8e8d641-408f-45ff-bd5c-c0bd0768b2b6)


## Version
#### 0.1.0

## Support
#### Osvaldo Reynoso
#### osvaldo.jrg@gmail.com
