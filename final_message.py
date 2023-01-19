
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

MESSAGE = '''
FlQJDA8HCAAJXkxeTVQdCwkFGVRWWUsHAh8WHA0DGBZdWVZEShYJDQkBABYeXkBEShYcHwMWGQBd WVZEShoUGh4BCRoYFQlDQVNdGA8MBBYMHAEBAwddWVZESgYUFQMHBhYeXkBESgEbGw4NGQBdWVZE 
SgAbHwlDQVNdHwMLSlNAWUsTBB1bXhE='''

KEY = 'mszyld'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))

# {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}