with open('Day4_input.txt', 'r') as file:
    lines = file.readlines()

def p1():
    total = 0
    for line in lines:
        # Fiecare card va fi impartit in 2 parti
        a, b = map(str.split, line.split('|'))
        # In "a" se va regasi prima parte ce cuprinde numarul cardului si numerele castigatoare
        #print(a)
        # In "b" se vor regasi elementele ce vor fi verificate
        #print(b)
        # Se stabilesc elementele comune celor doua parti
        common_elements  = set(a).intersection(set(b))
        #print(common_elements)
        if common_elements:
            # Stabilim puterea la care se va ridica 2 luand in vedere numarul de elemente comune
            power = len(common_elements) - 1
            # Stabilim numarul de puncte al cardului curent
            points = pow(2, power)
            # Stocarea numarului total de elemente
            total += points
        else:
            total += 0 # do nothing
    return total

print(p1())
