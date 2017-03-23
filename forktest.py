# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:59:02 2017

@author: warat.pue
"""

from multiprocessing import Pool,Process
from job_query import get_rows
import time
import os
import csv

def even(x,results):
    time.sleep(10)
    b = open('even_'+str(x)+'_'+str(time.time())+'.csv', 'wb')
    a = csv.writer(b)
    a.writerow(['data',x])
    b.close()
   
    results = results + str(time.time())

def odd(x,results):
    time.sleep(10)
    b = open('odd_'+str(x)+'_'+str(time.time())+'.csv', 'wb')
    a = csv.writer(b)
    a.writerow(['data',x])
    b.close()
    results = results + str(time.time())
   

if __name__ == '__main__':
    start = time.time()
    print start
    pool = Pool(multiprocessing.cpu_count())
    datas = [1,2,3,4,5,6,7,8,9,10]
    results = []
    for data in datas:
        if data%2 == 0:
            print 'even'+ ' '+str(data)
            pid = pool.apply_async(even,(data,results))
            print str(time.time())
            #print pid.get(timeout=2) 
            #Process(target=even,args=(data,results)).start()
        else:
            print 'odd'+ ' '+str(data)
            pid = pool.apply_async(odd,(data,results))
            print str(time.time())
            #print pid.get(timeout=2) 
            #Process(target=odd,args=(data,results)).start()
    print results
    print 'finish'
            
    