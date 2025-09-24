
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

