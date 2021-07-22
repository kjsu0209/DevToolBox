# DevTool: ddl to java
# How to run: Python 3.x shell
# In use
#    => Create dao from ddl
#    => Change pythonic name following java naming rule

# DDL to CamelCase
import clipboard

while(True):
    in_str = input('input:').split('_')

    if len(in_str) == 1:
        print('end')
        break

    out_str = ''

    for s in in_str:
        out_str += s.capitalize()


    print(out_str, 'is pasted in ur clipboard')
    clipboard.copy(out_str)
