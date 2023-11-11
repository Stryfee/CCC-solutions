ins = input();
a = ""
b = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
nums = False;
for i in ins:
  if(nums==True):
    if(b.count(i)==0):
      nums=False;
      print(a);
      a = ''
      a+=i
      continue;
    else:
      a+=i
      continue;
    
  if(i == '+'):
    a += ' tighten '
    nums = True
    continue;
  if(i == '-'):
    a += ' loosen '
    nums = True;
    continue;
  a+=i

print(a)
    
  
  
  