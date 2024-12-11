import sys
from time_calc import Time

print ("Time Calc v1")
print ("------------")

runtimes = sys.argv[1:]

def add_times(times_array):
    total = Time()
    for string in times_array:
        time_obj = Time(string)
        total.add(time_obj)
    return total

playtimes = runtimes.copy()
intermission = playtimes.pop(1)

# Play Time

playtime = add_times(playtimes)
print("Play Time: {}".format(playtime))

# Run Time

runtime = add_times(runtimes)
print("Run Time: {}".format(runtime))

print ("------------")
