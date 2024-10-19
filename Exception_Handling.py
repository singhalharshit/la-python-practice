try:
    a=10
    print(a/0)
except Exception as e:
    print(e)


try:
    open('new.txt','r')
except Exception as e:
    print(e)


# def askint(a):
#     try:
#         val= int(input('Please enter an Interger: '))
#     except:
#         print('Oops seems like an integer was not entered')
#         try:
#             val= int(input('Please enter an Interger: '))
#         except Exception as e:
#             print(e)
    
#     print(val)

# askint(9)


# Above code only but more optimized 

def askint1():
    while True:
        try:
            val = int(input('Please enter an integer: '))
            break  # Exit the loop if the input is a valid integer
        except Exception as e:  # Catch specifically ValueError
            print('Oops, seems like an integer was not entered. Please try again. And the Error is: ',e)
    
    print(f'The integer entered is: {val}')

askint1()




