alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
  new_text = ""
  for i in plain_text:
    idx = alphabet.index(i)
    if len(alphabet)-1-idx > shift_amount:
      new_idx = idx + shift_amount
      new_text += alphabet[new_idx]
    elif len(alphabet)-1-idx <= shift_amount:
      new_idx = shift_amount-(len(alphabet)-idx)
      new_text += alphabet[new_idx]
      
  print(new_text)


def decrypt(plain_text, shift_amount):
  new_text = ""
  for i in plain_text:
    idx = alphabet.index(i)
    if idx < shift_amount:
      new_idx = -(shift_amount - idx)
      new_text += alphabet[new_idx]
    elif idx >= shift_amount:
      new_idx = idx - shift_amount
      new_text += alphabet[new_idx]
      
  print(new_text)

def main(text, shift):
  if direction == "encode":

    encrypt(text, shift)
  if direction == "decode":

    decrypt(text, shift)

main(text, shift)
    