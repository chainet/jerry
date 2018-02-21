class game_object:
    def __init__(self, name):
        self.name = name
    
    def pick_up(self):
        pass
        #在这里添加代码，
        #将对象添加到玩家的对象中。

class coin(game_object):
    def __init__(self, value):
        game_object.__init__(self, 'coin')
        self.value = value

    def spend(self, buyer, seller):
        pass
        #在这了添加代码，
        #从买方的钱中取出硬币，
        #然后把它添加到卖方的钱中。