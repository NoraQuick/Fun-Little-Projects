#Towers of Hanoi

def ToH(n, s, f, i):
    if n == 1:
        print("Move disc 1 from pole", s, "to pole", f)
        return
    #Call recursive 
    ToH(n-1, s, i, f)
    #Print the move
    print("Move disc", n, "from pole", s, "to pole", f)
    #?
    ToH(n-1, i, f, s)

def main():
    n = int(input("Please enter the number of disks you want to move: "))
    ToH(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()

