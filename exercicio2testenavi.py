a1=input("Nome do Aluno 1: ")
n1=int(input("Nota do Aluno 1: "))
a2=input("Nome do Aluno 2: ")
n2=int(input("Nota do Aluno 2: "))
a3=input("Nome do Aluno 3: ")
n3=int(input("Nota do Aluno 3: "))
a4=input("Nome do Aluno 4: ")
n4=int(input("Nota do Aluno 4: "))
a5=input("Nome do Aluno 5: ")
n5=int(input("Nota do Aluno 5: "))

if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    ma=a1
    mn=n1
elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
    ma=a2
    mn=n2
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
    ma=a3
    mn=n3
elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
    ma=a4
    mn=n4
else:
    ma=a5
    mn=n5

print ("O melhor aluno é o(a) ", ma,", com a nota ", mn)
