import random
import socket
import threading


################################################################################

# 0 链接成功
# 1，2，3，4 客户端ID
# 5 发牌
# 6 一局结束
# 7 游戏结束

################################################################################

deck = []
def gen_deck():
    global deck
    for i in range(52):
        while True:
            n = random.randint(0, 51)
            if n not in deck:
                deck.append(n)
                break

################################################################################

# host = input('please input host:')
# port = input('please input port:')
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# soc.bind((host, port))
# soc.listen(4)
s = []
player_num = 0
player_name = []

def to_string(lis):
    if len(lis) == 0:
        return ''
    s = str(lis[0])
    for i in range(1, len(lis)):
        s += (' ' + str(lis[i]))
    return s

def player_join():
    global player_num
    for i in range(4):
        conn, addr = soc.accept()
        s.append([i, (conn, addr)])
        player_num += 1

# pj = threading.Thread(target = player_join)

def Main():
    global player_num
    global player_name
    global deck

#     # player_join()

    playing = True
    while playing:
        gen_deck()
        c1 = '5 ' + to_string(deck[0 : 13])
        c2 = '5 ' + to_string(deck[13 : 26])
        c3 = '5 ' + to_string(deck[26 : 39])
        c4 = '5 ' + to_string(deck[39 : 52])
        # 将牌发给各个客户端
        while True:
        # 获取来自某一个客户端的消息
        # 判断是否是协议‘6’，是则转发这条消息，睡眠两秒，跳出循环
        # 判断是否是协议‘7’，是则转发这条消息，playing = True，跳出循环
            playing = False
            break


if __name__ == '__main__':
    Main()