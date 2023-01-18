# Cryptography-2
Berisi beberapa langkah dari proses enkripsi dan dekripsi algoritma kriptografi modern, AES (Advanced Encryption Standard) dan DES (Data Encryption Standard).

## AES 
Langkah-langkah pada proses ekripsi antara lain :
  - Add round key
  - Sub byte [✓]
  - Shift row [✓]
  - Mix column

Sedangkan tahapan pada proses dekripsi yaitu :
  - Add round key
  - Inverse sub byte
  - Inverse shift row
  - Inverse mix column [✓]

## DES
Tahapan pada proses enkripsi antara lain :
  - Initial permutation [✓]
  - 16 rounds
    - Expansion box
    - XOR
    - S box [✓]
    - Permutation
  - Final permutation
