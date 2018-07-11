# -*- coding:utf-8 -*-

import random

class Count21:
    def __init__(self, seq, total, optimum=True):
        if(seq < 1): seq = 1
        if(total < 1): total = 1
        self.seq = seq # 一度に言える数の最大値(最小値は1)
        self.total = total # totalを言った方の負け
        self.opt = optimum # CPUが最善手を打つかどうか
        self.strategies = range((total - 1) % (seq + 1), total, seq+1) # 勝つために言うべき数

    def optimum(self, opt=True):
        self.opt = opt

    def play(self):
        print("先手か後手かを選んでください．")
        turn = input("先手:0, 後手:1 => ")
        if(turn < 0 or turn > 1): turn = 0
        last = 0
        while(last < self.total):
            says_min = last + 1
            says_max = last + self.seq
            if(says_max > self.total): says_max = self.total

            if(turn):
                if self.opt and self._optimazation(last):
                    says = self._optimazation(last)[0]
                else:
                    says = random.randint(says_min, says_max)
                print "CPU:",
            else:
                says = input(str(says_min) + "~" + str(says_max) + "の数を入力してください: ")
                if(says < says_min): says = says_min
                if(says > says_max): says = says_max
                print "You:",

            print ", ".join(map(str, range(says_min, says+1)))
            last = says
            turn = not turn
        if(turn):
            print("You LOSE")
        else:
            print("You WIN")

    def _optimazation(self, last):
        return filter(lambda x: last < x and x < last + self.seq + 1, self.strategies)

def main():
    # 連続した数字を数字を交互に入力(3つまで)，21を言った方の負け
    count21 = Count21(3, 21)
    # count21.optimum(False) # CPUランダム手
    count21.play()

if __name__ == "__main__":main()
