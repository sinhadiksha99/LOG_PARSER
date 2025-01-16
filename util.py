import argparse
import re
import sys

def print_help():
    print("""
Usage: ./util.py [OPTION]... [FILE]
Supported options:
---------------------
  -h, --help         Print help
  -f, --first=NUM    Print first NUM lines
  -l, --last=NUM     Print last NUM lines
  -t, --timestamps   Print lines that contain a timestamp in HH:MM:SS format
  -i, --ipv4         Print lines that contain an IPv4 address, matching IPs
                     are highlighted
  -I, --ipv6         Print lines that contain an IPv6 address (standard
                     notation), matching IPs are highlighted
If FILE is omitted, standard input is used instead.
If multiple options are used at once, the result is the intersection of their
results.
""")

def read_lines(file):
    if file:
        with open(file, 'r') as f:
            return f.readlines()
    else:
        return sys.stdin.readlines()

def filter_first(lines, num):
    return lines[:num]

def filter_last(lines, num):
    return lines[-num:]

def filter_timestamps(lines):
    timestamp_pattern = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
    return [line for line in lines if timestamp_pattern.search(line)]

def filter_ipv4(lines):
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    return [line for line in lines if ipv4_pattern.search(line)]

def filter_ipv6(lines):
    ipv6_pattern = re.compile(r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b')
    return [line for line in lines if ipv6_pattern.search(line)]

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-f', '--first', type=int)
    parser.add_argument('-l', '--last', type=int)
    parser.add_argument('-t', '--timestamps', action='store_true')
    parser.add_argument('-i', '--ipv4', action='store_true')
    parser.add_argument('-I', '--ipv6', action='store_true')
    parser.add_argument('file', nargs='?', default=None)

    args = parser.parse_args()

    if args.help:
        print_help()
        return

    lines = read_lines(args.file)

    if args.first is not None:
        lines = filter_first(lines, args.first)
    if args.last is not None:
        lines = filter_last(lines, args.last)
    if args.timestamps:
        lines = filter_timestamps(lines)
    if args.ipv4:
        lines = filter_ipv4(lines)
    if args.ipv6:
        lines = filter_ipv6(lines)

    for line in lines:
        print(line, end='')

if __name__ == '__main__':
    main()