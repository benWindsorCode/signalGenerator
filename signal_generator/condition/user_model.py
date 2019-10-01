# To be used to convert database query results into python object
class User_model:
    def __init__(self, json):
        self.iduser = json[0]
        self.username = json[1]
        self.sms_number = json[2]
        self.email = json[3]
