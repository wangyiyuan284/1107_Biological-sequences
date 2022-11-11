# -*- coding: utf-8 -*-
import os
import time

from Bio import Entrez, SeqIO


def get_sequence(user_specified_file_path_and_name,output_data_dir,number_of_initial_sequences_user_want):
    # Setting Parameter
    Entrez.email = "Author@163.com"
    Entrez.tool  = "exampleScript"

    # Query the total number of user sspecified data in Protein
    with open(user_specified_file_path_and_name,"r") as file:
        for line in file:
            result=[]
            result.append(list(line.strip('\n').split(',')))
            userSpecified=(result[0][1]+' '+result[0][2])
            
            # Set the name of the build folder
            name = result[0][0]+ "_" + result[0][1]+"_" + result[0][2]+"_" + result[0][3]
            
            # Create output directories
            if not os.path.isdir(output_data_dir):
                os.makedirs(output_data_dir, exist_ok=True)
            if not os.path.isdir(output_data_dir + "/" + name):
                os.makedirs(output_data_dir + "/" + name, exist_ok=True)
            
            # Get total number
            hd_egquery = Entrez.egquery(term=userSpecified)
            read_egquery = Entrez.read(hd_egquery)
            total = 0
            for ele in read_egquery["eGQueryResult"]:
                if ele["MenuName"] == "Protein":
                    total = ele["Count"]
                    # print(total)

            # Get sequence
            hd_search = Entrez.esearch(db="protein", term=userSpecified, usehistory="y")
            read_search = Entrez.read(hd_search)
            webenv = read_search["WebEnv"]
            query_key = read_search["QueryKey"]
            # Use the history feature to search
            # Entrez will buffer ahead of time to improve query efficiency
            # The user's allowable starting sequence set probably shouldn't have more than 1,000 sequences
            step = 5
            total = number_of_initial_sequences_user_want
            with open(output_data_dir+ "/" + name + "/sequence.fasta", "w+") as file:
                 for start in range(0, total, step):
                    end = min(total, start+step)
                    print("Download record %i to %i" % (start+1, end))
                    hd_fetch = Entrez.efetch(db="protein", rettype="fasta", retmode="fasta", retstart=start, retmax=step, webenv=webenv, query_key=query_key)
                    records = hd_fetch.read()
                    file.write(records)

        # Print finish
        print("The protein sequence was obtained successfully" + " " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))