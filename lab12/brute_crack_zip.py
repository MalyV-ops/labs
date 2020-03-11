import zipfile
import string
import itertools
def brute_crack_zip(file):
    alph, num = string.ascii_lowercase, string.digits
    dictionary = num+alph
    zp = zipfile.ZipFile(file)
    for n in range(1, 9):
        for password in itertools.product(dictionary, repeat=n):
            password = ''.join(password)
            try:
                zp.extractall(pwd=password.encode())
            except:
                continue
            else:
                return password