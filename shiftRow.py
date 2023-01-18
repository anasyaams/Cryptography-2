#Shift Row in AES Encryption
def ShiftRow(msg):
  state = [[] for j in range(4)]
  for r in range(4):
    for c in range(4):
      state[r].append(msg[r + 4 * c])
  
  state = np.array(state)

  for i in range(1, 4):
      state[i] = np.append(state[i, i:], state[i, :i])
  
  return state

#test
pt = "FUNGSISHIFTROW80"
print(ShiftRow(pt))
