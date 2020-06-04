#!/usr/bin/python3
import sys
import argparse
from random import random, choice

parser = argparse.ArgumentParser(description="Creates a Barabási-Albert network with the parameters N (nodes number) and E (new arrivals links to previous nodes) and export it in a .net file.\nCore nodes ammount (named Ncore) is set at 30% of N and the probability of these connecting with other core nodes (named p) is set at 7/Ncore to ensure that core will be connected. These parameters can be easily modified on the script.\n")

parser.add_argument('-N', '--nodes',
						dest = "nodes",
						action = "store",
						default = None,
						help = "Number of nodes in the network.\n")

parser.add_argument('-E', '--links',
						dest = "E",
						action = "store",
						default = None,
						help = "Number of links that, after the core creation, new arrival nodes will have.\n")

parser.add_argument('-o', '--output',
						dest = "output",
						action = "store",
						default = "",
						help = "Name for the output file.\n")

options=parser.parse_args()

def Barabasi_Albert_network_creator (N, E, outputfilename=""):

    #Output file name
    if not outputfilename:
        outputfilename=str(N)+"_"+str(E)+"_"+"Barabási-Albert_network.net"
    else:
        outputfilename=outputfilename+".net"

    outfile=open(outputfilename, "w")
    outfile.write("*Vertices " + str(N) + "\n*Edges\n")

    #Core creation (30% of the nodes)
    Ncore=int(N*0.3) #This can be modified to use different ammount of nodes in the core
    p=7/Ncore #Having 7 links per node in the core we ensure it will be connected
    already_connected=[]
    connections=0
    degree_dict={}

    for node in range(1,Ncore+1):
        if node not in degree_dict.keys():
            degree_dict[node]=0
        for other_node in range(1,Ncore+1):
            if other_node not in degree_dict.keys():
                degree_dict[other_node]=0
            if node != other_node:
                if random() <= p:
                    if node < other_node:
                        edge_to_add = str(node) + " " + str(other_node)
                    else:
                        edge_to_add = str(other_node) + " " + str(node)

                    if edge_to_add not in already_connected:
                        already_connected.append(edge_to_add)
                        outfile.write(edge_to_add+"\n")
                        connections+=1
                        degree_dict[node]=degree_dict[node]+1
                        degree_dict[other_node]=degree_dict[other_node]+1

    for new_node in range(Ncore+1,N+1):
        degree_dict[new_node]=0
        links=0
        while links < E:
            other_node = choice(list(degree_dict.keys()))
            if new_node != other_node:
                p_edge=degree_dict[other_node]/connections
                if random() <= p_edge:
                    edge_to_add = str(other_node) + " " + str(new_node)
                    outfile.write(edge_to_add+"\n")
                    degree_dict[other_node]=degree_dict[other_node]+1
                    degree_dict[new_node]=degree_dict[new_node]+1
                    links+=1
if __name__=='__main__':
    try:
        N=int(options.nodes)
        if N:
            try:
                E=int(options.E)
            except:
                sys.stderr.write("\n-E argument is missing, please, set the number of links that the nodes arriving after the core creation will have in the network.\n\n")

    except:
        sys.stderr.write("\n-N argument is missing, please, set the number of nodes in the network.\n\n")

    outputfilename=options.output

    Barabasi_Albert_network_creator(N,E,outputfilename)
