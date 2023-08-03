import json
import random

f = open("words.json", encoding="utf8")

words = json.load(f)
choice_c = random.choice(list(words.keys()))

print("Olá, Bem vindo!")
print("##################")

n_choices = 5

while n_choices > 0:

    print("Dica: " + words[choice_c])
    answer_user = input("Data: DDMMAAA\n")

    if len(answer_user) != 8:
        print("Erro!. A entrada deve conter 8 digitos")
        continue
    if answer_user.isdigit():
        check = []
        for i in range(8):
                if answer_user[i] == choice_c[i]
                    check.append("v")
                else:
                        check.append("x")

        print("Resposta: \n")
        print("|".join(check))
        print("|".join(answer_user))
        print("########################")
    else:
         print("Erro!. A entrada deve ser uma data")
         continue

    
    n_choices = n_choices - 1 
