# This script calculates points in 2d for a beizier-curve


#this function calculates the middle of 2 values "P1x", "P2x" with a ratio "t"
def tPointSc(P1x, P2x, t):
    ret = ((t * P1x) + ((1 - t) * P2x))
    return ret


#This funktion calculates a single Point "cP" ot the beizier curve at a given Stage "t" therefore 4 Variales are required. you can either calculate x or y coordinates
def currentPointSc(A, B, C, D, t):
    E = tPointSc(A, B, t)
    F = tPointSc(B, C, t)
    G = tPointSc(C, D, t)
    H = tPointSc(E, F, t)
    I = tPointSc(F, G, t)
    cP = tPointSc(H, I, t)
    return cP


#This function is actually calculating the beizier curve. Therefore 4 Points are required as x and y values. Bsp. Point "A": "pAx" and "pAy". The return is a list "bC" with x and y values
def beizierCurve(pAx, pAy, pBx, pBy, pCx, pCy, pDx, pDy):
    steps = int(input("Please enter the number of stages: "))
    bC = []
    for i in range(steps):
        t = i + 1
        t = (t / steps)
        bC.append(currentPointSc(pAx, pBx, pCx, pDx, t))
        bC.append(currentPointSc(pAy, pBy, pCy, pDy, t))
    return bC


Ax = int(input("Please enter a value for Point A, x: "))
Ay = int(input("Please enter a value for Point A, y: "))
Bx = int(input("Please enter a value for Point B, x: "))
By = int(input("Please enter a value for Point B, y: "))
Cx = int(input("Please enter a value for Point C, x: "))
Cy = int(input("Please enter a value for Point C, y: "))
Dx = int(input("Please enter a value for Point D, x: "))
Dy = int(input("Please enter a value for Point D, y: "))

print(beizierCurve(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy))

q = input("Press any ENTER to quit")