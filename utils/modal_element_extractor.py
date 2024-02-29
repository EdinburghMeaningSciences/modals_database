import pandas as pd
import csv
import argparse

def extract_modal_elements(fname):
    
    data = pd.read_csv(fname)

    glosses = data['gloss']
    words = data['words']

    glosses = [gloss.split() for gloss in glosses]
    words = [sent.split() for sent in words]

    modal_elements = []

    for gloss, sent in zip(glosses, words):

        mod_found = False

        if len(gloss) == len(sent):
            temp_lst = []
            for i, g in enumerate(gloss):
                if 'MOD' in g:
                    mod_found = True
                    temp_lst.append(sent[i])

            if len(temp_lst) == 1:
                modal_elements.append(temp_lst[0])

            elif not mod_found:
                modal_elements.append('None')

            else:
                modal_elements.append(temp_lst)

        elif len(sent) == 1:
            modal_elements.append(sent[0])

        else:
            modal_elements.append('None')

    for i, e in enumerate(modal_elements):

        if type(e) is str: 
            modal_elements[i] = e.lower()

        elif type(e) is list:
            modal_elements[i] = [s.lower() for s in e]
            
    print(modal_elements)
    return modal_elements

def save_to_csv(modal_elements, filename):
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        for element in modal_elements:
            
            if isinstance(element, list):
                writer.writerow(element)
                
            else:
                writer.writerow([element])
                
def main():
    parser = argparse.ArgumentParser(description='Extract modal elements from CSV.')
    parser.add_argument('filename', type=str, help='The filename of the CSV for processing.')

    args = parser.parse_args()

    modal_elements = extract_modal_elements(args.filename)

    save_option = input("Would you like to save the output to a CSV? (Y/N): ").strip().upper()
    if save_option == 'Y':
        output_filename = input("Please enter your desired filename: ").strip()
        save_to_csv(modal_elements, output_filename)
        print(f"Output saved to {output_filename}")

if __name__ == '__main__':
    main()
