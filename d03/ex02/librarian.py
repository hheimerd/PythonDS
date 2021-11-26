from pkg_resources import WorkingSet
import os
import sys
from subprocess import run


def main():
    if os.getenv("VIRTUAL_ENV") == None:
        raise Exception()
    
    run(f'pip install pytest beautifulsoup4'.split(' '))
    
    working_set = WorkingSet()
    with open('./requirements.txt', 'w') as file:
        print(
            *map(lambda p: f"{p.project_name}=={p.version}",
                 working_set),
            
            file=file,
            sep='\n'
        )
        


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print('operation failed', file=sys.stderr)
