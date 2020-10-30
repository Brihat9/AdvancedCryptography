'''
    Brihat Ratna Bajracharya
    CRN: 19/075
    CDCSIT
    HILL CIPHER - DECRYPTION (2x2 matrix)
'''

import numpy as np
from numpy.linalg import inv

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

'''
    30 Common Digrams
    TH, HE, IN, ER, AN, RE, ED, ON, ES, ST, EN, AT, TO, NT, HA,
    ND, OU, EA, NG, AS, OR, TI, IS, ET, IT, AR, TE, SE, HI, OF
'''
common_digrams = ["TH", "HE", "IN", "ER", "AN", "RE", "ED", "ON", "ES", "ST",
                  "EN", "AT", "TO", "NT", "HA", "ND", "OU", "EA", "NG", "AS",
                  "OR", "TI", "IS", "ET", "IT", "AR", "TE", "SE", "HI", "OF"]

''' encoding digrams into numbers '''
# encoded_digrams = []
# for digram in common_digrams:
#     encoded_digrams.append([alphabet_list.index(digram[0].lower()),
#                             alphabet_list.index(digram[1].lower())])
# digrams = encoded_digrams


digrams = [[19, 7],  [7, 4],   [8, 13],  [4, 17],  [0, 13],  [17, 4],
           [4, 3],   [14, 13], [4, 18],  [18, 19], [4, 13],  [0, 19],
           [19, 14], [13, 19], [7, 0],   [13, 3],  [14, 20], [4, 0],
           [13, 6],  [0, 18],  [14, 17], [19, 8],  [8, 18],  [4, 19],
           [8, 19],  [0, 17],  [19, 4],  [18, 4],  [7, 8],   [14, 5]]


'''
    CIPHER TEXT:
    LMQETXYEAGTXCTUIEWNCTXLZEWUAISPZYVAPEWLMGQWYA
    XFTCJMSQCADAGTXLMDXNXSNPJQSYVAPRIQSMHNOCVAXFV
'''

default_cipher_text = ("LMQETXYEAGTXCTUIEWNCTXLZEWUAISPZYVAPEWLMGQWYA"
                       "XFTCJMSQCADAGTXLMDXNXSNPJQSYVAPRIQSMHNOCVAXFV")

default_cipher_num = [11, 12, 16, 4,  19, 23, 24, 4,  0,  6,  19, 23, 2,  19,
                      20, 8,  4,  22, 13, 2,  19, 23, 11, 25, 4,  22, 20, 0,
                      8,  18, 15, 25, 24, 21, 0,  15, 4,  22, 11, 12, 6,  16,
                      22, 24, 0,  23, 5,  19, 2,  9,  12, 18, 16, 2,  0,  3,
                      0,  6,  19, 23, 11, 12, 3,  23, 13, 23, 18, 13, 15, 9,
                      16, 18, 24, 21, 0,  15, 17, 8,  16, 18, 12, 7,  13, 14,
                      2,  21, 0,  23, 5,  21]


key_file = "key_file.txt"
decrypted_text_file = "decrypted_texts.txt"


def encode_cipher(cipher_text):
    ''' returns number encoded cipher text '''
    cipher_num = []
    for char in cipher_text:
        cipher_num.append(alphabet_list.index(char.lower()))

    # print(cipher_num)
    return cipher_num


def matrix_mul(mat_a, mat_b):
    ''' returns product of two matrices '''
    if (len(mat_a[0]) != len(mat_b)):
        print("dimensions do not match")
        return None

    result = np.zeros((len(mat_a), len(mat_b[0]))).tolist()
    for i in range(len(mat_a)):
        for j in range(len(mat_b[0])):
            for k in range(len(mat_a[0])):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    return result


def matrix_mod(mat, mod_num=26):
    ''' returns modulo mod_num (default 26) of each element '''
    result = np.zeros((len(mat), len(mat[0]))).tolist()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i][j] = int(mat[i][j]) % mod_num
    return result


def matrix_2_det(mat):
    ''' returns determinant of 2x2 matrix '''
    if ((len(mat) != len(mat[0])) or (len(mat) != 2)):
        print("Either not square matrix or not 2x2 matrix")
        return None
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def get_inv_deter(num):
    ''' returns inverse number for given number such that
        (inverse_number * number) mod 26 = 1 '''
    res = 1
    for valid_inv_deter in range(1, 26):
        if ((num * valid_inv_deter) % 26) == 1:
            res = valid_inv_deter
    return res


def matrix_inv(mat):
    ''' returns inverse of given matrix (using numpy) '''
    mat_np = np.array(mat)
    mat_np_inv = inv(mat_np).round(6)
    return mat_np_inv.tolist()


def matrix_2_inv_whole(mat):
    ''' returns inverse matrix in modulo 26 of given 2x2 matrix
        (using adjoint, and inverse determinant method) '''
    temp_mat_1 = np.zeros((2, 2)).tolist()
    temp_mat_2 = np.zeros((2, 2)).tolist()
    result = np.zeros((2, 2)).tolist()

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            temp_mat_1[i][j] = mat[j][i]

    temp_mat_2[0][0] = temp_mat_1[1][1]
    temp_mat_2[0][1] = -temp_mat_1[1][0]
    temp_mat_2[1][0] = -temp_mat_1[0][1]
    temp_mat_2[1][1] = temp_mat_1[0][0]

    mat_det = matrix_2_det(mat)
    mat_det_inv = get_inv_deter(mat_det)
    mat_det_inv_mod = mat_det_inv % 26

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i][j] = mat_det_inv_mod * temp_mat_2[i][j]
    return result


def matrix_adj(mat):
    ''' returns adjugate matrix of given 2x2 matrix '''
    mat_det = matrix_2_det(mat)
    mat_inv = matrix_inv(mat)
    result = np.zeros((len(mat), len(mat[0]))).tolist()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            result[i][j] = round((mat_det * mat_inv[i][j]), 3)
    return result


def get_inv_key(inv_deter, mat_adj_mod):
    result = np.zeros((len(mat_adj_mod), len(mat_adj_mod[0]))).tolist()
    for i in range(len(mat_adj_mod)):
        for j in range(len(mat_adj_mod[0])):
            result[i][j] = round((inv_deter * mat_adj_mod[i][j]), 3)
    return result


def get_inv_key_from_key(key_mat):
    ''' returns inverse key of given 2x2 key matrix (hill cipher) '''
    deter = matrix_2_det(key_mat)
    deter_mod = deter % 26
    inv_deter = get_inv_deter(deter_mod)

    mat_adj = matrix_adj(key_mat)
    mat_adj_mod = matrix_mod(mat_adj)
    inv_key = get_inv_key(inv_deter, mat_adj_mod)
    return matrix_mod(inv_key)


''' MAIN HERE '''
# deter = matrix_2_det([[4, 13], [11, 9]])
# deter_mod = deter % 26
# inv_deter = get_inv_deter(deter_mod)
# mat_adj = matrix_adj([[4, 13], [11, 9]])
# mat_adj_mod = matrix_mod(mat_adj)
# inv_key = get_inv_key(inv_deter, mat_adj_mod)
# print(matrix_mod(inv_key))
# key_mat = [[4, 13], [11, 9]]


def main():
    ''' main function '''
    print("\nAdvanced Cryptography (Hill Cipher Decryptor (m=2))")
    print("Brihat Ratna Bajracharya\n19/075\nCDCSIT\n---------")

    open(key_file, 'w').close()
    open(decrypted_text_file, 'w').close()

    ''' for user inputted cipher text (test only) '''
    # user_cipher = input("Enter Cipher Text (alphabets only, no spaces): ")
    #
    # if user_cipher == "":
    #     print("Cipher Text Empty, using default")
    #     user_cipher = default_cipher_text
    #
    # cipher_text = encode_cipher(user_cipher)

    # hardcoded cipher text, encoding done
    cipher = default_cipher_text
    cipher_text = encode_cipher(cipher)

    print("\nCIPHER TEXT:")
    print(cipher)
    print("-------------")

    ''' EXHAUSTIVE SEARCH '''
    # for i in range(1, 26):
    #     for j in range(1, 26):
    #         for k in range(1, 26):
    #             for p in range(1, 26):
    #                 key = [[i, j], [k, p]]
    #                 # print(key)
    #                 # print("i: " + str(i) + " , j: " + str(j)
    #                 #       + " , k: " + str(k) + ", p: " + str(p))
    #                 if (matrix_2_det(key) != 0):
    #                     inverse_key = get_inv_key_from_key(key)
    #                     decrypted_text = ""
    #                     for index in range(0, len(cipher_text), 2):
    #                         # print(index)
    #                         cip = [[cipher_text[index]],
    #                                [cipher_text[index+1]]]
    #                         # print(alphabet_list[cipher_text[index]])
    #                         # print(alphabet_list[cipher_text[index+1]])
    #                         plain_text = matrix_mod(matrix_mul(inverse_key,
    #                                                            cip))
    #                         # print(plain_text)
    #                         # print(alphabet_list[plain_text[0][0]], end="")
    #                         # print(alphabet_list[plain_text[1][0]], end="")
    #
    #                         decrypted_text += alphabet_list[plain_text[0][0]]
    #                         decrypted_text += alphabet_list[plain_text[1][0]]
    #
    #                     print(decrypted_text)
    #
    #                     keyfile = open(key_file, "a")
    #                     keyfile.write(str(key) + "\n")
    #                     keyfile.close()
    #
    #                     decryptedtext = open(decrypted_text_file, "a")
    #                     decryptedtext.write(decrypted_text + "\n")
    #                     decryptedtext.close()

    # print("\n NEXT METHOD\n")

    ''' SEARCH USING KNOWN DIGRAMS '''
    key_mat = [[0, 0], [0, 0]]
    for i in range(len(digrams)):
        for j in range(len(digrams)):
            if (j != i):
                key_mat = [digrams[i], digrams[j]]

                ''' taken from cipher text
                    most frequent diagram is LM and TX '''
                frequent_digrams = [[11, 12], [19, 23]]

                inv_key_mat = matrix_2_inv_whole(key_mat)

                encrypt_key_temp = matrix_mul(inv_key_mat, frequent_digrams)
                # print(encrypt_key_temp)

                encrypt_key = matrix_mod(encrypt_key_temp)

                ''' this is required for key_matrix * plain_text product '''
                temp = encrypt_key[0][1]
                encrypt_key[0][1] = encrypt_key[1][0]
                encrypt_key[1][0] = temp

                if (matrix_2_det(encrypt_key) != 0):
                    inverse_key = get_inv_key_from_key(encrypt_key)
                    decrypted_text = ""
                    for index in range(0, len(cipher_text), 2):
                        cip = [[cipher_text[index]], [cipher_text[index+1]]]
                        plain_text = matrix_mod(matrix_mul(inverse_key, cip))

                        decrypted_text += alphabet_list[plain_text[0][0]] + \
                            alphabet_list[plain_text[1][0]]

                    ''' display various intermediate calculation matrices '''
                    print("\nChoosen Digram Matrix: ", end="\t\t\t")
                    print(key_mat)
                    print("Inverse of Choosen Digram Matrix: ", end="\t")
                    print(inv_key_mat)
                    print("KEY Matrix Calculated: ", end="\t\t\t")
                    print(encrypt_key)
                    print("INVKEY Matrix Calculated: ", end="\t\t")
                    print(inverse_key)

                    ''' display decrypted text '''
                    print("\nDECRYPTED TEXT from above KEY:")
                    print(decrypted_text)
                    print("-------")

                    keyfile = open(key_file, "a")
                    keyfile.write(str(encrypt_key) + "\n")
                    keyfile.close()

                    decryptedtext = open(decrypted_text_file, "a")
                    decryptedtext.write(decrypted_text + "\n")
                    decryptedtext.close()


if __name__ == "__main__":
    main()

    '''
        SOLUTION

        CIPHER TEXT:
        LM QE TX YE AG TX CT UI EW NC TX LZ EW UA IS PZ YV AP EW LM GQ WY AX
        FT CJ MS QC AD AG TX LM DX NX SN PJ QS YV AP RI QS MH NO CV AX FV

        PLAIN TEXT
        th ek in gw as in hi sc ou nt in gh ou se co un ti ng ou th is mo ne
        yt he qu ee nw vo wj do wp lo ur ea ti ng br ea da nd ho ne yz

        the king was in his counting house counting out his money
        the queen wvowjdowplour eating bread and honey z

        REFERENCES
        https://crypto.interactive-maths.com/hill-cipher.html
    '''
