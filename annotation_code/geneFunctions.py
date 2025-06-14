#!/usr/bin/env python3

#Given a list of genes from an ME, find the biological functions

from modules.FileRead_class import Gene
import pandas as pd

def get_func(line):
    return line[3:5]

def get_gene(line):
    return line[0]

def genFunc(g_reference, target_genes):
    collapsedGenes=[]
    #iterate through the lines in the file
    for line in g_reference:
        line=line.strip().split("\t") #fix line
        id=get_gene(line) #get the id form each one
        
        if id in target_genes: #ad if the id is one of the genes of interest
            gNames=get_func(line) #get symbol and full name (names correspond to function)
            shortLine=[id]+gNames  #join them in a list with ID

            collapsedGenes.append(shortLine) #append to large list
            
    return collapsedGenes
            
            
        

#Zm00001eb068950
#Zm00001eb255730
#Zm00001eb000110
def main():
    genlist=['Zm00001eb374360', 'Zm00001eb144680', 'Zm00001eb213590', 'Zm00001eb265650', 'Zm00001eb403140', 'Zm00001eb281920', 'Zm00001eb157160', 'Zm00001eb279650', 'Zm00001eb292930', 'Zm00001eb411830', 'Zm00001eb044730', 'Zm00001eb040250', 'Zm00001eb229520', 'Zm00001eb252620', 'Zm00001eb327730', 'Zm00001eb291410', 'Zm00001eb134790', 'Zm00001eb160510', 'Zm00001eb329600', 'Zm00001eb194120', 'Zm00001eb411820', 'Zm00001eb167260', 'Zm00001eb296200', 'Zm00001eb416230', 'Zm00001eb326850', 'Zm00001eb205780', 'Zm00001eb213890', 'Zm00001eb309900', 'Zm00001eb110680', 'Zm00001eb316450', 'Zm00001eb349330', 'Zm00001eb082980', 'Zm00001eb214130', 'Zm00001eb008800', 'Zm00001eb057630', 'Zm00001eb427100', 'Zm00001eb329610', 'Zm00001eb068540', 'Zm00001eb235620', 'Zm00001eb065120', 'Zm00001eb220920', 'Zm00001eb249100', 'Zm00001eb255750', 'Zm00001eb178010', 'Zm00001eb157340', 'Zm00001eb347640', 'Zm00001eb126370', 'Zm00001eb208580', 'Zm00001eb106060', 'Zm00001eb241300', 'Zm00001eb042240', 'Zm00001eb351020', 'Zm00001eb428470', 'Zm00001eb403980', 'Zm00001eb412500', 'Zm00001eb232230', 'Zm00001eb272470', 'Zm00001eb393150', 'Zm00001eb131420', 'Zm00001eb222420', 'Zm00001eb060380', 'Zm00001eb187140', 'Zm00001eb368060', 'Zm00001eb274090', 'Zm00001eb257980', 'Zm00001eb257990', 'Zm00001eb329230', 'Zm00001eb409880', 'Zm00001eb040380', 'Zm00001eb353680', 'Zm00001eb000220', 'Zm00001eb255060', 'Zm00001eb257110', 'Zm00001eb060660', 'Zm00001eb311900', 'Zm00001eb059960', 'Zm00001eb078170', 'Zm00001eb290580', 'Zm00001eb153360', 'Zm00001eb227970', 'Zm00001eb375210', 'Zm00001eb007250', 'Zm00001eb061530', 'Zm00001eb403270', 'Zm00001eb340790', 'Zm00001eb066590', 'Zm00001eb192110', 'Zm00001eb010730', 'Zm00001eb225570', 'Zm00001eb369150', 'Zm00001eb201090', 'Zm00001eb129710', 'Zm00001eb154050', 'Zm00001eb255050', 'Zm00001eb204890', 'Zm00001eb012010', 'Zm00001eb212160', 'Zm00001eb121880', 'Zm00001eb336960', 'Zm00001eb157120', 'Zm00001eb123690', 'Zm00001eb101420', 'Zm00001eb065460', 'Zm00001eb046110', 'Zm00001eb327720', 'Zm00001eb297190', 'Zm00001eb116810', 'Zm00001eb035860', 'Zm00001eb121240', 'Zm00001eb217750', 'Zm00001eb384300', 'Zm00001eb135920', 'Zm00001eb225540'] 


    with open("../data/annotation/genes_all.txt") as file:
        totGen=file.readlines()
        
    matchGen=genFunc(totGen, genlist)
    print(matchGen)
    
    
if __name__ == "__main__":
    main()