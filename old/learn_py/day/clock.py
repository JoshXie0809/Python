import time, os
from day7 import Clock

os.system('clear')



def main():
    [hr,minute,sec] = [0, 0, 0]
    
    for i in [hr,minute,sec]:

        i = int(input("%d" % (i)))
        
    clock = Clock(hr,minute,sec)
    while True:
        
        print(clock.show())
        time.sleep(1)
        clock.run()
        os.system('clear')


if __name__ == '__main__':
    main()