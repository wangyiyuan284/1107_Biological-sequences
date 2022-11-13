from collections import Counter
import time

def plot_conservation(generated_sequence_file,output_data_dir,dir_name,specified_amount):

	#Turn on the protein sequence
	with open(generated_sequence_file,"r") as SeqInitial:             
		
		#Used to store post-processing sequences
		with open(output_data_dir+ "/" + dir_name + "/sequenceTreatment.fasta", "w+") as SeqTreatment: 
			#Read by row
			for line in SeqInitial.readlines(): 
				#Remove the newline character       
					line=line.strip('\n')         
					if'>' not in line:
						#Read by row          
						SeqTreatment.write(line)           
					if'>'in line :    
						#Use '.'instead of protein name information         
						SeqTreatment.write('.')     
	SeqInitial.close()
	SeqTreatment.close()
	SeqTreatment = open(output_data_dir+ "/" + dir_name + "/sequenceTreatment.fasta")            

	# reads all into one string
	allTxt=SeqTreatment.read()  

	#Drop the beginning dot
	lineTxt=allTxt[:0]+allTxt[1:]

	# Create a list with 1000 strings             
	slist=[0 for column in range(int(specified_amount))]
 
	for i in range (int(specified_amount)): 
		#Split the sequence by dot '.'
		slist[i]= lineTxt.split('.')[i]
		
	#Create a variable to hold the vertical columns of the matrix
	compare_list = str()  
	#Create a variable to hold the feature sequence                 
	lsen = str()                  
 
	for j in range(int(specified_amount)):
		for k in range(len(slist[j])): 
			compare_list = compare_list+slist[j][k]
		#Find the amino acid that appears most frequently in the listed string
		if ( Counter(compare_list).most_common(1)[0][0]!='-'): 
			# more than half of specified_amount           
			if(Counter(compare_list).most_common(1)[0][1]>int(int(specified_amount)/2)):
				# Store them one by one
				lsen = lsen+Counter(compare_list).most_common(1)[0][0] 
		#Reset the compare list     
		compare_list = '-'

	# Use as many initial sequences as the user wants for conservative analysis
	lsen=lsen[:int(specified_amount)]                                          
	print("Similar sequence length:"+ str(len(lsen)))
	print(lsen)
	with open(output_data_dir + "/" + dir_name + "/Seqfeature.fasta",'w+')as SeqDealtWith:
		#Create a fasta file and save it
		SeqDealtWith.write(lsen)
	
	# Print finish
	print("Extraction of similar sites of protein sequences has been completed" + " " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	