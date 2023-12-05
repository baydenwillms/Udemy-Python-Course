#these functions are for a robot maze and not true Python functions
#maze exercise can be found here: 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json 
#my solution was far fewer lines of code than the solution, while still following the same algorithm as instructed

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#strategy: move along the right-side walls

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    else:
        turn_left()
    
    
