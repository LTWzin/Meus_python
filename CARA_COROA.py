import random
result = random.randint(1, 2)
print('\033[31;1mCARA\033[m' if result == 2 else '\033[32;1mCOROA\033[m')