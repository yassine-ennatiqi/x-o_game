def printForm():
    for i in range(3):
        for j in range(3):
            print(list1[i][j] , end="  ")
            print("|" , end="  ")
        print("\n================")
def valide():
    for i in range(3):
        for j in range(3):
            if list1[i][j] == "?":
                return False
    return True




list1=[]



for i in range(3):
    list2=[]
    for j in range(3):
        list2.append("?")
    list1.append(list2)

while True :
    printForm()

    lign = (input("entrer le numero de lign: "))
    while lign not in ["1","2","3"]:
        lign = (input("entrer le numero de lign: "))
    col = (input("entrer le numero de colon: "))
    while col not in ["1","2","3"]:
        col = (input("entrer le numero de colon: "))
    form = input("entrer la form: ")
    while form not in ["x","o"]:
        form = input("entrer la form: ")
    lign = int(lign)
    col = int (col)
    list1[lign-1][col-1] = form
    for i in range(3):
        for j in range(3):
            if j == 2:
                if list1[i][j] == list1[i][j-1] == list1[i][j-2]== "o":
                    
                    list1[i][j] = list1[i][j-1] = list1[i][j-2]= "O"
                    printForm()
                    print("moul o howa li rbh")
                    exit()
                if list1[i][j] == list1[i][j-1] == list1[i][j-2]== "x":
                    
                    list1[i][j] = list1[i][j-1] = list1[i][j-2]= "X"
                    printForm()
                    print("moul x howa li rbh")
                    exit()
    for i in range(3):
        for j in range(3):
            if j == 2:
                if list1[j][i] == list1[j-1][i] == list1[j-2][i]== "o":
                   
                    list1[j][i] = list1[j-1][i] = list1[j-2][i]= "O"
                    printForm()
                    print("moul o howa li rbh")
                    exit()
                if list1[j][i] == list1[j-1][i] == list1[j-2][i]== "x":
                    
                    list1[j][i] = list1[j-1][i] = list1[j-2][i]= "X"
                    printForm()
                    print("moul x howa li rbh")
                    exit()  
    for i in range(3):
        for j in range(i , i+1):
            if j == 2:
                if list1[i][j] == list1[j-1][i-1] == list1[j-2][i-2] == "o":
                    
                    list1[i][j] = list1[j-1][i-1] = list1[j-2][i-2] = "O"
                    printForm()
                    print("moul o howa li rbh")
                    exit()
                if list1[i][j] == list1[j-1][i-1] == list1[j-2][i-2]== "x":
                    
                    list1[i][j] = list1[j-1][i-1] = list1[j-2][i-2]= "X"
                    printForm()
                    print("moul x howa li rbh")
                    exit() 
    for i in range(3):
        for j in range(i , i+1):
            if j == 2:
                if list1[i-2][j] == list1[j-1][i-1] == list1[j][i-2]== "o":
                    list1[i-2][j] = list1[j-1][i-1] = list1[j][i-2]= "O"
                    printForm()
                    print("moul o howa li rbh")
                    exit()
                if list1[i-2][j] == list1[j-1][i-1] == list1[j][i-2]== "x":
                    list1[i-2][j] = list1[j-1][i-1] = list1[j][i-2]= "X"
                    printForm()
                    print("moul x howa li rbh")
                    exit() 
    if valide() :
        printForm()
        print("hta hd marbh")
        exit()
    else :
        continue
