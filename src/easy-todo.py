#!/usr/bin/env python3

import sys, getopt, re

todo_file = "/Users/tomwans/Dropbox/Homeworkers/todo"

def main():
    cmd = ""
    if (len(sys.argv) > 1):
        searcher = re.compile(".*"+' '.join(sys.argv[2:])+".*\n")
        cmd = sys.argv[1]
    if (cmd == "did"):
        did_task()
    elif (cmd == "for"):
        search_tasks()
    elif (cmd == ""):
        list_tasks()
    else:
        add_task(' '.join(sys.argv[1:]))

def add_task(task_str):
    with open(todo_file, mode="a") as todo:
        todo.write(task_str) + '\n')

def list_tasks():
    print(open(todo_file, mode='r').read().rstrip())

def did_task():
    possibles = []
    okays = []
    with open(todo_file, mode='r') as todo_read:
        for line in todo_read:
            if searcher.search(line) != None:
                possibles.append(line)
            else:
                if line != "":
                    okays.append(line)
        if (len(possibles) > 1):
            count = 0
            for p in possibles:
                count += 1
                print(count, p.rstrip())
            to_kill = int(input('? '))
            if to_kill <= count:
                del possibles[to_kill - 1]
            else:
                print("kill what?")
            okays.extend(possibles)
        elif (len(possibles) == 0):
            print("> error! nothing found")
        open(todo_file, mode='w').write('\n'.join(okays))


def search_tasks():
    with open(todo_file, mode='r') as todo_read:
        for found in searcher.findall(todo_read.read()):
            print(found.rstrip())


if __name__ == "__main__":
    main()
