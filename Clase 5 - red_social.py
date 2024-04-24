nombre = "Juan"
edad = 25
dni = "5012345"
control_parental = None
print(control_parental)

if (edad < 12):
    print("No podés crearte una cuenta por ser menor a 12 años")
elif (edad >= 13 and edad <= 17):
    control_parental = True
    print("Te creaste una cuenta correctamente")
    print("Control parental: ", control_parental)
else:
    control_parental = False
    print("Te creaste una cuenta correctamente")
    print("Control parental: ", control_parental)