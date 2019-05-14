#멀티덱스일 경우?
#apk들 전부 한 경로에 unzip
#폴더명이 이미지명
#라벨링도 해줘야함

import os, sys, io
import time
import PIL
from PIL import Image

tmp_str = ""
path = 'C:/Users/jysrm/OneDrive/바탕 화면/study/androguard/'
file_name = 'new.txt'

androguard_output = open(path + file_name,'r')
# for lines in dump_output.readlines():
# 	if lines.startswith('CODEITEMS_BYTECODE'):
# 		tl = lines.split(' : ')[1].replace('\n','')
# 		tl = tl.split('  ')[0]
# 		tl = tl.split('du')[0]

# 		while len(tl) %8 != 0:
# 			tl+='0'
# 		tmp_str += tl
tt = androguard_output.read()
# print(tt)
# print(type(tt))
b = int(tt,16)

photo_image = PIL.Image.frombytes('P', (299, 299), b.to_bytes(int(len(tt)/2), sys.byteorder))
photo_image.save(path + file_name+'_img.png')

# photo_infile = io.StringIO(str(b.to_bytes(int(len(tmp_str)/2), sys.byteorder)))
# photo_data = b.to_bytes(int(len(tmp_str)/2), sys.byteorder)
# f = open(path + 'hextodec_output.dex','wb')
# f.write(b.to_bytes(int(len(tmp_str)/2), sys.byteorder))
# f.close()

# f = open(path + 'hextodec_output.dex','r', encoding = 'ISO-8859-1')
# for_image = f.read()
# photo_data = for_image
# photo_infile = io.StringIO(photo_data)
# photo_image = PIL.Image.frombytes('P', (500, 500), b.to_bytes(int(len(tmp_str)/2), sys.byteorder))
# print(type(photo_image))
# photo_image.save("C:/Users/hacke/Desktop/for_codeitem/codeitem/qweqwe.png")

androguard_output.close()