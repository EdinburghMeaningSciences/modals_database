import pandas as pd
import re
import os

def write_evidence_file(f):
    
    evidence_columns = ['ref', 'context', 'premise', 'example', 'judgment', 'comment']

    data = pd.read_csv(f)

    evid = pd.DataFrame(columns = evidence_columns)
    evid['example'] = data['ref']

    pattern = r'(-\D*?)(\d)'
    replacement = r'\1evid\2'
    evid['ref'] = [re.sub(pattern, replacement, entry) for entry in list(evid['example'])]
    evid['context'] = data['context']
    evid['premise'] = 'na'

    judgments = []

    for sent in data['words']:
        if sent[0] == '#':
            judgments.append(('infelicitous', ''))
        elif sent[0] == '*':
            judgments.append(('ungrammatical', ''))
        elif sent[0] == '?':
            judgments.append(('felicitous', 'marginal'))
        else:
            judgments.append(('felicitous', ''))

    evid['judgment'] = [j[0] for j in judgments]
    evid['comment'] = [j[1] for j in judgments] 
    
    evid.index.name = 'index'

    output_filename = input('Please write output filename: ')
    
    if os.path.exists(output_filename):
        overwrite_flag = input('File already exists – would you like to overwrite? Y/N ')
    
    if overwrite_flag == 'Y': 
        evid.to_csv(output_filename)
        print(f'{output_filename} written successfully to {os.getcwd()}')
        
    else:
        print('Operation canceled')

write_evidence_file(input('Input source filename: '))
