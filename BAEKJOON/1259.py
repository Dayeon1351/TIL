import sys
while 1:
    line = sys.stdin.readline().strip()
    if line == '0':
        break
    
    start,end = 0,-1
    for i in range(len(line)//2):
        if line[start] != line[end]:
            print("no")
            break
        else:
            start += 1
            end -= 1
    else:
        print("yes")