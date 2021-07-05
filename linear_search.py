# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:33:00 2020

@author: fatih
"""
import time

def search(arr,aranan):
    for x in arr:
        if x==aranan:
            return 1
    return -1

start_time = time.time()

aranan=9999999

arr=[x for x in range(10000000)]

result=search(arr, aranan)

if result==1:
    print("Değer bulundu")
    print("--- %s saniye ---" % (time.time() - start_time))
else:
    print("Değer bulunamadı.")
    print("--- %s saniye ---" % (time.time() - start_time))