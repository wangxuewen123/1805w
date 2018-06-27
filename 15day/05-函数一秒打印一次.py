import time
def da():
    a = 0
    while True:
        a = a+1
        time.sleep(1)
        if a%2 == 0:
            print("我喜欢玩游戏")
        else:
            ji()
def ji():
    print("我喜欢打代码")
da()
