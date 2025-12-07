Fin = open("input.txt")
sum = 0
suma = []

for s in Fin:
    s = s.strip()
    if s.isdigit():
        sum += int(s)
        print(s)
    else:
        for i in s:
            if i.isdigit():
                suma.append(i)
                print(suma)
            elif i.isalpha() and suma:
                x = int(''.join(suma))
                print(x)
                sum  = sum + x
                suma = []
        if suma:
            x = int(''.join(suma))
            sum = sum + x
            suma = []

Fin.close()           
print(sum)             
