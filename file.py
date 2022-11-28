from ast import main

while True:
        
    try:
        line :str= input("Введите строку: ")
        if len(line) <= 3:
            print("Введите больше 3-ёх букв")
            continue
        if not line.isalpha():
            print("Строка должна быть без цифр и символов")
            continue

        path   =  "files/" + line + ".txt"

        with open(path, "w") as fo:
            pass

    except Exception as e:
         print(e)
