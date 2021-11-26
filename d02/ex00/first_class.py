class Must_read:
  try:
    path = 'data.csv'
    with open(path) as file:
      print (file.read())
  except Exception:
    print('File not found ' + path)
  
if __name__ == "__main__":
  pass


# head,tail
# 0,1
# 1,0
# 0,1
# 1,0
# 0,1
# 0,1
# 0,1
# 1,0
# 1,0
# 0,1
# 1,0
# 0,1