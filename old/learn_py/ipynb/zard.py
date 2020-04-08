import time
import os

def main():
    content = 'ZARD!!! ZARD!!! ZARD!!! I love U!!!'
    while True:

        
        #clear_output() # os.system('clear')
        os.system('clear')

        print(content)

        
        content = content[1:] + content[0]
        time.sleep(0.3)

if __name__ == '__main__':
    main()