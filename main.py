import random
import colorama

class DimensionError(Exception):
    pass

class MultiplicationError(Exception):
    pass

def random_generator(num:int) -> list:
    result:list = []
    for i in range(num):
        result.append(random.randint(0,50))
    else:
        return result

print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] Creating the matrices")

a: list = [
    random_generator(5),
    random_generator(5),
    random_generator(5),
]

b: list = [
    random_generator(3),
    random_generator(3),
    random_generator(3),
    random_generator(3),
    random_generator(3),
]

for row in a:
    print(row)
else:
    print('\n')

for row in b:
    print(row)
else:
    print('\n')

# Checking the condition before multiplication
print(f"[{colorama.Fore.YELLOW}?{colorama.Fore.RESET}] Checking multiplicity ... ", end='')
if len(a[0]) == len(b):
    print(f"{colorama.Fore.GREEN}OK{colorama.Fore.RESET}")
else:
    print(f"{colorama.Fore.RED}Error{colorama.Fore.RESET}")
    raise DimensionError(f"[{colorama.Fore.RED}-{colorama.Fore.RESET}] These two matrices do not have the same number of rows and columns")

print(f"[{colorama.Fore.GREEN}+{colorama.Fore.RESET}] Doing the multiplication ... ", end='')
# Initialing the result Matrix
c:list = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

# Multiplication itself
try:
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j] = a[i][0] * b[0][j]
            for k in range(1, len(a[0])):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
except MultiplicationError:
    print(f"{colorama.Fore.RED}Error{colorama.Fore.RESET}")
    raise MultiplicationError("There is a multiplication error")
else:
    print(f"{colorama.Fore.GREEN}done{colorama.Fore.RESET}")
    for row in c:
        print(row)
