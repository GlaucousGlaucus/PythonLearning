from Content.Consumers import Consumers
from Content.ModCustomExceptions import InvalidCommand
from Content.Admin import *
from Content.Util import *
from Content.IteratorCustomForList import *
import math
import json
import os


class Main:
    consumer = Consumers()
    """
    consumer.addConsumer(str(input("Consumer Name: ")))
    consumer.getConsumer(int(input("ID: ")))
    consumer.removeConsumer(int(input("ID: ")))
    """
    consumer.addConsumer("mark")  # 0
    consumer.addConsumer("John")  # 1
    consumer.addConsumer("Matt")  # 2
    consumer.addConsumer("Bob")  # 3

    command = str(input("COMMAND: "))

    filePathOfJson = 'C:\\Users\\User\\PycharmProjects\\firstOne\\GeneratedData\\'
    filePathOfAdminJson = 'C:\\Users\\User\\PycharmProjects\\firstOne\\GeneratedData\\Admin\\'

    if command == "A":
        try:
            print(consumer.getConsumer(int(input("ID: "))))
        except Exception as e:
            print("ERROR: ", type(e))

        try:
            consumer.removeConsumer(int(input("ID: ")))
        except Exception as e:
            print("ERROR: ", e)

        try:
            print(consumer.getConsumer(int(input("ID: "))))
        except Exception as e:
            print("ERROR: ", e)

        pause()

    elif command == "ADMIN":
        UName = input("Username: ")
        Password = input("PASSWORD: ")
        admin = Admin()
        if admin.LoginSetup(UName, Password):
            print("Success")
            admin.AdminSpecialFunctions(UName)
        else:
            print("ACCESS DENIED")

    elif command == "File_Read":
        with open('test.txt', 'r') as fileHandler:
            lineToRead = int(input("Line To Read: "))
            try:
                print(fileHandler.readlines()[lineToRead])
            except Exception as e:
                print("Line Out Of Bounds")

    elif command == "File_AddData":
        with open('test.txt', 'a') as fileHandler:
            name = str(input("Name: "))
            age = int(input("Age: "))
            id = int(input("ID: "))
            D = {'id': id, 'name': name, 'age': age}
            fileHandler.write("\n" + str(D).replace("{", "").replace("}", ""))
        # fileHandler.close()
        # use to close the file and free up system resources,
        # no need if using with

    elif command == "exit":
        exit()
    elif command == "json_w":
        name = str(input("Name: "))
        age = int(input("Age: "))
        bio = str(input("Bio: "))
        A = {
            'name': name,
            'age': age,
            'bio': bio
        }
        with open(filePathOfJson + name.strip() + '.json', 'w') as fh:
            fh.write(json.dumps(A, indent=4))
        print("File Name: " + name)
        pause()

    elif command == "json_r":
        fileName = str(input("File Name: "))
        with open(filePathOfJson + fileName + '.json', 'r') as fh:
            json_string = fh.read()
            json_val = json.loads(json_string)
            parameter = str(input("Parameter: "))
            print("Your Requested Parameter: \n" + "--->  " + json_val[parameter] + "\n")
        pause()

    elif command == "itr":
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        A_List = IteratorCustomForList(A)
        amount = int(input("Amount: "))
        x = 0
        while x < amount:
            x += 1
            print(next(A_List))

    elif command == "NewAdmin":
        userName = str(input("Username: "))
        Password = str(input("Password: "))
        bio = str(input("Bio: "))
        tag = "GENERATED" if bio == "" else "PROVIDED"
        if userName == "" or Password == "" or len(userName) < 3 or len(Password) < 3:
            print("Username and Password should be greater than 3 characters, Restart Program")
        else:
            A = {
                'name': userName,
                'password': Password,
                'bio': bio,
                'tags': tag
            }
            with open(filePathOfAdminJson + userName.strip() + '.json', 'w') as fh:
                fh.write(json.dumps(A, indent=4))
            print("File Name: " + userName)
            if bio == "":
                print("BioData found blank, tagging with " + tag)
        pause()

    elif command == "AdminProfile":
        username1 = str(input("Username (To Edit): "))
        password1 = str(input("Password: "))
        try:
            with open(filePathOfAdminJson + username1.strip() + '.json', 'r+') as fh:
                file = fh.read()
                val = json.loads(file)
                if username1 == val['name'] and password1 == val['password']:
                    print("Logged in as: " + val['name'])
                    print("Values Available", str(val))
                    FC = str(input("What field to change (Case Sensitive): "))
                    try:
                        print( "------------- \nCurrent: \n" + val[FC] + "\n")
                        newValueEdited = str(input("New Value for field " + val[FC] + " : \n"))
                        # This is how to modify a json file
                        val[FC] = newValueEdited
                        fh.seek(0)
                        fh.write(json.dumps(val, indent=4))
                        fh.truncate()
                    except Exception as e:
                        print(e)
                        pause()
                else:
                    print("Invalid Data Provided")
        except Exception as e:
            print("Access Denied")
            pause()
    elif command == "AdminDel":
        print("ATTENTION: RISKY MOVE")
        delname = str(input("Username to delete: "))
        delpass = str(input("Password: "))
        try:
            with open(filePathOfAdminJson + delname.strip() + '.json', 'r+') as fh:
                if passwordCheckJSON(fh, delname, delpass, 'name', 'password'):
                    print("Delete User: " + delname + " ? Type username to continue")
                    confirmationInput = str(input("Confirm: "))
                    if confirmationInput == delname:
                        try:
                            fh.close()
                            os.remove(fh.name)
                            print("File Deleted")
                        except Exception as e:
                            print(e)
                            print("File not deleted")
                    else:
                        print("File Deletion Cancelled")
                else:
                    print("Access Denied")
        except Exception as e:
            print(e)
        pause()
    else:
        raise InvalidCommand(command)
