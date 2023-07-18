#leia um valor em metros e converta para centimetros e milimetros e mostre o resultado
num_m = float(input('Digite um numero em metros: '))
num_cm = (num_m * 100)
num_mm = (num_m * 1000)
print('O numero digitado foi: {}m\nconvertido para centimetros é: {}cm\nconvertido para milimetros é: {}mm'.format(num_m, num_cm, num_mm))