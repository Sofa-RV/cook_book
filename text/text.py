import os
import glob
from os import path


for filename in os.listdir('sorted'):
    with open(os.path.join('sorted', filename), 'r', encoding='utf-8') as f:
        text = f.readlines()
len_ = len(text)
dict_ = {filename: len_}
print(dict_)

#  не могу разобраться что тут делать и как, вроде логгику пониамю а как реализовать не доходит