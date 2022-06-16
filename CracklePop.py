if __name__== "__main__":
    for num in range(101):
        print(num, end=" ")
        
        if num%3 == 0:
            print("Crackle", end = "")
        if num%5 == 0:
            print("Pop", end = "")
        
        print("")
                