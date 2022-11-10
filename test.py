# 首先给出文件路径
import numpy as np
resultpath = 'input_data\user_specified.txt'
coox=[]
cooy=[]
cooz=[]
with open("r"+resultpath) as f:
    for line in f.readlines():  # 打开后逐行读取
        each_line = line.decode().rstrip().split(',')  
        # ‘,’分割，存储为list元素
        cooy.append(float(each_line[0]))  # 保存第一个元素
        coox.append(float(each_line[1]))  # 保存第二个元素
        
        # 如果要倒叙输出 也可以直接利用reverse()函数
        a = each_line.reverse()
        cooz.append(float(a[0]))  # 保存倒数第一个元素
		
		# 或者使用切片的高级用法，结果同样是倒叙输出
        b = each_line[::-1]
# 如果要转换成np序列
coox = np.asarray(coox)
