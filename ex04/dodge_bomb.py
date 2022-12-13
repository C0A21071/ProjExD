import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")#タイトルバーに「逃げろ！こうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1600,900))#800x600の画面surfacを生成する

    pgbg_sfc = pg.image.load("fig/pg_bg.png")#Surface
    pgbg_rct = pgbg_sfc.get_rect()#Rect
    pgbg_rct.center = 400,300
    #scrn_sfcにtori_rctに従って、tori_sfcを貼り付ける
    scrn_sfc.blit(pgbg_sfc,pgbg_rct)#blit
    pg.display.update()
    clock.tick(0.5)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()