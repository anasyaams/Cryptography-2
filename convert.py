import binascii
import numpy as np

def asc2bin(text, encoding='utf-8', errors='surrogatepass'):
  res = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
  return res.zfill(8 * ((len(res) + 7) // 8))

def bin2dec(bin):
  binary1 = bin
  decimal, i, n = 0, 0, 0
  while(bin != 0):
    dec = bin % 10
    decimal = decimal + dec * pow(2, i)
    bin = bin // 10
    i += 1
  return decimal

def dec2bin(dec):
  return "{0:b}".format(int(dec))

def bytes2matrix(text):
  return [list(text[i:i+4]) for i in range(0, len(text), 4)]
