list_a = [1,2,3,4,5,6,7,9]

#map: for mapping each element in list
list_square = list(map(lambda x:x**2,list_a))
print(list_square)

#filter => To filter elements in a list
list_odd = list(filter(lambda x:x%2!=0, list_a))
print(list_odd)

# def prime(x):
#     if x< 2:
#         return False
#     elif x==2:
#         return True
#     else:
#         for i in range(2,int(x**0.5+1)):
#             if (x%i == 0):
#                 return False
#         return True
is_prime = lambda x : x>=2 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
list_prime = list(filter(is_prime,list_a))
print(list_prime)


list_a = [1,2,3,4,5,6]

req = map((lambda x:x**2),list_a)
print(list(req))

req1 = filter((lambda x:x%2==0),list_a)
print(list(req1))
from functools import reduce
req2 = reduce((lambda a,b:a+b),list_a)
print(req2)

list_req = [0,1]

for i in range(8):
    need = list_req[i:i+2]
    print(need)
    need = reduce((lambda a,b:a+b), need)
    list_req.append(need)
print(list_req)