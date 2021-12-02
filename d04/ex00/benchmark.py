from timeit import timeit

def get_gamils_list_comprehension(mails: list):
    return [mail for mail in mails if mail.endswith('@gmail.com')]

def get_gamils_loop(mails: list):
    result = []
    for mail in mails:
        if mail.endswith('@gmail.com'):
            result.append(mail)
    
    return result

def main():
    test_unique = ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    
    target = [mail for mail in test_unique for i in range(0,5)]
    
    # assert get_gamils_list_comprehension(target) == get_gamils_loop(target)
    
    list_comprehension = timeit(lambda: get_gamils_list_comprehension(target))
    loop = timeit(lambda: get_gamils_loop(target))
    
    result = f'it is better to use a {"list comprehension" if list_comprehension < loop else "loop"}'
    
    print(result)
    print(min(list_comprehension, loop), 'vs', max(list_comprehension, loop))
    



if __name__ == '__main__':
    main()
