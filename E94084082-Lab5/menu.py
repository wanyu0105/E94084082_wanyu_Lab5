import pygame
import os

# 匯入圖片並調整為適當的大小
MENU_IMAGE = pygame.image.load("./images/upgrade_menu.png")
UPGRADE_IMAGE = pygame.transform.scale(pygame.image.load("./images/upgrade.png"), (60, 30))
SELL_IMAGE = pygame.transform.scale(pygame.image.load("./images/sell.png"), (45, 45))

class UpgradeMenu:
    def __init__(self, x, y):
        # 調整 menu image 的大小
        self.menu_image = pygame.transform.scale(MENU_IMAGE, (200, 200))
        # 利用 get_rect() 獲取矩形圖像 menu image 的 area
        self.rect = self.menu_image.get_rect()
        # 設置該 area 的中心座標
        self.rect.center = (x, y)
        # 創建 upgrade和 sell buttons的 list，其中各元素的內容則利用"Button"這個 clss來宣告
        self.__buttons = [Button(UPGRADE_IMAGE, "upgrade", self.rect.centerx, self.rect.centery-75),
                          Button(SELL_IMAGE, "sell", self.rect.centerx, self.rect.centery+75)] 
        # 設置 menu,upgrade,sell圖片左上角的座標位置
        self.menu_x , self.menu_y = self.rect.centerx-100 , self.rect.centery-100
        self.updrade_btn_x , self.updrade_btn_y = self.rect.centerx-30 , self.rect.centery-85
        self.sell_btn_x , self.sell_btn_y = self.rect.centerx-20 , self.rect.centery+50

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image,(self.menu_x , self.menu_y))
        # draw button
        win.blit(UPGRADE_IMAGE,(self.updrade_btn_x , self.updrade_btn_y))
        win.blit(SELL_IMAGE,(self.sell_btn_x , self.sell_btn_y))
        # (Q2) Draw buttons here
        

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        # 宣告圖像的名字("upgrade"或"sell")
        self.name = name 
        # 利用 get_rect() 獲取矩形圖像(upgrade或sell)的 area
        self.rect = image.get_rect()
        # 設置該 area 的中心座標
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """ 
        # 判斷滑鼠點選的位置是否有在 button 的矩形範圍內
        if(self.rect.collidepoint(x, y) == True):
            return True
        else:
            False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        # 回傳被按到的 button的屬性"name"("upgrade"或"sell")
        return self.name






