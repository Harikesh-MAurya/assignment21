# 1. Write a recursive python function to print first N natural numbers.
# 2. Write a recursive python function to print first N natural numbers in reverse order
# 3. Write a recursive python function to print first N odd natural numbers
# 4. Write a recursive python function to print first N odd natural numbers in reverse order
# 5. Write a recursive python function to print first N even natural numbers.
# 6. Write a recursive python function to print first N even natural numbers in reverse
# order.
# 7. Write a recursive python function to print squares of first N natural numbers
# 8. Write a recursive python function to print cubes of first N natural numbers
# 9. Write a recursive python function to print first N multiples of a given number.
# 10. Write a recursive python function to print a number in reverse order.


# 1) .....................................
# def n_list(n):
#     if n>0:
#         n_list(n-1)
#     print(n,end=" ")
   
# n_list(int(input("Enter n : ")))


# 2) .........................................
# def print_num(x):
#     if x==1:
#         return 1
#     else:
#         print(x,end=" ")
#         return print_num(x-1)
        
    
# print(print_num(int(input("Enter n : "))))


# 3) ........................................
# def odd(a,b):
#     if a>b:
#         return
#     print(a,end=' ')
#     return odd(a+2,b)

# odd(1,20)


# 4) ........................................
# def odd(a,b):
#     if a>b:
#         return
#     print(b,end=' ')
#     return odd(a,b-2)

# odd(1,20)

# 5) ......................................
# def even(a,b):
#     if a>b:
#         return
#     print(a,end=' ')
#     even(a+2,b)
# even(2,20)


# 6) ...................................
# def even(a,b):
#     if a>b:
#         return
#     print(b,end=' ')
#     even(a,b-2)
# even(2,20)


# 7) ....................................
# def square(n):
#     if n>1:
#         square(n-1)
#     print(pow(n,2),end=' ')
    
# square(int(input("Enter n : ")))


# 8) ....................................
# def square(n):
#     if n>1:
#         square(n-1)
#     print(pow(n,3),end=' ')
    
# square(int(input("Enter n : ")))


# 9) .....................................
# def multiple(n,x):
#     if n>1:
#         multiple(n-1,x)
#     print(x*n,end=' ')
    
    
# multiple(int(input("Enter n : ")),int(input("Enter x as a multiple : ")))


# 10) .......................................
def revers(n):
    while n!=0:
        r=n%10
        print(r,end='')
    revers(n//10)
        
revers(int(input("Enter n : ")))
