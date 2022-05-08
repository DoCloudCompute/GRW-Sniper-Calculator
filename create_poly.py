'''
useless file now
'''

import numpy as np

lx = [0,300,400,500,600,700,800,900,1000]
ly = [538,559,581,604,626,655,677,723,769]

r = np.polyfit(lx, ly, 3)
[print(float(a)) for a in r]
