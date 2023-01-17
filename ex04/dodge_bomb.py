import pygame as pg
import random
import sys
import time

def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate



#ゲーム自体を関数化
def nigerokouka():
    clock =pg.time.Clock()
        # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 


    #1つめの爆弾生成 bomb
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 

    #2つめの爆弾生成 bomb2
    bomb2_sfc = pg.Surface((80, 80)) # 正方形の空のSurface
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0), (40, 40), 40)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb2_sfc, bomb2_rct) 

    vx, vy = +1, +1
    dx, dy = +1, +1
    
    #ゲーム開始時に待機時間を設ける
    pg.time.wait(1000)

    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 

        #爆弾１つ目生成
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        #爆弾２つめ生成
        bomb2_rct.move_ip(dx, dy)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) 
        yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
        dx *= yoko2
        dy *= tate2

        

        #練習8
        if tori_rct.colliderect(bomb_rct):
            return
        if tori_rct.colliderect(bomb2_rct):
            return

        pg.display.update()
        clock.tick(1000000)

#スタート画面生成用関数を呼び出す
def makestart():
    #スタート画面の作成
    start = pg.display.set_mode((200,200))
    pg.display.set_caption("Start Window")

    #ゲームスタート用ボタンの作成
    button = pg.Rect(30,50,140,100)

    #フォントの用意
    font = pg.font.SysFont(None,50)

    #テキストの設定
    text = font.render("Start",True,(0,0,0))

    return start,button,text
def main():
    
    start,button,text = makestart() #スタート画面生成用関数を呼び出す
    while (1):
        start.fill((0,0,0)) #画面を黒く塗る

        #ボタンの設置
        pg.draw.rect(start,(255,0,0),button)
        #ボタンに文字を乗せる
        start.blit(text,(60,85))

        pg.display.update()

        #バツが押されたら閉じる
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            #スタートボタンが押されたらゲームを起動
            if event.type == pg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    nigerokouka() #ゲームを起動
                    start,button,text = makestart() #ゲーム終了後にスタート画面の表示が崩れる為、リセットする
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()