import sys
from time_calc import Time

print ("Time Calc v1")
print ("============")

times = sys.argv[1:]

start_act1 = Time(times[0])
end_act1 = Time(times[1])
end_act1.subtract(start_act1)
act1 = str(end_act1)

start_im = Time(times[1])
end_im = Time(times[2])
end_im.subtract(start_im)
im = str(end_im)

start_act2 = Time(times[2])
end_act2 = Time(times[3])
end_act2.subtract(start_act2)
act2 = str(end_act2)

runtimes = [end_act1, end_im, end_act2]

def add_times(times_array):
    total = Time()
    for time_obj in times_array:
        total.add(time_obj)
    return total

playtimes = runtimes.copy()
intermission = playtimes.pop(1)

# Durations

print("Act I:\t\t {}".format(act1))
print("Intermission:\t {}".format(im))
print("Act II:\t\t {}".format(act2))

print ("------------")

# Play Time

playtime = add_times(playtimes)
print("Play Time:\t {}".format(playtime))

# Run Time

runtime = add_times(runtimes)
print("Run Time:\t {}".format(runtime))

print ("============")
