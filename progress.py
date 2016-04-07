from math import ceil
from time import sleep
import os

def print_progress_bar(finished_percent):
    fixed_space = 9

    tput_o = os.popen('tput cols').read()
    width = float(tput_o) - fixed_space

    finished_count = ceil(finished_percent*width/100)
    empty_count = width - finished_count

    finished = "#" * int(finished_count)
    empty = "-" * int(empty_count)

    print "\r[ {0}{1} ] {2}%".format(finished, empty, finished_percent)

def main():

    for count in range(100):
        print_progress_bar(count)
        sleep(0.05)

    for count in range(100):
        print_progress_bar(100-count)
        sleep(0.05)

if __name__=='__main__':
    main()
