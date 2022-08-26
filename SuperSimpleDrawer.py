counter=0
image=["░░░░░░░",
       "░█░░░█░",
       "░█░░░█░",  ##The great thing about this is you can edit this list to have more items, or make the items longer, and it will still work.
       "░░░░░░░",  ##I've used unicode characters here, but letters are fine too. For example, you could swap the grey ones for a dot and the black ones for an O or whatever.
       "░█░░░█░",
       "░░███░░",
       "░░░░░░░"]
for i in range(0, len(image)):
    print(map[counter])
    counter += 1
