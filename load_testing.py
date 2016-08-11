'''
This is an initial grouping of time mechanisms that can be used for testing, instead of a single spike
we can see possibly multiple spikes, and if the application is able to recover with multiple spikes.



control_time = run a section of code for a duration of time

control_time_interval = run section of code for duration but build in increments.

example:    testing web front ends and see what load is put on memory/cpu
            testing db with web front end or other network appliances


'''

import time


def control_time(duration):
    '''

    :param duration: minutes
    :return:
    '''
    snap_ahead = int(time.time() + 60 * duration)

    while True:
        snap_now = int(time.time())
        if snap_now < snap_ahead:
            print("blah " + str(snap_now))
            # <some code to run ? #

        else:
            break
    #
    print("outside of while")


def control_time_interval(duration, interval):
    '''

    :param duration: minutes
    :param interval: seconds
    :return:
    '''

    if isinstance(duration, int) and isinstance(interval, int):

        snap_ahead = int(time.time() + 60 * duration)
        incr = 1
        while True:
            snap_now = int(time.time())
            if snap_now < snap_ahead:
                print(str(incr) + "\t" + str(snap_now))
                incr += 1
                # <some code to run ? #
                time.sleep(interval)
            else:
                break
        #
        print("outside of while")
    else:
        print("Check <type> on duration or interval, should be <type> int")


#control_time(1)
control_time_interval(1,5)