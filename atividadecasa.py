hora=float(input('Que horas são?'))

if(hora >00.00) and (hora <11.00):
    print('Bom dia')
elif (hora >12.00) and (hora<18.00): 
    print('Boa tarde')
elif (hora >18.00) and (hora <24.00):
    print('Boa noite')
