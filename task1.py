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

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        m = int(lines[1].strip())
    return n, m

def write_output(file_path, result):
    with open(file_path, 'w') as file:
        file.write(''.join(map(str, result)) + '\n')

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        n, m = read_input(input_file)
        result = circle_list(n, m)
        write_output(output_file, result)
        print(''.join(map(str, result))) 
    except Exception as e:
        print(f"Ошибка: {e}")
