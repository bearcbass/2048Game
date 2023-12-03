#This file will be the main file to run the 2048 game.
import logic

if __name__ == '__main__':
    mat = logic.start_game

while(True):
    x = input("Please enter command: ")

    if (x == 'W' or x == 'w'):
        mat, flag = logic.move_up(mat)
        status = logic.get_current_state(mat)
        print(status)

        if(status == "GAME IS NOT OVER"):
            logic.add_new_2(mat)
        
        else:
            break

    elif (x == 'S' or x == 's'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == "GAME IS NOT OVER"):
            logic.add_new_2(mat)
        
        else:
            break
    elif (x == 'A' or x == 'a'):
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == "GAME IS NOT OVER"):
            logic.add_new_2(mat)
        
        else:
            break
    elif (x == 'd' or x == 'D'):
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == "GAME IS NOT OVER"):
            logic.add_new_2(mat)

        else:
            break
    else:
        print("Invalid Key Pressed")

    print(mat)