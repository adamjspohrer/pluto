# pluto.py
# My brother Steven and father Jim collaborated buiding this program
# I modified the output - to print the vector and return the string "Done"

# === import random.py and statistics.py
import random
import statistics


# === initialize temperatures in a vector that represents n layers of pluto's surface
# === the top is temp_low, the bottom is temp_high, and smooth gradient between
# === note: n > 2 (n must be greater than 2, since first layer is temp_low constant, and last layer is temp_high constant)
# === test case
# >>> init_temp(10,40,45)
# [40, 40.553479088950986, 41.10695817790197, 41.66140886865191, 42.21585955940185, 42.77179883047424, 43.32773810154663, 43.88498640818992, 44.442234714833205, 45]
def init_temp(n,temp_low,temp_high):
    "init_temp = return a vector of size n, with smooth temperature gradient from temp_low to temp_high"

    # initialize vector x of size n to temp_low
    x = []
    for i in range(0,n):
        x = x + [temp_low]
    x[n-1] = temp_high # set last (deepest) layer to temp_high


    # intialize another vector of size n to hold intermediate calculations
    y = []
    for j in range(0,n):
        y = y + [0]

    # 100 diffusion steps, by averaging adjacent layers
    for i in range(0,100):
        for j in range(1,n-1):
            y[j] = (x[j-1] + x[j+1])/2.0
        for j in range(1,n-1):
            x[j]=y[j]

    print(x) # Adam modification
    
    return("Done") # Adam modification

# === initialize probability of absorption in a vector that represents n layers of pluto's surface
# === transmission coefficient is a probability between 0 and 100 percent
# === test case
# >>> init_absorb(10,80)
# [0, 120, 99, 75, 76, 62, 48, 34, 28, 0]
def init_absorb(n,transmission_coeff):
    "init_absorb = return a vector of size n, with probability of absorption of incident radiation, given a transmission co-efficient"

    # default reflection and absorbtion coefficients
    reflect_coeff = absorb_coeff = (100.0 - transmission_coeff)/2.0
    
    # initialize vector x of size n to zero
    x = []
    for i in range(0,n):
        x = x + [0]

    # 1000 incident radiation experiments - increment the layer that absorbs it
    for i in range(0,1000):
        absorbed = False
        direction = 1 # 1 = down, -1 = up
        layer = 1
        while (not absorbed):
            # roll dice to see if transmitted
            p = random.uniform(0,100)
            if p <= transmission_coeff:
                layer = layer + direction
            elif p <= transmission_coeff + reflect_coeff:
                direction = -1*direction
                layer = layer + direction
            else:
                x[layer] = x[layer] + 1
                absorbed = True
                
            # going to high or too low, same as being absorbed - but with no temp change impact
            if (layer == 0) or (layer == n-1):
                absorbed = True

    return(x)

