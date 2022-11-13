import sys
from biological_sequence import BiologicalSequence

FILE_NAME = "input_data/user_specified.txt"
OUT_DIR = "output_data"

biological_sequence = BiologicalSequence(
    FILE_NAME,
    OUT_DIR,
)

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Must supply exactly two arguments: file_name,out dir")
        exit(1)
    else:
        biological_sequence.compute(
            args[0],
            args[1],
        )

if __name__ == '__main__':
    main()
    