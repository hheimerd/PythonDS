from timeit import timeit
import sys
from functools import reduce


def powers_sum_loop(repeat: int):
    result = 0
    for i in range(1, repeat + 1):
        result += i * i
    return result


def powers_sum_reduce(repeat: int):
    return reduce(lambda prev, x: prev + x * x, range(1, repeat + 1))


def on_error(message='error'):
    print(message)
    exit()


def main():
    commands = {
        'loop': powers_sum_loop,
        'reduce': powers_sum_reduce
    }


    try:
        command = commands[sys.argv[1]]
        repeats = int(sys.argv[2])
        command_arg = int(sys.argv[3])
    except Exception:
        on_error('invalid arguments')
    
    assert powers_sum_loop(command_arg) == powers_sum_reduce(command_arg)

    print(timeit(lambda: command(command_arg), number=repeats))


if __name__ == '__main__':
    main()
