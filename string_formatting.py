def print_formatted(n):
    w = len(str(bin(n)).replace('0b','')) #this will print length of binary digits without 0b
    for i in range(n):
        deci=i+1
        decimal=str(deci).rjust(w,' ')
        octa=str(oct(i+1)[2:]).rjust(w,' ')
        hexa=hex(i+1)[2:].rjust(w,' ')
        bina=str(bin(i+1)[2:]).rjust(w,' ')
        print(decimal,octa,hexa.upper(),bina)

n=int(input())
result=print_formatted(n)