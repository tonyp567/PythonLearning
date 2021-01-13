import time, sys
indent = 0      #how many spaces are indented
indentIncreasing = True #determines increasing/decreasing

try:
    while True:         #loop continues until Ctrl-C ends the program
        print(' '*indent, end='')
        print('*******')
        time.sleep(.1)  #pause for .1 second

        if indentIncreasing:
            indent += 1
            if indent == 10:        #change direction
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:       #Ctrl-C ends loop
    sys.exit()