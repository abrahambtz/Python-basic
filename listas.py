def run():
    list_integer = [5,10,1,2,4,5]
    print(list_integer)
    list_integer.append(9)
    print(list_integer)
    print(list_integer[0:3])
    list_integer.pop(2)
    print(list_integer)
    for item in list_integer:
        print(item)


if __name__ == '__main__':
    run()