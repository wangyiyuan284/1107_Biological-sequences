import time
from weblogo import *


def plot_png(output_data_dir,dir_name):
    # Read the file as a standard input stream
    f = open(output_data_dir + "/" + dir_name + "/Seqfeature.fasta","r")
    # Obtaining sequence data
    seqs = read_seq_data(f)
    data = LogoData.from_seqs(seqs)   
    options = LogoOptions() 
    # Generate the lower Angle script
    options.fineprint = 'Python plot the conversation photo'   
    format = LogoFormat(data, options)

    eps = eps_formatter(data, format)
    with open(output_data_dir + "/" + dir_name + "/SeqfeaturePhoto.eps",'wb') as photo:
        photo.write(eps) 
    #  Eps Files need to be opened in Adobe illustrator or Photoshop
    
    # Print finish
    print("The similarity graph of the selected sequence set has been drawn" + " " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))