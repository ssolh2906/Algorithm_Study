import LRU
import Optinal


while True:
    input_l = []
    default_input = [1, 2, 1, 4, 5, 6, 3, 4, 6, 3, 7, 3, 1, 5, 3, 7, 3, 4, 2, 4, 1, 4, 5, 1]
    #default_input = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    print("* Input the page reference string\n* input 0 to use default test string")
    print("\tDefault String : ", default_input)
    input_str = input(
        "*input \"exit\" to exit \n:")
    if input_str == "0":
        input_l = default_input

    elif input_str == "exit":
        print("......exit........")
        exit(0)
    else:
        input_l = list(map(int, input_str.split()))

    while True:
        result = []
        print("Select mode")
        print("1: LRU")
        print("2: Optimal")
        key = input()
        if key == "1":
            mode = "LRU"
            result = LRU.myLRU(input_l)
            break
        elif key == "2":
            mode = "Optimal"
            result = Optinal.myOptimal(input_l)
            break
        else:
            continue

    print("Page fault :",result,'\n')



