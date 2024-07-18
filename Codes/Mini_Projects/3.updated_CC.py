from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(text,shift_value,direction):
    crpted_text = ""
    if direction == "encode":
        for letter in text:
            position = alphabet.index(letter) + shift_value
            if position > 26:
                position = position % 26 
            crpted_text += alphabet[position]
        print(f"Encoded text is {crpted_text}")
            

    elif direction == "decode":
        for letter in text:
            position = alphabet.index(letter)
            new_postion = position - shift_value
            if new_postion < 0:
                new_postion = new_postion + 26
            crpted_text += alphabet[new_postion]
        print(f"Decoded text is {crpted_text}")
ceasar(text = text,shift_value = shift,direction = direction)   

# flag = True
# while flag:
#     temp = input("Type yes if you want to go agian, otherwise no.").lower()
#     if temp == 'no':
#         flag = False
#     else:
#         ceasar(text = text,shift_value = shift,direction = direction)

