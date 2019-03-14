import string
import tqdm
import itertools
import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


chars = "1234567890qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM-"
# chars = "1234567890"

#print(string.printable)
print(chars)

password = input("Enter password to guess: ")
all_combos = round(nCr(len(chars), len(password)))
print(f"Possible combinations with password length {len(password)}: {all_combos}")
print(f"Estimated time to guess {all_combos} combinations: {(all_combos/4000000):.2f}s / {all_combos/(4000000*60):.2f}t / {all_combos/(4000000*60*24):.2f}d")

combos = itertools.permutations(chars, len(password))

password = tuple(password)
for c in tqdm.tqdm(combos):
	#print(c, password)
	if c == password:
		print(f"\nPassword entered: {''.join(password)}\nPassword guessed: {''.join(c)}")
		break
