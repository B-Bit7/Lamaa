from os import system

while True:
      system("title Lamaa command line")
      inp = input(">> ")
      system(f"title Lamaa command line -- {inp}")
      if inp == "exit":
            break
      elif inp == "cls":
            system("cls")
            continue
      mathchars = ["+", "-", "*", "/", ":", "÷", "×", "(", ")"]
      ismath = any(ele in inp for ele in mathchars)
      if ismath:
            out = eval(inp)
            print(out)
