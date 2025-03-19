from flask import *
import datetime as date

# Creation of object <class 'flask.app.Flask'>
endpointAPI = Flask(__name__)
# Definition of common messages
helpCommand = "help"
errorMsg = "No valid parameter received, type 'help' for more information"

# Definition of GET methods
# Main Address
@endpointAPI.route('/',methods = ['GET'])
def endpointAPIHome():
    return "Welcome to API Tools, functionalities implemented: /datetime and /calculator, type command 'help' for more information."

# Datetime functionality
@endpointAPI.route('/datetime/',methods = ["GET"])
def datetimeInfo():
    return "Type 'help' for information"

@endpointAPI.route('/datetime/<string:command>',methods = ["GET"])
def datetime(command):
    # Validation of help command to send information
    if command == helpCommand:
        return "Valid parameters for return datetime information: 'year', 'month', 'day', 'hour', 'minute', 'second' and 'complete'."
    # Process commands different to 'help'
    else:
        # Getting current time from datetime library
        currentTime = date.datetime.now()
        if command == 'year':
            return str(currentTime.year)
            #return jsonify({'year': str(currentTime.year)})
        elif command == 'month':
            return str(currentTime.month)
        elif command == 'day':
            return str(currentTime.day)
        elif command == 'hour':
            return str(currentTime.hour)
        elif command == 'minute':
            return str(currentTime.minute)
        elif command == 'second':
            return str(currentTime.second)
        elif command == 'complete':
            return str(str(currentTime.year) + " "
                     + str(currentTime.month) + " "
                     + str(currentTime.day) + " "
                     + str(currentTime.hour) + " "
                     + str(currentTime.minute) + " "
                     + str(currentTime.second))
        else:
            return errorMsg

# Calculator functionality
@endpointAPI.route('/calculator/',methods = ["GET"])
def calculatorInfo():
    return "Type 'help' for information"

@endpointAPI.route('/calculator/<string:command>',methods = ["GET"])
def calculator(command):
    # Validation of help command to send information
    if command == helpCommand:
        return "Valid commands for operation are: 'ADD','SUB','MUL','DIV','MOD','EXP','FLO', use '_' to separate the two numbers, e.g. SUM_8.78_16.15."
    else:
        # Replace "_" to " " blank spaces in order to process the command
        command = command.replace("_" , " ")
        # Split the command in a list
        cmd = command.split()
        # List should contain 3 elements if not the command should be clasified as invalid
        if len(cmd) == 3:
            # Validate if first position of command is valid and if the numbers as the correct format (second and third position)
            if cmd[0] == "ADD" and valNumFormat(cmd):
                return str(float(cmd[1]) + float(cmd[2]))
            elif cmd[0] == "SUB" and valNumFormat(cmd):
                return str(float(cmd[1]) - float(cmd[2]))
            elif cmd[0] == "MUL" and valNumFormat(cmd):
                return str(float(cmd[1]) * float(cmd[2]))
            elif cmd[0] == "DIV" and valNumFormat(cmd):
                return str(float(cmd[1]) / float(cmd[2]))
            elif cmd[0] == "MOD" and valNumFormat(cmd):
                return str(float(cmd[1]) % float(cmd[2]))
            elif cmd[0] == "EXP" and valNumFormat(cmd):
                return str(float(cmd[1]) ** float(cmd[2]))
            elif cmd[0] == "FLO" and valNumFormat(cmd):
                return str(float(cmd[1]) // float(cmd[2]))
            # If the format is not correct error message is sent
            else:
                return errorMsg
        # Command is clasified as invalid and an error message is sent
        else:
            return errorMsg

# Method to validate number's format
def valNumFormat(cmd):
    # If the format of numbers is not correct an exception is raise and the method returns False
    try:
        cmd[1] = float(cmd[1])
        cmd[2] = float(cmd[2])
        return True
    except ValueError:
        return False

# Run flask
if __name__ == '__main__':
    endpointAPI.run(debug=True)