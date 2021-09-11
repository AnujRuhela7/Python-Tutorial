L = {'Language' : ['Python','Java','C/C++','Javascript'],'Year':[1991,1995,1980,1995]}
print("Dictionary Languages : ",L)
L_year = dict(zip(L['Language'],L['Year']))
print("Flattened Dictionary Language : ",L_year)