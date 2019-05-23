from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.bytecodes.dvm import ClassDefItem
import os, sys, io
import time
import PIL
from PIL import Image

def make_img(dirname, img_path):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:

            try:
                full_filename = os.path.join(dirname, filename)
                if os.path.isdir(full_filename):
                    make_img(full_filename, img_path)
                else:
                    file_split = os.path.splitext(full_filename)
                    if file_split[1] == '.apk':
                        apk = APK(full_filename)
                        dalvik = DalvikVMFormat(apk)

                        code_item = dalvik.get_codes_item()
                        code_item_str = code_item.show()

                        binary = int(code_item_str, 16)

                        photo_image = PIL.Image.frombytes('P', (100, 100), binary.to_bytes(int(len(code_item_str)/2), sys.byteorder))

                        split_name = os.path.splitext(filename)
                        full_img_path = img_path + split_name[0] + '.png'
                        print(full_img_path)
                        
                        photo_image.save(full_img_path)
                    else:
                        pass
            except:
                print("except error")

    except PermissionError:
        pass

dir_path = 'G:/dataset_share/images/drebin(mal)/'
filename = '000a067df9235aea987cd1e6b7768bcc1053e640b267c5b1f0deefc18be5dbe1.apk'
img_path = 'G:/dataset_share/androguard/drebin(mal)_img/'
apk_path = dir_path + filename

apk = APK(apk_path)
dalvik = DalvikVMFormat(apk)

code_item = dalvik.get_codes_item()
code_item_str = code_item.show()

binary = int(code_item_str, 16)
cnt = 0

try:
    photo_image = PIL.Image.frombytes('P', (299, 299), binary.to_bytes(int(len(code_item_str)/2), sys.byteorder))
    
    img_name = filename.split('.')
    img_name = img_name[0] + '.png'
    
    photo_image.save(img_path + img_name)

except ValueError:
    cnt = cnt+1
    pass

print(cnt)