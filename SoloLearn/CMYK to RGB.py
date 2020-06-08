def check(colors):
    chk = [0 <= x <= 1 for x in colors]
    return all(chk)


def calculate(data):
    rv = round(255 * (1 - data[0]) * (1 - data[-1]))
    gv = round(255 * (1 - data[1]) * (1 - data[-1]))
    bv = round(255 * (1 - data[2]) * (1 - data[-1]))
    return rv, gv, bv


try:
    cyan = float(input('Cyan'))
    magenta = float(input('Magenta'))
    yellow = float(input('yellow'))
    black = float(input('black'))
    cmyks = [cyan, magenta, yellow, black]
    assert check(cmyks)
    r, g, b = calculate(cmyks)
    print('{0},{1},{2}'.format(r, g, b))
except:
    print('Invalid color values!')
