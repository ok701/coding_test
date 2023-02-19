words = input().upper()
alphabets = list(set(words))
# print('alphabets: ',alphbets)

num = []
for alphabet in alphabets:
  num.append(words.count(alphabet))
# print('alphbets: ',alphabets)

# print('num: ',num)
# print('num.indexmax: ',num.index(max(num)))

# print('num.count: ',num.count(max(num)))

if num.count(max(num)) != 1:
  print('?')

else:
  print(alphabets[num.index(max(num))])
