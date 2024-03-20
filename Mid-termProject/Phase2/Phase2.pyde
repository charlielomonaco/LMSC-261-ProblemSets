def setup():
    size(150, 150) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def draw():
    fill(0, 0, 255) # Fill in with blue color
    ellipse(50, 50,  100, 100)
    fill(255) # Fill in white color
    ellipse((30),(40), 40, 40)
    ellipse( 70, 40,  40, 40)
    fill(0) # Fill in with black color
    ellipse((30),40,  15, 15)
    ellipse((70),40,  15, 15)
    fill(255) # Fill in white color
    rect(35, 75,  30, 15)
