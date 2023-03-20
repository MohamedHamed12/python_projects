


import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def examples():
    """ 
    This function creates a file called user_manual.txt
    getting input from user and checking it
    it opens the file and appends the formula of equation in it depending on the given number
    using some strings like eq, x, a  and SUB(to subscript numbers)
    to write them in the file
    it also prints the path of the created file
    """
    import os

    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    try:
        number_of_equation = int(input("enter number of equations : "))
    except ValueError:
        file = open('user_manual.txt', 'w', encoding='utf-8', errors='ignore')
        file.write(
            "the number should be an integar(like this 2 or 3 or .....) not string ")
        print("the path of the file is: ", os.path.abspath('user_manual.txt'))
        return 0

    while int(number_of_equation) < 2:
        print("number of equations should at least be 2")
        number_of_equation = int(input("enter number of equations : "))

    file = open('user_manual.txt', 'w', encoding='utf-8', errors='ignore')
    L = ["Number of equations: ", str(number_of_equation), "\n"]
    file.writelines(L)
    a, d, f, zero = "x", "a", "eq", "0"

    for line in range(0, number_of_equation):
        s = str(line+1)
        str1 = (f + s).translate(SUB)
        # print(str1)
        str8 = (d + s + zero).translate(SUB)
        L = [str1, ' : ', ' = ', str8]
        position = 2
        for i in range(0, number_of_equation):
            j = str(i + 1)
            str2 = (d + s + j + a + j).translate(SUB)
            string = ' ' + str2 + ' '
            L[position: -3] = string
            if i == number_of_equation - 1:
                break
            else:
                position = position + len(string)
                L[position: -3] = '+'
            position = position + 1
        file.writelines(L)
        file.write('\n')

    file = open("user_manual.txt", "r", encoding='utf-8', errors='ignore')
    # print(file.readlines())
    file.close()


    # print('\n', '#' * 150)
    print("the path of the file is: ", os.path.abspath('user_manual.txt'))
    # print('#' * 150, '\n')
# examples()
def getting_equations():
    
    try:
        path = open(os.path.abspath('equations.txt'), 'r',
                    encoding='utf-8', errors='ignore')
    except FileNotFoundError:
        f = open('solution.txt', 'w', encoding='utf-8', errors='ignore')
        return f.write("file not found!!")
    
    num=int(path.readline().split()[-1])
    lst=[]
    for line in path:
        line.replace('+',' + ')
        line.replace('-',' - ')
        line=line.replace('=',' = ')
        line=line.strip().split()[1:]
        tmplst=[0]*(num+1)
        for idx ,element in enumerate(line):
            if 'x' not in element :continue
            factor,ordx=element.split('x')
            factor=int(factor)
            if line[idx-1]=='-':factor*=-1
            ordx=int(str(ord(ordx))[3:])
        
            tmplst[ordx-1]=factor
        tmplst[-1]=int(line[-1])
        lst.append(tmplst)
        
       
    return lst












# def examples():
#     num =int(input('hi enter the number of equations : '))
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     file=open('user_manual.txt', 'w')
#     file.write(f'Number of equations: {num}\n')
#     for i in range(1,num+1):
#         eq=''
#         for j in range(1,num+1):
#             if j!=1:eq+='+'               # not add + in last of equation 
#             eq+=f'a{i}{j} x {j}'          # every time  add term such a11x2
#         eq+=f'= a{i}\n'                   # at the end of equation add =a2
#         file.write(eq.translate(SUB))     # write the equation at the end 

# examples()



















# def examples(): #This function creates a file called user_manual.txt
 
#     file=open('user_manual.txt','x',encoding='utf-8',errors='ignore')
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     number_of_equation=int(input("enter number of equations : "))
#     file=open('user_manual.txt','w',encoding='utf-8',errors='ignore')
#     L = ["Number of equations: ",str(number_of_equation)]
#     file.writelines(L)
#     file.write('\n')
#     a="x"
#     d="a"
#     f="eq"
#     zero ='0'
#     for line in range(0,number_of_equation):
#         s=str(line+1)
#         str1=(f+s).translate(SUB)
#         str8=(d+s+zero).translate(SUB)
#         L=[str1,' : ',' = ',str8]
#         position=2
#         for i in range(0,number_of_equation):
#             j=str(i+1)
#             str2=(d+s+j).translate(SUB)
#             str3=(a+j).translate(SUB)
#             string=str2+str3
#             L[position:-3]=string
#             if i==number_of_equation-1 :
#                 break
#             else :
#                position=position+len(string)
#                L[position:-3]=' + '
#             position=position+1
#         file.writelines(L)
#         file.write('\n')
#     file = open("user_manual.txt", "r",encoding='utf-8',errors='ignore')
#     f_contents=file.readlines()
#     # print(f_contents,end='')
#     print( " user_manual is in this path ")
#     print('\n',os.path.join(BASE_DIR, " user_manual.txt"))
#     # print('\n',__file__)
#     file.close()
    
    
# # examples()






# def getting_equations():
    
#     path = open(os.path.join(BASE_DIR, " equations.txt"),'r')
#     num=int(path.readline().split()[-1])
#     lst=[]
#     for line in path:
#         line.replace('+',' + ')
#         line.replace('-',' - ')
#         line=line.replace('=',' = ')
#         line=line.strip().split()[1:]
#         tmplst=[0]*(num+1)
#         for idx ,element in enumerate(line):
#             if 'x' not in element :continue
#             factor,ordx=element.split('x')
            
#             factor=int(factor)
#             if line[idx-1]=='-':factor*=-1
#             ordx=int(str(ord(ordx))[3:])
        
#             tmplst[ordx-1]=factor
#         tmplst[-1]=int(line[-1])
#         lst.append(tmplst)
        
       
#     return lst







# # def examples():
# #     num =int(input('hi enter the number of equations : '))
# #     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
# #     file=open('user_manual.txt', 'w')
# #     file.write(f'Number of equations: {num}\n')
# #     for i in range(1,num+1):
# #         eq=''
# #         for j in range(1,num+1):
# #             if j!=1:eq+=' + '               # not add + in last of equation 
# #             eq+=f'a{i}{j}x{j}'          # every time  add term such a11x2
# #         eq+=f'= a{i}\n'                   # at the end of equation add =a2
# #         file.write(eq.translate(SUB))     # write the equation at the end 

# # examples()
