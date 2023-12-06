import os

def system():
    os.system("clear")
    print ("")                                                                                                                           os.system("figlet IP address |lolcat")
    print ("___________________________________________ ")                                                                               print ("            Scan Tool by-:")
    print ("                   Termux-hacking")
    print ("___________________________________________")
    print ("\033[1;31m[1]\033[1;32m Start")
    print ("\033[1;31m[2]\033[1;32m updat")
    print ("\033[1;31m[3]\033[1;32m help")
    print ("\033[1;31m[4]\033[1;32m exit")
    print ("")
    x=int(input("\033[1;31m[*] \033[1;33mEnter Your choice \033[1;31m》》\033[1;34m"))
    print ("")
    if x==1:
       g=str(input("\033[1;31m[*] \033[1;33mEnter Your ip address \033[1;31m:-: \033[1;34m"))
       os.system("nmap -A "+g)
    elif x==2:
         os.system("apt update && apt upgrade")
    elif x==3:
         print ("\033[1;37m")
         os.system("nmap -h")
    elif x==4:
         os.system("clear")
    else:
        print ("\033[1;31mnot fund ../")


def main():
    print ("")
    print ("\033[1;31m[1]\033[1;32m[Y]")
    print ("\033[1;31m[2]\033[1;32m[N]")
    print ("\033[1;31m[3]\033[1;32m[exit]")
    print ("")
    package=int(input("\033[1;31m[*]\033[1;33m Tool package install \033[1;31m:-: \033[1;34m"))
    if package==1:
       os.system("pkg install nmap -y")
       os.system("pkg install figlet -y")
       os.system("pkg install gem -y")
       os.system("gem install lolcat -y")
       system()
    elif package==2:
         system()
    elif package==3:
         os.system("clear")
    else:
       print ("\033[1;31mnot ")
main()
