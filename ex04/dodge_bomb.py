import pygame as pg
import random
import sys

def check_bound(obj_rct,scrn_rct):
    #第1引数：こうかとんrectまたは爆弾rect
    #第２引数：スクリーンrect
    #範囲内：＋１/範囲外：-1
    yoko,tate = +1,+1
    if obj_rct.left < scrn_rct.left or scrn_rct.right < obj_rct.right:
        yoko =-1
    if obj_rct.top < scrn_rct.top or scrn_rct.bottom < obj_rct.bottom:
        tate =-1
    return yoko,tate

def main():
    clock =pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    bomb_sfc = pg.Surface((20,20))#正方形の空のSurface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    
    vx,vy = +1,+1

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            #F1,F2,F3キーを押すと爆弾の動く速さが変わる(ゲームの難易度変更)
            if event.type == pg.KEYDOWN and event.key == pg.K_F1:
                vx,vy = +2,+2
            if event.type == pg.KEYDOWN and event.key == pg.K_F2:
                vx,vy = +3,+3
            if event.type == pg.KEYDOWN and event.key == pg.K_F3:
                vx,vy = +4,+4
            #SPACEキーを押すと爆弾が止まる
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                vx,vy = +0,+0
        key_dct = pg.key.get_pressed() #辞書型
        #矢印キーか、wasdを押したときにこうかとんを移動させる
        if key_dct[pg.K_UP] or key_dct[pg.K_w]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN] or key_dct[pg.K_s]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT] or key_dct[pg.K_a]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT] or key_dct[pg.K_d]:
            tori_rct.centerx += 1

        if check_bound(tori_rct,scrn_rct) != (+1,+1):
            #こうかとんが画面からはみ出ないようにしている
            if key_dct[pg.K_UP] or key_dct[pg.K_w]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN] or key_dct[pg.K_s]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT] or key_dct[pg.K_a]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT] or key_dct[pg.K_d]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        bomb_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate

        if tori_rct.colliderect(bomb_rct):
            #return
            tori_sfc = pg.image.load("fig/9.png")
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        pg.display.update()
        clock.tick(1000)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()