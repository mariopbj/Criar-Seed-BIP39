import subprocess

binario = ""

for c in range(1, 24):
    while True:
        palavra = str(input("Digite os 11 bits da " + str(c) + "º linha: "))
        if len(palavra) == 11 and all(char in '01' for char in palavra):
            binario += palavra
            break
        else:
            print("Erro na digitação . Tente novamente")

while True:
        palavra = str(input("Digite os 3 bits da 24º linha: "))
        if len(palavra) == 3 and all(char in '01' for char in palavra):
            binario += palavra
            break
        else:
            print("Erro na digitação . Tente novamente")

comando_sha256 = f'''echo {binario} | shasum -a 256 -0'''

sha256 = subprocess.run(comando_sha256, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

primeiros_2_digitos = sha256.stdout[0:2]
checksum = bin(int(primeiros_2_digitos, 16))[2:]

binario_seed = binario + checksum

contador = 1

for i in range(0, len(binario_seed), 11):
    pedaco_binario = binario_seed[i:i+11]
    inteiro = int(pedaco_binario, 2)

    with open('english.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    if 0 <= inteiro < len(linhas):
        linha_especifica = linhas[inteiro].strip()
        print(f"{contador}) {linha_especifica} ({inteiro})")
    else:
        print("Número da linha fora do intervalo.")
    contador += 1