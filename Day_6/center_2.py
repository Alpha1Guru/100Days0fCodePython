from library import *
def mark_center():
    num_of_moves = 0
    while front_is_clear():
        move()
        num_of_moves += 1
    turn_around()
    target_position = num_of_moves//2
    for _ in range(target_position):
        move()

    if right_is_clear():
        turn_right()
        num_of_moves = 0
        while front_is_clear():
            move()
            num_of_moves += 1
        turn_around()
        target_position = num_of_moves//2
        for _ in range(target_position):
            move()
        put()
    else:
        put()

        
mark_center()
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