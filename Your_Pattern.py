'''
    Type your name and see what happens  you can get pattern of any "string".
    where each letter is programmed in a different way.
            
            -- Rishabh Sikarwar()
'''

n=7 

# Where n is size of the letter.

def A():
    for i in range (n+1):
        j = n-i
        if i == round(n/2):
            print (j*" "+"a"+i*"aa"+"a")
        else:
            print (j*" "+"a"+i*"  "+"a")
def B():
    for i in range(n):
        if i == 0 or i == n-1 or i ==int(n/2):
            print (int(n/2)*"b ")
        else:
            print ("b"+int(n/2)*"  "+"b")
def C():
    for i in range(n):
        if i == 0 or i ==n-1:
            print(round(n/2)*" c")
        else:
            print ("c")
def D():
    for i in range(n):
        if i == 0 or i == n-1 :
            print (int(n/2)*"d ")
        else:
            print ("d"+int(n/2)*"  "+"d")
def E():
    for i in range(n):
        if i == 0 or i == n-1 or i ==int(n/2):
            print (round(n/2)*"e ")
        else:
            print ("e")
def F():
    print((n-1)*"f ")
    for i in range(n-1):
        if i ==int(n/2)-1:
            print((int(n/2)+1)*"f ")
        else:
            print("f")
def G():
    for i in range(n):
        if i == 0 or i==n-1:
            print(round(n/2)*" g")
        elif 0<i<int(n/2):
            print("g")
        elif int(n/2)<i<n-1:
            print("g"+n*" "+"g")
        else:
            print("g"+(n-1)*" "+3*"g")
def H():
    for i in range(n):
        if i == int(n/2):
            print(round(n/2)*"hh")
        else:
            print ("h"+int(n/2)*"  "+"h")
def I():
    for i in range(n):
        if i == 0 or i ==n-1:
            print(n*"i")
        else:
            print (int(n/2)*" "+"i")
def J():
    for i in range(n):
        if i == 0:
            print(n*"j")
        elif i == n-1:
            print (round(n/2)*"j")
        else:
            print (round(n/2)*" "+"j")
def K():
    j = 0
    for i in range(n):
        if i <= int(n/2):
            j = n-(2*i)
            print ("k"+j*" "+"k")
        else:
            j+=1
            print("k"+j*"  "+"k")
def L():
    for i in range(n-1):
        print ("l")
    print(round(n/2)*"l ")
def M():
    string=""
    for i in range (7):
        for j in range(7):
            if (j == 0 or j==6 or (i ==1 and (j==1 or j==5)) or (i==2 and (j==2 or j==4)) or (i==3 and j==3)):
                string+="m "
            else:
                string+="  "
        string+="\n"
    print(string)
def N():
    for i in range(n):
        j =n-i
        print("n"+i*" "+"n"+j*" "+"n")
def O():
    for i in range(n):
        if i == 0 or i ==n-1:
            print(round(n/2)*" o")
        else:
            print ("o"+n*" "+"o")
def P():
    for i in range(n):
        if i == 0 or i == int(n/2) :
            print (int(n/2)*"p ")
        elif 0<i<n/2:
            print ("p"+int(n/2)*"  "+"p")
        else:
            print("p")
def Q():
    for i in range(n+1):
        if i == 0 or i ==n-1:
            print(round(n/2)*" q")
        elif i==n:
            print ((n-1)*" "+round(n/4)*"q")
        else:
            print ("q"+n*" "+"q")
def R():
    j=0
    for i in range(n+1):
        if i == 0 or i == int(n/2) :
            print (int(n/2)*"r ")
        elif 0<i<n/2:
            print ("r"+int(n/2)*"  "+"r")
        else:
            print("r"+j*"  "+"r")
            j+=1
def S():
    for i in range(n):
        if i in (0,n-1,int(n/2)):
            print(round(n/2)*"s ")
        elif 0<i<int(n/2):
            print("s")
        else:
            print ((n-1)*" "+"s")
def T():
    print(n*"t ")
    for i in range(1,n):
        print ((n-1)*" "+"t")
def U():
    for i in range(n):
        if i ==n-1:
            print (" "+ round(n/2)*"uu"+" ")
        else:
            print ("u"+ round(n/2)*"  "+"u")
def V():
    for i in range (n+1):
        j = n-i
        print(i*" "+"v"+j*"  "+"v")
def W():
    string=""
    for i in range (7):
        for j in range(7):
            if (j == 0 or j==6 or (i ==5 and (j==1 or j==5)) or (i==4 and (j==2 or j==4)) or (i==3 and j==3)):
                string+="w "
            else:
                string+="  "
        string+="\n"
    print(string)
def X():
    string=""
    for i in range (7):
        for j in range(7):
            if ((j == 0 and i ==0) or (i==6 and j==0) or (i==0 and j== 6) or (j==6 and i ==6) or ((i ==1 or i==5) and (j==1 or j==5)) or ((i==2 or i ==4) and (j==2 or j==4)) or (i==3 and j==3)):
                string+="x "
            else:
                string+="  "
        string+="\n"
    print(string)
def Y():
    a=int(n/2)
    for i in range (a+1):
        j = a-i
        print(i*" "+"y"+j*"  "+"y")
    for i in range ((a+1),n):
        print(a*" "+"y")
def Z():
    for i in range(n):
        j = n-i
        if i==0 or i ==n-1:
            print(round(n/2)*" z")
        else:
            print(j*" "+"z")
def space():
    for i in range(5):
        print("\r")
switcher ={
    "a":A,
    "b":B,
    "c":C,
    "d":D,
    "e":E,
    "f":F,
    "g":G,
    "h":H,
    "i":I,
    "j":J,
    "k":K,
    "l":L,
    "m":M,
    "n":N,
    "o":O,
    "p":P,
    "q":Q,
    "r":R,
    "s":S,
    "t":T,
    "u":U,
    "v":V,
    "w":W,
    "x":X,
    "y":Y,
    "z":Z,
    " ":space
}
user_input=(input("Type your name: \n\n>>>")).lower()
lst=list(user_input)
for i in lst:
    print(2*"\n")
    switcher[i]()
#bye=input("Press \"Enter\" to exit.") 

# I used line "232" to make it perfectly executable in Computer in "exe" format.
# But Here it has no use, so i am commenting it out.
