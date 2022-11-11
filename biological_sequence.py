# -*- coding: utf-8 -*-
import os
import sys

from Bio import Entrez, SeqIO

from main import FILE_NAME

sys.path.append('./util')
import tools


class BiologicalSequence:

    def __init__(
        self, 
        FILE_NAME,
        OUT_DIR,
        AMOUNT,
    ):
        self.FILE_NAME = FILE_NAME
        self.OUT_DIR = OUT_DIR
        self.AMOUNT = AMOUNT

    def compute(
        self,
        file_name,  # User - defined file path and file name
        out_dir,
        amount, # The number of initial sequences user want   
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
            tools.get_sequence(file_name,out_dir,amount)
        else:
            raise ValueError("Please enter the correct file path..." + file_name)
            
        #To determine, and plot, the level of conservation between the protein sequences
        print("Generating the level of conservation between the protein sequences...")
