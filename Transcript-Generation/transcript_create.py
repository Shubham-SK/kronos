#Array of words -> word, num
convarr = [["I'm", 1], ['prescribing', 1], ['10', 1], ['mg', 1], ['of', 1], ['alendronate', 1], ['and', 1], ['5', 1], ['mg', 1], ['of', 1], ['acetaminophen', 1], ['excellent', 3], ['that', 3], ['should', 3], ['work', 3]]
final = []
string = ""
doc_num = convarr[0][1]
print(len(convarr))
for i in range(len(convarr)):
	if(convarr[i][1] != doc_num):
		 pat_num = convarr[i][1]
print(doc_num, pat_num)

for i in range(len(convarr)):
	print(convarr[i][1])
	if(i == 0 ):
		string = convarr[0][0]
	if(i != 0 and  convarr[i][1] == convarr[i-1][1]):
		string += " "
		string += convarr[i][0]
	if(i != 0 and convarr[i][1] != convarr[i-1][1]):
		final.append(string)
		string = ""
final.append(string)
with open("transcript.txt", 'w') as f:
	f.write('TRANSCRIPT')
	f.write('\n___________')
	for i in range(len(final)):
		if(i % 2 == 0 ):
			final[i] = "\nDoctor: " + final[i]
			f.write(final[i])
		if(i % 2 == 1):
			final[i] = "\nPatient: " + final[i]
			f.write(final[i])
