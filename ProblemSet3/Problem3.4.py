#"TypeError: '>' not supported between instances of 'int' and 'str'" 
# How is this happening" 
#fixed with int
print ("How long is song?")
x = input ()
y = 2
c = 4
if y > int(x):
  print ("Short song")

if y < int(x) and int(x) < c:
    print ("medium song")

if int(x) > c:
   print ("long song")

