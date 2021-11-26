import sys

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
      
        def counts(data):
            count = [0, 0] # heads - count[0], tails - count[1]
            
            for line in data:
                count[line.index(1)] += 1
            return count

        def fractions(count):
            total = sum(count) 
            return [(i / total) * 100 for i in count]
        
        pass


def on_error(message):
    print(message, file=sys.stderr)
    exit()

def main():
    if len(sys.argv) != 2:
        on_error("Invalid arguments")

    researcher = Research(sys.argv[1])

    try:
        lines = researcher.file_reader()
    except IOError:
        on_error('File not found')
    except Exception as e:
        on_error("ValueError")
    
    print(lines)

    count = Research.Calculations.counts(lines)
    print(count)
    print(Research.Calculations.fractions(count))

if __name__ == "__main__":
    main()

