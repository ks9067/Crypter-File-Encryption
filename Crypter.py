import pyAesCrypt
import os
import webbrowser

print('''
________________________________________________________________________________________________
|     ____                  _                                                                   |
|    / ___|_ __ _   _ _ __ | |_ ___ _ __                                                        | 
|   | |   | '__| | | | '_ \| __/ _ \ '__|       ###########################################     |
|   | |___| |  | |_| | |_) | ||  __/ |          ######   Written by Jeet Swarnakar   ######     |
|    \____|_|   \__, | .__/ \__\___|_|          ###########################################     |
|               |___/|_|                                                                        |
|_______________________________________________________________________________________________|
''')

print("Crypter uses AES-256 CBC cipher to encrypt or decrypt any file with password  :)\n\n")


def encryptFile(p):    
    filename = input("\nEnter name or destination path of file to Encrypt   eg.: Example.txt or C:\\Path\\to\\destination\\file.txt\n")
    outfile=""
    for i in filename[-1::-1]:
       if i=="\\":
           break
       else:
           outfile = i + outfile
    mkdir(outfile[:-4])
    outfile+=".aes"
    try:
        pyAesCrypt.encryptFile(filename, outfile, p)
        print("\nSuccessfully Encrypted as", outfile,"\n")
    except ValueError:
        print("\nRequested File is missing OR Try removing space in filename if any\n")
        t=input("Press enter to exit")
        exit()
    file=open("Secret.txt", "w")
    file.write(p)
    file.close()
    

def decryptFile(p):
    filename = input("\nEnter name or destination path of file to Decrypt   eg.: Example.txt.aes or C:\\Path\\to\\destination\\file.txt.aes\n")
    outfile=""
    for i in filename[-1::-1]:
       if i=="\\":
           break
       else:
           outfile = i + outfile
    outfile=outfile[:-4]
    try:
        pyAesCrypt.decryptFile(filename, outfile, p)
        print("\nSuccessfully Decrypted as", outfile,"\n")
    except ValueError:
        print("\nIncorrect Password OR Requested File is missing OR Try removing space in filename if any\n")
        t=input("Press enter to exit")
        exit()
    

def mkdir(dirname):
    try:
        a=os.getcwd()
        path=os.path.join(a,dirname)
        os.mkdir(path)
        os.chdir(dirname)
    except FileExistsError:
        os.chdir(dirname)

def main():
    try:
        choice = int(input("Select 1 for Encryption or Select 2 for Decryption:\n"))
    except:
        print("\nInvalid Choice Input\n")
        main()
    if choice==1:
        password = input("\nEnter Password:\n")
    elif choice==2:
        try:
            ftype=int(input("\nEnter 1 to type password or Enter 2 to input passwordfile:\n"))
        except:
            print("\nInvalid choice\n")
            main()     
        if ftype==2:
            passfile=input("\nEnter name or destination path of password file   eg.: Secret.txt or C:\\Path\\to\\passphrase\\file.txt\n")
            try:
                file=open(passfile,"r")
                password=file.read()
                file.close()
            except:
                print("\nRequested File is missing OR Try removing space in filename, if any\n")
                main()
        elif ftype==1:
            password = input("\nEnter Password:\n")
        else:
            print("\nInvalid Choice Input\n")
            main()
    else:
        print("\nInvalid Choice Input\n")
        main()

    mkdir("Crypted")
    if choice == 1:
        encryptFile(password)
    elif choice == 2:
        decryptFile(password)
    
    tw=input("Wanna follow me up on twitter?  :)  Type Yes for twitter profile or press enter to quit: ")
    if tw=="Yes" or tw=="yes":
        webbrowser.open_new_tab("https://twitter.com/bingo07_bingo")
    exit()

if __name__=="__main__":
    main()