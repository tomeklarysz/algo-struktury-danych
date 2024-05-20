f = open(r'lab7\patterns\1000_pattern.txt')

lines = f.readlines()
pattern = 'ABC'

def naive(array, p):
    n = len(array)
    m = len(p)
    result = []
    for i in range(n-m):
        for j in range(n-m):
            if array[i][j:j+m] == p:
                isValid = True
                for k in range(i+1, i+m):
                    if array[k][j] != p[k-i]:
                        isValid = False
                        break
                if isValid:
                    result.append([i, j])
    return result


def rabin(array, p, q):
    n = len(array)
    m = len(p)
    result = []
    # hashing below
    h = 0
    cur = 0
    for i in range(m):
        val_pattern = int('0x'+p[i], 16)
        h += val_pattern * pow(10, m-i-1)
    h %= q
    for i in range(n-m):
        for j in range(m):
            val_text = int('0x'+array[i][j], 16)
            cur += val_text * pow(10, m-j-1)
        cur %= q
        for j in range(n-m):    
            if cur == h:
                h_down = 0
                text_down = ''
                for k in range(i, i+m):
                    val = int('0x'+array[k][j], 16)
                    h_down += val * pow(10, i+m - k - 1)
                    text_down += array[k][j]
                h_down %= q
                if h_down == h:
                    if array[i][j:j+m] == p and text_down == p:
                        result.append([i, j])
            cur = cur - int('0x'+array[i][j], 16) * pow(10, m-1)
            cur *= 10
            cur += int(array[i][j+m], 16)
            cur %= q
    return result


# result = naive(lines, pattern)

# print(result)
# print(len(result))

result = rabin(lines, pattern, 16)

print(result)
print(len(result))