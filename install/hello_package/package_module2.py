'''
Created on 2016/06/24

@author: tody4
'''

import time

start_time = time.time()

# 計算時間がかかる処理
for i in range(100000):
    print(i)

elapsed_time = time.time() - start_time
print ("elapsed time: %3f [sec]" % elapsed_time)
