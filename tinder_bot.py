from time import sleep
import pyautogui as cursor
import random
#Tinder bot for Tinder in web browser

class Tinder:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def navigate_to_like_button(self, speed):
        try:
            position = cursor.locateOnScreen("images/heart.png", confidence=.8)
            self.x = position[0] + random.randint(15, 20)
            self.y = position[1] + random.randint(15, 20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to black heart")
        except TypeError:
            position = cursor.locateOnScreen("images/black_heart.png", confidence=.8)
            self.x = position[0] + random.randint(15,20)
            self.y = position[1] + random.randint(15,20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to heart")
        finally:
            sleep(random.uniform(.3, 1))


    def navigate_to_x_button(self, speed):
        try:
            position = cursor.locateOnScreen("images/x.png", confidence=.8)
            self.x = position[0] + random.randint(15, 20)
            self.y = position[1] + random.randint(15, 20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to X button")
        except TypeError:
            position = cursor.locateOnScreen("images/black_x.png", confidence=.8)
            self.x = position[0] + random.randint(15,20)
            self.y = position[1] + random.randint(15,20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to dark x button")
        finally:
            sleep(random.uniform(.3, 1))


    def navigate_to_down_arrow(self, speed):
        try:
            position = cursor.locateOnScreen("images/down_arrow.png", confidence=.8)
            self.x = position[0] + random.randint(15, 20)
            self.y = position[1] + random.randint(15, 20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to down array")
        except TypeError:
            position = cursor.locateOnScreen("images/info_logo.png", confidence=.7)
            self.x = position[0] + 10
            self.y = position[1] + 10
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to dark info logo")
        finally:
            sleep(random.uniform(.3, 1))

    def navigate_to_superlike(self, speed):
        try:
            position = cursor.locateOnScreen("images/superlike.png", confidence=.8)
            self.x = position[0] + random.randint(15, 20)
            self.y = position[1] + random.randint(15, 20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to superlike")
        except TypeError:
            position = cursor.locateOnScreen("images/black_superlike.png", confidence=.8)
            self.x = position[0] + random.randint(15,20)
            self.y = position[1] + random.randint(15,20)
            cursor.moveTo(self.x, self.y, duration=speed)
            print("Navigating to dark superlike")
        finally:
            sleep(random.uniform(.3, 1))


    def navigate_to_next_pic(self, speed):
        position = cursor.locateOnScreen("images/black_superlike.png", confidence=.8)
        self.x = position[0] + random.randint(150,200)
        self.y = position[1] - random.randint(250, 300)
        cursor.moveTo(self.x, self.y, duration=speed)
        print("Navigating to next pic")
        sleep(random.uniform(.3, 1))

sleep(2)
tn = Tinder(0, 0)
