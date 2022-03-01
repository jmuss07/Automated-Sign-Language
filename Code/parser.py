import time
from ASL_functions import asl_dict, neutral

cont = False
while not cont:
    neutral()
    phrase = input("\nPlease enter a phrase, or type -q to quit: ").lower()
    if phrase == "-q":
        cont = True
    else:
        confirm = input(f"\nIs '{phrase}' correct? (Y/N)\t")
        if confirm.lower() == "y":
            print()
            for i in phrase:
                print(i)
                if i not in asl_dict:
                    print(f"Sorry, I don't know how to sign {i}")
                else:
                    asl_dict[i]()
                    time.sleep(1)
            neutral()

