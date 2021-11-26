import sys

OUTPUT = "employees.tsv"

# test cases
# ptr.ref@cpp.com
# ctrl.alt@del.com
# ser.gey@natural.com
# foo.bar@baz.com


def main():
    if len(sys.argv) != 2: return

    with open(sys.argv[1]) as file:
        rows = list(file)

    res_rows = map(email_to_tsv, rows)

    with open(OUTPUT, "w") as file:
        file.write('"Name"\t"Surname"\t"Email"\n')
        file.writelines(res_rows)


def email_to_tsv(email):
    email = email.lower().strip('\r\n \t')
    tmp = email.split('.')
    name = tmp[0].lower().capitalize()
    surname = tmp[1].split('@')[0]

    return f'"{name.capitalize()}"\t"{surname.capitalize()}"\t"{email}"\n'


if __name__ == '__main__':
    main()
