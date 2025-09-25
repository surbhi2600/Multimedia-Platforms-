# combine the tambola game and e_book
# e-commerce platform
import time
def commerce():
    print("!!Hey,",input("Enter your name: "),"Welcome to your shopping platform!!")
    print("We have listed categories..")
    def count_down(t):
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
        print("Time is in the hole")
            
    def shop():
        list=["Shoes","Cloths","Home decorator","Sports","Watches"]
        for i,idx in enumerate(list,start=1):
                print(f"{i}.) {idx}\n")
        print("In which section would you like to shop?")
        option=int(input("Enter your choice: "))
        if option==1:
            print("Welcome in shoes section..")
            print("We have some items in shoes are: ")
            shoes_item=["Sports shoes","Sneakesrs","Boot"]
            discount=(800-800*0.1)
            for i,idex in enumerate(shoes_item,start=1):
                print(f"{i}.) {idex}")
            choose=int(input("Enter the choice: "))
            if choose==1:
                print(f"Nike shoes\n Rs{800}\n discount 10% now amount  pay= {800-800*0.1}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==2:
                print(f"Bata Sneakers\n Rs{700}\ndiscount 15% now amount  pay= {700-700*0.15}\n Offer is valid for limited time. \n Buy now.") 
                count_down(5)
            elif choose==3:
                print(f"Woodland boot\n Rs{1700}\ndiscount 5% now amount  pay= {1700-1700*0.05}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            else:
                print("Thanking you sir/mam for visting in our shoes section..")
        elif option==2:
            print("Welcome in Cloths section..")
            print("We have some items in cloths are: ")
            cloth_item=["T-shirts","Shirts","Trouser"]
            for i,idex in enumerate(cloth_item,start=1):
                print(f"{i}.) {idex}")
            choose=int(input("Enter the choice: "))
            if choose==1:
                print(f"Men's T-shirt\n Rs{400}\n discount 7% now amount  pay= {400-400*0.07}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==2:
                print(f"Men's Shirt\n Rs{300}\ndiscount 5% now amount  pay= {300-300*0.05}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==3:
                print(f"Men's Trouser\n Rs{700}\ndiscount 15% now amount  pay= {700-700*0.15}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            else:
                print("Thanking you sir/mam for visting in our cloth section..")
        elif option==3:
            print("Welcome in Home Decorator section..")
            print("We have some items in home decoration are: ")
            home_item=["Curtains","Wall sticker","Flower pot"]
            for i,idex in enumerate(home_item,start=1):
                print(f"{i}.) {idex}")
            choose=int(input("Enter the choice: "))
            if choose==1:
                print(f"Designing curtain\n Rs{450}\n discount 4% now amount  pay= {450-450*0.04}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==2:
                print(f"Spider man sticker\n Rs{250}\ndiscount 2% now amount  pay= {250-250*0.02}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==3:
                print(f"Flower vessel\n Rs{150}\nBuy now")
                
            else:
                print("Thanking you sir/mam for visting in our home decorator section..")   
        elif option==4:
            print("Welcome in Sports section..")
            print("We have some items in sports are: ")
            sports_item=["Cricket Bat","Tennis ball","Badminton"]
            for i,idex in enumerate(sports_item,start=1):
                print(f"{i}.) {idex}")
            choose=int(input("Enter the choice: "))
            if choose==1:
                print(f"Cricket bat\n Rs{1000}\n discount 4% now amount  pay= {1000-1000*0.04}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==2:
                print(f"Tennis ball\n Rs{70}\ndiscount 1% now amount  pay= {70-70*0.01}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==3:
                print(f"Fonex Badminton\n Rs{1700}\nndiscount 2% now amount  pay= {1700-1700*0.02}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            else:
                print("Thanking you sir/mam for visting in our sports section..") 
        elif option==5:
            print("Welcome in Watch section..")
            print("We have some items in Watches are: ")
            watch_item=["Smart Watch","Formal watch","Chain watch"]
            for i,idex in enumerate(watch_item,start=1):
                print(f"{i}.) {idex}")
            choose=int(input("Enter the choice: "))
            if choose==1:
                print(f"Smart watch\n Rs{2999}\n discount 10% now amount  pay= {2999-2999*0.1}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==2:
                print(f"Formal watch\n Rs{799}\ndiscount 1.5% now amount  pay= {799-799*0.015}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            elif choose==3:
                print(f"Chain watch\n Rs{590}\nndiscount 2% now amount  pay= {590-590*0.02}\n Offer is valid for limited time. \n Buy now.")
                count_down(5)
            else:
                print("Thanking you sir/mam for visting in our sports section..")
        else:
            print("Thank you sir/mam for visting our platform..") 
    while True:
        print("Do you like to shop?")
        opinion=input("Enter your opinion in yes/no: ")
        if opinion=='yes':
            print("..Now choose your option..")
            shop()
        else:
            print("Thank you sir/mam for being my valuable purchaser..")
            break
def main():
    print("Hey,",input("Enter your name: "),"Welcome our website..")
    print("We have best offer for you. Are you interested in shoping?")
    opt1=input("Enter your choice in yes/no: ")
    if opt1=='yes':
        print("For get offer in items, you have to perform some task..")
        item=["Tambola game","E-book reader"]
        for i,index in enumerate(item,start=1):
            print(f"{i}.{index}")
        ch1=int(input("Enter your choice: "))
        if ch1==1:
            print("Great choice, enjoy the game..")
            # Tambola game
            import random
            class Game:
                player=0
                @staticmethod
                def tambola_game():  
                    print("!!Tambola Game!!")
                    name=input("Enter your name: ")
                    print(f"Hey, {name}, welcome to tambola game.. ")
                    Game.player=int(input("Enter no of player: "))
                    print(f"Number of are player is {Game.player}.")
                    ask_name="Enter the name of candidate: "
                    for i in range(Game.player):
                        print(f"Name of candidate {i} is {input(ask_name)}.")
                @staticmethod
                def number_of():
                    for i in range(Game.player):
                        print(f"list{i}={[random.randint(1,100) for _ in range(9)]}") 
                @staticmethod
                def match_number():
                    print("!!Match the number which are showm below..!!")
                    number=[random.randint(1,100) for _ in range(10*Game.player)]
                    print(number)
                @staticmethod
                def winner():
                    print("Match your list with the number..")
                    name=input("Enter the name of winner..: ")
                    print(f"Hey, {name}, you win the match Congratulations Yaar!!")
            s1=Game()
            s1.tambola_game()
            s1.number_of()
            s1.match_number()
            s1.winner()
            print("Do you like to play the match again..")
            while True:
                start=input("Enter True for continue or False to exit: ")
                if start=="True":
                    Game.tambola_game()
                    Game.number_of()
                    Game.match_number()
                    Game.winner()
                else:
                    print("Thank you for playing the tambola game...")
                    break
            opt2=input("Choose option yes If you win or no if loss: ")
            while True:
                if opt2=='yes':
                    print("You will get the bumper discount in items..")
                    # e-commerce platform
                    commerce()
                    break   
                else:
                    print("Better luck next time try again...")
                    break
#///////////////////////////////////////////////////////////////////////////////////    
        elif ch1==2:
            print("Great choice, start your reading task..")
            # # E-BOOK...
            def find_and_extract(file_path, search_word):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.readlines()  # Read file line by line
                        found = False  # Track if the word was found
                        
                        for i, line in enumerate(content):
                            if search_word in line:
                                found = True
                                print(f"\nFound '{search_word}' in: \n{line.strip()}")
                                user_choice = input("Is this the correct line? (yes/no): ").strip().lower()
                                
                                if user_choice == "yes":
                                    print("\nContent after the word:\n")
                                    print("".join(content[i+1:]))  # Display rest of the file
                                    return
                                else:
                                    print("Moving to next occurrence...\n")
                        
                        if not found:
                            print(f"'{search_word}' not found in the file.")
                
                except FileNotFoundError:
                    print("Oops! The book file is missing.")
                except Exception as e:
                    print(f"An error occurred: {e}")

            # Main Script
            print("E-BOOK")
            name = input("Your name: ")
            print("Hello", name)

            option = input("Do you want to read the book? (yes/no): ").strip().lower()
            if option == 'yes':
                print("Enjoy your reading...\n")
                file_path = "sme_training_python\\book.txt"

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        print(f.read())  # Display full book content

                    print("\nHave you forgotten where you left off? No worries! Give me a hint...")
                    num = input("Remember the last page number? (yes/no): ").strip().lower()

                    if num == 'no':
                        par = input("Do you remember the paragraph? (yes/no): ").strip().lower()
                        if par == 'no':
                            print("It's okay, no worries!")
                        
                        key = input("Do you remember any keyword? (yes/no): ").strip().lower()
                        if key == 'yes':
                            search_word = input("Enter your keyword: ").strip()
                            find_and_extract(file_path, search_word)
                except FileNotFoundError:
                    print("Oops! The book file is missing.")
            else:
                print("Go to that page and enjoy reading!")
            print("!!!I hope you have read the book and enjoy it..!!!")
            print("Question1: What is your favourite author name?")
            print(input("Answer: "),"great yaar badhiya")
            print("Question2: How many book you have read?")
            print(int(input("Answer: ")),"Great yaar badhiya")
            print("Question3:You are interested then share your knowledge?")
            print(input("Answer: "),"Amazing answer yaar.")
            print("Now are you interested in shoping?")
            a=input("Enter your excitement in yes/no? ")
            if a=='yes':
                print("Now moving towards shoping section..")
                commerce()
            else:
                print("Thanking you for your visit..")
    else:
        print("Thnak you sir for giving me your valuable time..")             
main()
    