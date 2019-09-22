# Importing speech2text from prev definition
from speech2textv2 import speech2text

conversation_array = speech2text("doctor.wav") # testing with doctor.wav
# print(conversation_array)

# Generating Transcript + Finding Key Words
def transcript_gen(conversation_array):
	"""
	Void function that creates Transcript File
	________________________________
	Args: Conversation Array (2D ex: [["word", speaker_idx]])
	Returns: transcripts.txt file
	"""

	# Final Transcript Intialization
	final = []
	string = ""
	doc_num = conversation_array[0][1]
	#print(len(conversation_array))

	# Determines index of the patient assuming doctor speaks first
	for i in range(len(conversation_array)):
		if(conversation_array[i][1] != doc_num):
			 pat_num = conversation_array[i][1]
	# print(doc_num, pat_num)

	# Creates an array based on speakers
	for i in range(len(conversation_array)):
		# print(conversation_array[i][1])
		if(i == 0):
			string = conversation_array[0][0]
		if(i != 0 and  conversation_array[i][1] == conversation_array[i-1][1]):
			string += " "
			string += conversation_array[i][0]
		if(i != 0 and conversation_array[i][1] != conversation_array[i-1][1]):
			final.append(string)
			string = ""

	# Important comments made by doctor
	log = []

	final.append(string)

	# File Handling
	with open("transcript.txt", 'w') as f:
		#creating transcript
		f.write('TRANSCRIPT')
		f.write('\n___________')

		# Writing the transcript to file
		for i in range(len(final)):
			if(final[i].split(' ')[0] == "log"):
				log.append(final[i])
			if(i % 2 == 0 ):
				final[i] = "\nDoctor: " + final[i]
				f.write(final[i])
			if(i % 2 == 1):
				final[i] = "\nPatient: " + final[i]
				f.write(final[i])

		# Writing the logs to file
		f.write('\nLOG')
		f.write('\n___________')
		for i in range(len(log)):
			f.write(log[i] + "\n")

# Testing
# transcript_gen(conversation_array)
