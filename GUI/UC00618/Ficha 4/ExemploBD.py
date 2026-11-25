# conectar-se a bd juju;
# cliente (cod, nome,morada)
# produto(cod, nome, precounit, validade)
#vender(cod, pvenda , codprod, codcl)

import mysql.connector as ligar

try:
    con = ligar.connect(host ="localhost", user="root",password="",database="juju")
    print("Conexao a juju com sucesso! ")
except:
    print("Erro na conexao! Verifique Credenciais !!")