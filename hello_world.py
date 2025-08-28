def existance(l):
    pass
print(2+2)
print(7%4)
print(25%7)
#sorry Dr. Ebee if you hate when people do this:
if(False):
    errors = ["print(hljsassf)","print(int('hello'))"," open('python','r')","print('hello\')","existance()"]
    print("hello, World!")
    for i in range(0,len(errors)):
        try:
            exec(errors[i])
        except Exception as e:
            print(e)
# File "c:\Users\aronk\github-classroom\t
# kscs\01-hello-world-and-error-hunt-unsteadyapp\hello_world.py", line 8, in <module>
#    print(int('hello'))
#          ~~~^^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'hello'
#File "c:\Users\aronk\github-classroom\tkscs\01-hello-world-and-error-hunt-unsteadyapp\hello_world.py", line 10
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#File "c:\Users\aronk\github-classroom\tkscs\01-hello-world-and-error-hunt-unsteadyapp\hello_world.py", line 10
#SyntaxError: unterminated string literal (detected at line 10); perhaps you escaped the end quote?