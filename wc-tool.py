import os
import argparse
import sys

def count_bytes(file_path):
    try:
        num_bytes = os.path.getsize(file_path)
        return num_bytes
    except FileNotFoundError:
        return None

def count_lines(file_path):
    line_count = 0
    try:
        with open(file_path, "r") as file:
            for _ in file:
                line_count+=1
        return line_count
    except FileNotFoundError:
        return None

def count_words(file_path):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
        words = contents.split(" ")
        word_count = len(words)
        return word_count
    except FileNotFoundError:
        return None

def count_chars(file_path):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
        char_count = len(contents)
        return char_count
    except FileNotFoundError:
        return None

def main():
    parser = argparse.ArgumentParser(description="Count the number of bytes in a file.")
    parser.add_argument("-c", "--count", action="store_true", help="Count the bytes in the file")
    parser.add_argument("-l", "--lines", action="store_true", help="Count the lines in the file")
    parser.add_argument("-w", "--words", action="store_true", help="Count the words in the file")
    parser.add_argument("-m", "--chars", action="store_true", help="Count the characters in the file")
    parser.add_argument("file_paths", metavar="FILE_PATH", type=str, nargs='*', help="Path to the file for byte counting")

    args = parser.parse_args()

    if not (args.count or args.lines or args.words or args.chars):
        args.count = args.lines = args.words = True

    if not args.file_paths and sys.stdin.isatty():
        parser.print_help()
        sys.exit(1)

    if len(args.file_paths) == 0:
        input_text = sys.stdin.read()
        if args.count:
            num_bytes = len(input_text.encode('utf-8'))
            print(f"{num_bytes} bytes in text")
        if args.lines:
            num_lines = input_text.count('\n')
            print(f"{num_lines} lines in text")
        if args.words:
            num_words = len(input_text.split())
            print(f"{num_words} words in text")

    else:
        for file_path in args.file_paths:
            file_name = file_path.split("/")[-1]

            if args.count:
                num_bytes = count_bytes(file_path)
                print(f"{num_bytes} bytes in {file_name}")
            if args.lines:
                line_count = count_lines(file_path)
                print(f"{line_count} lines in {file_name}")
            if args.words:
                word_count = count_words(file_path)
                print(f"{word_count} words in {file_name}")
            if args.chars:
                char_count = count_chars(file_path)
                print(f"{char_count} characters in {file_name}")

if __name__ == "__main__":
    main()





