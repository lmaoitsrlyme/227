print ('hi yourrmormorm')
import random
for i in range(1):
  keygen = (random.randint(11111111111, 999999999999999))
print ("")
message=input ('enter message you want to decrypt:')
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = input("encryption key:")
encrypt = ''
for i in message:
  position = alphabet.find(i)
  newpos = (position+ -int(key) )%94
  encrypt += alphabet [newpos]
output = (encrypt)
keyout = (keygen)
print ('decrypted message: '+ (output) )
