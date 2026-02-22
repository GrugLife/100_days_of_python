import string

letters = string.ascii_lowercase
again = "yes"


def encrypt(text, shift):
    encryption = []
    for t in text:
        if t in letters:
            idx = letters.index(t)
            new_char = letters[(idx + shift) % 26]
            encryption.append(new_char)
        else:
            encryption.append(t)

    print("".join(encryption))


def decrypt(text, shift):
    decryption = []
    for t in text:
        if t in letters:
            idx = letters.index(t)
            new_char = letters[(idx - shift) % 26]
            decryption.append(new_char)
        else:
            decryption.append(t)
    print("".join(decryption))


while again == "yes":
    direction = input("Type encode to encrypt, type decode to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encrypt":
        encrypt(text, shift)

    elif direction == "decrypt":
        decrypt(text, shift)

    again = input("type 'yes' if you want to go again. Otherwise type 'no'\n")
