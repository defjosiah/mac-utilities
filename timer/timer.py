import time
import sys
import os

def start_timer(minutes):
    wd = os.path.dirname(os.path.realpath(__file__))
    for x in xrange(minutes):
        time.sleep(60)
        print x+1
    os.system("osascript {0}".format(os.path.join(wd, "playpause.applescript")))
    os.system("say timer finished")
    os.system("osascript -e \'display notification \"Timer Finished\" with title \"Timer\"\'")
    return

if __name__ == '__main__':
    start_timer(int(sys.argv[1]))

