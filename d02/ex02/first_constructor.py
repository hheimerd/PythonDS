import sys

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        
        with open(self.path) as file:
            text = file.read()
            
        def on_syntax_error():
            raise ValueError()
    
        lines = [i.split(',') for i in text.split('\n')]
        if len(lines) < 2 or len(lines[0]) != 2 or lines[0][0] == '' or lines[0][1] == '':
            on_syntax_error()
        lines = lines[1:]

        for line in lines:
            if len(line) != 2 or line[0] not in ['0','1'] or line[1] not in ['0','1'] or line[0] == line[1]:
                on_syntax_error()

        return text

def on_error(message):
    print(message, file=sys.stderr)
    exit()

def main():
    if len(sys.argv) != 2:
        on_error("Invalid arguments")
    
    try:
        lines = Research(sys.argv[1]).file_reader()
    except IOError:
        on_error('File not found')
    except Exception as e:
        on_error("ValueError")

    print(lines)


if __name__ == "__main__":
    main()

