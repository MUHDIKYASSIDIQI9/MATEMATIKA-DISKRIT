print("TABEL KEBENARAN KONJUNGSI")
print("-------------------------")
#header tabel 
print("\n|P\t|Q\t|P AND Q|")
print("-------------------------")
#Menggunakan Operator Logika AND 
for P in [True,False]:
    for Q in [True,False]:
        Konjungsi= P and Q
        print(f"{P}\t{Q}\t{Konjungsi}")
print("\n|P\t|Q\t|P AND Q|")
print("-------------------------")
print("TABEL KEBENARAN DISJUNGSI")
print("-------------------------")
#Menggunakan Operator Logika or
for P in [True,False]:
    for Q in [True,False]:
        Disjungsi= P or Q
        print(f"{P}\t{Q}\t{Disjungsi}")
print("\n|P\t|Q\t|P AND Q|")
print("-------------------------")
print("TABEL KEBENARAN NEGASI")
print("-------------------------")
#Menggunakan Operator Logika not
for P in [True,False]:
    for Q in [True,False]:
        Negasi= not P
        print(f"{P}\t{Q}\t{Negasi}")
print("\n|P\t|Q\t|-P OR Q|")
print("-------------------------")
print("TABEL KEBENARAN NEGASI")
print("-------------------------")
#Menggunakan Operator Logika not or 
for P in [True,False]:
    for Q in [True,False]:
        Negasi= not P or Q
        print(f"{P}\t{Q}\t{Negasi}")
      
