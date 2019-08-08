import argparse
import os
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)
    args = parser.parse_args()

    try:
        os.mkdir(args.name)
    except FileExistsError:
        print("Folder already exists. Skipping.")
        exit()

    source_filepath = os.path.join(args.name, args.name + ".py")
    with open(source_filepath, "w") as source_file:
        print("\"\"\"", file=source_file)
        print("ID: mrlovre1", file=source_file)
        print("LANG: PYTHON3", file=source_file)
        print(f"PROB: {args.name}", file=source_file)
        print("\"\"\"", file=source_file)
        print(f"Created {source_filepath} with header.")

    in_filepath = os.path.join(args.name, args.name + ".in")
    with open(in_filepath, "w") as in_file:
        print(f"Created empty {in_filepath}.")

    out_filepath = os.path.join(args.name, args.name + ".out")
    with open(out_filepath, "w") as out_file:
        print(f"Created empty {out_filepath}.")
