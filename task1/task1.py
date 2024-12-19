import sys

def circle_list(n, m):
    result = []
    index = 0
    array = list(range(1, n + 1))
    

    while True:
        result.append(array[index])  
        index = (index + m - 1) % n 
        if index == 0:  
            break

    return result

n = int(sys.argv[1])
m = int(sys.argv[2])
print(''.join(map(str, circle_list(n, m))))
