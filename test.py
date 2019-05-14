from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.bytecodes.dvm import ClassDefItem

a = APK("C:/Users/jysrm/OneDrive/바탕 화면/study/test.apk")
f = open("new.txt", 'w')

d = DalvikVMFormat(a)

code_item = d.get_codes_item()

code = code_item.show()

f.write(code)

f.close()