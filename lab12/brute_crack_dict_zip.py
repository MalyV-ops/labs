import zipfile
file = "DICH.zip"
dict = "dictionary.txt"
def dictionary_crack_zip(file, dict):
    with open(dict) as password_dictionary:
        for current_password in password_dictionary:
            current_password = current_password.strip().lower().encode('utf-8')
            with zipfile.ZipFile(file, 'r') as zip_ref:
                try:
                    for fname in zip_ref.namelist():
                        zip_ref.open(fname, pwd=current_password)
                except:
                    continue
                else:
                    return current_password
        return None
print(dictionary_crack_zip(file, dict))