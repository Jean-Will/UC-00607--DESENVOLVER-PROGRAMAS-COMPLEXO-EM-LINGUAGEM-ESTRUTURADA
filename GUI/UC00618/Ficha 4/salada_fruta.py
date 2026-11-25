from ligacao import conectar

con = conectar()
if not con:
    print("Nao consegui estabelecer conexao com a base de dados")
    exit()

cursor = con.cursor()

sql = "SELECT nome, precounit FROM produto;"

cursor.execute(sql)
resp = cursor.fetchall()
#print(resp)

for tup in resp:
    print(f"Fruta: {tup[0]}\nPreco: {tup[1]:.2f}\n{" ❤️ "*12}")