# input() stores the received value as a string

import turtle as t

def main():
    distance = input("set a distance in hundreds of pixels [1-9]:") #python binds the value in a variable
    # t.fd(100*distance) #fails. why?
    t.setup(1000,100)
    t.setworldcoordinates(0,-50,1000,50)
    t.fd(100*int(distance))
    t.done()

main()