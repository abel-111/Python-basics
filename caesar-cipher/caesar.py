"""Caesar Cipher Encryption & Decryption Tool"""

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(original_text, shift_amount, encode_decode):
    result_text = ""
    if encode_decode == "decode":
        shift_amount = shift_amount * -1
    for alph in original_text:
        if alph not in alphabets:
            result_text += alph
        else:
            pos = alphabets.index(alph)
            pos = (pos + shift_amount) % 26
            result_text += alphabets[pos]
    print("The code is: " + result_text)


do_you_want_to_continue = "yes"

while do_you_want_to_continue == "yes":
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift amount: "))
    caesar(text, shift, direction)
    do_you_want_to_continue = input("Do you want to continue? (yes/no): ").lower()