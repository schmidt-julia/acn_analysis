# Adjustment of .dot graph and quantitative analysis
Deletes all nodes with one neighbor in a .dot graph. Determines the number of nodes, edges, the Euler number, and number of polygons/SCL contained in the .dot graph. Aimed at the analysis of capillary networks.

## Requirements
Required packages are listed in requirements.txt and can be installed using pip as follows:\
`pip3 install -r requirements.txt`

## Input
- .dot graph
- Optional: Output .dot graph filename (-o argument), data .csv filename (-d argument)

## Output
- .dot output file
- .csv output file: number of nodes, segments, Euler number, number of polygons/SCL

## Usage example
`python3 acn_analysis.py mygraph.dot -o myoutputdotfile.dot -d myoutputdatafile.csv` 
