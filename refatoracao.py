
#Refatoração
def valida_se_eh_maior_idade(idade): 
    #idade = 17

    #Clientes menores de 18 anos não podem realizar essa operação
    if idade < 18:
        print ("Operacao não permitida")
    else:
        print ("Operacao permitida")

valida_se_eh_maior_idade(18)
valida_se_eh_maior_idade(12)
valida_se_eh_maior_idade(15)
valida_se_eh_maior_idade(27)
valida_se_eh_maior_idade(63)




def soma_valores (valor_1, valor_2):
    return valor_1 + valor_2

# soma 10 com 5 
print (soma_valores(10, 5))
print (soma_valores(27, 51))
print (soma_valores(30, 51))
print (soma_valores(20, 26))


