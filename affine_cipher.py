# Program is made to encrypt and decrypt words using affine cypher. Program uses .json file types as an input and output. File encrypt.json has word and keys to encrypt file; file decrypt.json to decrypt. Files result_encrypt.json and result_decrypt.json are the output. Idea of the code is to have encrypt OR decrypt word as an input. If you run program multiple times you will have results in one output file, results are appended. 

import json

# TYPE NAME OF JSON FILE THAT IS IN THE SAME FOLDER
with open('encrypt.json') as f: # CHANGE THIS LINE
   data = json.load(f)

# THIS IS ALTERNATIVE WAY OF PREVIOUS STEP, TYPE PATH WHERE THE JSON FILE IS, IF SO - COMMENT PREVIOUS STEP
# path = '/Users/michal/Desktop/python_task/test.json' # CHANGE THIS LINE
# with open(path) as f:
#    data = json.load(f)

# Program logic

# ENCRYPTING
if "encrypt" in data:

  # Creating variables for encrypt
  for i in data['encrypt']:
    a = (i['a'])
    b = (i['b'])
    operation = (i['operation'])
    plainText = (i['plainText'])

  final1 = ''.join([ chr((( a*(ord(t) - ord('A')) + b ) % 26) + ord('A')) for t in plainText.upper().replace(' ', '') ])

  new_dict_encrypt=[{
    'a': a,
    'b': b,
    'operation': operation,
    'plainText': plainText,
    'cryptogram': final1.upper(),
  }]

  with open("result_encrypt.json", "a") as f: # CHANGE A-->W IF YOU WANT TO REPLACE / OVERWRITE PREVIOUS FILE
    json.dump(new_dict_encrypt, f, indent=2)

# DECRYPTING
if "decrypt" in data:

  # Creating variables for decrypt
  for k in data['decrypt']:
    ad = (k['a'])
    bd = (k['b'])
    operationd = (k['operation'])
    cryptogram = (k['cryptogram'])


  a_inv = 0
  final2 =''
  while ad * a_inv % 26 != 1:
		  a_inv += 1

  for c in cryptogram:
		
		  if ord(c) >= 0x41 and ord(c) <= 0x5a:
			  i = ord(c) - 0x41
			  i = ( a_inv * (i-bd) ) % 26
			  final2 += chr(i + 0x41)

		  elif ord(c) >= 0x61 and ord(c) <= 0x7a:
			  i = ord(c) - 0x61
			  i = ( a_inv * (i-bd) ) % 26
		  final2 += chr(i + 0x61)

  new_dict_decrypt=[{
    'a': ad,
    'b': bd,
    'operation': operationd,
    'cryptogram': cryptogram,
    'plainText': final2.upper(),
}]
  with open("result_decrypt.json", "a") as f: # CHANGE A-->W IF YOU WANT TO REPLACE PREVIOUS FILE
    json.dump(new_dict_decrypt, f, indent=2)

# new_dict_encrypt.extend(new_dict_decrypt) # UNCOMMENT IF BOTH ENCRYPT AND DECRYPT ARE IN INPUT JSON FILE

# CREATING NEW JSON FILE      # UNCOMMENT IF BOTH ENCRYPT AND DECRYPT ARE IN INPUT JSON FILE 
# with open("result.json", "a") as f:
    # json.dump(new_dict_encrypt, f, indent=2)
