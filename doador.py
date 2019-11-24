abo_paciente = input()
rh_paciente = input()
abo_doador = input()
rh_doador = input()

paciente = abo_paciente + rh_paciente
doador = abo_doador + rh_doador

if abo_paciente == 'A' and abo_doador == 'B' or abo_doador == 'AB':
    print('incompatível')

elif abo_paciente == 'B' and abo_doador == 'A' or abo_doador == 'AB':
    print('incompatível')

elif abo_paciente == 'O' and abo_doador == 'A' or abo_doador == 'B' or abo_doador == 'AB':
    print('incompatível')

elif paciente == 'AB+':
    print('compatível')

elif paciente == 'A-' and abo_doador == 'B' or abo_doador == 'AB' or doador == 'A+' or doador == 'O+':
    print('incompatível')

elif paciente == 'B-' and abo_doador == 'A' or abo_doador == 'AB' or abo_doador == 'B+' or abo_doador == 'O+':
    print('incompatível')

elif paciente == 'AB-' and doador == 'A+' or doador == 'B+' or doador == 'AB+' or doador == 'O+':
    print('incompatível')

elif paciente == 'O-' and abo_doador == 'A' or abo_doador == 'B' or abo_doador == 'AB' or doador == 'O+':
    print('incompatível')


else:
    print('compatível')
