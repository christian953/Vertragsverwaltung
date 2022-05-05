from Crypto.Cipher import AES

key = b'MKMKMKMKMKMKMKMK' # hier M_key für pw (16 ziechen lang)
def encrypt(pw):
    data_to_encrypt = pw

    # String to byte object
    data = data_to_encrypt.encode('utf-8')

    # Create the cipher object and encrypt the password
    cipher_encrypt = AES.new(key, AES.MODE_CFB)
    ciphered_bytes = cipher_encrypt.encrypt(data)

    # Encrypted password
    iv = cipher_encrypt.iv
    ciphered_password = ciphered_bytes

    return ciphered_password, iv


def decrypt(encrypted_pw ,iv):


    # decrypt encrypted password
    decryptpw = AES.new(key, AES.MODE_CFB, iv=iv)
    deciphered_bytes = decryptpw.decrypt(encrypted_pw)
    decrypted_pw = deciphered_bytes.decode('utf-8')

    return decrypted_pw
