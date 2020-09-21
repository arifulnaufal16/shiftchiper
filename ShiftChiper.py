def encrypt(plaintext,key):
    convert = [(ord(t) - 65) for t in plaintext]
    final = ""
    for i in convert:
        enc = (i + key)  % 26
        final += chr(enc + 65)
    return final

def decrypt(chipertext,key):
    convert = [(ord(t) - 65) for t in chipertext]
    final = ""
    for i in convert:
        dec = (i - key) % 26
        final += chr(dec + 65)
    return final

def main():
    text = "ECLIPSE"
    key = 18

    enc_text = encrypt(text,key)
    dec_text = decrypt(enc_text, key)
    print('\n==ENKRIPSI SHIFT CHIPER===')
    print('ENKRIPSI : ' ,(enc_text))
    print('DEKRIPSI : ' ,(dec_text),'\n')

if __name__ == "__main__":
    main()