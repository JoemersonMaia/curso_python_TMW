# %%
alunos = [
    ["Ana", 8.5, 7.0, 9.0],
    ["Carlos", 5.0, 6.5, 4.0],
    ["Marcos", 9.5, 8.0, 9.0],
    ["Julia", 3.0, 5.0, 4.5],
    ["Pedro", 7.0, 7.5, 6.0]
]

opcao = input("""
1 - Listar alunos
2 - Mostrar médias
3 - Mostrar aprovados
4 - Mostrar alunos em recuperação
5 - Mostrar reprovados
6 - Melhor aluno
7 - Média geral da turma
8 - Análise da turma
9 - Sair
""")

if opcao == "1":
    for i in alunos:
        print(i[0])

if opcao == "2":
    for i in alunos:
        notas = i[1:]
        media = sum(notas) / len(notas)   
        print(f"{media:.2}")

if opcao == "3":
    for i in alunos:
        notas = i[1:]
        media = sum(notas) / len(notas)   
        if media > 6:
            print(f"{media:.2}")

if opcao == "4":
    for i in alunos:
        notas = i[1:]
        media = sum(notas) / len(notas)   
        if media < 6:
            print(f"{media:.2}")

if opcao == "6":
    for i in alunos:
            notas = i[1:]
            aluno = i[0]
            media = sum(notas) / len(notas)
            if aluno  

