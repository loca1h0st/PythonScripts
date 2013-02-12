#! /usr/bin/env python

'DES decryption and encryption'
import base64

def encryption(cipher, key):
  'this will call xor, sub, and trans to encrypt the massage'
  #xor with the key
  cipher = xor_cipher(cipher, key)
  #use the ROT47 cipher on the text first
  cipher = sub(cipher)
  #now use rail fence cipher to transpose
  cipher = trans(cipher)
  #list comprehend cipher into a string
  #then turn it into a base64 cipher so 
  #the terminal can represent it
  return  base64.b64encode("".join([x for x in cipher]))
  
def decryption(text, key):
  'this will call trans, sub, and xor to decrypt the cipher'
  #Decode the cipher from base64 to 
  text = base64.b64decode(text)
  text = map(ord, text)
  #Decrypt the rail fence cipher
  text = decode(text)
  #Decrypt the ROT47 cipher
  text = sub(text)
  #xor with the key
  text = xor_cipher(map(ord,text),key)
  
  return ''.join(text)
  
 
def xor_cipher(text, key):
  'XOR the plaintext with the key'
  cipher = [text[i] ^ key[i] for i in range(len(text))]
  return map(chr, cipher)
  
def sub(text):
  'ROT47 cipher'
  x = []
  for i in xrange(len(text)):
    j = ord(text[i])
    if j >= 33 and j <= 126:
      x.append(chr(33 + ((j + 14) % 94)))
    else:
      x.append(text[i])
  return ''.join(x)
  
def trans(text):
 'rail fence cipher'
 fence = [[None] * len(text) for n in range(3)]
 rails = range(2) + range(2, 0, -1)
 for n, x in enumerate(text):
   fence[rails[n % len(rails)]][n] = x
 return [c for rail in fence for c in rail if c is not None]
 
def decode(text):
  'decodes rail fence cipher.... magic lol'
  text = ''.join(map(chr, text))
  rng = range(len(text))
  pos = trans(rng)
  answer = ''.join(text[pos.index(n)] for n in rng)
  return  answer#map(ord, answer)

def main():
  cipher = map(ord, raw_input('>Enter Plaintext: '))
  key = map(ord, raw_input('>Enter Key: '))
  if len(cipher) != len(key):
    key = key + [0]*(len(cipher) - len(key)) 
  lst = encryption(cipher, key)
  print lst
  
  print decryption(lst, key)
  
if __name__ == '__main__':
  main()
 
  
  
  
  
