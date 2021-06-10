class InvalidCommand(Exception):
    def __init__(self, command):
        super().__init__(
            """
            ERROR: 
            ERROR TYPE:""" + command)
