from expression import Expression

class Condition:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_condition(file_path)
        self.separators = self.find_all_separators()
        self.expressions_text = self.extract_expressions_text(self.separators, self.data)
        self.expressions = self.extract_expressions(self.expressions_text)

    def load_condition(self, file_path: str) -> str:
        f = open(file_path, 'r')
        data = f.read()[:-1]
        f.close()
        return data

    # Given text of expressions, turns into expressions class objects, leaving empty placeholders as is
    def extract_expressions(self, expressions_text):
        expressions = []
        for text in expressions_text:
            if not text:
                expressions.append('')
            else:
                expressions.append(Expression(text))
        return expressions

    # Extract the three word expressions between each separator and parse into expression object
    # This will include empty '' strings as placeholders between separators such as '... OR ( ...'
    def extract_expressions_text(self, separators, text: str):
        first_pos = separators[0][0]
        expressions = [ self.data[0: first_pos-1]]
        for i, pair in enumerate(separators):
            if i == len(separators)-1:
                break
            
            current_pos = pair[0]
            current_separator = pair[1]
            next_pos = separators[i+1][0]
            text = self.data[current_pos + len(current_separator) : next_pos-1].strip()
            expressions.append(text)
        return expressions
        
            
    # Returns sorted list of tuples of the form ( position of separator, separator )
    def find_all_separators(self):
        separators = ['AND', 'OR', '(', ')']
        positions = []
        for separator in separators:
            pairs = [ (x, separator) for x in self.find_occurances(separator, self.data)]
            positions.extend(pairs)
        return sorted(positions, key = lambda x: x[0])

    def find_occurances(self, word: str, text):
        occurances = []
        continue_search = True
        removed = 0
        while continue_search:
            pos = text.find(word)
            if pos == -1:
                continue_search = False
            else:
                text = text[pos+len(word):]
                occurances.append(pos+removed)
                removed += pos+len(word)
        return occurances

        

    
