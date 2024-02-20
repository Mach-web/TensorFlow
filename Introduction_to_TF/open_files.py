if __name__ == "__main__":
    """f = open("my_file.txt", "w")
    f.write("Hello World!!!!!")
    f.close()"""
    """files = open("my_file.txt", "r")
    print(files.read())
    files.close()"""
    with open("my_file.txt", "r") as f:
        print(f.read(5))

    def create_cast_list(filename):
        cast_list = []
        with open(filename) as f:
            for i in f.readlines():
                #             print(i)
                cast_list.append(i.split(",")[0])
        return cast_list
        # use with to open the file filename
        # use the for loop syntax to process each line
        # and add the actor name to cast_list
    cast_list = create_cast_list('flying_circus_cast.txt')
    print(cast_list)