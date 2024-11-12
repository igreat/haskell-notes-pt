# impure function
def add_to_list_impure(value, lst):
    lst.append(value)

# pure function
def add_to_list_pure(value, lst):
    lst_copy = lst.copy()
    lst_copy.append(value)
    return lst_copy

# mutable data
def sum_loop(lst):
    acc = 0
    for x in lst:
        acc += x
    return acc

# higher order functions
def get_adder(x):
    def adder(y):
        return x + y
    return adder

# immutable data?
# so how do we loop without a counter?
# answer: we use recursion

# head :: (tail = rest of the list)
# lst[0] :: lst[1:]
# sum lst = lst[0] + sum lst[1:]
def sum_rec(lst):
    if lst == []:
        return 0
    return lst[0] + sum_rec(lst[1:])
    # return lst[0] + lst[1] + lst[2] + ... + sum_rec([])

# lst[0] + lst[1] + lst[2] +

# mathematical induction
# sum [] = 0
# sum lst = lst[0] + sum lst[1:]
# prove that this is correct for all lst
# sum lst = lst[0] + lst[1] + lst[2] + ... + lst[n-1] + lst[n]
# sum x :: lst = x + lst[0] + lst[1] + ... + lst[n-1] + lst[n]
# sum x :: lst = x + lst[0] + lst[1] + ... + lst[n-1] + lst[n]

def main():
    a = [1, 2, 3]
    b = add_to_list_pure(4, a)

    adder_2 = get_adder(2)
    print(adder_2(3)) # 5
    print(adder_2(4)) # 6

    print(sum_loop([1, 2, 3])) # 6
    print(sum_rec([1, 2, 3])) # 6
    print(sum_rec([])) # 0

if __name__ == "__main__":
    main()
