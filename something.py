
import sys
try:
    if len(sys.argv) > 1 :
       
        cmd_parameter1 = ''.join(sys.argv[1])
    print(cmd_parameter1)
except:
    print('no cmd argument provided') 