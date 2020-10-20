'''
    Brihat Ratna Bajracharya
    CRN: 19/075
    CDCSIT
    SHIFT CIPHER - ENCRYPTION & DECRYPTION
'''

# DATA = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"
DATA = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt(cipher_text):
    '''
        decrypts the cipher text, ask user for correct one
        and return that text
    '''
    decrypted_list = []
    for key in range(1, 26):
        decrypted_text = ""

        for char in cipher_text:
            decrypted_text += alphabet_list[(alphabet_list.index(char.lower()) - key) % 26]

        print("For Key: " + str(key))
        print("Decrypted text: " + decrypted_text + "\n")

        decrypted_list.append(decrypted_text)

    cipher_key = int(input("Which is the right key? "))
    return decrypted_list[cipher_key - 1]


def encrypt(plain_text, key):
    ''' encrypts the plain text using given key '''
    encrypted_text = ""

    for char in plain_text:
        encrypted_text += alphabet_list[(alphabet_list.index(char.lower()) + key) % 26]

    # print("Key: " + str(key))
    # print("Encrypted Text: " + encrypted_text + "\n")

    return encrypted_text


def main():
    ''' main function '''
    print("\nAdvanced Cryptography (Shift Cipher)")
    print("Brihat Ratna Bajracharya\n19/075\n---------")

    cipher_text = input("Enter encrypted text (nospaces): ")
    if cipher_text == "":
        print("Empty Cipher Text, Using Default Cipher Text")
        cipher_text = DATA
        plain = decrypt(cipher_text)
    else:
        plain = decrypt(cipher_text)
    print(plain)

    plain_text = input("Enter text to encrypt (no spaces): ")
    cipher_key = int(input("Enter encryption key (1-25): "))
    if cipher_key < 1 or cipher_key > 25:
        print("Invalid Key. Program will terminate...")
        return

    cipher = encrypt(plain_text, cipher_key)
    print("Before encryption: " + plain_text.lower())
    print("After encryption: " + cipher.upper())


if __name__ == "__main__":
    main()
