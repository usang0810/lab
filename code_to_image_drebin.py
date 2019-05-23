from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.bytecodes.dvm import ClassDefItem
import os, sys, io
import time
import PIL
from PIL import Image
import math


def make_img(dirname, img_path):
    cnt = 0
    size = int()
    
    filenames = os.listdir(dirname)
    for filename in filenames[:]:
        cnt += 1
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            make_img(full_filename, img_path)
        else:
            file_split = os.path.splitext(full_filename)
            if file_split[1] == '.apk':
                try:
                    b = int()

                    apk = APK(full_filename)

                    dalvik = DalvikVMFormat(apk)

                    code_item = dalvik.get_codes_item()
                    code_item_str = code_item.show()

                    binary = int(code_item_str, 16)
                    size = int(((len(binary.to_bytes(int(len(code_item_str)/2), 'big')) // 8)))
                    size = int(math.sqrt(size))

                    photo_image = PIL.Image.frombytes('L', (size, size), binary.to_bytes(int(len(code_item_str)/2), 'big'))
                    split_name = os.path.splitext(filename)
                    full_img_path = img_path + split_name[0] + '.jpg'
                    print(full_img_path)
                    photo_image.save(full_img_path)

                except Exception as ex:
                    cnt -= 1
                    print(ex)
                    continue

            else:
                pass

    print("processed :",cnt)




dir_path = 'G:/dataset_share/images/drebin(apks)'
# file_list = os.listdir(dir_path)
img_path = 'G:/dataset_share/androguard/drebin(mal)_img/'

make_img(dir_path, img_path)
print("finish")