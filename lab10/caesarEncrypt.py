import string
s = "hello, world"
source = 'file'
key = 1
def caesarEncrypt(message, key, source = 'string'):
    alph = list(string.ascii_letters)
    if source == 'file':
        try:
            f = open(message)
        except FileNotFoundError:
            return "Can't open file {0}".format(message)
    elif source == 'string':
        f = [message]
    for line in f:
        line = list(line)
        for il in range(len(line)):
            if line[il] in alph and line[il].islower():
                line[il] = alph[(alph.index(line[il]) + key) % len(alph)].lower()
            elif line[il] in alph and line[il].isupper():
                line[il] = alph[(alph.index(line[il]) + key) % len(alph)].upper()
    return ''.join(line)
print(caesarEncrypt(s, 1))