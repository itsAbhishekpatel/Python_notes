alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode (plain_text,shift_amount):
    chipher_text = ''
    for letter in plain_text:
        # get index of the letter 
        position = alphabet.index(letter)
        # update the index with shift value 
        new_postion = position + shift_amount
        # check if letter is greater than 26, return remainder 
        if new_postion > 26:
            new_postion = new_postion % 26
        # update the new letter 
        new_letter = alphabet[new_postion]
        # concatinate the new letter into blank string
        chipher_text += new_letter

    return chipher_text

def decode(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        # get the index 
        postion = alphabet.index(letter)
        new_postion = postion - shift_amount
        if new_postion < 0:
            new_postion = new_postion + 26
        cipher_text += alphabet[new_postion]
    return cipher_text
        


# encoded_text = encode(plain_text=text, shift_amount=shift) 

# decoded_text = decode(plain_text=text, shift_amount=shift)

if direction == "encode":
    encode_text = encode(plain_text=text, shift_amount= shift)
    print(f"Encoded text id {encode_text}")
elif direction == "decode":
    decoded_text = decode(plain_text=text,shift_amount=shift)
    print(f"Decrypted text is {decoded_text}")


