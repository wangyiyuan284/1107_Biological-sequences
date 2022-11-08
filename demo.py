import pysam as sam
# 读取fasta
fasta = sam.FastaFile('ABO_sequence.fasta')
# 获取染色体编号
fasta.references
# 获取文件名
fasta.filename
# 获取染色体数
fasta.nreferences
# 获取每条染色体长
fasta.lengths
