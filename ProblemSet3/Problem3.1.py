# How do I get rid of the , and ()
#fixed with printing the variables
print ("How long is song in seconds?")
i = input ()
song_duration_in_seconds = int (i)
x = song_duration_in_seconds // 60 
y = song_duration_in_seconds % 60
z = 'minutes and'
w = 'seconds'
r = 'The song duration is'
n = r, x, z, y, w
print (r, x, z, y, w)
print