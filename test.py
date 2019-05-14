from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.bytecodes.dvm import ClassDefItem
import sys

a = APK("C:/Users/jysrm/OneDrive/바탕 화면/study/test.apk")
# sys.stdout = open('./code_item.txt', 'w')
f = open("new.txt", 'w')

d = DalvikVMFormat(a)

code_item = d.get_codes_item()

code = code_item.show()

print(len((code)))
f.write(code)

f.close()