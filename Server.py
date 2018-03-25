import random
import socket
import threading

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

host = input('please input host:')
port = input('please input port:')
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host, port))
soc.listen(4)
s = []
player_num = 0
player_name = []

def player_join():
    global player_num
    while player_num < 4:
        conn, addr = soc.accept()
        s.append((conn, addr))
        # 获取名字 player_name.append()
        player_num += 1

pj = threading.Thread(target = player_join)

def Main():
    global player_num
    while player_num < 4:
        pj.start()
    # 发牌
    






if __name__ == '__main__':
    Main()
