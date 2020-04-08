from guess import figure
def run():
    computer = figure()
    player=input('show your figure(p,c,s): ')
    if(player=='p' or player=='c' or player=='s'):
        print('computer\'s figure: ',computer)
        if(player==computer):
            print('not lose but not win')
        else:
            if(player=='c'):
                if(computer=='p'):
                    print('YOU WIN!!')
                else:
                    print('YOU LOSE!!')
            if(player=='p'):
                if(computer=='s'):
                    print('YOU WIN!!')
                else:
                    print('YOU LOSE!!')
            if(player=='s'):
                if(computer=='c'):
                    print('YOU WIN!!')
                else:
                    print('YOU LOSE!!')
    else:
        print('幹！！是不會玩猜拳膩')
for i in range(10):
    run()
    print('~~~~~~~')
    if i==9:
        print('該停囉')


              
                
