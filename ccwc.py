"""
Building your own wc Tool
"""
import argparse
import sys
from random import randint
import os


def open_file_and_count_bytes(filename):
    if filename is sys.stdin:
        content = sys.stdin.read().encode("utf-8")
        return len(bytes(content))
    else:
        file_size = os.path.getsize(filename)
        return file_size


def open_file_and_count_lines(filename):
    if filename.name == '<stdin>':
        content = sys.stdin.read().encode("utf-8")
    else:
        filename = open(filename.name, "r")
        content = filename.read()
    content = content.splitlines()
    return len(content)


def open_file_and_count_words(filename):
    if filename.name == '<stdin>':
        content = sys.stdin.read().encode("utf-8")
    else:
        filename = open(filename.name, "r")
        content = filename.read()
    words = content.split()
    count = len(words)
    return count


def open_file_and_count_chars(filename):
    count = 0
    if filename.name == "<stdin>":
        content = sys.stdin.read().encode("utf-8")
        for char in content:
            count += 1
    else:
        filename = open(filename.name, "r")
        file = filename.read()
        file = file.splitlines()
        for line in file:
            count += len(line.encode("utf-8"))
    return count


def main():
    parser = argparse.ArgumentParser(description="WC Tool to calculate bytes, words, and line count")
    parser.add_argument("-c", nargs="?", type=argparse.FileType("r"),
                        const=sys.stdin, help="The filename for which wc needs to be run")
    parser.add_argument("-l", nargs="?", type=argparse.FileType("r"),
                        const=sys.stdin, help="The filename for which wc needs to be run")
    parser.add_argument("-w", nargs="?", type=argparse.FileType("r"),
                        const=sys.stdin, help="The filename for which wc needs to be run")
    parser.add_argument("-m", nargs="?", type=argparse.FileType("r"),
                        const=sys.stdin, help="The filename for which wc needs to be run")
    parser.add_argument("filename", nargs="?",  help="The name of the file to process")
    args = parser.parse_args()
    if args.c:
        byte_count = open_file_and_count_bytes(args.c)
        if args.c.name != "<stdin>":
            print(byte_count, args.c.name)
        else:
            print(byte_count)
    elif args.l:
        line_count = open_file_and_count_lines(args.l)
        if args.l.name != "<stdin>":
            print(line_count, args.l.name)
        else:
            print(line_count)
    elif args.w:
        word_count = open_file_and_count_words(args.w)
        if args.w.name != "<stdin>":
            print(word_count, args.w.name)
        else:
            print(word_count)
    elif args.m:
        char_count = open_file_and_count_chars(args.m)
        if args.m.name != "<stdin>":
            print(char_count, args.m.name)
        else:
            print(char_count)
    else:
        if not args.filename:
            stdin_content = sys.stdin.read()
            file_name = f"{randint(2452, 387628)}.txt"
            # Create temporary file to store stdin data
            with open(file_name, "w") as file:
                file.write(stdin_content)
            byte_count = open_file_and_count_bytes(file)
            line_count = open_file_and_count_lines(file)
            word_count = open_file_and_count_words(file)
            print(line_count, word_count, byte_count)
        else:
            file = args.filename.name
            byte_count = open_file_and_count_bytes(file)
            line_count = open_file_and_count_lines(file)
            word_count = open_file_and_count_words(file)
            print(line_count, word_count, byte_count, file)


if __name__ == "__main__":
    sys.exit(main())
