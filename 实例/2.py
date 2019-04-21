#实例2
#http://www.runoob.com/python/python-exercise-example2.html
def  get_reward(I):
    rewards = 0
    if I <= 10:
        rewards = I * 0.1
    elif (I > 10) and (I <= 20):
        rewards = (I - 10) * 0.075 + get_reward(10)
    elif (I > 20) and (I <= 40):
        rewards = (I - 20) * 0.05 + get_reward(20)
    elif (I > 40) and (I <= 60):
        rewards = (I - 40) * 0.03 + get_reward(40)
    elif (I > 60) and (I <= 100):
        rewards = (I - 60) * 0.015 + get_reward(60)
    else:
        rewards = get_reward(100) + (I - 100) * 0.01
    return rewards
print("净利润:")
i = int(input())
if __name__ == '__main__':
    print("发放的奖金为：", get_reward(i / 10000) * 10000)