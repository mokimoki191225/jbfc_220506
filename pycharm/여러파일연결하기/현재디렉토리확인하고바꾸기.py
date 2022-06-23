
#현재 디렉터리 확인하고 바꾸기 (os.getcwd, os.chdir)

import os
import time

pdir = os.getcwd();
print(pdir)
time.sleep(1)

os.chdir('data');
print(os.getcwd())
time.sleep(1)

os.chdir('..'); # 전체 디렉토리
print(os.getcwd())
time.sleep(1)

os.chdir(pdir); # 전체 디렉토리
print(os.getcwd())


