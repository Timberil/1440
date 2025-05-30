def subsec_len(n, seq):
    req = set(range(1, 27))
    present_numbers = set()
    for num in seq:
        if 1 <= num <= 26:
            present_numbers.add(num)
    if len(present_numbers) < 26:
        return "NONE"
    
    req_count = {num: 1 for num in req}
    cur_count = {num: 0 for num in req}
    
    left = 0
    min_len = float('inf')
    count = 0  
    
    for right in range(n):
        num = seq[right]
        if num in req_count:
            cur_count[num] += 1
            if cur_count[num] == 1:
                count += 1
        
        # Пытаемся двигать левую границу, пока в окне есть все числа
        while count == 26:
            cur_len = right - left + 1
            if cur_len < min_len:
                min_len = cur_len
            
            left_num = seq[left]
            if left_num in req_count:
                cur_count[left_num] -= 1
                if cur_count[left_num] == 0:
                    count -= 1
            left += 1
    
    return min_len 


with open('D:\\programming\\filespy\\data_prog_contest_problem_2.txt', 'r') as file:
    data = file.read().split()
    n = int(data[0])
    seq = list(map(int, data[1:n+1]))

result = subsec_len(n, seq)
print(result)
