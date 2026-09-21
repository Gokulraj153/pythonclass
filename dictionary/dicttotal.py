myDict = [{"name":"Suriya","email":"suriya@gmail.com","Regno":"22uv2215","mark":[98,75,89,85,92]},
          {"name":"Kamesh","email":"Kamesh@gmail.com","Regno":"22uv2216","mark":[78,86,96,65,80]},
          {"name":"Vishnu","email":"vishnu@gmail.com","Regno":"22uv2217","mark":[87,75,95,56,75]},
          {"name":"Gokul","email":"gokul@gmail.com","Regno":"22uv2218","mark":[96,85,75,86,94]},
          {"name":"Lingesh","email":"lingesh@gmail.com","Regno":"22uv2219","mark":[99,56,84,76,84]},
          {"name":"Venkat","email":"venkat@gmail.com","Regno":"22uv2220","mark":[96,86,76,84,75]},
          {"name":"Jayavardhan","email":"jayavardhan@gmail.com","Regno":"22uv2221","mark":[86,84,75,95,94]},
          {"name":"Krishna","email":"krishna@gmail.com","Regno":"22uv2222","mark":[96,98,84,85,75]},
          {"name":"Ram","email":"ram@gmail.com","Regno":"22uv2223","mark":[98,95,86,75,83]},
          {"name":"Shiva","email":"shiva@gmail.com","Regno":"22uv2224","mark":[75,85,95,76,85]}]

Total = []

for i in myDict:
    sum = 0
    for j in i["mark"]:
        sum += j
    Dict = {"name":i["name"],"email":i["email"],"Regno":i["Regno"],"Marks":i["mark"],"Total":sum}
    Total.append(Dict)


for i in range(len(Total)):
    rank = 1
    for j in range(len(Total)):
        if Total[j]["Total"] > Total[i]["Total"]:
            rank += 1
    Total[i]["Rank"] = rank


x = 0
for i in Total:
    if 300 <=i["Total"] < 500:
        Total [x]["Review"] = "Very Good"
        x+=1
    elif 250 <= i["Total"] <300:
        Total [x]["Review"] = "Good"
        x+=1
    else:
        Total [x]["Review"] = "Need to Improve"
        x+=1


for i in range(len(Total)):
    for j in range(len(Total)):
        if Total[j]["Rank"] == i + 1:
            print(Total[j])