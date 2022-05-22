
# python -m auto_py_to_exe
# in command prompt

# @ProughCait

import random
import turtle
import datetime
import tweepy
import time
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from easygui import *
from PIL import Image, ImageDraw

# authorize to tweet
consumer_key = 'yvm5g0dk7LfP9iXQdgRjSLaTZ'
consumer_secret_key = 'BwoMmm3RmugkS0ppSl6aBw2v8aaij3fl2GKstpulBrD7TSJzT0'
access_token = '1421127678514638850-ZhNiNfRpFzyo3E8ponpq3WbLnVGkgX'
access_token_secret = 'hOqPLbZKydEz8oUw4gDsyoIAizux3K05EGi8htIYpTz6L'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# starts all necessary screens/information
turtle.colormode(255)
sc = turtle.Screen()
sc.setup(400,400)
round_number = 0
running_total = 0
d = datetime.now()
only_date = d.date()
only_date

text_file = open("RGB COLOR SCORES.txt", "a")
n = text_file.write(f"Date:{only_date}\n")

def again():
    # print(con)
    con = turtle.textinput("title", "(y/n)Continue?")

    if con == "y":
        play()
    else:
        exit

def play():
    # create color
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    color = (red,green,blue)
    
    # creates hex code of original color
    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb

    hex_color = (rgb_to_hex(color))

    # turtle.colormode(255)# sc = turtle.Screen()# sc.setup(400,400)# turtle.clear()
    turtle.clear()
    turtle.bgcolor((color))

    # redi = int(input("red:"))# greeni = int(input("green:"))# bluei = int(input("blue:"))

    #color guess input
    redi = turtle.numinput("RED","Red: ",0,minval=0,maxval=255)
    greeni = turtle.numinput("GREEN","Green: ",0,minval=0,maxval=255)
    bluei = turtle.numinput("BLUE","Blue: ",0,minval=0,maxval=255)

    # redi = turtle.numinput("RED","Red: ",0,minval=0,maxval=255)
    # greeni = turtle.numinput("GREEN","Green: ",0,minval=0,maxval=255)
    # bluei = turtle.numinput("BLUE","Blue: ",0,minval=0,maxval=255)
    
    # get percentage close per color
    def compare(a,b):
        if a == b:
            print(100)
            return 1.0
        else:
            dif = abs(a-b)
            div2 = 255-dif
            rou= div2/255
            per= round(rou, 3)
            print(per)
            return per

    # percentages of each color
    redper = compare(red,redi)
    greenper = compare(green,greeni)
    blueper = compare(blue,bluei)

    finalper = (redper+greenper+blueper)/3
    final_round = round(finalper, 3)
    # print("score:", final_round)
    
    color1 = (int(redi),int(greeni),int(bluei))

    # draw cirle of guessed color
    def circle(x,y):
        turtle.color((y))
        turtle.width(5)
        turtle.begin_fill()
        turtle.circle(x)
        turtle.end_fill()  

    circle(50,color1)

    # print("Color:", color) # print("Guess:", color1)

    # round number/ running total
    global round_number
    print(" ")
    round_number += 1
    if round_number == 1:
        print("you have played 1 round")
    else:
        print("you have played", round_number, "rounds")

    global running_total
    if round_number == 1:
        running_total = final_round

    if round_number >= 2:
        running_total = round((running_total + final_round)/2,2)


    #displays in popup
    messagebox.showinfo("Scores", f"Round number: {round_number}\nRound Score: {final_round}\nColor: {color}\nHex Color: {hex_color}\nGuess: {color1}\nRunning Total: {running_total}\n")

    # writes into text file for safe keeping
    n = text_file.write(" \n")
    n = text_file.write(str(f"Round Number: {round_number}\n"))
    n = text_file.write(str(f"Round Score: {final_round}\n"))
    n = text_file.write(str(f"Color: {color}\n"))
    n = text_file.write(str(f"Hex Color: {hex_color}\n"))
    n = text_file.write(str(f"Guess: {color1}\n"))
    n = text_file.write(str(f"Running Total: {running_total}\n"))
    n = text_file.write("-\n")
    
 
    def color_image(color_rgb):
        image = Image.new('RGB', (800, 500), color=(color_rgb))
        d = ImageDraw.Draw(image)

        image.save('color_image.png')


    def tweet(x,y):
        
        color_image(x)
    
        media = api.media_upload("color_image.png")

        api.update_status(f'{x} / {y}', media_ids=[media.media_id])

    tweet(color, hex_color)

    again()

play()
print(">")
text_file.close()
