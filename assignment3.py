import sys
liste= {}
commands=[]
with open(sys.argv[1]) as smn:
    for line in smn:
        splitted_line=line.split(":")
        liste[splitted_line[0]]=splitted_line[1].split()
with open(sys.argv[2]) as com:
    for line in com:
        commands.append(line.strip("\n"))
o=open("output.txt", "w")
def ANU(username):
    if username in liste:
        o.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")
    else:
        liste[username]=list("")
        o.write(f"User {username} has been added to the social network successfully\n")
def DEU(username):
    if username in liste:
        for i in liste[username]:
            liste[i].pop(liste[i].index(username))
        liste.pop(username)
        o.write(f"User {username} and his/her all relations have been deleted successfully\n")
    else:
        o.write(f"ERROR: Wrong input type! for 'DEU'!--There is no user named {username}!!\n")
def ANF(username,username2):

    if username in liste and username2 in liste:
        if username in liste[username2]:
            o.write(f"ERROR: A relation between {username} and {username2} already exists!!\n")
        else:
            liste[username].append(username2)
            liste[username2].append(username)
            o.write(f"Relation between {username} and {username2} has been added successfully\n")
    elif username in liste:
        o.write(f"""ERROR: Wrong input type! for 'ANF'! -- No user named {username2} found!!\n""")
    elif username2 in liste:
        o.write(f"""ERROR: Wrong input type! for 'ANF'! -- No user named {username} found!!\n""")
    else:
        o.write(f"""ERROR: Wrong input type! for 'ANF'! -- No user named {username} an {username2} found!!\n""")
def DEF(username, username2):
    if username in liste and username2 in liste:
        if username in liste[username2]:
            liste[username].pop(liste[username].index(username2))
            liste[username2].pop(liste[username2].index(username))
            o.write(f"Relation between {username} and {username2} has been deleted successfully\n")
        else:
            o.write(f"ERROR: No relation between {username} and {username2} found\n")
    elif username in liste:
        o.write(f"""ERROR: Wrong input type! for 'ANF'! -- No user named {username2} found!!\n""")
    elif username2 in liste:
        o.write(f"""ERROR: Wrong input type! for 'ANF'! -- No user named {username} found!!\n""")
    else:
        o.write(f"""ERROR: Wrong input type! for 'ANF'! -- No user named {username} an {username2} found!!\n""")
def CF(username):
    if username in liste:
        o.write(f"User {username} has {len(liste[username])} friends\n")
    else:
        o.write(f"ERROR: Wrong input type! for 'CF'! -- No user named {username} found!\n")
def FPF(username,max_distance):
    if username in liste:
        if 1<=max_distance<=3:
            arkadas_oneri=[]
            for i in liste[username]:
                arkadas_oneri.append(i)
            if max_distance == 1:
                for i in liste[username]:
                    arkadas_oneri.append(i)
            elif max_distance==2:
                for i in liste[username]:
                    for b in liste[i]:
                        arkadas_oneri.append(b)
            elif max_distance == 3:
                for i in liste[username]:
                    for b in liste[i]:
                        arkadas_oneri.append(b)
                for i in liste[username]:
                    for b in liste[i]:
                        for c in liste[b]:
                            arkadas_oneri.append(c)



            arkadas_oneri=set(arkadas_oneri)
            arkadas_oneri=list(arkadas_oneri)
            if username in arkadas_oneri:
                arkadas_oneri.pop(arkadas_oneri.index(username))
            arkadas_oneri.sort()
            k="{'"
            k+="', '".join(arkadas_oneri)
            k+="'}"
            o.write(f"User {username} has {len(arkadas_oneri)} possible friends when maximum distance is {max_distance}\n")
            o.write(f"These possible friends:{k}\n")
        else:
            o.write(f"ERROR: Wrong input type! for 'FPF'! -- Maximum distance out of range!\n")

    else:
        o.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named {username} found!\n")
def SF(username,md):
    if username in liste:
        if md>1 and md<4:
            arkadass = []
            mutual_fiends = []

            for i in liste[username]:
                for b in liste[i]:
                    if b != username:
                        arkadass.append(b)

            for b in arkadass:
                if arkadass.count(b) >= md:
                    mutual_fiends.append(b)
            mutual_fiends=set(mutual_fiends)
            mutual_fiends=list(mutual_fiends)
            mutual_fiends.sort()
            if len(mutual_fiends) == 0:
                o.write(f"Dont have any mutual friend!!")
            else:
                o.write(f"Suggestion List for {username} (when MD is {md}):\n")
                for i in mutual_fiends:
                    o.write(f"{username} has {arkadass.count(i)} mutual friends with {i}\n")
                k="'"
                k+="','".join(mutual_fiends)
                k+="'"
                o.write(f"The suggested friends for {username}:{k}\n")
        else:
            o.write(f"Error: Mutually Degree cannot be less than 1 or greater than 4\n")

    else:
        o.write(f"Error: Wrong input type! for 'SF'! -- No user named {username} found!!\n")




for i in commands:
    i=i.split()
    if i[0] == "ANU":
        ANU(i[1])
    elif i[0] == "ANF":
        ANF(i[1],i[2])
    elif i[0] == "DEF":
        DEF(i[1],i[2])
        blabla = "blabla"
    elif i[0] == "CF":
        CF(i[1])
    elif i[0] == "FPF":
        FPF(i[1],int(i[2]))
    elif i[0] == "SF":
        SF(i[1],int(i[2]))
    elif i[0] == "DEU":
        DEU(i[1])
    else:
        o.write("WRONG COMMAND!!\n")

o.close()