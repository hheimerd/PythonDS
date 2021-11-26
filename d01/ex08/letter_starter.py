import sys

INPUT = 'employees.tsv'

def main():
    if len(sys.argv) != 2:    return

    search_email = sys.argv[1].rstrip(' \r\n\t')

    with open(INPUT) as file:
        rows = list(file)[1:]
    
    splitted_rows = list(map(lambda row: row.split('\t'), rows))

    

    for row in splitted_rows:
        if row[2].strip('"\n') == search_email:
            name = row[0].strip('"')
            print (f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
            return



if __name__ == '__main__':
    main()
