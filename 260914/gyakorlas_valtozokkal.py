# 8. feladat
a = 5
b = 10
print(f"a={a}, b={b}")
 
print(f"a={a*2}, b={b*2}")
 
# operátorok
# aritmetikai operátor: műveleti jelek: + - * / //-egész osztás, % - maradékos osztás
# értékadó operátor: =
# összevont értékadó operátor: += -= *= /= %= //=
 
 
print(10%3) # csak a maradékot adja vissza
print(10//3) # csak az egész részt adja vissza, levágja a tizedesjegyeket
 
 
a = a*2
b *= 2
print(f"a={a}, b={b}")
 
a += 1
b -= 1
print(f"a={a}, b={b}")
 
a= 66
print(f"a={a}, b={b}")
 
osszeg = a+b
 
"""változók elvárásai:
- mindig kisbetűvel kezdődik
- mindig az abc betűivel kezdődik
- nem kezdődhet számmal vagy különleges karakterrel (_ kivétel)
- nincs benne ékezet
- nem használhatunk foglalt szakat: (print, type, int, float... )
- ne legyen ugyanaz a neve, mint a file neve
"""
 
print(f"a + b összege: {a} + {b} = {osszeg}")
 
# 9. feladat

a = 1
b = 7
c = -3

print(f"(a-b)/c = ({a}-{b})/{c} = {(a-b)/c}")
print(f"(a+b)*(2a-c) = ({a}+{b})*(2*{a}-{c}) = {(a+b)*(2*a-c)}")
print(f"(3a-3b)/c = (3*{a}-3*{b})/{c} = {(3*a-3*b)/c}")
print(f"2ac+4b = 2*{a}*{c}+4*{b} = {2*a*c+4*b}")

# 10. feladat
x = 10
y = 3
print(  f"x\t=\t\t{x}\n"
        f"y\t=\t\t{y}\n"
        f"{'-'*30}\n"
        f"x+y\t=\t\t{x+y}\n"
        f"x-y\t=\t\t{x-y}\n"
        f"x*y\t=\t\t{x*y}\n"
        f"x/y\t=\t\t{x/y}\n"
        f"x//y\t=\t\t{x//y}\n"
        f"x%y\t=\t\t{x%y}\n"
)
