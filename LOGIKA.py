from tabulate import tabulate
data=[]
for P in [True,False]:
    for Q in [True,False]:
        data.append([P,Q,P and Q, P or Q, not P or Q])
headers=["P", "Q", "P AND Q", "P OR Q", "NOT P OR Q"]
print(tabulate(data, headers, tablefmt="grid"))
