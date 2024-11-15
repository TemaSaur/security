import re
import math


def _shift(c: str, offset: int) -> str:
	if not c.isalpha():
		return c

	x = ord(c)

	base = 0
	if ord('a') <= x <= ord('z'):
		base = ord('a')
	else:
		base = ord('A')

	x -= base

	return chr(base + (x + offset) % 26)


words = None

def _ensure_words():
	global words

	if words is not None:
		return words

	words = []
	with open('words.txt', 'r') as f:
		words = f.read().split()
	return words


def _evaluate(message: str) -> int:
	global words
	_ensure_words()

	result = 0

	for word in re.split(r'[^a-z]', message.lower()):
		if len(word) == 0:
			continue

		if word not in words:
			result -= 1
			continue
		index = words.index(word)
		result += math.log(len(words) - index + 1)
	return result


def encrypt(message: str, offset: int = 3) -> str:
	return "".join(_shift(c, offset) for c in message)


def decrypt(message: str, offset: int = 3) -> str:
	return encrypt(message, -offset)


def bruteforce(message: str) -> dict:
	top = {}
	for offset in range(26):
		msg = decrypt(message, offset)
		top[msg] = _evaluate(msg), offset
	return sorted(top.items(), key=lambda x: x[1][0])


if __name__ == "__main__":
	import sys

	message = ""
	offset = 3

	if len(sys.argv) >= 3:
		message = sys.argv[2]
		offset = offset if len(sys.argv) < 4 else int(sys.argv[3])
	else:
		message = sys.stdin.read()

	if sys.argv[1] in {'encrypt', 'e'}:
		print(encrypt(message, offset))
	elif sys.argv[1] in {'decrypt', 'd'}:
		print(decrypt(message, offset))
	elif sys.argv[1] in {'bruteforce', 'b'}:
		for option, val in bruteforce(message):
			print(f'{val[1]}: {val[0]}\n{option}')
			print('===============')
	else:
		raise Exception("encrypt or decrypt")

