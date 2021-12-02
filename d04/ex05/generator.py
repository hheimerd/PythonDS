import sys
import os
import psutil

def read_file(filename) -> list:
    with open(filename) as f:
        line = f.readline()
        while True:
            line = f.readline()
            if not line: break
            
            yield line

def main():
    try:
        lines = read_file(sys.argv[1])
        for line in lines:
            pass
        
        process = psutil.Process(os.getpid())
        time = process.cpu_times()
        
        ram = process.memory_info()
        ram = (ram.peak_wset + ram.peak_paged_pool) if hasattr(ram, 'peak_wset') else (ram.data + ram.text)
        ram /= 1024 * 1024 * 1024
        
        
        total_time = (time.user + time.system)
        print(f'Peak Memory Usage = {ram:.2f}GB')
        print(f'User Mode Time + System Mode Time = {total_time:.2f}s')
    except Exception:
        print('file not found')

if __name__ == '__main__':
    main()