def inverter_string(s):
    string_invertida = ""
    comprimento = len(s)
    for i in range(comprimento - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

entrada = input("Digite uma string para inverter: ")

resultado = inverter_string(entrada)

print(f"String invertida: {resultado}")
