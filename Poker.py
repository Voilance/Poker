import os
import tkinter
import socket
import threading


########################################Prepare#################################
# Get image path
img_path = os.curdir + os.sep + 'image' + os.sep
# Diamond
DA_img  = img_path + 'diamond_A.gif'
D2_img  = img_path + 'diamond_2.gif'
D3_img  = img_path + 'diamond_3.gif'
D4_img  = img_path + 'diamond_4.gif'
D5_img  = img_path + 'diamond_5.gif'
D6_img  = img_path + 'diamond_6.gif'
D7_img  = img_path + 'diamond_7.gif'
D8_img  = img_path + 'diamond_8.gif'
D9_img  = img_path + 'diamond_9.gif'
D10_img = img_path + 'diamond_10.gif'
DJ_img  = img_path + 'diamond_J.gif'
DQ_img  = img_path + 'diamond_Q.gif'
DK_img  = img_path + 'diamond_K.gif'
# Club
CA_img  = img_path + 'club_A.gif'
C2_img  = img_path + 'club_2.gif'
C3_img  = img_path + 'club_3.gif'
C4_img  = img_path + 'club_4.gif'
C5_img  = img_path + 'club_5.gif'
C6_img  = img_path + 'club_6.gif'
C7_img  = img_path + 'club_7.gif'
C8_img  = img_path + 'club_8.gif'
C9_img  = img_path + 'club_9.gif'
C10_img = img_path + 'club_10.gif'
CJ_img  = img_path + 'club_J.gif'
CQ_img  = img_path + 'club_Q.gif'
CK_img  = img_path + 'club_K.gif'
# Heart
HA_img  = img_path + 'heart_A.gif'
H2_img  = img_path + 'heart_2.gif'
H3_img  = img_path + 'heart_3.gif'
H4_img  = img_path + 'heart_4.gif'
H5_img  = img_path + 'heart_5.gif'
H6_img  = img_path + 'heart_6.gif'
H7_img  = img_path + 'heart_7.gif'
H8_img  = img_path + 'heart_8.gif'
H9_img  = img_path + 'heart_9.gif'
H10_img = img_path + 'heart_10.gif'
HJ_img  = img_path + 'heart_J.gif'
HQ_img  = img_path + 'heart_Q.gif'
HK_img  = img_path + 'heart_K.gif'
# Spade
SA_img  = img_path + 'spade_A.gif'
S2_img  = img_path + 'spade_2.gif'
S3_img  = img_path + 'spade_3.gif'
S4_img  = img_path + 'spade_4.gif'
S5_img  = img_path + 'spade_5.gif'
S6_img  = img_path + 'spade_6.gif'
S7_img  = img_path + 'spade_7.gif'
S8_img  = img_path + 'spade_8.gif'
S9_img  = img_path + 'spade_9.gif'
S10_img = img_path + 'spade_10.gif'
SJ_img  = img_path + 'spade_J.gif'
SQ_img  = img_path + 'spade_Q.gif'
SK_img  = img_path + 'spade_K.gif'
# Joker
J1_img  = img_path + 'joker_moon.gif'
J2_img  = img_path + 'joker_sun.gif'


class Card():
    def __init__(self, color, face_val, order, img):
        self.color    = color     # 花色
        self.face_val = face_val  # 牌面值
        self.order    = order     # 顺序值
        self.img      = img

    def __lt__(self, other):
        return self.order < other.order
    def __gt__(self, other):
        return self.order > other.order

# Initial a deck
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
deck.append(Card('D', '10', 28, D10_img))
deck.append(Card('C', '10', 29, C10_img))
deck.append(Card('H', '10', 30, H10_img))
deck.append(Card('S', '10', 31, S10_img))
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
deck.append(Card('J',  'm', 52, J1_img))
deck.append(Card('J',  's', 53, J2_img))

player_name = []
player_id   = 0
player_cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
player_card_num = [13, 13, 13, 13]
player_score = []

########################################UI######################################

def login():
    global ip
    global port
    global name
    ip = str(e_ip.get())
    port = str(e_port.get())
    name = str(e_name.get())
    play()

def play():
    playUI = tkinter.Toplevel()
    playUI.title('playing')
    playUI.geometry('1000x500')
    global photo
    cards_prepare = []

    def to_string(lis):
        l = len(lis)
        if l == 0:
            return ''
        else:
            lis.sort()
            s = str(lis[0])
            for i in range(1, l):
                s += (' ' + str(lis[i]))
            return s

    def button_responed(btn):
        if btn['bg'] == 'blue':
            btn['bg'] = 'red'
            cards_prepare.append(int(photo_str.index(btn['image'])))
        elif btn['bg'] == 'red':
            btn['bg'] = 'blue'
            cards_prepare.remove(int(photo_str.index(btn['image'])))
        else:
            pass

    #test
    def discard():
        global prev_info
        global answer
        nonlocal cards_prepare
        info_list = prev_info.split()
        info_id = (int(info_list[0]) + 4 - player_id) % 4
        if info_id == player_id:
            pass
        else:
            prev_cards = ''
            for i in range(1, len(info_list)):
                prev_cards += (' ' + str(info_list[i]))
            cards_prepare.sort()
            play_cards = to_string(cards_prepare)
            if check(prev_cards, play_cards):
                answer = str(player_id) + ' ' + play_cards
                ls_pass['bg'] = 'white'
                ls_pass['text'] = ''
                player_card_num[player_id] -= len(cards_prepare)
                ls_num['text'] = 'num:' + str(player_card_num[player_id])
                for i in range(5):
                    cs[i]['image'] = ''
                for j in range(len(cards_prepare)):
                    cs[j]['image'] = photo[cards_prepare[j]]

                reflash()
                clear()
                # 发送给客户端
            else:
                clear()

    def reflash():
        global player_cards
        nonlocal cards_prepare
        for i in cards_prepare:
            player_cards.remove(i)
        for i in bs:
            i['image'] = ''
            i['bg'] = 'white'
        for i in range(len(player_cards)):
            bs[i]['image'] = photo[player_cards[i]]
            bs[i]['bg'] = 'blue'

    def clear():
        nonlocal cards_prepare
        cards_prepare = []
        for i in bs:
            if i['bg'] == 'red':
                i['bg'] = 'blue'
    
    def pas():
        clear()
        ls_pass['bg'] = 'red'
        ls_pass['text'] = 'pass'

    def show_cards():
        global information
        global player_id
        info_list = information.split()
        info_len = len(info_list)
        info_id  = (int(info_list[0]) + 4 - player_id) % 4

        if info_id == 1:
            if int(info_list[0]) == -1:
                le_pass['bg'] = 'red'
                le_pass['text'] = 'pass'
            else:
                le_pass['bg'] = 'white'
                le_pass['text'] = ''
                player_card_num[info_id] -= (info_len - 1)
                le_num['text'] = 'num:' + str(player_card_num[info_id])
                for i in range(5):
                    ce[i]['image'] = ''
                for j in range(1, info_len):
                    ce[j - 1]['image'] = photo[int(info_list[j])]
        elif info_id == 2:
            if int(info_list[0]) == -1:
                ln_pass['bg'] = 'red'
                ln_pass['text'] = 'pass'
            else:
                ln_pass['bg'] = 'white'
                ln_pass['text'] = ''
                player_card_num[info_id] -= (info_len - 1)
                ln_num['text'] = 'num:' + str(player_card_num[info_id])
                for i in range(5):
                    cn[i]['image'] = ''
                for j in range(1, info_len):
                    cn[j - 1]['image'] = photo[int(info_list[j])]
        elif info_id == 3:
            if int(info_list[0]) == -1:
                lw_pass['bg'] = 'red'
                lw_pass['text'] = 'pass'
            else:
                lw_pass['bg'] = 'white'
                lw_pass['text'] = ''
                player_card_num[info_id] -= (info_len - 1)
                lw_num['text'] = 'num:' + str(player_card_num[info_id])
                for i in range(5):
                    cw[i]['image'] = ''
                for j in range(1, info_len):
                    cw[j - 1]['image'] = photo[int(info_list[j])]
        else:
            pass


    fn = tkinter.Frame(master = playUI)
    fn.pack(side = tkinter.TOP)
    fn1 = tkinter.Frame(master = fn)
    fn1.pack(pady = 5)
    fn2 = tkinter.Frame(master = fn)
    fn2.pack(pady = 5)
    ln_name = tkinter.Label(master = fn1, bg = 'blue', text = 'Bokjan')
    ln_name.grid(row = 0, column = 0, padx = 5)
    ln_num = tkinter.Label(master = fn1, bg = 'blue', text = 'num:' + '13')
    ln_num.grid(row = 0, column = 1, padx = 5)
    ln_score = tkinter.Label(master = fn1, bg = 'blue', text = 'score:' + '100')
    ln_score.grid(row = 0, column = 2, padx = 5)
    ln_pass = tkinter.Label(master = fn1, bg = 'white', text = '')
    ln_pass.grid(row = 0, column = 3, padx = 5)
    cn = []
    for i in range(5):
        cn.append(tkinter.Label(master = fn2, image = ''))
        cn[i].grid(row = 0, column = i)


    fw = tkinter.Frame(master = playUI)
    fw.pack(side = tkinter.LEFT)
    fw1 = tkinter.Frame(master = fw)
    fw1.pack(pady = 5)
    fw2 = tkinter.Frame(master = fw)
    fw2.pack(pady = 5)
    lw_name = tkinter.Label(master = fw1, bg = 'blue', text = 'JayC')
    lw_name.grid(row = 0, column = 0, padx = 5)
    lw_num = tkinter.Label(master = fw1, bg = 'blue', text = 'num:' + '13')
    lw_num.grid(row = 0, column = 1, padx = 5)
    lw_score = tkinter.Label(master = fw1, bg = 'blue', text = 'score:' + '100')
    lw_score.grid(row = 0, column = 2, padx = 5)
    lw_pass = tkinter.Label(master = fw1, bg = 'white', text = '')
    lw_pass.grid(row = 0, column = 3, padx = 5)
    cw = []
    for i in range(5):
        cw.append(tkinter.Label(master = fw2, image = ''))
        cw[i].grid(row = 0, column = i)



    fe = tkinter.Frame(master = playUI)
    fe.pack(side = tkinter.RIGHT)
    fe1 = tkinter.Frame(master = fe)
    fe1.pack(pady = 5)
    fe2 = tkinter.Frame(master = fe)
    fe2.pack(pady = 5)
    le_pass = tkinter.Label(master = fe1, bg = 'white', text = '')
    le_pass.grid(row = 0, column = 0, padx = 5)
    le_name = tkinter.Label(master = fe1, bg = 'blue', text = 'Sticnarf')
    le_name.grid(row = 0, column = 1, padx = 5)
    le_num = tkinter.Label(master = fe1, bg = 'blue', text = 'num:' + '13')
    le_num.grid(row = 0, column = 2, padx = 5)
    le_score = tkinter.Label(master = fe1, bg = 'blue', text = 'score:' + '100')
    le_score.grid(row = 0, column = 3, padx = 5)
    ce = []
    for i in range(5):
        ce.append(tkinter.Label(master = fe2, image = ''))
        ce[i].grid(row = 0, column = i)



    fs = tkinter.Frame(master = playUI)
    fs.pack(side = tkinter.BOTTOM)
    fs0 = tkinter.Frame(master = fs)
    fs0.pack(pady = 5)
    fs1 = tkinter.Frame(master = fs)
    fs1.pack(pady = 5)
    fs2 = tkinter.Frame(master = fs)
    fs2.pack(pady = 5)
    fs3 = tkinter.Frame(master = fs)
    fs3.pack(pady = 5)
    cs = []
    for i in range(5):
        cs.append(tkinter.Label(master = fs0))
        cs[i].grid(row = 0, column = i)
    ls_name = tkinter.Label(master = fs1, bg = 'blue', text = 'Voilance')
    ls_name.grid(row = 0, column = 0, padx = 5)
    ls_num = tkinter.Label(master = fs1, bg = 'blue', text = 'num:' + '13')
    ls_num.grid(row = 0, column = 1, padx = 5)
    ls_score = tkinter.Label(master = fs1, bg = 'blue', text = 'score:' + '100')
    ls_score.grid(row = 0, column = 2, padx = 5)
    ls_pass = tkinter.Label(master = fs1, bg = 'white', text = '')
    ls_pass.grid(row = 0, column = 3, padx = 5)
    bs = []
    for i in range(13):
        bs.append(tkinter.Button(master = fs2, bg = 'blue', image = photo[i]))
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
    bs_disc = tkinter.Button(master = fs3, text = '出牌', command = discard)
    bs_disc.grid(row = 0, column = 0, padx = 10)
    bs_pass = tkinter.Button(master = fs3, text = 'pass', command = pas)
    bs_pass.grid(row = 0, column = 1, padx = 20)

    #test
    show_cards()


root = tkinter.Tk()
l_ip = tkinter.Label(root, text = 'IP:')
l_ip.grid(row = 0, column = 0, sticky = tkinter.W)
e_ip = tkinter.Entry(root)
e_ip.grid(row = 0, column = 1, sticky = tkinter.E)
l_port = tkinter.Label(root, text = 'Port:')
l_port.grid(row = 1, column = 0, sticky = tkinter.W)
e_port = tkinter.Entry(root)
e_port.grid(row = 1, column = 1, sticky = tkinter.E)
l_name = tkinter.Label(root, text = 'Name:')
l_name.grid(row = 2, column = 0, sticky = tkinter.W)
e_name = tkinter.Entry(root)
e_name.grid(row = 2, column = 1, sticky = tkinter.E)
b_login = tkinter.Button(root, text = 'Login', command = login)
b_login.grid(row = 3, column = 1, sticky = tkinter.E)

photo = []
photo.append(tkinter.PhotoImage(file = D3_img))
photo.append(tkinter.PhotoImage(file = C3_img))
photo.append(tkinter.PhotoImage(file = H3_img))
photo.append(tkinter.PhotoImage(file = S3_img))
photo.append(tkinter.PhotoImage(file = D4_img))
photo.append(tkinter.PhotoImage(file = C4_img))
photo.append(tkinter.PhotoImage(file = H4_img))
photo.append(tkinter.PhotoImage(file = S4_img))
photo.append(tkinter.PhotoImage(file = D5_img))
photo.append(tkinter.PhotoImage(file = C5_img))
photo.append(tkinter.PhotoImage(file = H5_img))
photo.append(tkinter.PhotoImage(file = S5_img))
photo.append(tkinter.PhotoImage(file = D6_img))
photo.append(tkinter.PhotoImage(file = C6_img))
photo.append(tkinter.PhotoImage(file = H6_img))
photo.append(tkinter.PhotoImage(file = S6_img))
photo.append(tkinter.PhotoImage(file = D7_img))
photo.append(tkinter.PhotoImage(file = C7_img))
photo.append(tkinter.PhotoImage(file = H7_img))
photo.append(tkinter.PhotoImage(file = S7_img))
photo.append(tkinter.PhotoImage(file = D8_img))
photo.append(tkinter.PhotoImage(file = C8_img))
photo.append(tkinter.PhotoImage(file = H8_img))
photo.append(tkinter.PhotoImage(file = S8_img))
photo.append(tkinter.PhotoImage(file = D9_img))
photo.append(tkinter.PhotoImage(file = C9_img))
photo.append(tkinter.PhotoImage(file = H9_img))
photo.append(tkinter.PhotoImage(file = S9_img))
photo.append(tkinter.PhotoImage(file = D10_img))
photo.append(tkinter.PhotoImage(file = C10_img))
photo.append(tkinter.PhotoImage(file = H10_img))
photo.append(tkinter.PhotoImage(file = S10_img))
photo.append(tkinter.PhotoImage(file = DJ_img))
photo.append(tkinter.PhotoImage(file = CJ_img))
photo.append(tkinter.PhotoImage(file = HJ_img))
photo.append(tkinter.PhotoImage(file = SJ_img))
photo.append(tkinter.PhotoImage(file = DQ_img))
photo.append(tkinter.PhotoImage(file = CQ_img))
photo.append(tkinter.PhotoImage(file = HQ_img))
photo.append(tkinter.PhotoImage(file = SQ_img))
photo.append(tkinter.PhotoImage(file = DK_img))
photo.append(tkinter.PhotoImage(file = CK_img))
photo.append(tkinter.PhotoImage(file = HK_img))
photo.append(tkinter.PhotoImage(file = SK_img))
photo.append(tkinter.PhotoImage(file = DA_img))
photo.append(tkinter.PhotoImage(file = CA_img))
photo.append(tkinter.PhotoImage(file = HA_img))
photo.append(tkinter.PhotoImage(file = SA_img))
photo.append(tkinter.PhotoImage(file = D2_img))
photo.append(tkinter.PhotoImage(file = C2_img))
photo.append(tkinter.PhotoImage(file = H2_img))
photo.append(tkinter.PhotoImage(file = S2_img))
photo.append(tkinter.PhotoImage(file = J1_img))
photo.append(tkinter.PhotoImage(file = J2_img))

photo_str = []
for i in photo:
    photo_str.append(str(i))


########################################Logic###################################

def one(cards):
    return (1, int(cards[0]))

def two(cards):
    if (deck[int(cards[0])].face_val == deck[int(cards[1])].face_val):
        return (2, int(cards[1]))
    return (-1, -1)
        
def three(cards):
    if (deck[int(cards[0])].face_val == deck[int(cards[1])].face_val == deck[int(cards[2])].face_val):
        return (3, int(cards[2]))
    return (-1, -1)

def three_with_two(cards):
    if (deck[int(cards[0])].face_val == deck[int(cards[1])].face_val == deck[int(cards[2])].face_val and
        deck[int(cards[3])].face_val == deck[int(cards[4])].face_val):
        return (9, int(cards[2]))
    elif (deck[int(cards[2])].face_val == deck[int(cards[3])].face_val == deck[int(cards[4])].face_val and
        deck[int(cards[0])].face_val == deck[int(cards[1])].face_val):
        return (9, int(cards[4]))
    else:
        return (-1, -1)
def four_with_one(cards):
    if (deck[int(cards[0])].face_val == deck[int(cards[1])].face_val == 
        deck[int(cards[2])].face_val == deck[int(cards[3])].face_val):
        return (10, int(cards[3]))
    elif (deck[int(cards[1])].face_val == deck[int(cards[2])].face_val == 
        deck[int(cards[3])].face_val == deck[int(cards[4])].face_val):
        return (10, int(cards[4]))
    else:
        return (-1, -1)

def five(cards):
    color = False
    if (deck[int(cards[0])].color ==
        deck[int(cards[1])].color ==
        deck[int(cards[2])].color ==
        deck[int(cards[3])].color ==
        deck[int(cards[4])].color):
        color = True
    v0 = deck[int(cards[0])].face_val
    v1 = deck[int(cards[1])].face_val
    v2 = deck[int(cards[2])].face_val
    v3 = deck[int(cards[3])].face_val
    v4 = deck[int(cards[4])].face_val
    if ((v0 == 'A' and v1 == '2' and v2 == '3' and v3 == '4' and v4 == '5') or
        (v0 == '2' and v1 == '3' and v2 == '4' and v3 == '5' and v4 == '6') or
        (v0 == '3' and v1 == '4' and v2 == '5' and v3 == '6' and v4 == '7') or
        (v0 == '4' and v1 == '5' and v2 == '6' and v3 == '7' and v4 == '8') or
        (v0 == '5' and v1 == '6' and v2 == '7' and v3 == '8' and v4 == '9') or
        (v0 == '6' and v1 == '7' and v2 == '8' and v3 == '9' and v4 == '10') or
        (v0 == '7' and v1 == '8' and v2 == '9' and v3 == '10' and v4 == 'J') or
        (v0 == '8' and v1 == '9' and v2 == '10' and v3 == 'J' and v4 == 'Q') or
        (v0 == '9' and v1 == '10' and v2 == 'J' and v3 == 'Q' and v4 == 'K') or
        (v0 == '10' and v1 == 'J' and v2 == 'Q' and v3 == 'K' and v4 == 'A')):
        if (color):
            if (deck[int(cards[4])].color == 'D'):
                return (11, int(cards[4]))
            elif (deck[int(cards[4])].color == 'C'):
                return (12, int(cards[4]))
            elif (deck[int(cards[4])].color == 'H'):
                return (13, int(cards[4]))
            else: # deck[int(cards[4])].color == 'S'
                return (14, int(cards[4]))
        else:
            return (4, int(cards[4]))
    else:
        if (color):
            if (deck[int(cards[4])].color == 'D'):
                return (5, int(cards[4]))
            elif (deck[int(cards[4])].color == 'C'):
                return (6, int(cards[4]))
            elif (deck[int(cards[4])].color == 'H'):
                return (7, int(cards[4]))
            else: # deck[int(cards[4])].color == 'S'
                return (8, int(cards[4]))
        else:
            return (-1, -1)

def tuple_of_five(cards):
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

def check(prev_cards, play_cards):
    prev_c = prev_cards.split()
    play_c = play_cards.split()
    prev_l = len(prev_c)
    play_l = len(play_c)

    if (prev_l == play_l == 1):
        prev_t = one(prev_c)
        play_t = one(play_c)
        if (play_t[1] > prev_t[1] > -1):
            return True
        return False
    elif (prev_l == play_l == 2):
        prev_t = two(prev_c)
        play_t = two(play_c)
        if (play_t[1] > prev_t[1] > -1):
            return True
        return False
    elif (prev_l == play_l == 3):
        prev_t = three(prev_c)
        play_t = three(play_c)
        if (play_t[1] > prev_t[1] > -1):
            return True
        return False
    elif (prev_l == play_l == 5):
        prev_t = tuple_of_five(prev_c)
        play_t = tuple_of_five(play_c)
        if (play_t[0] > prev_t[0] > -1):
            return True
        elif (play_t[0] == prev_t[0] and play_t[1] > prev_t[1] > -1):
            return True
        else:
            return False
    else:
        return False

########################################Network#################################

ip = ''
port = ''
name = ''
information = '3 0 5 8 14 17'
prev_info = '3 0 5 8 14 17'
answer = ''

########################################Main####################################

def Main():
    root.mainloop()

if __name__ == '__main__':
    Main()
