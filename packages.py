import site
import sys
from pprint import pprint

# 添加到全局
site.addsitedir("/opt")
# 打印py用户环境
pprint(site.getsitepackages())
# '/home/lqc/.local/lib/python3.8/site-packages'.打印py用户环境
pprint(site.getusersitepackages())
# 全局环境
pprint(sys.path)