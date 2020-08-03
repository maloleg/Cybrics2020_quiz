Just answer 100 simple questions in the row about emojis and you will get the flag, this is quite easy lol

![1](1.png)

ok, now jokes aside

We will use lovely pyautogui just because we don't know how to use telegram api and you know, we wont be stuffy.

Bot want's us to make a "top" of emojis - so we need to determine it we will use dictionary in python (or a map if you are more C++ alike guy)

So we will define what bot want's us: best or worst emoji:

~~~
if s3[2][17] == 'b':
            best = 1
        else:
            best = 0
~~~

where s3 - string from message with 'best' or 'worst' phrase

so then depending on ansvers should constantly recorrecting our dict just by changing places of correct answer with something in the list of given by the bot emojis:

~~~
if best == 1:
            max = -1
            for i in range(3, len(s4)):
                if dict[s4[i][2:len(s4[i])]] > max:
                    max = dict[s4[i][2:len(s4[i])]]
                    id = i

            temp = dict[s4[2 + number][2:len(s4[2 + number])]]
            dict[s4[2 + number][2:len(s4[2 + number])]] = max
            dict[s4[id][2:len(s4[id])]] = temp

        else:
            min = 10000
            for i in range(3, len(s4)):
                if dict[s4[i][2:len(s4[i])]] < min:
                    min = dict[s4[i][2:len(s4[i])]]
                    id = i
            temp = dict[s4[2 + number][2:len(s4[2 + number])]]
            dict[s4[2 + number][2:len(s4[2 + number])]] = min
            dict[s4[id][2:len(s4[id])]] = temp
~~~

and we also need to check what is best possible emoji according to our already collected data:

~~~
for i in range(3, len(s3)):
            if dict.get(s3[i][2:len(s3[i])]) == None:
                dict[s3[i][2:len(s3[i])]] = count
                print('count = ', count)
                count += 1
                check = 0
                
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
~~~


and the final thing: we need to check what answer was right, i did a function like that for it:

~~~
def right_number(up_amount, down_amount):
    a = [[907, 945], [869, 908, 944], [832, 870, 907, 945], [793, 831, 869, 908, 945]]
    b = [177, 215, 253, 291]                                                           #those lists of pixels are just for my position of telegram client
    result = 0

    for i in range(up_amount):
        # print(a[up_amount-2][i] - b[down_amount-2])
        # print(up_amount-2, i)
        pyautogui.moveTo(309, a[up_amount-2][i] - b[down_amount-2], 0.1)
        if get_pixel_colour(pyautogui.position().x, pyautogui.position().y) > 205 and get_pixel_colour(pyautogui.position().x, pyautogui.position().y) < 225:
            result = i + 1
            break
    return result
~~~

And we also need to click on emojis, check RGB of pixels, copy text of messages and so on:

~~~
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
    
def click_on(amount, number):
    a = [[907, 945], [869, 908, 944], [832, 870, 907, 945], [793, 831, 869, 908, 945]]
    pyautogui.moveTo(309, a[amount - 2][number - 1], 0.1)
    pyautogui.click()
    
~~~

oh and bot sometimes stops working, so i did check on it as well to restart it:

~~~
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
~~~

![look at this beauty and say if using telegram api is better :)](2.gif)

so after all work and about an our of wathing it answering questions and learning we got our leet flag: cybrics{AL13N5_L0v3_5m1l35_AnD_3M0J132}

Full python script is on this github repository
