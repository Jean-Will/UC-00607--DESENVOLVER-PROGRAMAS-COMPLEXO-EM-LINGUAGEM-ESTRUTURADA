"""way = "UC00607/dados.txt"
filePointer = open(way, "r" , encoding="utf-8")
content = filePointer.read() # le conteudo como sendo uma string 

print(f"{content}")
filePointer.close()"""
################################

way = "UC00607/dados.txt"
with open(way,"r", encoding="utf-8") as fp:
    content = fp.read()
print(content)    