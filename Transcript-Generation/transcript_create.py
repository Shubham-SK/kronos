# Importing speech2text from prev definition
from speech2text-v2 import speech2text

conversation_array = speech2text("doctor.wav") # testing with doctor.wav

# Generating Transcript + Finding Key Words
def transcript_gen(conversation_array):
	final = []
	string = ""
	doc_num = conversation_array[0][1]
	print(len(conversation_array))
	for i in range(len(conversation_array)):
		if(conversation_array[i][1] != doc_num):
			 pat_num = conversation_array[i][1]
	print(doc_num, pat_num)

	for i in range(len(conversation_array)):
		print(conversation_array[i][1])
		if(i == 0):
			string = conversation_array[0][0]
		if(i != 0 and  conversation_array[i][1] == conversation_array[i-1][1]):
			string += " "
			string += conversation_array[i][0]
		if(i != 0 and conversation_array[i][1] != conversation_array[i-1][1]):
			final.append(string)
			string = ""
	log = []

	final.append(string)
	with open("transcript.txt", 'w') as f:
		#creating transcript
		f.write('TRANSCRIPT')
		f.write('\n___________')
		for i in range(len(final)):
			if(final[i].split(' ')[0] == "log"):
				log.append(final[i])
			if(i % 2 == 0 ):
				final[i] = "\nDoctor: " + final[i]
				f.write(final[i])
			if(i % 2 == 1):
				final[i] = "\nPatient: " + final[i]
				f.write(final[i])

		f.write('\nLOG')
		f.write('\n___________')
		for i in range(len(log)):
			f.write(log[i])
