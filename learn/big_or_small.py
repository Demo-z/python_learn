import random
#  取随机数
# point1 = random.randrange(1,7)
# point2 = random.randrange(1,7)
# point3 = random.randrange(1,7)

# print(point1,point2,point3)
# 存储筛子
def roll_dice(numbers=3,points=None):
    print("<<<<<  ROLL  THE  DICE!  >>>>>")
    if points==None:
        points=[]
    while numbers > 0:
        point=random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points
#　点数化大小
def roll_result(total):
    isBig=11<=total<=18
    isSmall=3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

# 开始创建游戏
def start_game(money=0):
    print("<<<<<  GAME START  >>>>>")
    choices = ['Big','Small']
    your_choices = input('Big or Small:')
    your_money=input('How much you wanna bet ?-')
    if your_money=='':
        your_money=0
    your_money=int(your_money)
    if your_money>0:
        if your_choices in choices:
            points=roll_dice()
            total=sum(points)
            youWin=your_choices==roll_result(total)
            if youWin:
                money=money+your_money
                print('The points are',points,'You win!')
                print('You gained',your_money,'you have',money,'now')
                start_game(money)
            else:
                money=money-your_money
                print('The points are',points,'You lose!')
                print('You lost',your_money,'you have',money,'now')
                if money<0:
                    print("GAME OVER") 
                else:
                    start_game(money)
        else:
            print('Invalid Words')
            start_game()
    else:
        print('No money')
        start_game()
start_game()