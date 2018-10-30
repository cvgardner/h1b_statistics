'''Module containing functions to properly format and extract relevant data from h1b csv files'''

from pathlib import Path
import sys
from collections import defaultdict

def read_input(filepath):
    '''Takes an input csv file from commandline arguments and converts it into a list of lists

    Args:
        commandline filepath: csv file delimited by ; characters, representing h1b visa data

    Returns:
        data: list of lists representation of the data'''
    data = []
    with open(filepath, 'r') as f:
        line = f.readline()
        #loop over the rest of the file
        while line:
            data.append(line.split(';'))
            line = f.readline()
    return data

def clean_data(data, certified=True):
    '''Cleans data based on given requirements. Modifies input and returns nothing

    Args:
        data: list of lists containing the h1b data

    Returns:
        None'''
    
    #Remove all non certified positions
    if(certified):
        ind = data[0].index('CASE_STATUS')
        pointer = 1 #skip header row
        while pointer < len(data):
            if data[pointer][ind] == 'CERTIFIED':
                pointer += 1
            else:
                data.pop(pointer)

def top10s(data, filepath, column, outcolumn):
    '''Count the top 10 occupations from the dataset and save statistics to the given filepath

    Args:
        Data: dataset to process
        filepath: path to save data to
        column: column of data to count top 10s over
        outcolumn: what to name the unique column in the output file.

    Returns:
        None'''
    #Put data into an appropriate format
    counts = defaultdict(list)
    ind = data[0].index(column)
    for i in range(len(data)):
        title = data[i][ind]
        if title in counts:
            counts[title][0] += 1
        else:
            counts[title].append(1)
        
    #Build percentage statistic
    for job in counts:
        counts[job].append(counts[job][0] / len(data))
    #sort 
    sorted_counts = sorted(counts.items(), key = lambda x: x[1][0], reverse=True)

    #write to file
    with open(filepath, 'w') as f:
        f.write("{};NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n".format(outcolumn)
        count = 1
        for job in sorted_counts:
            f.write("{};{};{:.1%}\n".format(job[0], job[1][0], round(job[1][1],1))
            if count >=  10:
                break
            else:
                count += 1
    

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) ==  4:
        a, in_file, out1, out2 = sys.argv
    elif len(sys.argv) > 4:
        raise ValueError("Too many arguments passed. Please only pass 1 filepath")
    else:
        raise ValueError("No arguments provided, please provide a filepath argument")
    data = read_input(in_file)
    clean_data(data)
    top10s(data, out1, 'JOB_TITLE', 'TOP_OCCUPATIONS')
    top10s(data, out1, 'WORKSITE_STATE', 'TOP_STATES')
