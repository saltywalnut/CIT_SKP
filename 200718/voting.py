# mode = "voting"
#
# votes = {"vote1" : 0, "vote2" : 0, "vote3" : 0, "vote4" : 0, "vote5" : 0, "vote6" : 0, "vote7" : 0, "vote8" : 0
# while mode != "finish":
#     vote = input ("please vote for your candidate :")
#     if vote == "-1":
#         mode = "finish"
#
# if vote = "finish":
#     print

votes = [{"name" : "Darius", "code" : 1, "votes": 0},
{"name" : "Jax", "code" : 2, "votes": 0},
{"name" : "Fiora", "code" : 3, "votes": 0},
{"name" : "Ahri", "code" : 4, "votes": 0},
{"name" : "Camile", "code" : 5, "votes": 0},
{"name" : "Riven", "code" : 6, "votes": 0},
{"name" : "Teemp", "code" : 7, "votes": 0},
{"name" : "Invalid", "code" : 8, "votes": 0},
]
candidates = 7
votecount = 0
mode = "voting"

while mode != "finish":
    vote = int (input("please vote for a candidate : "))
    if vote == -1:
        mode = "finish"
    elif vote < 0 or vote > candidates:
        votes [candidates]["votes"] = votes [candidates]["votes"] + 1
    else :
        votes[vote-1]["votes"] = votes[vote-1]["votes"] + 1
    votecount = votecount + 1
    print (votes)

winner = 0
challenger = 0
while challenger < candidates:
    if votes[winner]["votes"] < votes[challenger]["votes"]:
        winner = challenger
    challenger = challenger + 1


print (votes[winner]["name"])
print (votes[winner]["votes"]/votecount)
