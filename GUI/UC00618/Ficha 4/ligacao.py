# conectar-se a bd juju;
# cliente (cod, nome,morada)
# produto(cod, nome, precounit, validade)
#vender(cod, pvenda , codprod, codcl)

import mysql.connector as ligar


def conectar():
    try:
        con = ligar.connect(host ="localhost", user="root",password="",database="juju")
        print("\nConexao a juju com sucesso! \n")
        return con
        
    except:
        print("\nErro na conexao! Verifique Credenciais !!\n")
        return False