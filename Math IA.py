import numpy as np

def eval_line(line1_eq, b2):
    def line1(x):
        return 5*x + initial_velocity 
    def line2(x):
        return -8 * x + b2
    return line1, line2

initial_velocity = float(input("Enter initial velocity: "))
exit_velocity = float(input("Enter exit velocity: "))

x_values = np.linspace(0, exit_velocity, 10000)

b2 = 100


Area = float(input('Enter the Area: '))
print("calculating...")

def find_intersection(m1, b1, m2, b2):
    if m1 == m2:
        print("Lines are parallel. No intersection point.")
        return None

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    return x, y


while True:
    line1, line2 = eval_line(initial_velocity, b2)
    absolute_difference = np.abs(line1(x_values) - line2(x_values))

    condition = line1(x_values) > line2(x_values)
    area = np.trapz(absolute_difference[condition], x=x_values[condition])

    if abs(area - Area) < 0.001:
        intersection = find_intersection(5, initial_velocity, -8, b2)
        i, j = intersection
        if j>17:
            b2 -= 0.001
        else:
            print("Intersection coordinates:", intersection)
            time_value = (3 - b2) / -8
            print("Time Taken: " + str(time_value))
            break
    else:
        b2 -= 0.001
    
    if b2<-50:
        print('no value found')
        break