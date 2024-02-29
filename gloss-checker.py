import pandas as pd
import argparse
import os
import glob

def gloss_word_checker(fname):
 
    lang = pd.read_csv(fname)
 
    lang['words'] = lang['words'].str.replace('\t', ' ')
    lang['gloss'] = lang['gloss'].str.replace('\t', ' ')
 
    lang['words'] = lang['words'].str.replace('\t', ' ')
    lang['gloss'] = lang['gloss'].str.replace('\t', ' ')
 
    word_lens = [len(wordlst.split()) for wordlst in list(lang['words'])]
    gloss_lens = [len(glosslst.split()) for glosslst in list(lang['gloss'])]
 
    counter = 0
    discrepancies = []
 
    for pair in zip(word_lens, gloss_lens):
        if pair[0] != pair[1]:
            discrepancies.append((pair, lang.loc[counter], "Discrepancy in file {}: row {}".format(fname, counter+2)))
        counter += 1
 
    return discrepancies
 
   
def process_path(input_path):
 
    if os.path.isdir(input_path):
        for filename in glob.glob(os.path.join(input_path, '*.csv')):
            discrepancies = gloss_word_checker(filename)
            print(f"Discrepancies in {filename}:")
            for discrepancy in discrepancies:
                print(discrepancy)
               
    elif os.path.isfile(input_path):
 
        discrepancies = gloss_word_checker(input_path)
        print(f"Discrepancies in {input_path}:")
        for discrepancy in discrepancies:
            print(discrepancy)
           
    else:
        print("The provided path is neither a directory nor a file.")
       
 
def write_discrepancies_to_csv(discrepancies, output_filename):
 
    df = pd.DataFrame(discrepancies, columns=['Length Pair', 'Row Data', 'Message'])
    df.to_csv(output_filename, index=False)
       
 
if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description='Check discrepancies between word and gloss lengths in a CSV file or all CSV files within a directory.')
    parser.add_argument('input_path', type=str, help='File name or directory of the CSV(s) to be processed')
    parser.add_argument('--o', type=str, help='Optional: Output CSV file to write discrepancies')
 
    args = parser.parse_args()
   
    process_path(args.input_path, args.output_csv)