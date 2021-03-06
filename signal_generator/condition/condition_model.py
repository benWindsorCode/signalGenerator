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
        self.condition_name = json[7]

    def __eq__(self, other):
        return self.idcondition == other.idcondition and self.user_id == other.user_id and self.condition_text == other.condition_text and self.notification_method = other.notification_method and self.symbol == other.symbol and self.last_value == other.last_value and self.is_active == other.is_active and self.condition_name == other.condition_name
