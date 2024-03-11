# How do I get rid of the , and ()
#was printing r and not the variables
print ("Enter a MIDI number between 0 and 127")
y = input()
x = 2**((int(y)-69)/12)*440
w = 'The frequency of the MIDI note number'
z = "is"
r = w, y, z, x
print (w, y, z, x)