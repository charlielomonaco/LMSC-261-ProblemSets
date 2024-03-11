# I dont know how to add the comma after the number
#The rest of it should work fine
print ("What is the song tempo in BPM")
bpm = input ()
print ("how long is the song in seonds?")
length = input ()

bps = int (bpm) / 60

c = 0

textone = "At second"
texttwo = "total beats:"

while c < int (length): 
    c += 1
    w = bps * c
    if c== int(length)+1:
        continue
    print (textone,c,texttwo,w)

