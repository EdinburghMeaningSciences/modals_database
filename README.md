# Cross-linguistic dataset of force-flavor combinations in modal elements

This repository stores data in the Cross-linguistic dataset of force-flavor combinations in modal elements
(Uegaki, Mucha, Engels, Hannon & Fred Whibley. accepted. Cross-linguistic dataset of force-flavor combinations in modal elements. _Linguistic Variation_). The dataset contains the data in a machine-readable CSV format (in the `language-data` directory) and in a PDF format (in the `language-questionnaires` directory). Please refer to Uegaki et al. (to appear) for the description of the data in the PDF format. To a large extent, the data in the CSV format and the PDF format are equivalent, but the PDF data also contains ancillary comments that are not recorded in the CSV format. Details of the CSV format is described in the section [Format of the CSV tables](#Format-of-the-CSV-tables) below.

## Basic repository structure

- README.md
- language-data
    - lang1
        - lang1-metadata.yml
        - lang1-examples.csv
        - lang1-evidence.csv
        - lang1-summary.csv
    - lang2
        - lang2-metadata.yml
        - lang2-examples.csv
        - lang2-evidence.csv
        - lang2-summary.csv
    - ...
- language-questionnaires
    - _Modals Questionnaire version 2.1.pdf
    - lang1.pdf
    - lang2.pdf
    - ...
- utils
    - examples-to-evidence.py
    - gloss-checker.py
    - modal_element_extractor.py

## Format of the CSV tables

The CSV format of the data consists of four files: the metadata YAML file and three CSV tables: **the examples table**, **the evidence table**, and **the summary table**. In a nutshell, **the examples table** lists all relevant example sentences while **the evidence table** records felicity judgements regarding the examples in **the example table**. **The summary table** summarizes the modal inventory, with information about relevant morpho-syntactic and semantic properties of each modal element in the language. 

#### Language metadata (lang-metadata.yml)



#### The examples table (lang-examples.csv)

| ref |	words	| gloss	| translation |	comment |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| aka-modal-1 | ɛsɛsɛ Ben dware	| MOD Ben swim	| Ben must be swimming	| The morphological analysis of ɛsɛsɛ according to Owusu (2014): Ɛ-sɛ-sɛ: expletive-fit-Comp |
| aka-modal-1b	| Ɛwɔsɛ Ben dware	| MOD Ben swim	| Ben must be swimming	|
| aka-modal-2	| Ɛwɔsɛ John wɔ sukuu |	MOD John be school | John must be at school	|

#### The evidence table (lang-evidence.csv)

| ref | context	| premise	| example	| judgment	| comment	|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| aka-modal-evid1 |	epi-nec-1 | na	| aka-modal-1	| felicitous	|
| aka-modal-evid1b	| epi-nec-1	| na	| aka-modal-1b	| infelicitous	|
| aka-modal-evid2	| epi-nec-2	| na	| aka-modal-2	| felicitous |

#### The summary table  (lang-summary.csv)

| expression | force | flavor | can_express	| evidence	| polarity	| syntactically_negated	| full_form	| notes	|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| ɛsɛsɛ	| strong	| epistemic	| 1	| aka-modal-evid1, aka-modal-evid2b, aka-modal-evid3	| positive	| no	| ɛsɛsɛ		|
| ɛsɛsɛ	| weak necessity	| epistemic	| 1	| aka-modal-evid5, aka-modal-evid6	| positive	| no	| ɛsɛsɛ	|
| ɛsɛsɛ	| weak	| epistemic	| ?		| positive	| no	| ɛsɛsɛ	|

## How to cite the data

Uegaki, Wataru, Anne Mucha, James Engels, Ella Hannon and Fred Whibley. to appear. Cross-linguistic dataset of force-flavor combinations in modal elements. _Linguistic Variation_
