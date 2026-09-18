myDict = {"name":"Suriya","email":"suriya@gmail.com","Regno":"22uv2215","mark":[98,75,89,85,92]}

Total = myDict["mark"][0] + myDict["mark"][1] + myDict["mark"][2] + myDict["mark"][3] + myDict["mark"][4]

print("Total Marks:",Total)
#-----------------------------------------------X------------------------------------------
length = len(myDict["mark"])
Total1 = 0

for i in range(length):
    Total1 += myDict["mark"][i]

print("Total Marks:",Total1)