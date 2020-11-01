# Один ход КБ
cb_speed = 170
me_speed = 306
# turn = 0


def prbar(spd):
    # s = v * t
    # cb_bar = cb_speed * time ; time = cb_bar / cb_speed   } time = time
    # me_bar = me_speed * time ; time = me_bar / me_speed   }
    # me_bar / me_speed = cb_bar / cb_speed
    # me_bar = (cb_bar / cb_speed) * me_speed ; cb_bar = (me_bar / me_speed) * cb_speed
    prbar_bar = prbar_cb_bar = 0
    for icb in range(1, cb_speed + 1):
        prbar_cb_bar = prbar_cb_bar + (1 / cb_speed)
        prbar_bar = (prbar_cb_bar / cb_speed) * spd
    prbar_cb_bar = round(prbar_cb_bar, 10)
    prbar_bar = round(prbar_bar, 10)
    return prbar_cb_bar, prbar_bar

bar0 = 0
bar1 = 0
for turn in range(0, 5):
    cb_bar, bar = prbar(250)
    bar0 = cb_bar + bar0
    bar1 = bar + bar1

    # if bar1 >= 1:
    #     bar1 = bar1 - 1
    #     print('---turn1---bar1:', bar1)



    print('CB_Turn: {}, CB_bar {}, ME_bar {}'.format(turn, bar0, bar1))
    turn = turn + 1

