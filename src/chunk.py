import sys

'''
each chunk will contain at least one "block" of 3 non-blank lines
each chunk will be at least seven non-blank lines
empty lines between chunks will be removed
'''

prefix, = sys.argv[1:]

n = 0
cur_chunk = []
chunk_has_big_block = False
block_size = 0
chunk_lines = 0

while True:
    ln = sys.stdin.readline()
    if not ln:
        break
    l = ln.strip()
    if l == '':
        if not cur_chunk:
            continue
        block_size = 0
    else:
        block_size += 1
        if block_size >= 3:
            chunk_has_big_block = True
        chunk_lines += 1

    if chunk_has_big_block and block_size == 0 and chunk_lines >= 7:
        f = file(prefix + '.' + str(n), 'w')
        f.write(''.join(cur_chunk))
        f.close()

        n += 1
        cur_chunk = []
        chunk_has_big_block = False
        block_size = 0
        chunk_lines = 0
    else:
        cur_chunk.append(ln)

f = file(prefix + '.' + str(n), 'w')
f.write(''.join(cur_chunk))
f.close()
