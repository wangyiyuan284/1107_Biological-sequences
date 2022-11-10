# -*- coding: utf-8 -*-
import sys
from Bio import Entrez, SeqIO

# Get user's inputet

# proteinFamily = str(input("Please enter the specified protein family:"))
# taxonomicGroup = str(input("Please enter the specified taxonomic group:"))

# 参数设置 Setting Parameter
Entrez.email = "Author@163.com"
Entrez.tool  = "exampleScript"

# 查询 oct4 基因的在 Nucleotide 中的总数
with open('input_data/user_specified.txt') as file:
    for line in file:
        result=[]
        result.append(list(line.strip('\n').split(',')))
        userSpecified=(result[0][1]+' '+result[0][2])
        hd_egquery = Entrez.egquery(term=userSpecified)
        read_egquery = Entrez.read(hd_egquery)
        total = 0
        for ele in read_egquery["eGQueryResult"]:
            if ele["MenuName"] == "Protein":
                total = ele["Count"]
                print(total)

        # # 得到查询 id 列表
        # hd_esearch = Entrez.esearch(db="protein", term=userSpecified, retmax=total)
        # read_esearch = Entrez.read(hd_esearch)
        # # 这里我们只取前1000个序列，建议用户不要超过1000个序列
        # ids = read_esearch["IdList"][:2]

        # # 用得到的 id 列表去下载每一条 fasta 文件，并合并，以便后续分析使用（比如进化树构建）
        # hd_efetch_fa = Entrez.efetch(db='protein', id=ids, rettype='fasta')
        # read_efetch_fa = hd_efetch_fa.read()
        # with open("output_data/sequence.fasta","w") as file:
        #     file.write(read_efetch_fa)
        hd_search = Entrez.esearch(db="protein", term=userSpecified, usehistory="y")
        read_search = Entrez.read(hd_search)
        webenv = read_search["WebEnv"]
        query_key = read_search["QueryKey"]
        # 使用历史记录特性来进行搜索。
        # Entrez 将会提前进行缓冲，提高查询效率
        step = 5
        total = 1000
        with open("output_data/sequence1000.fasta", "w") as file:
             for start in range(0, total, step):
                end = min(total, start+step)
                print("Download record %i to %i" % (start+1, end))
                hd_fetch = Entrez.efetch(db="protein", rettype="fasta", retmode="fasta", retstart=start, retmax=step, webenv=webenv, query_key=query_key)
                records = hd_fetch.read()
                file.write(records)

# # 同理你可以得到 xml 格式的序列信息
# hd_efetch_xml = Entrez.efetch(db="nucleotide", id=ids, retmode="xml")
# read_efetch_xml = Entrez.read(hd_efetch_xml)
# print(read_efetch_xml)
# hd_efetch_gb = Entrez.efetch(db="nuccore", id=ids, rettype="gb", retmode="text")
# # 这里读取的是文本文件，保存为本地数据
# read_efetch_gb = hd_efetch_gb.read()
# with open("input_data/sequence.fasta","w") as file:
#     file.write(read_efetch_gb)

# # 如果需要提取其中一些信息，可以按照以下步骤, 这里需要注意需要重新得到 efetch 句柄
# hd_efetch_gb = Entrez.efetch(db="nuccore", id=ids, rettype="gb", retmode="text")
# parse_efetch_gb = SeqIO.parse(hd_efetch_gb, "gb")
# # 这里可以保存为 xls 或者 csv 格式
# for ele in parse_efetch_gb:
#     print(ele.name, ele.annotations['molecule_type'], ele.seq)
