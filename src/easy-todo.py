#!/usr/bin/env python3

import sys, getopt, re

todo_file = "/Users/tomwans/Dropbox/Homeworkers/todo"

def main():
    cmd = ""
    if (len(sys.argv) > 1):
        cmd = sys.argv[1]

    # load todo-list into python list
    todo_list = [x.rstrip() for x in open(todo_file, mode='r').readlines()]

    if (cmd == "did"):
        todo_list = did_task(todo_list, re.compile(".*"+' '.join(sys.argv[2:])+".*"))
    elif (cmd == "for"):
        [print(x) for x in search_tasks(todo_list, re.compile(".*"+' '.join(sys.argv[2:])+".*"))]
    elif (cmd == ""):
        [print(x) for x in todo_list]
    else:
        add_task(todo_list, ' '.join(sys.argv[1:]))

    # save to file
    with open(todo_file, mode='w') as f:
        f.write('\n'.join(todo_list))

def add_task(tlist, task_str):
    tlist.append(task_str.rstrip())

def did_task(tlist, task_desc):
    possibles = []
    okays = []
    for line in tlist:
        if task_desc.search(line) != None:
            possibles.append(line)
        else:
            okays.append(line)
    
    if (len(possibles) > 1):
        count = 0
        for p in possibles:
            count += 1
            print(count, p)
        to_kill = int(input('? '))
        while to_kill > count or to_kill == 0:
            to_kill = int(input('? '))
        del possibles[to_kill - 1]
        okays.extend(possibles)
    elif (len(possibles) == 0):
        print("> error! nothing found")
    
    return okays

def search_tasks(tlist, task_desc):
    return [x for x in tlist if task_desc.search(x) != None]

if __name__ == "__main__":
    main()
