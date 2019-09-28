from expression import Expression
import re


class Condition:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_condition(file_path)
        self.separators = self.find_all_separators()
        self.expressions = self.extract_expressions(self.separators, self.data)

    def load_condition(self, file_path: str) -> str:
        f = open(file_path, 'r')
        data = f.read()[:-1]
        f.close()
        return data

    def evaluate(self, data):
        evaluated_expressions = [ str(expr.evaluate(data)) for expr in self.expressions ]
        separator_tokens = [ match.group() for match in self.separators ]
        print(evaluated_expressions)
        combined_list = [None]*(len(evaluated_expressions) + len(separator_tokens))
        if self.separators[0].start() == 0:
            combined_list[::2] = separator_tokens
            combined_list[1::2] = evaluated_expressions
        else:
            combined_list[::2] = evaluated_expressions
            combined_list[1::2] = separator_tokens
        combined_string = ''.join(combined_list)

        # todo: ensure combined_string safe to perform eval on or use some kind of library here to eval
        return eval(combined_string)

    # Extract the three word expressions between each separator and parse into expression object
    def extract_expressions(self, separators, text: str):
        expressions = []
        current_pos = 0
        for match in self.separators:
            expression = self.data[current_pos : match.start()].strip()
            current_pos = match.end()

            # Filter out emptry strings, such as if the text starts with a separator
            if expression:
                expressions.append(Expression(expression))
            
        return expressions
        
            
    # Returns list of match objects
    def find_all_separators(self):
        # Regex to find all occurances of 'and', 'or', '(', ')', grouping if adjacent such as 'and (', with spaces before and after 
        regex = r"\s?(\(|\))?\s?(and|or|\(|\))\s?(\(|\))?\s?"
        matches = re.finditer(regex, self.data, re.MULTILINE)
        return list(matches)

    # return list of positions of first letter of word occurances found in text passed in
    def _find_occurances(self, word: str, text):
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

        

    
