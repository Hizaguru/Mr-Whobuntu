import pyautogui as pt
from time import sleep
import random

from tinder_bot import Tinder

print("Starting Tinder bot")
sleep(3)

heart_swipes = 0
x_swipes = 0

tn = Tinder(0, 0)

for number in range(5):
    random_number = random.randrange(1, 5)
    random_number_swipe = random.randrange(10)

    # Performs simulated Tinder Swipe
    tn.navigate_to_next_pic(.3)
    pt.click(clicks=random_number, interval=.3)
    sleep(2)
    tn.navigate_to_down_arrow(.3)
    pt.click()


    # swipe away rate = 1/10
    if random_number_swipe <= 5:
        tn.navigate_to_x_button(.3)
        pt.click()

        x_swipes += 1

    else:
        tn.navigate_to_like_button(.3)
        pt.click()

        heart_swipes += 1

        print(f"""--------------
        Total swipes:
        Heart = {heart_swipes}
        X = {x_swipes}""")
        sleep(random_number)

