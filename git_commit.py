#!/usr/bin/env python3
import subprocess
import re
import sys


def print_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Exception - {}".format(e))
            sys.exit(1)
    return wrapper


@print_error
def fetch_branch_name():
    branch_name = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE).stdout
    if branch_name:
        return str(branch_name.rstrip(), 'utf-8')
    return ""


@print_error
def extract_ticket_number(branch_name):
    matches = re.findall('(.{3}-\\d{3})', branch_name)
    if matches:
        return matches[0]
    else:
        return ""


@print_error
def commit(msg):
    subprocess.run(['git', 'commit', '-m', msg], stdout=subprocess.PIPE)


if __name__ == '__main__':
    commit_msg = sys.argv[1]
    ticket_number = extract_ticket_number(fetch_branch_name())
    if ticket_number:
        commit("{} {}".format(ticket_number, commit_msg))
    else:
        commit("{}".format(commit_msg))



