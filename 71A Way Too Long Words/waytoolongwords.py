cant = int(input())

for i in range(cant):
  text = input()

  size = len(text)
  if size > 10:
    print(text[0], str(size-2), text[size-1], sep = "")
  else:
    print(text)