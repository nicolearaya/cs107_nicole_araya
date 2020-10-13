import numpy
import matplotlib.pyplot as plt
import math
import datetime

### Closure defined up here
def r_closure(r):
    def coordinates(theta):
        radians = math.pi/180*theta
        x = r*math.cos(radians)
        y = r*math.sin(radians)
        c = [x, y]
        return c
    return coordinates
currentDT = datetime.datetime.now()

#ensure these inputs are floats
hour = float(currentDT.hour)
minute = float(currentDT.minute)
second = float(currentDT.second)

# Calculate theta in degrees for each hand

theta_h = 90 - 30*hour - minute/2
theta_m = 90 - 6*minute
theta_s = 90 - 6*second

#take in size of hour hand

hour_w = 4
minute_w = 2
second_w = 1


# Specify the length of hour, minute and second hands

hour_r = float(20)
minute_r = float(40)
second_r = float(60)

# hour_hand = name_of_closure(length_of_hour_hand)

hour_hand = r_closure(hour_r)
minute_hand = r_closure(minute_r)
second_hand = r_closure(second_r)

# x_hour, y_hour = hour_hand(theta_hour)

h_coord = hour_hand(theta_h)
m_coord = minute_hand(theta_m)
s_coord = second_hand(theta_s)
# Plot the clock

x_hour = [0, h_coord[0]]
y_hour = [0, h_coord[1]]

x_minute = [0, m_coord[0]]
y_minute = [0, m_coord[1]]

x_second = [0, s_coord[0]]
y_second = [0, s_coord[1]]

plt.xlim(-100,100)
plt.ylim(-100,100)
plt.plot(x_hour, y_hour, linewidth = hour_w)
plt.plot(x_minute, y_minute, linewidth = minute_w)
plt.plot(x_second, y_second, linewidth = second_w)
plt.show()


