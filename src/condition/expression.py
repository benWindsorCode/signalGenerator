from expression_type import Expression_type

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
        comparison_value = words[2]
        if expression_type == '>':
            


