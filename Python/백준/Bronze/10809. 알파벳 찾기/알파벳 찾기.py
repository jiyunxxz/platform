s = input()

for ch in range(ord('a'), ord('z') + 1):
    print(s.find(chr(ch)), end=' ')