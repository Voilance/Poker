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
host = '110.64.87.213'
port = 2333
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host, int(port)))
soc.listen(4)
conn = []
player_num = 0
player_name = ['', '', '', '']
player_cards_num = [0, 0, 0, 0]

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
        c, a = soc.accept()
        print(c, a)
        conn.append((c, a))
        name = conn[i][0].recv(1024).decode('utf-8')
        player_name[i] = name
        player_num += 1
    
def frist_player():
    return deck.index(0) // 13 + 1

id = 0

def Main():
    global id
    global player_num
    global player_name
    global deck

    player_join()
    print('player join finished')
    all_name = '0'
    for i in player_name:
        all_name += (' ' + i)
    for j in conn:
        j[0].send(all_name.encode('utf-8'))
    print(all_name)

    playing = True
    while playing:
        gen_deck()
        c1 = '5 ' + to_string(deck[0 : 13])
        c2 = '5 ' + to_string(deck[13 : 26])
        c3 = '5 ' + to_string(deck[26 : 39])
        c4 = '5 ' + to_string(deck[39 : 52])
        conn[0][0].send(c1.encode('utf-8'))
        conn[1][0].send(c2.encode('utf-8'))
        conn[2][0].send(c3.encode('utf-8'))
        conn[3][0].send(c4.encode('utf-8'))
        print(c1, c2, c3, c4)
        player_cards_num = [13, 13, 13, 13]
        id = frist_player()
        while True:
            info = conn[id - 1][0].recv(1024).decode('utf-8')
            conn[0][0].send(info.encode('utf-8'))
            conn[1][0].send(info.encode('utf-8'))
            conn[2][0].send(info.encode('utf-8'))
            conn[3][0].send(info.encode('utf-8'))
            info_list = info.split()
            if int(info_list[1]) != -1:
                player_cards_num[id - 1] -= (len(info_list) - 1)
            if player_cards_num[id - 1] == 0:
                break
            else:
                id = (1 if id == 4 else id + 1)


if __name__ == '__main__':
    Main()