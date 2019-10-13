from expression_type import EXPRESSION_TYPE


class Expression:
    def __init__(self, text: str):
        self.text = text
        self.value_1, self.expression_type, self.value_2 = self.process()

    # e.g. for price > 50, return three values: 'price', 'GT', '50'
    # Assume an expression is only three words?
    def process(self):
        words = self.text.split(' ')
        value_1 = words[0]
        expression_type = words[1]
        value_2 = words[2]
        if expression_type == '>':
            expression_type = EXPRESSION_TYPE.GT
        elif expression_type == '<':
            expression_type = EXPRESSION_TYPE.LT
        elif expression_type == '<=':
            expression_type = EXPRESSION_TYPE.LEQ
        elif expression_type == '>=':
            expression_type = EXPRESSION_TYPE.GEQ
        elif expression_type == '==':
            expression_type = EXPRESSION_TYPE.EQ
        else: 
            raise Exception("Expression type {} not recognised".format(expression_type))
        return value_1, expression_type, value_2

    def evaluate(self, data):
        converted_value_1 = self._get_value_or_convert_float(self.value_1, data)
        converted_value_2 = self._get_value_or_convert_float(self.value_2, data)

        if self.expression_type == EXPRESSION_TYPE.GT:
            return converted_value_1 > converted_value_2
        elif self.expression_type == EXPRESSION_TYPE.LT:
            return converted_value_1 < converted_value_2
        elif self.expression_type == EXPRESSION_TYPE.LEQ:
            return converted_value_1 <= converted_value_2
        elif self.expression_type == EXPRESSION_TYPE.GEQ:
            return converted_value_1 >= converted_value_2
        elif self.expression_type == EXPRESSION_TYPE.EQ:
            return converted_value_1 == converted_value_2
        else:
            raise Exception("Expression type {} not supported".format(expression_type))

    def _get_value_or_convert_float(self, value, data)
        if self._is_float(value):
            return float(value)
        else:
            return data[value]

    def _is_float(self, val):
        try:
            float(val)
            return True
        except ValueError:
            return False


           
