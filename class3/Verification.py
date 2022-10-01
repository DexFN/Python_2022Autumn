Q1 = input("Who are you? ")
if Q1 == "Louie":
    a = input("Hello Louie, Welcome back ")
    ld1 = input("Loading ··········· 20%")
    ld2 = input("Loading ··········· 40%")
    ld3 = input("Loading ··········· 60%")
    ld4 = input("Loading ··········· 80%")
    ld5 = input("Loading ··········· 100% ᴄᴏᴍᴘʟᴇᴛᴇ")
    verify = input("Please type your password to access to this computer: ")
    if verify == "12345":
        correct = input("You have successfully logged in to this computer, you may now have access to use it")
    elif verify != "12345":
        incorrect = input("Incorrect password, please try again")
    verify1 = input("Please type your password again: ")
    if verify1 != "12345":
        inocorrect = input("Incorrect password, you have now ran out of chances, the computer will turn off soon")
    elif verify1 == "12345":
        correct = input("You have successfully logged in to this computer, you may now have access to use it")
if Q1 != "Louie":
    Q2 = input("Why are you using his computer? ")
if Q2 == "He let me use":
    Q3 = input("Are you sure? ")
elif Q2 != "He let me use":
    Q3 = "Undentified person tried to login this computer, the system will turn off soon"
if Q3 == "Yes":
    Q4 = input("Ok, I trust this user")
elif Q3 != "Yes": 
    Q4 = input("I don't trust this user, I will report some undentified person is using his computer")