# To be used to convert database query results into python object
class User_model:
    def __init__(self, json):
        self.iduser = json[0]
        self.username = json[1]
        self.sms_number = json[2]
        self.email = json[3]

    def __eq__(self, other: User_model) -> bool:
        return self.iduer == other.iduser and self.username == other.username and self.sms_number == other.sms_number and self.email == other.email
