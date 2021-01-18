# GuessKey2 (131 solves, 133 pts)

Fixed task (without "print key"). The alogrithm is build in the way that more 0s than 1s gonna be XORed with the mask, therefore use 0xffffffffffffffff mask until all values become 1s. Then use 0 mask, so key stay unchanged.
