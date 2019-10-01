from notification_method import NOTIFICATION_METHOD 

# To be used to convert database query objects into python objects
class Condition_model:
    def __init__(self, json):
        self.idcondition = json[0]
        self.user_id = json[1]
        self.condition_text = json[2]
        self.notification_method = NOTIFICATION_METHOD[json[3]]
        self.symbol = json[4]
        self.last_value = bool(json[5])
        self.is_active = bool(json[6])
