import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに文字列表示
    scrn_sfc = pg.display.set_mode((1600,900)) #800x600の画面surfaceを生成

    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()