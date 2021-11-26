def data_types():
  ans = [ 3, '', 2.0, True, [], {}, (), set() ]
  ans = list(map(get_type_name, ans))
  print(ans)

def get_type_name(obj):
  return obj.__class__.__name__


if __name__ == '__main__':
  data_types()