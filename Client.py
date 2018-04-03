import os
import tkinter as tk
import socket
import threading

#  设置扑克牌路径
img_path = os.curdir + os.sep + 'image' + os.sep
#  方块Diamond
DA_img = img_path + 'DA.gif'
D2_img = img_path + 'D2.gif'
D3_img = img_path + 'D3.gif'
D4_img = img_path + 'D4.gif'
D5_img = img_path + 'D5.gif'
D6_img = img_path + 'D6.gif'
D7_img = img_path + 'D7.gif'
D8_img = img_path + 'D8.gif'
D9_img = img_path + 'D9.gif'
DX_img = img_path + 'DX.gif'
DJ_img = img_path + 'DJ.gif'
DQ_img = img_path + 'DQ.gif'
DK_img = img_path + 'DK.gif'
#  梅花Club
CA_img = img_path + 'CA.gif'
C2_img = img_path + 'C2.gif'
C3_img = img_path + 'C3.gif'
C4_img = img_path + 'C4.gif'
C5_img = img_path + 'C5.gif'
C6_img = img_path + 'C6.gif'
C7_img = img_path + 'C7.gif'
C8_img = img_path + 'C8.gif'
C9_img = img_path + 'C9.gif'
CX_img = img_path + 'CX.gif'
CJ_img = img_path + 'CJ.gif'
CQ_img = img_path + 'CQ.gif'
CK_img = img_path + 'CK.gif'
#  红心Heart
HA_img = img_path + 'HA.gif'
H2_img = img_path + 'H2.gif'
H3_img = img_path + 'H3.gif'
H4_img = img_path + 'H4.gif'
H5_img = img_path + 'H5.gif'
H6_img = img_path + 'H6.gif'
H7_img = img_path + 'H7.gif'
H8_img = img_path + 'H8.gif'
H9_img = img_path + 'H9.gif'
HX_img = img_path + 'HX.gif'
HJ_img = img_path + 'HJ.gif'
HQ_img = img_path + 'HQ.gif'
HK_img = img_path + 'HK.gif'
#  黑桃Spade
SA_img = img_path + 'SA.gif'
S2_img = img_path + 'S2.gif'
S3_img = img_path + 'S3.gif'
S4_img = img_path + 'S4.gif'
S5_img = img_path + 'S5.gif'
S6_img = img_path + 'S6.gif'
S7_img = img_path + 'S7.gif'
S8_img = img_path + 'S8.gif'
S9_img = img_path + 'S9.gif'
SX_img = img_path + 'SX.gif'
SJ_img = img_path + 'SJ.gif'
SQ_img = img_path + 'SQ.gif'
SK_img = img_path + 'SK.gif'
#  大小王Joker
JM_img = img_path + 'JM.gif'
JS_img = img_path + 'JS.gif'

#  定义扑克牌类
class Card():
    def __init__(self, color, value, order, image):
        self.color = color  #  花色
        self.value = value  #  牌面值
        self.order = order  #  大小顺序（0 ~ 53）
        self.image = image  #  扑克图案

#  一副牌
deck = []
deck.append(Card('D',  '3',  0, D3_img))
deck.append(Card('C',  '3',  1, C3_img))
deck.append(Card('H',  '3',  2, H3_img))
deck.append(Card('S',  '3',  3, S3_img))
deck.append(Card('D',  '4',  4, D4_img))
deck.append(Card('C',  '4',  5, C4_img))
deck.append(Card('H',  '4',  6, H4_img))
deck.append(Card('S',  '4',  7, S4_img))
deck.append(Card('D',  '5',  8, D5_img))
deck.append(Card('C',  '5',  9, C5_img))
deck.append(Card('H',  '5', 10, H5_img))
deck.append(Card('S',  '5', 11, S5_img))
deck.append(Card('D',  '6', 12, D6_img))
deck.append(Card('C',  '6', 13, C6_img))
deck.append(Card('H',  '6', 14, H6_img))
deck.append(Card('S',  '6', 15, S6_img))
deck.append(Card('D',  '7', 16, D7_img))
deck.append(Card('C',  '7', 17, C7_img))
deck.append(Card('H',  '7', 18, H7_img))
deck.append(Card('S',  '7', 19, S7_img))
deck.append(Card('D',  '8', 20, D8_img))
deck.append(Card('C',  '8', 21, C8_img))
deck.append(Card('H',  '8', 22, H8_img))
deck.append(Card('S',  '8', 23, S8_img))
deck.append(Card('D',  '9', 24, D9_img))
deck.append(Card('C',  '9', 25, C9_img))
deck.append(Card('H',  '9', 26, H9_img))
deck.append(Card('S',  '9', 27, S9_img))
deck.append(Card('D', '10', 28, DX_img))
deck.append(Card('C', '10', 29, CX_img))
deck.append(Card('H', '10', 30, HX_img))
deck.append(Card('S', '10', 31, SX_img))
deck.append(Card('D',  'J', 32, DJ_img))
deck.append(Card('C',  'J', 33, CJ_img))
deck.append(Card('H',  'J', 34, HJ_img))
deck.append(Card('S',  'J', 35, SJ_img))
deck.append(Card('D',  'Q', 36, DQ_img))
deck.append(Card('C',  'Q', 37, CQ_img))
deck.append(Card('H',  'Q', 38, HQ_img))
deck.append(Card('S',  'Q', 39, SQ_img))
deck.append(Card('D',  'K', 40, DK_img))
deck.append(Card('C',  'K', 41, CK_img))
deck.append(Card('H',  'K', 42, HK_img))
deck.append(Card('S',  'K', 43, SK_img))
deck.append(Card('D',  'A', 44, DA_img))
deck.append(Card('C',  'A', 45, CA_img))
deck.append(Card('H',  'A', 46, HA_img))
deck.append(Card('S',  'A', 47, SA_img))
deck.append(Card('D',  '2', 48, D2_img))
deck.append(Card('C',  '2', 49, C2_img))
deck.append(Card('H',  '2', 50, H2_img))
deck.append(Card('S',  '2', 51, S2_img))
deck.append(Card('J',  'M', 52, JM_img))
deck.append(Card('J',  'S', 53, JS_img))

player_id         = 1                     #  该玩家ID
player_cards      = [1, 2, 3, 4, 5]                    #  该玩家手牌
player_name       = ['', '', '', '']      #  各玩家姓名
player_cards_num  = [13, 13, 13, 13]      #  各玩家手牌数
player_score      = [100, 100, 100, 100]  #  各玩家分数

################################################################################
##  出牌类型 ------------------------> 返回值
##  单张:one(cards) ----------------> (1,  val)
##  对子:two(cards) ----------------> (2,  val)
##  三张:tree(cards) ---------------> (3,  val)
##  小顺:five(cards) ---------------> (4,  val)
##  同花:five(cards) ---------------> (5,  val)  #  方块
##                   ---------------> (6,  val)  #  梅花
##                   ---------------> (7,  val)  #  红心
##                   ---------------> (8,  val)  #  黑桃
##  三带二:three_with_two(cards) ---> (9,  val)
##  四带一:four_with_one(cards) ----> (10, val)
##  同花顺:five(cards) -------------> (11, val)  #  方块
##                     -------------> (12, val)  #  梅花
##                     -------------> (13, val)  #  红心
##                     -------------> (14, val)  #  黑桃
##
##  val表示在跟牌时关键牌中最大的一张牌的序号值
##  如果发现不符合出牌类型中的任一种，则返回(-1, -1)
################################################################################
def one(cards):
    return (1, int(cards[0]))

def two(cards):
    if (deck[int(cards[0])].value ==
        deck[int(cards[1])].value):
        return (2, int(cards[1]))
    return (-1, -1)

def three(cards):
    if (deck[int(cards[0])].value ==
        deck[int(cards[1])].value ==
        deck[int(cards[2])].value):
        return (3, int(cards[2]))
    return (-1, -1)

def three_with_two(cards):
    if (deck[int(cards[0])].value == 
        deck[int(cards[1])].value ==
        deck[int(cards[2])].value and
        deck[int(cards[3])].value ==
        deck[int(cards[4])].value):
        return (9, int(cards[2]))
    elif (deck[int(cards[2])].value ==
        deck[int(cards[3])].value   ==
        deck[int(cards[4])].value  and
        deck[int(cards[0])].value   ==
        deck[int(cards[1])].value):
        return (9, int(cards[4]))
    return (-1, -1)

def four_with_one(cards):
    if (deck[int(cards[0])].value ==
        deck[int(cards[1])].value ==
        deck[int(cards[2])].value ==
        deck[int(cards[3])].value):
        return (10, int(cards[3]))
    elif (deck[int(cards[1])].value ==
        deck[int(cards[2])].value   ==
        deck[int(cards[3])].value   ==
        deck[int(cards[4])].value):
        return (10, int(cards[4]))
    return (-1, -1)

def five(cards):
    color = 'F'
    if (deck[int(cards[0])].color ==
        deck[int(cards[1])].color ==
        deck[int(cards[2])].color ==
        deck[int(cards[3])].color ==
        deck[int(cards[4])].color):
        color = deck[int(cards[0])].color
    v0 = deck[int(cards[0])].value
    v1 = deck[int(cards[1])].value
    v2 = deck[int(cards[2])].value
    v3 = deck[int(cards[3])].value
    v4 = deck[int(cards[4])].value
    v = (v0, v1, v2, v3, v4)
    if (v == ('A',  '2',  '3',  '4',  '5' ) or
        v == ('2',  '3',  '4',  '5',  '6' ) or
        v == ('3',  '4',  '5',  '6',  '7' ) or
        v == ('4',  '5',  '6',  '7',  '8' ) or
        v == ('5',  '6',  '7',  '8',  '9' ) or
        v == ('6',  '7',  '8',  '9',  '10') or
        v == ('7',  '8',  '9',  '10', 'J' ) or
        v == ('8',  '9',  '10', 'J',  'Q' ) or
        v == ('9',  '10', 'J',  'Q',  'K' ) or
        v == ('10', 'J',  'Q',  'K',  'A' )):
        if (color == 'D'):
            return (11, int(cards[4]))
        elif (color == 'C'):
            return (12, int(cards[4]))
        elif (color == 'H'):
            return (13, int(cards[4]))
        elif (color == 'S'):
            return (14, int(cards[4]))
        else:  #  color == 'F'
            return (4, -1)
    else:
        if (color == 'D'):
            return (5, int(cards[4]))
        elif (color == 'C'):
            return (6, int(cards[4]))
        elif (color == 'H'):
            return (7, int(cards[4]))
        elif (color == 'S'):
            return (8, int(cards[4]))
        else:  #  color == 'F'
            return (-1, -1)

#  当选择的牌数是5张是判断是什么出牌类型
def type_of_five(cards):
    t = three_with_two(cards)
    if (t[0] != -1):
        return t
    t = four_with_one(cards)
    if (t[0] != -1):
        return t
    t = five(cards)
    if (t[0] != -1):
        return t
    return (-1, -1)

#  检查出牌是否符合规则
#  prev_cards是其他玩家出的牌，play_cards是自己将要出的牌
def check(prev_cards, play_cards):
    prev_c = prev_cards.split()
    play_c = play_cards.split()
    if (len(play_c) == len(prev_c) == 1):
        return (True if one(play_c)[1] > one(prev_c)[1] > -1 else False)
    elif (len(play_c) == len(prev_c) == 2):
        return (True if two(play_c)[1] > two(prev_c)[1] > -1 else False)
    elif (len(play_c) == len(prev_c) == 3):
        return (True if three(play_c)[1] > three(prev_c)[1] > -1 else False)
    elif (len(play_c) == len(prev_c) == 5):
        if (type_of_five(play_c)[0] > type_of_five(prev_c)[0] > -1):
            return True
        elif (type_of_five(play_c)[0] == type_of_five(prev_c)[0] and
            type_of_five(play_c)[1] > type_of_five(prev_c)[1] > -1):
            return True
        else:
            return False
    else:
        return False

def self_check(play_cards):
    play_c = play_cards.split()
    if (len(play_c) == 1):
        return True
    elif (len(play_c) == 2):
        return False if two(play_c)[0] == -1 else True
    elif (len(play_c) == 3):
        return False if three(play_c)[0] == -1 else True
    elif (len(play_c) == 5):
        return False if type_of_five(play_c)[0] == -1 else True
    else:
        return False

################################################################################
##  Socket网络数据交互及协议
##  ip:string，服务器的IP地址
##  port:string，服务器的端口号
##  name:string，玩家的昵称
##  information:string，接受到的服务器发来的内容
##  prev_info:string，接收到的服务器发来的最近一条有用的内容，用来解决上家不出牌的情况
##  answer:string，客户端发送给服务端的消息
##  协议（(id + info):string）
##  0  : 初始化各个玩家姓名及对应的ID
##  1~4: 表示对应id的玩家的出牌情况，在该客户端显示出来
##  5  : 发牌
################################################################################  
ip          = '110.64.87.213'
port        = 2333
name        = ''
information = ''
prev_info   = ''
answer      = ''
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

################################################################################
##  UI界面
##  s，e，n，w分别表示自己，下家，对家，上家
################################################################################
def login():
    global ip, port, name, soc
    # ip   = str(e_ip.get())
    # port = int(e_port.get())
    name = str(e_name.get())
    r = soc.connect_ex((ip, port))
    if (r == 0):
        l_msg['text'] = 'Success!'
        soc.send(name.encode('utf-8'))
        play()
    else:
        l_msg['text'] = 'Fail'

def play():
    global p, cn, cw, ce, cs, bs
    global information, prev_info, answer, player_id
    play_ui = tk.Toplevel()
    play_ui.title('playing')
    play_ui.geometry('1000x500')

    #  初始化各个玩家信息
    def initialize():
        global information, player_name, player_id, player_score, name
        info_list = information.split()
        print(information)
        print(len(info_list))
        for i in range(4):
            player_name[i] = info_list[i + 1]
        print(info_list)
        player_id = info_list.index(name)
        player_score = [100, 100, 100, 100]
        ls_score['text'] = '分数:100'
        le_score['text'] = '分数:100'
        lw_score['text'] = '分数:100'
        ln_score['text'] = '分数:100'
        ls_name['text'] = player_name[player_id - 1]
        le_name['text'] = player_name[(player_id + 1) % 4 - 1]
        ln_name['text'] = player_name[(player_id + 2) % 4 - 1]
        lw_name['text'] = player_name[(player_id + 3) % 4 - 1]
        ls_name['text'] = '手牌数:13'
        le_name['text'] = '手牌数:13'
        ln_name['text'] = '手牌数:13'
        lw_name['text'] = '手牌数:13'

    def get_cards():
        global information, player_cards, player_cards_num
        info_list = information.split()
        player_cards = []
        for i in range(13):
            player_cards.append(int(info_list[i + 1]))
        player_cards_num = [13, 13, 13, 13]
        reflash()
        to_wait()

    def to_disc():
        for i in range(len(player_cards)):
            bs[i]['bg'] = 'blue'
        bs_disc['bg'] = 'green'
        bs_disc['text'] = '出牌'
        bs_pass['bg'] = 'green'
        bs_pass['text'] = '不出'

    def to_wait():
        for i in range(len(player_cards)):
            bs[i]['bg'] = 'white'
        bs_disc['bg'] = 'white'
        bs_disc['text'] = ''
        bs_pass['bg'] = 'white'
        bs_pass['text'] = ''

    #  出牌函数
    def discard():
        if bs_disc['bg'] == 'white':
            return
        global prev_info, answer, cards_selected, play_id, soc
        info_list = prev_info.split()
        info_id = (int(info_list[0]) + 4 - player_id) % 4
        if (info_id == player_id):
            cards_selected.sort()
            play_cards = ''
            for j in range(len(cards_selected)):
                play_cards += (str(cards_selected[j]) + ' ')
            if (self_check(play_cards)):
                answer = str(player_id) + ' ' + play_cards
                ls_pass['bg'] = 'white'
                ls_pass['text'] = ''
                reflash()
                soc.send(answer.encode('utf-8'))
            clear()
        else:
            prev_cards = ''
            for i in range(1, len(info_list)):
                prev_cards += (str(info_list[i]) + ' ')
            cards_selected.sort()
            play_cards = ''
            for j in range(len(cards_selected)):
                play_cards += (str(cards_selected[j]) + ' ')
            if (check(prev_cards, play_cards)):
                answer = str(player_id) + ' ' + play_cards
                ls_pass['bg'] = 'white'
                ls_pass['text'] = ''
                reflash()
                soc.send(answer.encode('utf-8'))
            clear()
        to_wait()
        
    #  不出牌函数
    def pas():
        global answer
        clear()
        ls_pass['bg'] = 'red'
        ls_pass['text'] = 'pass'
        answer = str(player_id) + ' -1'
        to_wait()
        soc.send(answer.encode('utf-8'))

    def reflash():
        global player_cards, cards_selected, bs
        for i in cards_selected:
            player_cards.remove(i)
        for j in bs:
            j['image'] = ''
            j['bg'] = 'white'
        for k in range(len(player_cards)):
            bs[k]['image'] = p[player_cards[k]]
            bs[k]['bg'] = 'blue'
    
    def clear():
        global cards_selected, bs
        cards_selected = []
        for i in bs:
            if i['bg'] == 'red':
                i['bg'] = 'blue'
    
    #  显示出牌函数
    #  id(1~4) + card IDs(-1表示pass)
    #  如果某一方手牌打完了就统计分数
    def show():
        global information, prev_info, player_id
        global cn, cw, ce, cs
        info_list = information.split()
        info_len = len(info_list)
        info_id = (int(info_list[0]) + 4 - player_id) % 4
        if (info_id == 0):
            if (int(info_list[1]) == -1):
                ls_pass['bg'] = 'red'
                ls_pass['text'] = 'Pass'
            else:
                prev_info = information
                ls_pass['bg'] = 'white'
                ls_pass['text'] = ''
                player_cards_num[info_id] -= (info_len - 1)
                ls_num['text'] = '手牌数:' + str(player_cards_num[info_id])
                for i in cs:
                    i['image'] = ''
                for j in range(1, info_len):
                    cs[j - 1]['image'] = p[int(info_list[j])]
        elif (info_id == 1):
            if (int(info_list[1]) == -1):
                le_pass['bg'] = 'red'
                le_pass['text'] = 'Pass'
            else:
                prev_info = information
                le_pass['bg'] = 'white'
                le_pass['text'] = ''
                player_cards_num[info_id] -= (info_len - 1)
                le_num['text'] = '手牌数:' + str(player_cards_num[info_id])
                for i in ce:
                    i['image'] = ''
                for j in range(1, info_len):
                    ce[j - 1]['image'] = p[int(info_list[j])]
        elif (info_id == 2):
            if (int(info_list[1]) == -1):
                ln_pass['bg'] = 'red'
                ln_pass['text'] = 'Pass'
            else:
                prev_info = information
                ln_pass['bg'] = 'white'
                ln_pass['text'] = ''
                player_cards_num[info_id] -= (info_len - 1)
                ln_num['text'] = '手牌数:' + str(player_cards_num[info_id])
                for i in cn:
                    i['image'] = ''
                for j in range(1, info_len):
                    cn[j - 1]['image'] = p[int(info_list[j])]
        elif (info_id == 3):
            if (int(info_list[1]) == -1):
                lw_pass['bg'] = 'red'
                lw_pass['text'] = 'Pass'
            else:
                prev_info = information
                lw_pass['bg'] = 'white'
                lw_pass['text'] = ''
                player_cards_num[info_id] -= (info_len - 1)
                lw_num['text'] = '手牌数:' + str(player_cards_num[info_id])
                for i in cw:
                    i['image'] = ''
                for j in range(1, info_len):
                    cw[j - 1]['image'] = p[int(info_list[j])]
            to_disc()
        else:
            pass
        if (0 in player_cards_num):
            cal_score()

    def cal_score():
        global player_cards_num, player_score
        for i in range(4):
            if 0 <= player_cards_num[i] < 8:
                player_score[i] -= player_cards_num[i]
            elif 8 <= player_cards_num[i] < 10:
                player_score[i] -= player_cards_num[i] * 2
            elif 10 <= player_cards_num[i] < 12:
                player_score[i] -= player_cards_num[i] * 3
            else:  #  player_cards_num[i] == 13
                player_score[i] -= player_cards_num[i] * 4
        ls_score['text'] = '分数:' + str(player_score[0])
        le_score['text'] = '分数:' + str(player_score[1])
        ln_score['text'] = '分数:' + str(player_score[2])
        lw_score['text'] = '分数:' + str(player_score[3])

    #  对家布局
    fn = tk.Frame(master = play_ui)
    fn.pack(side = tk.TOP)
    fn1 = tk.Frame(master = fn)
    fn1.pack(pady = 5)
    fn2 = tk.Frame(master = fn)
    fn2.pack(pady = 5)
    ln_name = tk.Label(master = fn1, text = '')
    ln_name.grid(row = 0, column = 0, padx = 5)
    ln_num = tk.Label(master = fn1, text = '手牌:0')
    ln_num.grid(row =0, column = 1, padx = 5)
    ln_score = tk.Label(master = fn1, text = '分数:0')
    ln_score.grid(row = 0, column = 2, padx = 5)
    ln_pass = tk.Label(master = fn1, bg = 'white', text = '')
    ln_pass.grid(row = 0, column = 3, padx = 5)
    for i in range(5):
        cn.append(tk.Label(master = fn2, image = ''))
        cn[i].grid(row = 0, column = i)

    #  上家布局
    fw = tk.Frame(master = play_ui)
    fw.pack(side = tk.LEFT)
    fw1 = tk.Frame(master = fw)
    fw1.pack(pady = 5)
    fw2 = tk.Frame(master = fw)
    fw2.pack(pady = 5)
    lw_name = tk.Label(master = fw1, text = '')
    lw_name.grid(row = 0, column = 0, padx = 5)
    lw_num = tk.Label(master = fw1, text = '手牌:0')
    lw_num.grid(row = 0, column = 1, padx = 5)
    lw_score = tk.Label(master = fw1, text = '分数:0')
    lw_score.grid(row = 0, column = 2, padx = 5)
    lw_pass = tk.Label(master = fw1, bg = 'white', text = '')
    lw_pass.grid(row = 0, column = 3, padx = 5)
    for i in range(5):
        cw.append(tk.Label(master = fw2, image = ''))
        cw[i].grid(row = 0, column = i)

    #  下家布局
    fe = tk.Frame(master = play_ui)
    fe.pack(side = tk.RIGHT)
    fe1 = tk.Frame(master = fe)
    fe1.pack(pady = 5)
    fe2 = tk.Frame(master = fe)
    fe2.pack(pady = 5)
    le_pass = tk.Label(master = fe1, bg = 'white', text = '')
    le_pass.grid(row = 0, column = 0, padx = 5)
    le_name = tk.Label(master = fe1, text = '')
    le_name.grid(row = 0, column = 1, padx = 5)
    le_num = tk.Label(master = fe1, text = '手牌:0')
    le_num.grid(row = 0, column = 2, padx = 5)
    le_score = tk.Label(master = fe1, text = '分数:0')
    le_score.grid(row = 0, column = 3, padx = 5)
    for i in range(5):
        ce.append(tk.Label(master = fe2, image = ''))
        ce[i].grid(row = 0, column = i)

    #  自己布局
    fs = tk.Frame(master = play_ui)
    fs.pack(side = tk.BOTTOM)
    fs0 = tk.Frame(master = fs)
    fs0.pack(pady = 5)
    fs1 = tk.Frame(master = fs)
    fs1.pack(pady = 5)
    fs2 = tk.Frame(master = fs)
    fs2.pack(pady = 5)
    fs3 = tk.Frame(master = fs)
    fs3.pack(pady = 5)
    for i in range(5):
        cs.append(tk.Label(master = fs0, image = ''))
        cs[i].grid(row = 0, column = i)
    ls_name = tk.Label(master = fs1, text = '')
    ls_name.grid(row = 0, column = 0, padx = 5)
    ls_num = tk.Label(master = fs1, text = '手牌:0')
    ls_num.grid(row = 0, column = 1, padx = 5)
    ls_score = tk.Label(master = fs1, text = '分数:0')
    ls_score.grid(row = 0, column = 2, padx = 5)
    ls_pass = tk.Label(master = fs1, bg = 'white', text = '')
    ls_pass.grid(row = 0, column = 3, padx = 5)
    for i in range(13):
        bs.append(tk.Button(master = fs2, bg = 'white', image = ''))
        bs[i].grid(row = 0, column = i)
    bs[0]['command']  = lambda : button_responed(bs[0])
    bs[1]['command']  = lambda : button_responed(bs[1])
    bs[2]['command']  = lambda : button_responed(bs[2])
    bs[3]['command']  = lambda : button_responed(bs[3])
    bs[4]['command']  = lambda : button_responed(bs[4])
    bs[5]['command']  = lambda : button_responed(bs[5])
    bs[6]['command']  = lambda : button_responed(bs[6])
    bs[7]['command']  = lambda : button_responed(bs[7])
    bs[8]['command']  = lambda : button_responed(bs[8])
    bs[9]['command']  = lambda : button_responed(bs[9])
    bs[10]['command'] = lambda : button_responed(bs[10])
    bs[11]['command'] = lambda : button_responed(bs[11])
    bs[12]['command'] = lambda : button_responed(bs[12])
    bs_disc = tk.Button(master = fs3, bg = 'white', text = '', command = discard)
    bs_disc.grid(row = 0, column = 0, padx = 20)
    bs_pass = tk.Button(master = fs3, bg = 'white', text = '', command = pas)
    bs_pass.grid(row = 0, column = 1, padx = 20)

    def listen():
        global information
        while True:
            information = soc.recv(1024).decode('utf-8')
            print(information)
            info_list = information.split()
            info_id = int(info_list[0])
            if (info_id == 0):
                initialize()
            elif (1 <= info_id <= 4):
                show()
            elif (info_id == 5):
                get_cards()

    net_t = threading.Thread(target = listen)
    net_t.start()


def button_responed(btn):
    global cards_selected
    if btn['bg'] == 'blue':
        btn['bg'] = 'red'
        cards_selected.append(int(p_str.index(btn['image'])))
    elif btn['bg'] == 'red':
        btn['bg'] = 'blue'
        cards_selected.remove(int(p_str.index(btn['image'])))
    else:
        pass

root = tk.Tk()
l_ip = tk.Label(master = root, text = 'IP:')
l_ip.grid(row = 0, column = 0, sticky = tk.W, padx = 5, pady = 5)
e_ip = tk.Entry(master = root)
e_ip.grid(row = 0, column = 1, sticky = tk.E, padx = 5, pady = 5)
l_port = tk.Label(master = root, text = 'Port:')
l_port.grid(row = 1, column = 0, sticky = tk.W, padx = 5, pady = 5)
e_port = tk.Entry(master = root)
e_port.grid(row = 1, column = 1, sticky = tk.E, padx = 5, pady = 5)
l_name = tk.Label(master = root, text = 'Name:')
l_name.grid(row = 2, column = 0, sticky = tk.W, padx = 5, pady = 5)
e_name = tk.Entry(master = root)
e_name.grid(row = 2, column = 1, sticky = tk.E, padx = 5, pady = 5)
l_msg = tk.Label(master = root, text = 'Welcome!')
l_msg.grid(row = 3, column = 0, sticky = tk.W, padx = 5, pady = 5)
b_login = tk.Button(master = root, text = 'Login', command = login)
b_login.grid(row = 3, column = 1, sticky = tk.E, padx = 5, pady = 5)

cn, cw, ce, cs, bs = [], [], [], [], []
cards_selected = []  #  选择的牌
#  将扑克牌图案变成tkinter.PhotoImage类型保存
p = []
p.append(tk.PhotoImage(file = D3_img))
p.append(tk.PhotoImage(file = C3_img))
p.append(tk.PhotoImage(file = H3_img))
p.append(tk.PhotoImage(file = S3_img))
p.append(tk.PhotoImage(file = D4_img))
p.append(tk.PhotoImage(file = C4_img))
p.append(tk.PhotoImage(file = H4_img))
p.append(tk.PhotoImage(file = S4_img))
p.append(tk.PhotoImage(file = D5_img))
p.append(tk.PhotoImage(file = C5_img))
p.append(tk.PhotoImage(file = H5_img))
p.append(tk.PhotoImage(file = S5_img))
p.append(tk.PhotoImage(file = D6_img))
p.append(tk.PhotoImage(file = C6_img))
p.append(tk.PhotoImage(file = H6_img))
p.append(tk.PhotoImage(file = S6_img))
p.append(tk.PhotoImage(file = D7_img))
p.append(tk.PhotoImage(file = C7_img))
p.append(tk.PhotoImage(file = H7_img))
p.append(tk.PhotoImage(file = S7_img))
p.append(tk.PhotoImage(file = D8_img))
p.append(tk.PhotoImage(file = C8_img))
p.append(tk.PhotoImage(file = H8_img))
p.append(tk.PhotoImage(file = S8_img))
p.append(tk.PhotoImage(file = D9_img))
p.append(tk.PhotoImage(file = C9_img))
p.append(tk.PhotoImage(file = H9_img))
p.append(tk.PhotoImage(file = S9_img))
p.append(tk.PhotoImage(file = DX_img))
p.append(tk.PhotoImage(file = CX_img))
p.append(tk.PhotoImage(file = HX_img))
p.append(tk.PhotoImage(file = SX_img))
p.append(tk.PhotoImage(file = DJ_img))
p.append(tk.PhotoImage(file = CJ_img))
p.append(tk.PhotoImage(file = HJ_img))
p.append(tk.PhotoImage(file = SJ_img))
p.append(tk.PhotoImage(file = DQ_img))
p.append(tk.PhotoImage(file = CQ_img))
p.append(tk.PhotoImage(file = HQ_img))
p.append(tk.PhotoImage(file = SQ_img))
p.append(tk.PhotoImage(file = DK_img))
p.append(tk.PhotoImage(file = CK_img))
p.append(tk.PhotoImage(file = HK_img))
p.append(tk.PhotoImage(file = SK_img))
p.append(tk.PhotoImage(file = DA_img))
p.append(tk.PhotoImage(file = CA_img))
p.append(tk.PhotoImage(file = HA_img))
p.append(tk.PhotoImage(file = SA_img))
p.append(tk.PhotoImage(file = D2_img))
p.append(tk.PhotoImage(file = C2_img))
p.append(tk.PhotoImage(file = H2_img))
p.append(tk.PhotoImage(file = S2_img))
p.append(tk.PhotoImage(file = JM_img))
p.append(tk.PhotoImage(file = JS_img))
p_str = []
for i in p:
    p_str.append(str(i))
################################################################################
def Main():
    root.mainloop()

if __name__ == '__main__':
    Main()