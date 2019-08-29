#!/usr/bin/env python
import subprocess
import re
import sys


def print_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("Exception - {}".format(e.message))
            sys.exit(1)
    return wrapper


@print_error
def fetch_branch_name():
    return str(subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE).stdout, 'utf-8')


@print_error
def extract_ticket_number(branch_name):
    matches = re.findall('((?:GB|gb)-\\d{4})', branch_name)
    print(matches)
    if matches:
        return ""
    else:
        return matches[0]


@print_error
def commit(msg):
    print(msg)
    #subprocess.run(['git', 'commit', '-m', msg], stdout=subprocess.PIPE)


if __name__ == '__main__':
    commit_msg = sys.argv[1]
    ticket_number = extract_ticket_number(fetch_branch_name())
    commit("{} - {}".format(ticket_number, commit_msg))


