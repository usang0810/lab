import sys, os
import zipfile
import shutil
import math
import time

path_googleplay = 'G:/dataset_share/apks/csos_crawl-nodup-vt/googleplay/'

for (p,d,f) in os.walk(path_googleplay):
    print(p)
    print(d)



    # for dir_name in d:
    #     full_dir = os.path.join(p, dir_name)
    #     filenames = os.listdir(full_dir)
    #     for filename in filenames:
    #         full_path = os.path.join(full_dir, filename)
    #         print(full_path)
    #         time.sleep(1)
        #print(full_dir)
        

    for filename in f:
        full_filename = os.path.join(p, filename)
        print(full_filename)
        #time.sleep(1)

    



    

    