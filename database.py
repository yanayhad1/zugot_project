import pandas
import pygame
import time
import consts
import main
import soldier


def check_time():
    start = time.time()



def write_data_in_base(data):
    output = pandas.DataFrame()
    data_base = pandas.DataFrame([data])
    output = pandas.concat([pygame.KEYDOWN[0], data_base])
    output.to_csv(consts.DATABASE_NAME)


def decide_read_or_write(time_pressed):
    print(time_pressed)
    if time_pressed > 2:
        print("here")#write_data_in_base()
    else:
        print("here2")


