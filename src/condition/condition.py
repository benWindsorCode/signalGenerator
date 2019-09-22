class Condition:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_condition(file_path)

    def load_condition(self, file_path: str) -> str:
        f = open(file_path, 'r')
        data = f.read()[:-1]
        return data

    def find_occurances(self, word: str, text):
        occurances = []
        continue_search = True
        removed = 0
        while continue_search:
            print(text)
            pos = text.find(word)
            if pos == -1:
                continue_search = False
            else:
                text = text[pos+len(word):]
                occurances.append(pos+removed)
                removed += pos+len(word)
        return occurances

        

    
