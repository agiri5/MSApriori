#CS 583 Project 1 - MS APriori Algorithm 
#Contributors: Ayush and Kashyap

T = []

def readInput():
    ''' reads the input transactions from the file '''
    
    f = open('input-data.txt','r')

    for line in f.readlines():
        transaction = line.strip().replace('{','').replace('}','').split(',')
        transaction = [int(x) for x in transaction]
        T.append(transaction)
