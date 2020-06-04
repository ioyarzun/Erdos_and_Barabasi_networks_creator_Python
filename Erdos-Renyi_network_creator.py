  #!/usr/bin/python3
import sys
import argparse
from random import random

parser = argparse.ArgumentParser(description="Creates an Erdös-Renyi network with the parameters N (nodes number) and p (probability of links between nodes) and export it in a .net file.\n")

parser.add_argument('-N', '--nodes',
						dest = "nodes",
						action = "store",
						default = None,
						help = "Number of nodes in the network.\n")

parser.add_argument('-p', '--probability',
						dest = "p",
						action = "store",
						default = None,
						help = "Probability of the node to have an edge with any other node in the network.\n")

parser.add_argument('-o', '--output',
						dest = "output",
						action = "store",
						default = "",
						help = "Name for the output file.\n")

options=parser.parse_args()

def Erdos_Renyi_network_creator (N, p, outputfilename=""):

    #Output file name
    if not outputfilename:
        outputfilename=str(N)+"_"+str(p)+"_"+"Erdös-Rényi_network.net"
    else:
        outputfilename=outputfilename+".net"

    outfile=open(outputfilename, "w")
    outfile.write("*Vertices " + str(N) + "\n*Edges\n")

    already_connected=[]

    #Edge creation
    for node in range(1,N+1):
        for other_node in range(1,N+1):
            if node != other_node:
                if random() <= p:
                    if node < other_node:
                        edge_to_add = str(node) + " " + str(other_node)
                    else:
                        edge_to_add = str(other_node) + " " + str(node)

                    if edge_to_add not in already_connected:
                        already_connected.append(edge_to_add)
                        outfile.write(edge_to_add+"\n")

if __name__=='__main__':
    try:
        N=int(options.nodes)
        if N:
            try:
                p=float(options.p)
            except:
                sys.stderr.write("\n-p argument is missing, please, set a probability of links (between 0 and 1) for the network.\n\n")

    except:
        sys.stderr.write("\n-N argument is missing, please, set the number of nodes in the network.\n\n")

    outputfilename=options.output

    Erdos_Renyi_network_creator(N,p,outputfilename)
