
file = open("Day3/data.txt" , "r")


# with open("Day3/data.txt" , "r") as f:
    # print(f.readable())
with open("Day3/data.txt" , "w") as f:
    f.write("\nUsman")
    f.write("\nAli")
    f.write("\nAbdullah")






with open("Day3/data.txt" , "a")as addData:
    addData.write("\nAhsan")

# print(len(file.readlines()))
print(file.read())


file.close()


