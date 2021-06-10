import json


class Admin:
    # use list id to match uname and passowrd

    usernames = ["ADMIN", "AEGIS"]
    passwords = ["123", "321"]
    AEGISTargets = ["GLaDOS", "Mel", "Virgil"]
    AEGISTargetTypes = ["Mechanical", "ORGANIC", "Mechanical"]
    secutiryStatus = ""
    filePathOfAdminJson = 'C:\\Users\\User\\PycharmProjects\\firstOne\\GeneratedData\\Admin\\'

    def LoginSetup(self, username, password):
        """
        if username in self.usernames and password in self.passwords:
            if self.usernames.index(username) == self.passwords.index(password):
                return True
            else:
                return False
        else:
            return False
            """

        try:
            with open(self.filePathOfAdminJson + username.strip() + '.json', 'r') as fh:
                file = fh.read()
                val = json.loads(file)
                print("Username Found! ->" + val['name'])
                if username == val['name'] and password == val['password']:
                    return True
                else:
                    return False
        except Exception as e:
            print("\n ------------------ \n" + str(e) + "\n ------------------ \n")
            return False

    def AEGISSecurityStatus(self):
        i = input()
        if i == "DEmRN":
            return "AT RISK"
        else:
            return "GOOD :)"

    def AdminSpecialFunctions(self, admin):
        if admin == "AEGIS" or admin == "Nexorel":
            command = str(input("COMMAND: "))
            if command == "PING_LIST_TARGETS":
                for A in self.AEGISTargets:
                    print("" + "\n" +
                          """ TARGET:  """ + str(self.AEGISTargets.index(A)) + "\n" +
                          """ NAME: --> """ + A + "\n" +
                          " TARGET TYPE: " + self.AEGISTargetTypes[self.AEGISTargets.index(A)])
                print("" "\n" + "COMMAND EXECUTED FROM: " r"AEGIS:SECURITY/Emergency$SEROUS?bool-->True/Ping_List_Targets")
                print(" " + "\n" + "Press Enter to Exit")
                input()
                self.AdminSpecialFunctions(admin)

            elif command == "INSPECTION":
                print("Inspection Started")
                counter = 0
                while counter < 5:
                    counter += 1
                    print("Loading:..." + str(int(counter/5 * 100)) + "%")

                print("ENTER ASCII INPUT:")
                print("INSPECTION RESULTS: \n AEGIS CORE: ONLINE \n SECURITY STATUS --> " + self.AEGISSecurityStatus())
                print(" " + "\n" + "Press Enter to Exit")
                input()
                self.AdminSpecialFunctions(admin)

            elif command == "exit":
                print(" " + "\n" + "Press Enter to Exit")
                input()

            else:
                print("Welcome " + admin)
                print("Press Enter to Exit")
                input()
                self.AdminSpecialFunctions(admin)
        else:
            print("Welcome " + admin)
            print("Press Enter to Exit")
            input()
