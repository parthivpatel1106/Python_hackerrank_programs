def print_formatted(n):
    for i in range(n):
        deci=i+1
        decimal=str(deci)
        octa=str(oct(i+1)[2:])
        hexa=hex(i+1)[2:]
        bina=str(bin(i+1)[2:])
        print("",decimal.rjust(2),"",octa.rjust(2),"",hexa.upper().rjust(2),bina.rjust(5))

n=int(input())
result=print_formatted(n)
