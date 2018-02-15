#CS 583 Project 1 - MS APriori Algorithm 
#Contributors: Ayush and Kashyap

T = []
MS = {} 
illegal = []
must = []

def readInput():
    ''' reads the input transactions from the file '''
    
    f = open('input-data.txt','r')

    for line in f.readlines():
        transaction = line.strip().replace('{','').replace('}','').split(',')
        transaction = [int(x) for x in transaction]
        T.append(transaction)

def readParams():
    f = open('parameter-file.txt','r')

    for line in f.readlines():
        if line.find("MIS") != -1:
            temp = line.strip().replace('MIS','').replace('(','').replace(')','').split('=')
            MS[int(temp[0])] = float(temp[1])
        
        if line.find("SDC") != -1:
            phi = float(line.replace(' ','').rstrip().split('=')[1])

        if line.find("cannot_be_together") != -1:
            cannot = line.strip().replace('cannot_be_together','').replace(':','').replace('{','').split('},')
            for i in cannot: 
                grp = i.strip().replace('}','').split(',')
                grp = [int(x) for x in grp]
                illegal.append(grp)
        
        if line.find("must-have") != -1:
            have = line.strip().replace('must-have','').replace(':','').split('or')
            must = [int(x) for x in have]        
