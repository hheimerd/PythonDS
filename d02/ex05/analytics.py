from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header = True):
        
        
        with open(self.path) as file:
            text = file.read()

        def on_syntax_error():
            raise ValueError()
    
        lines = text.split('\n')
        
        
        if has_header:
            header = lines[0].split(',')
            if  len(header) != 2 or header[0] == '' or header[1] == '':
                on_syntax_error()
    
        lines = lines[1:] if has_header else lines

        if (len(lines) < 1): on_syntax_error()

        split_line = lambda line: [int(l) for l in line.split(',')]
        
        try:  lines = [split_line(l) for l in lines]
        except Exception: on_syntax_error()

        for line in lines:
            if len(line) != 2 or line[0] not in [0,1] or line[1] not in [0,1] or line[0] == line[1]:
                on_syntax_error()

        return lines


    class Calculations:
        def __init__(self, data):
            self.data = data
        
        def counts(self, data = None):
            count = [0, 0] # heads - count[0], tails - count[1]
            
            if data is None:
                data = self.data
            
            for line in data:
                count[line.index(1)] += 1
            return count

        def fractions(self, count = None):
            if count is None:
                count = self.counts()
            total = sum(count) 
            return [(i / total) * 100 for i in count]
        
        pass

class Analytics(Research.Calculations):
    
    def predict_random(self, count_of_predictions):
        predictions = []
        
        for _ in range(0, count_of_predictions):
            res = randint(0, 1)
            predictions.append([1,0] if res == 1 else [0,1])
        
        return predictions
    
    def save_file(self, data, filename, format):
        with open(f'{filename}.{format}' , 'w') as f:
            print(data, file=f)

    
    def predict_last(self): 
        length = len(self.data) - 1
        if length < 0: 
            return None
        
        return self.data[length] 
    
pass



