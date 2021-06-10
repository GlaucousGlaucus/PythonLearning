import json

def pause():
    print("Press Enter to Exit")
    input()

def passwordCheckJSON(FileHandler, Username, Password, usernameField, passwordField):
    file = FileHandler.read()
    val = json.loads(file)
    if Username == val[usernameField] and Password == val[passwordField]:
        return True
    else:
        return False
