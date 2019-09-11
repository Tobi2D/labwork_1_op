import math

k = int('4858450636189713423582095962494202044581400587983244549483093085061' + \
        '93470470880992845064476986552436484999724702491511911041160573917740785' + \
        '69197543265718554420572104457358836818298237541396343382251994521916512' + \
        '84348332905131193199953502413758765239264874613394906870130562295813219' + \
        '48111368533953556529085002387509285689269455597428154638651073004910672' + \
        '30589335860525440966643512653493636439571255656959368151843348576052669' + \
        '40161251266951421550539554519153785457525756590740540157929001765967965' + \
        '480064427829131488548259914721248506352686630476300')


def checkParams(x, y):
    isRightX = 0 <= x < 106
    isRightY = k <= y < k + 17

    if isRightX and isRightY:
        return True
    return False


def tapper(x, y):
    return 0.5 < math.floor(
        math.fmod(math.floor(y / 17) * (2 ** (-1 * math.floor(x) - math.fmod(math.floor(y), 2))), 2))


while True:
    x, y = input('Write param - x \n'), input('Write param - y \n')
    try:
        x, y = float(x), float(y)
        if checkParams(x, y):
            if tapper(x, y):
                print('x=', x, 'and y=', y, 'are on the Tappers chart')
            else:
                print('x=', x, 'and y=', y, "aren't on the Tappers chart")
            break
        else:
            print('You wrote wrong number(x or y, or both). Try again.')
    except ValueError:
        print('You wrote not a number. Try again.')

