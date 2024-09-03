def inverter_string(s):
    string_invertida = ''
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

def main():
    string_original = input("Digite a string para inverter: ")
    
    string_invertida = inverter_string(string_original)
    
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
