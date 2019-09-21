class Condition:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.load_condiiton(file_path)

    def load_condition(self, file_path: str):
        f = open(file_path, 'r')
        data = f.read()[:-1]

    
