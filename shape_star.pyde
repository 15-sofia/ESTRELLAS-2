def septup():
 size(600,600)
  
  

def draw():
 h = (random(600))
 k = (random(600))
 r = (random(10, 50))

 beginShape()

 for i in range(1,7):
    fill(250,223,15)
    vertex(h + r * cos(i * PI / 3), k + r * sin(i * PI / 3))
    vertex(h + (r / 2) * cos(i * PI / 3 + PI / 6), k + (r / 2) * sin(i * PI / 3 + PI / 6))
 endShape(CLOSE)   
