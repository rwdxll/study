

"""
每一个yaml文件都是从一个列表开始
列表中的每一项都是一个键值对, 通常它们被称为一个 “哈希” 或 “字典”. 所以, 我们需要知道如何在 YAML 中编写列表和字典.

yaml文件格式：
    以 --- 开始
    列表的所有成员都开始于相同的缩进级别并且使用一个 "- " 作为开头(一个横杠和一个空格):

eg:
---
# 一个美味水果的列表
- Apple
- Orange
- Strawberry
- Mango

一个字典


"""
import os
import yaml


dir_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(dir_path, 'test.yaml')
# print(path)
f = open(path)
data = yaml.load(f, Loader=yaml.FullLoader)
print(data)