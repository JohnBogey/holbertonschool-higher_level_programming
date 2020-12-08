#!/usr/bin/python3
for c in range(ord('a'), ord('z')):
    if c == ord('e') or c == ord('q'):
        continue
    print(chr(c), end="")
