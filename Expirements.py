from time import time
from AVL_tree import AVLTreeMap

import sys



def Hash_map_base_setTime(n):
    h = AVLTreeMap(10)
    start = time()
    for i in range(10):
        AVLTreeMap.__setitem__(h,4,5)
    end = time()
    fill_time = (end - start)/n

    return fill_time



try:
    maxM = int(sys.argv[1])
except:
    maxM = 10**12



m = 10
print()
print("Set Function")
print()
while m <= (maxM):
  print('Average of {0} for m {1}'.format(Hash_map_base_setTime(m), m))
  m *= 10
