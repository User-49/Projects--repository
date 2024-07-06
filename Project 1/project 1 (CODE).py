dict_civilian = {'kapil': ['kapil2006@', '1A', '976XX XXXX0'], 'aditya': ['aditya200$', '1B', '816XX XXXX7']}
l_civilian = ['kapil', 'aditya']
dict_worker = {'plumber': ["adi234", '849XX XXXX8'], 'electrician': ['goda987', '456XX XXXX9'],
               'carpenter': ['bau567', '678XX XXXX4'], 'painter': ['kamal890', '596XX XXXX4'],
               'cleaner': ['ohm789', '655XX XXXX4'], 'welder': ['hemu452', '458XXX XXX7']}
l_worker = ['plumber', 'electrician', 'carpenter', 'painter', 'cleaner', 'welder']
while True:
    a = 3
    name = input("\nUsername: ")
    if name not in (l_civilian + l_worker) and name != 'admin':
        print('username not in records, try again \n', '-'*80)
        continue
    print("please enter your password")
    while True:
        if a == 0 and name != 'admin':
            if name in l_civilian:
                del dict_civilian[name], l_civilian[l_civilian.index(name)]
            elif name in l_worker:
                del dict_worker[name], l_worker[l_worker.index(name)]
            print("\nyour 3 attempts are up, you are now banned.")
            print("please contact the server moderator for further info-")
            print("email address: abc_morderator@gmail.com \nph.number: 978XXX XXX7 \n", '='*80)
            break
        elif a == 0 and name == 'admin':
            print("\nfor multiple incorrect attempts you have been logged out")
            print("please recheck the password and try again later", '-'*80)
            break
        password = input("Password (or exit): ")
        if password == 'exit':
            print('='*80)
            break
        elif name in dict_civilian and dict_civilian[name][0] == password:
            while True:
                pr_c = dict_civilian[name][3:]
                print("\nwelcome", name, 'what do you wish to do..?')
                print('1. Check profile \n2. Report a problem  \n3. log out \n')
                choice_1 = int(input('enter choice: '))
                if choice_1 == 1:
                    while True:
                        print('-' * 80, '\nprofile-\n\nName: ', name, '\nblock number: ', dict_civilian[name][1])
                        print('registered mobile number: ', dict_civilian[name][2])
                        print('pending requests: ', str(pr_c).count('pending'))
                        print("\nwhat do you wish to do..?\n1. check pending requests\n2. check completed requests")
                        print("3. go back")
                        choice_0 = int(input('\nenter choice: '))
                        if choice_0 == 1:
                            flag = 0
                            print('-'*80, '\nlist of pending requests-')
                            for i in pr_c:
                                if i[2] == "pending":
                                    print(str(pr_c.index(i)+1) + ".", i[1])
                                    print("   assigned worker:", i[0])
                                    flag = 1
                            if flag == 0:
                                print("NO PENDING REQUESTS")
                            h = input("\npress enter to go back")
                        elif choice_0 == 2:
                            flag = 0
                            print('-'*80, "\nlist of requests completed-")
                            for j in pr_c:
                                if j[2] == "completed":
                                    print(str(pr_c.index(j) + 1) + ".", j[1])
                                    print("       confirmed by:", j[0])
                                    flag = 1
                            if flag == 0:
                                print("NO REQUESTS COMPLETED")
                            m = input("\npress enter to exit")
                        elif choice_0 == 3:
                            print('-'*80)
                            break
                        else:
                            print('invalid choice, enter again')
                elif choice_1 == 2:
                    while True:
                        print('-' * 80)
                        problem = input("\nwhat seems to be the issue?\n>")
                        print("\nlist of workers-")
                        for i in range(1, len(l_worker)+1):
                            print(str(i)+". ", l_worker[i-1])
                        t = int(input("\nenter choice: "))
                        if t <= len(l_worker):
                            (dict_civilian[name]).append([l_worker[t-1], problem, "pending"])
                            dict_worker[l_worker[t-1]].append((name, problem))
                            print("request sent\n", "-"*80)
                        else:
                            print('Invalid choice, please recheck and enter again\n')
                            continue
                        break
                elif choice_1 == 3:
                    print("\nyou are now logged out \n", "="*80)
                    break
                else:
                    print('invalid choice enter again\n', '-'*80)
                    continue
            break
        elif name in dict_worker and dict_worker[name][0] == password:
            while True:
                pr_w = dict_worker[name][2:]
                print("\nwelcome employee,", name, ' \nwhat do you wish to do..?')
                print("1. check profile \n2. check pending requests \n3. sign out\n")
                choice_2 = int(input("enter choice: "))
                if choice_2 == 1:
                    print("-"*80, "\nprofile-\naccount: ", name, "\nregistered mobile number: ", dict_worker[name][1])
                    print("requests pending: ", len(pr_w))
                    x = input("\npress enter to go back")
                    print("-"*80)
                elif choice_2 == 2:
                    while True:
                        print("-" * 80, "\nrequests log-")
                        if len(pr_w) != 0:
                            for i in range(len(pr_w)):
                                print(str(i + 1) + ".", "requested by: ", pr_w[i][0])
                        else:
                            print("no requests pending")
                            k = input("\npress enter to go back")
                            print('-'*80)
                            break
                        print("\nwhat do you wish to do..?")
                        print("(1-" + str(i + 1) + "). check for more details\n  " + str(i + 2) + "  . go back")
                        n = int(input("\nenter choice: "))-1
                        if n in range(i+1):
                            print('-'*80, "\nrequest     -", pr_w[n][1], "\nrequested by-", pr_w[n][0])
                            print("block number-", dict_civilian[pr_w[n][0]][1])
                            print("phone number-", dict_civilian[pr_w[n][0]][2])
                            while True:
                                print("\nwhat do you wish to do..?\n1. report completion\n2. go back")
                                g = int(input("\nenter choice: "))
                                if g == 1:
                                    x = dict_civilian[pr_w[n][0]].index([name, pr_w[n][1], "pending"])
                                    dict_civilian[pr_w[n][0]][x][2] = "completed"
                                    del pr_w[n],  dict_worker[name][n+2]
                                    print('completion confirmed')
                                    x = input("\npress enter to go back")
                                    break
                                elif g == 2:
                                    print("-"*80)
                                    break
                                else:
                                    print("invalid choice, enter again\n", '-'*80)
                        elif n == i+1:
                            print('-'*80)
                            break
                        else:
                            print("invalid choice, enter again")
                elif choice_2 == 3:
                    print("\nyou are now logged out\n", '='*80)
                    break
                else:
                    print("invalid choice, enter again\n", "-"*80)
            break
        elif name == 'admin' and password == 'admin2468':
            while True:
                print("\nwelcome administrator, what do you wish to do..?")
                print("1. edit dict_civilian\n2. view dict_civilian\n3. edit dict_worker\n4. view dict_worker")
                print("5. server shutdown\n6. log out\n")
                choice_3 = int(input("enter choice: "))
                if choice_3 == 1:
                    while True:
                        print('-'*80, "\n\nwhat do you wish to do..?")
                        print("1. add account\n2. remove account\n3. go back")
                        choice_4 = int(input('\nenter choice: '))
                        if choice_4 == 1:
                            print("\ninput details of the account-")
                            w = input("enter the username: ")
                            x = input("enter the password: ")
                            y = input("enter block number: ")
                            z = input("enter phone number: ")
                            dict_civilian[w] = [x, y, z]
                            l_civilian.append(w)
                            print("\naccount added")
                        elif choice_4 == 2:
                            u = input("\nenter account username: ")
                            if u in l_civilian:
                                del dict_civilian[u], l_civilian[l_civilian.index(u)]
                                print("account deleted")
                            else:
                                print("name not in records")
                        elif choice_4 == 3:
                            print('-'*80)
                            break
                        else:
                            print("invalid choice, enter again\n", '-'*80)
                elif choice_3 == 2:
                    print('-'*80, '\ndict_civilian-')
                    for i in dict_civilian:
                        j = 11 - len(i)
                        k = 11 - len(dict_civilian[i][0])
                        print("\n", i, ' '*j, ':', dict_civilian[i][:3], ' '*k, "\n\trequests pending:")
                        for x in range(len(dict_civilian[i][3:])):
                            print('\t', x+1, ". ", dict_civilian[i][3+x])
                    x = input("\npress enter to go back")
                    print('-'*80)
                elif choice_3 == 3:
                    while True:
                        print('-'*80, "\n\nwhat do you wish to do..?\n1. add account\n2. remove account\n3. go back")
                        choice_5 = int(input('\nenter choice: '))
                        if choice_5 == 1:
                            print("\ninput details of the account-")
                            x = input("enter the username: ")
                            y = input("enter the password: ")
                            z = input("enter phone number: ")
                            dict_worker[x] = [y, z]
                            l_worker.append(x)
                            print("\naccount added")
                        elif choice_5 == 2:
                            u = input("enter account username: ")
                            if u in l_worker:
                                del dict_worker[u], l_worker[l_worker.index(u)]
                                print("account deleted")
                            else:
                                print("name not in records")
                        elif choice_5 == 3:
                            print('-'*80)
                            break
                        else:
                            print("invalid choice, enter again\n", '-'*80)
                elif choice_3 == 4:
                    print('-'*80, '\ndict_worker-')
                    for i in dict_worker:
                        j = 11-len(i)
                        k = 10-len(dict_worker[i][0])
                        print(i, ' '*j, ':', dict_worker[i][:2],  ' '*k, ";   due requests:", dict_worker[i][2:])
                    x = input("\npress enter to go back")
                    print('-'*80)
                elif choice_3 == 5:
                    print('-'*80, "\n\nenter 'CONFIRM' if you really want to shut the server down")
                    x = input("> ")
                    if x == 'CONFIRM':
                        print("\nTHE SERVER HAS BEEN SHUT DOWN\n", '*'*80)
                        exit()
                    else:
                        print("\nsince you entered '", x, "'  instead of ' CONFIRM '\nthe server shout down is aborted")
                        x = input("\npress enter to go back")
                        print('-'*80)
                elif choice_3 == 6:
                    print("\nyou are now logged out\n", '='*80)
                    break
                else:
                    print('invalid choice, enter again\n', '-'*80)
            break
        else:
            if a != 1:
                print("\nincorrect password, try again\nyou have", a-1, "chances left\n", '-'*80)
            else:
                print("\nincorrect password\nyou have", a - 1, "chances left")
            a -= 1
