import json;
from random import choice

data = json.loads(open("input.json").read()); #read json
dkeys = data.keys(); #extract keys in data
dkeys = list(dkeys); #dict_keys to array


flag = False;
randomNode = choice(dkeys); #choice a random number in the array
actuallyNode = data[randomNode]; #select the node of the random number

while not flag:	
	actuallyNode['Ranking'] += 1;
	nextNode=choice(actuallyNode['Links']);
	actuallyNode = data[nextNode];
	if actuallyNode['Ranking']>99999:
		flag = True;
	
	
	
	
with open('output.json','w') as outfile:
	json.dump(data,outfile); #save result in out.json


