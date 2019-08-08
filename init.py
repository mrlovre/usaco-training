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

    source_file, in_file, out_file = [args.name + ext for ext in [".py", ".in", ".out"]]
    source_path, in_path, out_path = [os.path.join(args.name, file) for file in [source_file, in_file, out_file]]

    with open(source_path, "w") as source:
        print("\"\"\"", file=source)
        print("ID: mrlovre1", file=source)
        print("LANG: PYTHON3", file=source)
        print(f"PROB: {args.name}", file=source)
        print("\"\"\"", file=source)
        print(file=source)
        print(f"with open(\"{in_path}\", \"r\") as fin, open(\"{out_path}\", \"w\") as fout:", file=source)
        print("    pass", file=source)
        print(f"Created {source_path} with header.")

    with open(in_path, "w"):
        print(f"Created empty {in_path}.")

    with open(out_path, "w"):
        print(f"Created empty {out_path}.")
