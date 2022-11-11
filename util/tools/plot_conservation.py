from collections import Counter

import numpy as np


def plot_conservation(generated_sequence_file,output_data_dir,dir_name):

    #Turn on the protein sequence
    with open(generated_sequence_file,"r") as SeqInitial:             
        
        #Used to store post-processing sequences
        with open(output_data_dir+ "/" + dir_name + "/sequenceTreatment.fasta", "w+") as SeqTreatment: 
            #Read by row
	        for line in SeqInitial.readlines(): 
                #Remove the newline character       
                    line=line.strip('\n')         
                    if'>' not in line:
                        #Read by row          
                        SeqTreatment.write(line)           
                    if'>'in line :    
                        #Use '.'instead of protein name information         
                        SeqTreatment.write('.')     
    SeqInitial.close()
    SeqTreatment.close()
    SeqTreatment = open('sequenceTreatment.fasta')            

    # reads all into one string
    allTxt=SeqTreatment.read()  

    #Drop the beginning dot
    lineTxt=allTxt[:0]+allTxt[1:]

    # Create a list with 1000 strings             
    slist=[0 for col in range(1000)]
 
    for i in range (1000):                #按点‘.’分割序列
    	slist[i]= txt.split('.')[i]
comlist=str()                    #创建一个而用来存放矩阵竖列的变量
lsen=str()                          #创建一个用来存放特征序列的变量
 
  
for i in range(1000):
    for j in range(len(slist[i])): 
        comlist=comlist+slist[i][j]
    if ( Counter(comlist).most_common(1)[0][0]!='-'):            #找出列字符串里出现频率最高的氨基酸
        if(Counter(comlist).most_common(1)[0][1]>500):            #大于一半的
            lsen=lsen+Counter(comlist).most_common(1)[0][0]      #一个一个存放起来
            comlist='-'                                                        #重置compare list
 
lsen=lsen[:100]                                          #取前100个
print(len(lsen))                                          
print(lsen)
with open('A1feature.fasta','w')as feature:
	feature.write(lsen)                          #创建个fasta文件存起来