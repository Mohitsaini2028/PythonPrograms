#Write a function that computes the area of a rectangle. Then, write a second function that calls this function three times to compute the surface area of a rectangular solid.


def areaOfRectangle(l,b):
    return l*b

def surfaceAreaOFRectangleSolid(l,b):
    return 2*areaOfRectangle(l,b)+2*areaOfRectangle(l,b)+2*areaOfRectangle(l,b)

print(surfaceAreaOFRectangleSolid(2,4))
