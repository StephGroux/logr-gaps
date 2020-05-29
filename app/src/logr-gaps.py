import sys
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
logfile = (sys.argv[1])
f = open('/logs/' + logfile, 'r')
match = 'start processing'


def get_gaps(my_list, size):
    resized_l = my_list[-size:]
    resized_l.reverse()
    gaps = []
    while len(resized_l) > 1:
        gaps.append(resized_l[0:2][0] - resized_l[0:2][1])
        resized_l.pop(0)
    gaps.reverse()
    return gaps


def get_epochs(file):
    epochs = []
    for line in iter(file):
        if match in line:
            (d) = line.split(" ")[0]
            (t) = line.split(" ")[1]
            epoch = (d + " " + t + "+00:00")
            epoch = datetime.fromisoformat(epoch).timestamp()
            epochs.append(epoch)
    return epochs

#print(get_gaps(get_epochs(f), 10))


style = '-'
color = 'green'
plt.plot(get_gaps(get_epochs(f), 1400),
         linestyle=style, color=color, linewidth=1)
plt.ylabel('gaps (seconds)')
plt.xlabel('# of starts - could modify to timestamp ')
plt.title('logr processing gaps')
plt.show()
