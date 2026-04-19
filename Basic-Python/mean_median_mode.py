#1 2 8 6 6 9 6 3 7
#1 7 4 5 32 48 7


def find_mean(num_list):
    avg = sum(num_list)/len(num_list)
    print(f'Mean: {round(avg,2)}')
    # Complete this function

def find_median(num_list):
    num_list.sort()
    l = len(num_list) // 2
    if len(num_list) % 2 ==0:
        med = (num_list[l] + num_list[l-1]) * 0.5
    else:
        med = num_list[l]
    print(f'Median: {round(med,2)}')
    # Complete this function

def find_mode(num_list):
    req = set(num_list)
    list_count = {}
    max_count = 0
    for num in req:
        if max_count<num_list.count(num):
            max_count = num_list.count(num)
        list_count[num] = num_list.count(num)
    max_count_list = []
    for nu,coun in list_count.items():
        if coun == max_count:
            max_count_list.append((nu))
    max_count_list = list(map(str,sorted(max_count_list)))
    print(f'Mode: {" ".join(max_count_list)}')        

# Get the input and convert each number to int directly
num_list = []
integers = input().split()
for num in integers:
    num_list += [int(num)] # concatenates the new number to the existing list
find_mean(num_list)
find_median(num_list)
find_mode(num_list)
# Call the appropriate functions and print the results