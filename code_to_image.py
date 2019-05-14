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

                    photo_image = PIL.Image.frombytes('P', (299, 299), binary.to_bytes(int(len(code_item_str)/2), sys.byteorder))

                    split_name = os.path.splitext(filename)
                    full_img_path = img_path + split_name[0] + '.png'
                    print(full_img_path)
                    
                    photo_image.save(full_img_path)
                else:
                    pass

    except PermissionError:
        pass

dir_path = 'C:/Users/jysrm/OneDrive/바탕 화면/study/apk/benign'
file_list = os.listdir(dir_path)
img_path = 'C:/Users/jysrm/OneDrive/바탕 화면/study/apk/benign_img/'

make_img(dir_path, img_path)