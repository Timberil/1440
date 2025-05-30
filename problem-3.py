def compute_A_k(k):

    A = []

    f_prev2 = 1  
    f_prev1 = 3  

    if f_prev2 % 2 == 1:
        A.append(f_prev2)
    if len(A) <= k and f_prev1 % 2 == 1:
        A.append(f_prev1)

    n = 2
   
    while len(A) <= k:
        f_n = 5 * f_prev1 + f_prev2
      
        if f_n % 2 == 1:
            A.append(f_n)
    
        f_prev2, f_prev1 = f_prev1, f_n
        n += 1

    return A[k]


   
result = compute_A_k(39)
print(result)