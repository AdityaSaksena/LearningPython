list=['john', 'mary', 'peter', 'susan']
list=['bob']+list
list=list+['alice']
list=list[0:3]+list[4:]
print(list)
list=list[0:-2]
print(list)
