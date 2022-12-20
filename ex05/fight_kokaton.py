import pygame as pg
import random
import sys



class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        

    def update(self, scr:Screen):
        

        #ここから下がもともとあったやつ
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)  
                


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

#追加クラス
class Wakiyakukokaton: #敵こうかとんを出現させる
    def __init__(self, img_path, ratio, vxy, scr:Screen):

        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)




def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()

    # 練習１
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/6.png", 1.5, (900,400)) 
    kkt.update(scr)

    #追加機能 敵こうかとん
    ene = Wakiyakukokaton("fig/1.png",3.0,(+1, +1),scr)
    ene.update(scr)

    # 練習５
    bkd_lst = [] #食べられる爆弾のリスト
    bkd_num = 20 #食べられる爆弾の数
    for i in range(bkd_num):
        bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
        bkd_lst.append(bkd)

    no_eat_lst = [] #食べられない爆弾のリスト
    for i in range(2):
        noeatbkd = Bomb((50,50,50),18,(+1,+1),scr)
        no_eat_lst.append(noeatbkd)

    

    # 練習２
    while True:        
        scr.blit()

        list_len = len(bkd_lst)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        ene.update(scr)

        #食べられない爆弾の当たり判定
        for i in range(2):
            no_eat_lst[i].update(scr)
            if kkt.rct.colliderect(no_eat_lst[i].rct):
                return

        #食べられる爆弾に関わる処理
        for i in range(list_len):
            bkd_lst[i].update(scr)
            if kkt.rct.colliderect(bkd_lst[i].rct):
                #こうかとんが爆弾を食べる
                bkd_lst.pop(i) #衝突判定を受けた爆弾をリストから削除
                list_len -= 1 #リストの長さが１減る
                if (list_len == 0):
                    return #爆弾を全て食べ終えたらゲーム終了
                break #リストの長さが変わった状態でfor文が続くとエラーが起きる為ループから抜ける

        #敵こうかとんの接触判定            
        if kkt.rct.colliderect(ene.rct):
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()