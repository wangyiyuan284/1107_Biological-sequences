# -*- coding: utf-8 -*-
import os
import sys

from Bio import Entrez, SeqIO

sys.path.append('./util')
import tools
import plot


class BiologicalSequence:

    def __init__(
        self, 
        FILE_NAME,
        OUT_DIR,
    ):
        self.FILE_NAME = FILE_NAME
        self.OUT_DIR = OUT_DIR

    def compute(
        self,
        file_name,  # User - defined file path and file name
        out_dir,
    ):

        # Gets the build folder directory name
        with open(file_name,"r") as file:
            for line in file:
                result=[]
                result.append(list(line.strip('\n').split(',')))
                userSpecified=(result[0][1]+' '+result[0][2])
            
                # Set the name of the build folder
                name = result[0][0]+ "_" + result[0][1]+"_" + result[0][2]+"_" + result[0][3]
            
                # Create output directories
                if not os.path.isdir(out_dir):
                    os.makedirs(out_dir, exist_ok=True)
                if not os.path.isdir(out_dir + "/" + name):
                    os.makedirs(out_dir + "/" + name, exist_ok=True)
        
                # Get sequence
                print("Generating the protein sequences...")
                if(isinstance(file_name,str)):  
                    tools.get_sequence(line,out_dir,result[0][3])
                else:
                    raise ValueError("Please enter the correct file path..." + file_name)
                    
                #To determine, and plot, the level of conservation between the protein sequences
                print("Generating the level of conservation between the protein sequences...")
                tools.plot_conservation(out_dir+ "/" + name + "/sequence" + "_"+ result[0][3] +".fasta",out_dir,name,result[0][3])

                #plot png
                plot.plot_png(out_dir,name)