#S-Box 7 in DES Encryption
def index(x):
  msb = x >> 7
  lsb = x & 1
  row = (msb << 1) ^ lsb
  col = (x >> 1) & 0xf

  return row * 16 + col

def sBox7(msg):
  sB7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
         13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
         1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
         6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
  
  res = []
  pt = []
  temp = []

  for i in msg:
    pt.append(ord(i)) 

  for i in range (len(pt)):
    temp.append(sB7[index(pt[i])])
  print("hasil desimal\t: ", temp)
  
  for i in range (len(temp)):
    res.append(dec2bin(temp[i]))
  print("hasil biner\t: ", res)

#test
pt = "STUJUH"
sBox7(pt)
