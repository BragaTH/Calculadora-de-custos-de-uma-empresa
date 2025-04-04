def calcular_lucro():
    while True:
        try:
            total_alunos = int(input("Digite o número total de alunos na turma:"))
            if total_alunos < 0:
                print ("O número de alunos não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Digite um número inteiro válido")
    
    
    while True:
        try:
            alunos_reciclagem = int(input("Digite o número de alunos de reciclagem:"))
            if alunos_reciclagem < 0:
                print ("O número de alunos de reciclagem não pode ser negativo.")
            elif alunos_reciclagem > total_alunos:
                print ("O número de reciclagem não pode ser maior que o número total de alunos.")
            else:
                break
        except ValueError:
            print ("Digite um número inteiro válido")
    
    
    alunos_novos = total_alunos - alunos_reciclagem
    receita = (alunos_novos * 1050) + (alunos_reciclagem * 525) #1050 e 525 são os valores do curso.

    print("\nA receita gerada pela nova turma é: ")
    print(f"- Alunos novos ({alunos_novos}): R${alunos_novos * 1050:.2f}")
    print(f"- Alunos de reciclagem ({alunos_reciclagem}): R${alunos_reciclagem * 525:.2f}")
    print(f"Receita total: R${receita:.2f}")

    while True:
        desp_fix = input("\nDeseja calcular os gastos para obter o lucro final? (s/n): ").strip().lower()
        
        if desp_fix == 's':
            break        

        elif desp_fix == 'n':
            return # Sai da função se o usuário não quiser calcular os gastos
        
        else:
            print ("Digite apenas 's' para Sim ou 'n' para Não.")

    despesas = {
        "Contador": 1412,
        "Recepcionistas": 2000 * 2, #São duas recepcionistas
        "Aluguel": 2400,
        "Internet": 300
    }

    def pedir_valor(mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                if valor < 0:
                    print ("O valor não pode ser negativo.")
                else:
                    return valor
            except ValueError:
                print ("Digite um valor númerico válido.")
    
    despesas ["Luz"] = pedir_valor("Digite o valor gasto com a luz: ")
    despesas ["Água"] = pedir_valor("Digite o valor gasto com a água: ")

    while True:
        nome_despesa = input("Digite o nome da despesa extra (ou 'sair' para finalizar): ")
        if nome_despesa.lower() == 'sair':
            break
        else:
            despesas[nome_despesa] = pedir_valor (f"Digite o valor gasto com {nome_despesa}: ")

    despesas_professores = (
        (160 * 3 * 8 ) +  # Torquato - R$160/hora, 3h por aula, 8 aulas
        (140 * 3 * 2 ) +  # Renato - R$140/hora, 3h por aula, 2 aulas
        (140 * 3 * 2 )    # Feudmann - R$140/hora, 3h por aula, 2 aulas
    )


    despesas_totais = despesas_professores + sum(despesas.values())
    lucro = receita - despesas_totais

    print ("\nResultados: ")
    print (f"Receita total: R${receita:.2f}")
    print (f"Despesas totais: R${despesas_totais:.2f}")
    print (f"Lucro final: R${lucro:.2f}")

    
    while True:
        ver_detalhes = input("\nDeseja ver o detalhamento das despesas? (s/n): ").strip().lower()
        if ver_detalhes == 's':
            print ("\nDetalhamento das Despesas: ")
            for nome, valor in despesas.items():
                print (f"- {nome}: R${valor:.2f}")
            print (f"- Professores: R${despesas_professores:.2f}")
            break

        elif ver_detalhes == 'n':
            break
        else:
            print ("Digite apenas 's' para Sim ou 'n' para Não. ")
        
calcular_lucro()