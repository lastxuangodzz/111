import re # 导入正则包
import os
import shutil

path1 = "C:\\Users\\97918\\Desktop\\system\\"  # 文件夹1目录
path2 = "C:\\Users\\97918\\Desktop\\sam\\"     # 文件夹2目录
outfile = "C:\\Users\\97918\\Desktop\\test\\"          # 输出目录
files1 = os.listdir(path1) # 读取文件夹1目录
files2 = os.listdir(path2) # 读取文件夹2目录

systemname = []
samname = []
rults = []


# 正则匹配文件夹1中IP
for item in files1:
    rults = re.compile(r'(.*?)system.hive')
    systemname.append(re.findall(rults,str(item))[0])
# 正则匹配文件夹2中IP
for item in files2:
    rults = re.compile(r'(.*?)sam.hive')
    samname.append(re.findall(rults,str(item))[0])
# 对比两个文件夹IP，相同IP则输出目录
for item1 in systemname:
    for item2 in samname:
        if item1 == item2:
            file_path = outfile + str(item1)
            try:
                os.mkdir(file_path)
            except FileExistsError as e:
                print('File already exists')
            except OSError as e:
                print(f"An error has occurred: {e}")
                raise
            shutil.copy(path1 + item1 + 'system.hive',file_path + '\\' + 'system.hive')
            shutil.copy(path2 + item2 + 'sam.hive',file_path + '\\' + 'sam.hive')
            continue