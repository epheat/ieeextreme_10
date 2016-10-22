from math import *

def LRU(p,s,calls):
    stack = []
    repl = 0
    for i in calls:
        page = floor(i / s)
        if len(stack) < p:
            if page not in stack:
                stack.insert(0, page)
            else:
                stack.remove(page)
                stack.insert(0, page)
        else:
            if page not in stack:
                stack.pop()
                stack.insert(0, page)
                repl += 1
            else:
                stack.remove(page)
                stack.insert(0, page)
    return repl

def FIFO(p, s, calls):
    stack = []
    repl = 0
    for i in calls:
        page = floor(i / s)
        if len(stack) < p:
            if page not in stack:
                stack.append(page)
        else:
            if page not in stack:
                repl += 1
                del stack[0]
                stack.append(page)
    return repl

def main():
    cases = int(input())
    for i in range(0,cases):
        buff = input().split(' ')
        pages = int(buff[0])
        size = float(buff[1])
        n = int(buff[2])
        calls = []
        for j in range(0, n):
            buff = int(input())
            calls.append(buff)
        fifo = FIFO(pages,size,calls)
        lru = LRU(pages,size,calls)
        result = ""
        if lru < fifo:
            result += "yes "
        else:
            result += "no "
        result += (str(fifo) + " " + str(lru))
        print(result)
    
    
main()from math import *

def LRU(p,s,calls):
    stack = []
    repl = 0
    for i in calls:
        page = floor(i / s)
        if len(stack) < p:
            if page not in stack:
                stack.insert(0, page)
            else:
                stack.remove(page)
                stack.insert(0, page)
        else:
            if page not in stack:
                stack.pop()
                stack.insert(0, page)
                repl += 1
            else:
                stack.remove(page)
                stack.insert(0, page)
    return repl

def FIFO(p, s, calls):
    stack = []
    repl = 0
    for i in calls:
        page = floor(i / s)
        if len(stack) < p:
            if page not in stack:
                stack.append(page)
        else:
            if page not in stack:
                repl += 1
                del stack[0]
                stack.append(page)
    return repl

def main():
    cases = int(input())
    for i in range(0,cases):
        buff = input().split(' ')
        pages = int(buff[0])
        size = float(buff[1])
        n = int(buff[2])
        calls = []
        for j in range(0, n):
            buff = int(input())
            calls.append(buff)
        fifo = FIFO(pages,size,calls)
        lru = LRU(pages,size,calls)
        result = ""
        if lru < fifo:
            result += "yes "
        else:
            result += "no "
        result += (str(fifo) + " " + str(lru))
        print(result)
    
    
main()