from cryptography.fernet import Fernet

def crypt_file(source_file, dest_file, key):
    key = str.encode(key)

    cipher = Fernet(key)

    lines = []

    with open(source_file, 'r') as f:
        lines = f.readlines()

    crypto_lines = []

    for l in lines:
        l = l[0:len(l)-1]
        crypto_text = cipher.encrypt(str.encode(l))
        crypto_lines.append(crypto_text.decode() + '\n')


    with open(dest_file, 'w') as f:
        for l in crypto_lines:
            f.write(l)

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        print(Fernet.generate_key().decode())
    else:
        crypt_file(sys.argv[1], sys.argv[2], sys.argv[3])