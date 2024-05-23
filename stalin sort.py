import random
def StalinSort(list):
    i = 0
    gulag = []
    length = len(list)
    if length > 0:
        aux = list[0]
    while i < length and length > 0:
        if aux <= list[i] :
            aux = list[i]
            i = i+1
        else:
            gulag.append(list[i])
            del list[i]
            length = length -1
    print("numbers in gulag" ,gulag)
    return list 
def main():
    bunch_of_nums = [random.randint(0,500) for i in range(random.randint(1, 68))]
    #bunch_of_nums = [random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500)]
    print(bunch_of_nums)
    print("there were", len(bunch_of_nums),"now there are only",StalinSort(bunch_of_nums))
if __name__ == '__main__':
    main()