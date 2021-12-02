from timeit import timeit

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
    list(map(lambda mail: result.append(mail) if mail.endswith('@gmail.com') else '', mails))
    return result

def main():
    test_unique = ['john@gmail.com', 'james@gmail.com',
'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    
    target = [mail for mail in test_unique for i in range(0,5)]
    
    assert get_gamils_list_comprehension(target) == get_gamils_loop(target) == get_mails_map(target)
    
    results = {}
    
    results['list_comprehension'] = timeit(lambda: get_gamils_list_comprehension(target))
    results['loop'] = timeit(lambda: get_gamils_loop(target))
    results['map'] = timeit(lambda: get_gamils_loop(target))
    
    sorted_results = sorted(results.items(), key=lambda item: item[1])
    
    result = f'it is better to use a {sorted_results[0][0]}'
    
    print(result)
    print(' vs '.join([str(x[1]) for x in sorted_results]))
    



if __name__ == '__main__':
    main()
