from expression_type import EXPRESSION_TYPE


class Expression:
    def __init__(self, text: str):
        self.text = text
        self.property_name, self.expression_type, self.comparison_value = self.process()

    # e.g. for price > 50, return three values: 'price', 'GT', '50'
    # Assume an expression is only three words?
    def process(self):
        words = self.text.split(' ')
        property_name = words[0]
        expression_type = words[1]
        comparison_value = float(words[2])
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
        return property_name, expression_type, comparison_value

    def evaluate(self, data):
        val = data[self.property_name]
        if self.expression_type == EXPRESSION_TYPE.GT:
            return val > self.comparison_value
        elif self.expression_type == EXPRESSION_TYPE.LT:
            return val < self.comparison_value
        elif self.expression_type == EXPRESSION_TYPE.LEQ:
            return val <= self.comparison_value
        elif self.expression_type == EXPRESSION_TYPE.GEQ:
            return val >= self.comparison_value
        elif self.expression_type == EXPRESSION_TYPE.ET:
            return val == self.comparison_value


           
