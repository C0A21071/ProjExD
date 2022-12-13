import pygame as pg
import sys

def main():#ここにゲームの処理をかく
    pg.display.set_caption("初めてのPygame") #タイトルバーに文字列表示
    scrn_sfc = pg.display.set_mode((800,600)) #800x600の画面surfaceを生成

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.enter = 400,300
    scrn_sfc.blit(tori_sfc,tori_rct) 

    pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()