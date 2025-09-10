# crie um codigo python que verifique se a senha digitada
# pelo usuario for "1234", exiba "acesso permitido

# etapas para resolução
# criar uma variavel e a atribuir a ela uma senha
# atraves de  um input solicitar a senha do usuario
# atrasves da condicional checar se a senha é igual a senha
# armazenada 
# liberar ou nao o acesso ao usuario

senha_certa = "1234"
senha = input("Digite sua senha: ")
if senha == senha_certa:
    print("Acesso Liberado")
else:
    print("Acesso Negado. Tente novamente mais tarde!")