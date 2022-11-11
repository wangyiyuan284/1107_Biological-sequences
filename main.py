import sys

from Bio import Entrez, SeqIO

from biological_sequence import BiologicalSequence

FILE_NAME = "input_data/user_specified.txt"
OUT_DIR = "output_data"
AMOUNT = 1000

biological_sequence = BiologicalSequence(
    FILE_NAME,
    OUT_DIR,
    AMOUNT,
)

def main():
    args = sys.argv[1:]
    if len(args) != 3:
        print("Must supply exactly three arguments: file_name,out dir and amount")
        exit(1)
    else:
        biological_sequence.compute(
            args[0],
            args[1],
            args[2],
        )

if __name__ == '__main__':
    main()
    