from notification_method import NOTIFICATION_METHOD 


class Conditionmodel:
    def __init__(self, json):
        self.idcondition = json[0]
        self.user_id = json[1]
        self.condition_text = json[2]
        self.notification_method = NOTIFICATION_METHOD[json[3]]
        self.symbol = json[4]
        self.last_value = bool(json[5])
