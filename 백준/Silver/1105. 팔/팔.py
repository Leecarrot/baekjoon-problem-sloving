L, R = map(str, input().split())

if len(L) != len(R):
  print(0)
else:
  cnt = 0
  for i in range(len(L)):
    if L[i] == R[i] and L[i] !='8':
      continue
    if L[i] == '8' and R[i] =='8':
      cnt+=1
    else:
      break
  print(cnt)
