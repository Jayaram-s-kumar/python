def caesar_encrypt(distance, plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.islower():
            encrypted_char = chr((ord(char) - ord('a') + distance) % 26 + ord('a'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(distance, ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char.islower():
            decrypted_char = chr((ord(char) - ord('a') - distance) % 26 + ord('a'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Take input from the user
distance = int(input("Enter the distance value: "))
string = input("Enter the string: ")

# Encryption
encrypted_string = caesar_encrypt(distance, string)
print("Encrypted string:", encrypted_string)

# Decryption
decrypted_string = caesar_decrypt(distance, encrypted_string)
print("Decrypted string:", decrypted_string)
