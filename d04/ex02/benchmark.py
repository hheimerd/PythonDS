from timeit import timeit
import sys


def get_gamils_list_comprehension(mails: list):
    return [mail for mail in mails if mail.endswith('@gmail.com')]


def get_gamils_loop(mails: list):
    result = []
    for mail in mails:
        if mail.endswith('@gmail.com'):
            result.append(mail)

    return result


def get_mails_map(mails: list):
    result = []
    list(map(lambda mail: result.append(mail)
         if mail.endswith('@gmail.com') else '', mails))
    return result


def on_error(message = 'error'):
    print(message)
    exit()

def main():
    test_unique = ['john@gmail.com', 'james@gmail.com',
                   'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']

    target = [mail for mail in test_unique for i in range(0, 5)]

    commands = {
        'list_comprehension': get_gamils_list_comprehension,
        'loop': get_gamils_loop,
        'map': get_gamils_loop
    }
    
    
    try:
        command = commands[sys.argv[1]]
        repeats = int(sys.argv[2])
    except Exception:
        on_error('invalid arguments')
        

    print(timeit(lambda: command(target), number=repeats))


if __name__ == '__main__':
    main()
