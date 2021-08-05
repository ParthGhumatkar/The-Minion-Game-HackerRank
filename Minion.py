def minion_game(string):
    Kevin=0
    Stuart=0
    v="AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in v:
            Kevin=Kevin+len(string)-i
        else:
            Stuart=Stuart+len(string)-i    
    
    if Kevin>Stuart:
        print("Kevin",Kevin)
    elif Kevin==Stuart:
        print("Draw")    
    else:
        print("Stuart",Stuart)            



if __name__ == '__main__':
