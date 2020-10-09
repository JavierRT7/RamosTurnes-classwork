def rec_func(input_value):
  item = input_value[0]
  if len(input_value) == 1:
    return item
  else:
    return rec_func(input_value[1:]) + item
  #endif
#end function
print(rec_func('STAR'))