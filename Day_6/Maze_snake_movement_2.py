from library import *

#Snake Around Variations
def snake_anticlockwise_tracker():

    put() #Only works if a token was given
    moves = 0 #to count number of translational motion made
    while True:
        if wall_in_front() and not right_is_clear():
            turn_left()
        if front_is_clear() and wall_on_right():
            move()
            moves+=1
        elif right_is_clear() and front_is_clear():
            turn_right()
            move()
            moves+=1
        elif wall_in_front() and right_is_clear():
            turn_right()
            move()
            moves += 1
        #This is to pick up items if it was a marker token we stop
        if object_here() and moves>0:
            for item in object_here():
                if item == "apple":
                    take("apple")
                elif item == "token":
                    done()

def snake_anticlockwise_dead_end():
    """Stops at a dead end"""
    while True:
        #Removing the first part will make the car turn around and continue it's journey when it hit a dead
        if dead_end():
            done()
        if wall_in_front() and not right_is_clear():
            turn_left()
        if front_is_clear() and wall_on_right():
            move()
        elif right_is_clear() and front_is_clear():
            turn_right()
            move()
        elif wall_in_front() and right_is_clear():
            turn_right()
            move()
 
def snake_anticlockwise_lm(length=27):
    moves = 0
    length = length
    while moves < length:
        if wall_in_front() and not right_is_clear():
            turn_left()
        if front_is_clear() and wall_on_right():
            move()
            moves+=1
        elif right_is_clear() and front_is_clear():
            turn_right()
            move()
            moves+=1
        elif wall_in_front() and right_is_clear():
            turn_right()
            move()
            moves+=1

def snake_anticlockwise():
    while True:
        if wall_in_front() and not right_is_clear():
            turn_left()
        if front_is_clear() and wall_on_right():
            move()
        elif right_is_clear() and front_is_clear():
            turn_right()
            move()
        elif wall_in_front() and right_is_clear():
            turn_right()
            move()

def snake_clockwise():
    face_west()
    while True:
        #print(wall_on_left())
        if front_is_clear() and wall_on_left():
            move()
        if wall_in_front() and wall_on_left():
            if right_is_clear():
                turn_right()
                move()
            else:
                turn_around()
                move()
        if right_is_clear() and not wall_on_left():
            turn_left()
            move()
           

def snake_anticlockwise_at_goal():
    """Stops at goal"""
    while not at_goal():
        if wall_in_front() and not right_is_clear():
            turn_left()
        if front_is_clear() and wall_on_right():
            move()
        elif right_is_clear() and front_is_clear():
            turn_right()
            move()
        elif wall_in_front() and right_is_clear():
            turn_right()
            move()

snake_anticlockwise_at_goal()
#snake_clockwise()
#snake_anticlockwise()
#snake_anticlockwise_lm()
#snake_anticlockwise_dead_end()
#snake_anticlockwise_tracker()              

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
           
def face_north():
    while not is_facing_north():
        turn_left()

def face_south():
    face_north()
    turn_around()

def face_east():
    face_north()
    turn_right()

def face_west():
    face_north()
    turn_left()
    
def jump_the_hurdle():
    face_north()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

def wall_on_left():
    turn_left()
    result = wall_in_front()   # now the "front" is the original left
    turn_right()
    return result

    
def wall_on_both_sides():
    return wall_on_right() and wall_on_left()

def dead_end():
    return wall_on_both_sides() and wall_in_front()


#The Make Square
def make_square_clockwise():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def make_square_anticlockwise():
    for _ in range(4):
        move()
        turn_left()
