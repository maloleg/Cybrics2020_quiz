import sys
import pyautogui
import time


def get_pixel_colour(i_x, i_y):
    return pyautogui.screenshot(region=(i_x, i_y, 1, 1)).getcolors()[0][1][2]

def copy_and_paste_to_python():
    pyautogui.moveTo(650, 850, 0.01)
    pyautogui.click(button='right')
    pyautogui.moveTo(660, 860, 0.2)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(670, 870, 0.2)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(900, 988, 0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')

def right_number(up_amount, down_amount):
    a = [[907, 945], [869, 908, 944], [832, 870, 907, 945], [793, 831, 869, 908, 945]]
    b = [177, 215, 253, 291]
    result = 0

    for i in range(up_amount):
        # print(a[up_amount-2][i] - b[down_amount-2])
        # print(up_amount-2, i)
        pyautogui.moveTo(309, a[up_amount-2][i] - b[down_amount-2], 0.1)
        if get_pixel_colour(pyautogui.position().x, pyautogui.position().y) > 205 and get_pixel_colour(pyautogui.position().x, pyautogui.position().y) < 225:
            result = i + 1
            break
    return result

def click_on(amount, number):
    a = [[907, 945], [869, 908, 944], [832, 870, 907, 945], [793, 831, 869, 908, 945]]
    pyautogui.moveTo(309, a[amount - 2][number - 1], 0.1)
    pyautogui.click()

# s = 'AlienQuizBot, [25.07.20 16:52]\n[ Poll : Wins: 1/100\nWhich one is the best emoji? ]\n- 🙇🏻\n- 🏬\n- 👮🏿\n- 🙆\n- 🇬🇭\n'

# s2 = sys.stdin.read()

s3 = []

s4 = []

count = 0

id2 = 0

ss = ''

dict = {'👚': 22, '🇬🇧': 12, '🏁': 16, '😜': 2, '🦄': 4, '🐢': 5, '👨🏽\u200d🔬': 1, '👨🏽\u200d🏭': 9, '👮🏿': 11, '🙆': 17, '🦃': 7, '🙇🏻': 24, '\U0001f90d': 15, '🕳': 13, '🏬': 3, '💞': 8, '🦁': 6, '👏🏽': 21, '🕑': 23, '5⃣': 14, '⬜': 0, '🍄': 19, '🇩🇰': 20, '⛏': 10, '🇬🇭': 18}

new_size = 3

param = 0

id = 0

time.sleep(5)

while 1:
    if param == 1:
        old_size = new_size
        s4 = s3

        # # print(s3[3][0])
        # if s3[2][17] == 'b':
        #     best = 1
        # else:
        #     best = 0
        #
        # check = 1
        # for i in range(3, len(s3)):
        #     if dict.get(s3[i][2:len(s3[i])]) == None:
        #         dict[s3[i][2:len(s3[i])]] = count
        #         print('count = ', count)
        #         count += 1
        #         check = 0
        #
        #
        # # print('write down 1 for best 0 for worst:')
        #
        # # best = int(sys.stdin.read(1))
        #
        # # number = sys.stdin.read(1)
        #
        # if check == 1:
        #     if best == 1:
        #         print('you better choose', end=' ')
        #         max = 0
        #         for i in range(3, len(s3)):
        #             if dict[s3[i][2:len(s3[i])]] > max:
        #                 max = dict[s3[i][2:len(s3[i])]]
        #                 id = i
        #         print(id-2)
        #     else:
        #         print('you better choose', end=' ')
        #         min = 10000
        #         for i in range(3, len(s3)):
        #             if dict[s3[i][2:len(s3[i])]] < min:
        #                 min = dict[s3[i][2:len(s3[i])]]
        #                 id = i
        #         print(id - 2)
        #     id2 = id - 2

        # print('write down which emoji(number):')

        # number = sys.stdin.read(1)

        # number = int(sys.stdin.read(1))

        # print(number)

        # print('lol', dict)




        # number = sys.stdin.read(1)

            # print(s3[i][2:len(s3[i])])

    copy_and_paste_to_python()
    time.sleep(0.3)
    pyautogui.typewrite('v')
    time.sleep(0.3)
    pyautogui.press('enter')

    ss = ''
    s2 = sys.stdin.read(1)
    while s2 != 'v':
        # print(s2, end=' ')
        ss += s2
        s2 = sys.stdin.read(1)



    # print(s2)
    s3 = ss.split('\n')
    if s3[0] == '':
        s3.pop(0)
    print(s3)
    new_size = len(s3) - 3


    if param == 1:
        time.sleep(1)
        number = right_number(old_size, new_size)
        print('number=', number)

        if s4[2][17] == 'b':
            best = 1
        else:
            best = 0

        if best == 1:
            max = -1
            for i in range(3, len(s4)):
                if dict[s4[i][2:len(s4[i])]] > max:
                    max = dict[s4[i][2:len(s4[i])]]
                    id = i

            # print('1:', dict[s3[2 + number][2:len(s3[2 + number])]], '2:', max)
            temp = dict[s4[2 + number][2:len(s4[2 + number])]]
            dict[s4[2 + number][2:len(s4[2 + number])]] = max
            dict[s4[id][2:len(s4[id])]] = temp

        else:
            min = 10000
            for i in range(3, len(s4)):
                if dict[s4[i][2:len(s4[i])]] < min:
                    min = dict[s4[i][2:len(s4[i])]]
                    id = i
            # print('1:', dict[s3[2 + number][2:len(s3[2 + number])]], s3[2 + number][2:len(s3[2 + number])],  '2:', min, id)
            temp = dict[s4[2 + number][2:len(s4[2 + number])]]
            dict[s4[2 + number][2:len(s4[2 + number])]] = min
            dict[s4[id][2:len(s4[id])]] = temp



        if s3[2][17] == 'b':
            best = 1
        else:
            best = 0

        check = 1
        for i in range(3, len(s3)):
            if dict.get(s3[i][2:len(s3[i])]) == None:
                dict[s3[i][2:len(s3[i])]] = count
                print('count = ', count)
                count += 1
                check = 0


        # print('write down 1 for best 0 for worst:')

        # best = int(sys.stdin.read(1))

        # number = sys.stdin.read(1)

        if check == 1:
            if best == 1:
                print('you better choose', end=' ')
                max = 0
                for i in range(3, len(s3)):
                    if dict[s3[i][2:len(s3[i])]] > max:
                        max = dict[s3[i][2:len(s3[i])]]
                        id = i
                print(id-2)
            else:
                print('you better choose', end=' ')
                min = 10000
                for i in range(3, len(s3)):
                    if dict[s3[i][2:len(s3[i])]] < min:
                        min = dict[s3[i][2:len(s3[i])]]
                        id = i
                print(id - 2)
            id2 = id - 2





    if id2 == 0:
        pyautogui.moveTo(309, 946, 0.1)
        pyautogui.click()
    else:
        print('new_size=', new_size, 'id-2=', id2)
        click_on(new_size, id2)

    param = 1


    print(dict)

    pyautogui.moveTo(354, 968, 0.01)

    time1 = time.time()
    time2 = time.time()
    while get_pixel_colour(354, 968) <= 60:
        time.sleep(0.1)
        time2 = time.time()
        if time2 - time1 > 20:
            pyautogui.moveTo(348, 1018, 0.1)
            pyautogui.click()
            pyautogui.typewrite('/start')
            time.sleep(0.1)
            pyautogui.press('enter')
            s3 = []
            s4 = []
            count = 0
            id2 = 0
            ss = ''
            new_size = 3
            param = 0
            id = 0
            break


    time.sleep(1)


