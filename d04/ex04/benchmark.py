from timeit import timeit
from random import randint
from collections import Counter


def my_counter(numbers: list):
    result = {}
    for num in numbers:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    
    return result

def get_top(dictionary: dict, limit: int):
    result_len = min(limit, len(dictionary))
    result = [[float('-inf'), float('-inf')] for i in range(0, result_len)]
    for it in dictionary.items():
        for i in range(0, result_len):
            if it[1] >= result[i][1]:
                result[i], it = it, result[i]


    return dict(result)

def get_top_from_list(nums: list, limit: int):
    return get_top(my_counter(nums), limit)

def on_error(message='error'):
    print(message)
    exit()


def main():

    target = [randint(0, 100) for i in range(0, 1000000)]

    # assert dict(Counter(target)) == my_counter(target)
    
    my_ctr = timeit(lambda: my_counter(target), number=1)
    ctr = timeit(lambda: dict(Counter(target)), number=1)
    
    print(f'my function: {my_ctr:.7f}')
    print(f'Counter: {ctr:.7f}')

    # assert get_top_from_list(target, 13) == dict(Counter(target).most_common(13))
    
    my_ctr = timeit(lambda: get_top_from_list(target, 13), number=1)
    ctr = timeit(lambda: dict(Counter(target).most_common(13)), number=1)

    print(f'my top: {my_ctr:.7f}')
    print(f'Counter\'s top: {ctr:.7f}')

if __name__ == '__main__':
    main()
