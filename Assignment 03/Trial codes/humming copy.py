def find_r(m):
    for r in range(m+1):
        if 2**r > m + r + 1:
            break
    return r - 1

def calculate_r(arr, n):
    parity = True
    flag = True
    c = 0
    for i in range(n, len(arr)):
        if flag == True:
            c+=1
            if arr[i] == '1':
                parity = not parity
            if c>n:
                flag = not flag
                c = 0
        else:
            c+=1
            if c>n:
                flag = not flag
                c = 0
    return 0 if parity else 1

def data_sent(data):
    bin_data = ''.join([format(ord(i), '08b') for i in data])
    print('Binary data:', bin_data)
    r = find_r(len(bin_data))
    data_array = [i for i in bin_data]
    data_array.reverse()
    for i in range(r + 1):
        data_array.insert(2**i - 1, None)
    data_array.reverse()

    data_array.reverse()
    for i in range(r + 1):
        data_array[2**i - 1] = calculate_r(data_array, 2**i - 1)

    data_array.reverse()

    return ''.join([str(i) for i in data_array])

def check_error(data_recieved):
    err = []
    r = find_r(len(data_recieved))

    data_recieved = [i for i in data_recieved]
    data_recieved.reverse()
    for i in range(r + 1):
        err.append(calculate_r(data_recieved, 2**i - 1))

    err.reverse()
    err = ''.join([str(i) for i in err])
    print(err)

    if int(err) == 0:
        return 'No error in the recieved input.'
    else:
        binary = int(err, 2)
        return f'Error at position {binary}'

if __name__ == '__main__':
    data = input("Enter data for humming method: ")
    print(f'Data sent is {data_sent(data)}')
    data_recieved = input("Enter the data recieved: ")
    print(check_error(data_recieved))