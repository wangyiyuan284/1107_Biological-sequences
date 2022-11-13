# Biological-sequences

Biological-sequences will allow the user to define a dataset that is of interest to them, which will then be processed to produce the required outputs.

**Line format for non-extended (without position): user_specified.txt**
**Amount:The start sequence that the user wants**
**The user's allowable starting sequence set probably shouldn't have more than 1,000 sequences**

```
[id: int],[protein family: string],[taxonomic group: string],[amount: int]

```
**Example:**

```
0,pyruvate dehydrogenase,ascomycete fungi,1000
1,immunoglobulin,archaea,1000
2,transaminase,viruses,1000

```

## Biological-sequences need to be generic

1.the user of Biological-sequences will specify the protein family, and the taxonomic group, and then Biological-sequences will need to obtain the relevant protein sequence data, and perform all subsequent analyses and outputs in the user's space on the server. the user's allowable starting sequence set probably shouldn't have more than 1,000 sequences.

2.to determine, and plot, the level of conservation between the protein sequences.

3.to scan protein sequence(s) of interest with motifs from the PROSITE database, to determine whether any known motifs (domains) are associated with this subset of sequences.

It consists of four main components:

* `input_data` : user will specify the protein family and the taxonomic group,The input is required in the specified format,like user_specified.txt
* `output_data`: Users want to output data to the file directory, you can customize the location
* `util`: Contains tools and plot for obtaining protein sequences, analyzing conformance, and mapping similarity bitmaps

## Getting started

1. System setup:
   - Python version 3.6+
   - Windows 7 or higher

2. Install dependencies:
   ```
   pip install sys os time bio collections weblogo 

   ```
   
3. Set up your input file, including the protein family, the taxonomic group and the desired initial sequence size:
   
  **Example:**
  ```
  input_data\user_specified.txt

  ```
4. Run main.py:
  ```
  python .\main.py "input_data/user_specified.txt" "output_data"
  
  ```