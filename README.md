# Cross-linguistic dataset of force-flavor combinations in modal elements

This repository stores data in the Cross-linguistic dataset of force-flavor combinations in modal elements
(Uegaki, Mucha, Engels, Hannon & Whibley. to appear. Cross-linguistic dataset of force-flavor combinations in modal elements. _Linguistic Variation_). The dataset contains the data in a machine-readable CSV format (in the `language-data` directory) and in a PDF format (in the `language-questionnaires` directory). Please refer to Uegaki et al. (to appear) for the description of the data in the PDF format as well as the data collection methodology. To a large extent, the data in the CSV format and the PDF format are equivalent, but the PDF data also contains ancillary comments that are not recorded in the CSV format. Details of the CSV format are described in the section [Format of the CSV tables](#Format-of-the-CSV-tables) below.

## Basic repository structure

- README.md
- language-data
    - modals-questionnaire.csv 
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

The CSV format of the data for each language consists of four files: the metadata YAML file and three CSV tables: **the examples table**, **the evidence table**, and **the summary table**. In a nutshell, **the examples table** lists all relevant example sentences while **the evidence table** records felicity judgements regarding the examples in **the example table**. **The summary table** summarizes the modal inventory, with information about relevant morpho-syntactic and semantic properties of each modal element in the language. In addition, the `language-data` contains `modals-questionnaire.csv` which contains the contexts (based on Vander Klok 2022[^1]) used in the elicitation sessions to obtain the felicity of examples sentences. 

[^1]: Vander Klok, Jozina. 2022. "Discourse contexts targeting modality in fieldwork: A revised modal questionnaire." In J. Vander Klok, N. Rech and S. Guesser (eds.) _Studying modality in underdescribed languages: Methods and insights._ (Trends in Linguistics series). Berlin: Mouton de Gruyter.

#### Language metadata (lang-metadata.yml)

The matadata YAML files containts the following information about the language:

- Language name
- ISO 639-3 code
- Glottolog code
- Consultant demographics
- Elicitation dates

#### The examples table (lang-examples.csv)

The example table contains all examples elicited for the language with unique reference `ref` for each example. 
The examples are represented in a way similar to the Interlinear Glossed Text, where the `words` correspond to the transcription with word boundaries, the `gloss` corresponds to the gloss for each word in `words` and `translation`
corresponds to the translation of the example. For the purpose of this dataset, the relevant modal element is glossed as MOD. The `comment` contains additional information relevant for the analysis of the example. 

| ref |	words	| gloss	| translation |	comment |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| aka-modal-1 | ɛsɛsɛ Ben dware	| MOD Ben swim	| Ben must be swimming	| The morphological analysis of ɛsɛsɛ according to Owusu (2014): Ɛ-sɛ-sɛ: expletive-fit-Comp |
| aka-modal-1b	| Ɛwɔsɛ Ben dware	| MOD Ben swim	| Ben must be swimming	|
| aka-modal-2	| Ɛwɔsɛ John wɔ sukuu |	MOD John be school | John must be at school	|

#### The evidence table (lang-evidence.csv)

The evidence table records the acceptability and felicity judgments of the examples given a certain context in `modals-questionnaire.csv`. For example, in the following sample table from Akan, the initial row indicates that example `aka-modal-1` in the example table is felicitous in context `epi-nec-1` in `modals-questionnaire.csv`. This piece of evidence then has the unique reference `aka-modal-evid1`. The `premise` column is provided to record judgments about inference patterns if necessary. 

| ref | context	| premise	| example	| judgment	| comment	|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| aka-modal-evid1 |	epi-nec-1 | na	| aka-modal-1	| felicitous	|
| aka-modal-evid1b	| epi-nec-1	| na	| aka-modal-1b	| infelicitous	|
| aka-modal-evid2	| epi-nec-2	| na	| aka-modal-2	| felicitous |

#### The summary table  (lang-summary.csv)

The summary table records the properties of each modal expression in the language, given the evidence available in the evidence table. For example, in the following sample table from Akan, the initial row indicates that the expression _ɛsɛsɛ_ can express epistemic necessity (`strong` force in the `epistemic` flavor) with reference to the evidence `aka-modal-evid1`, `aka-modal-evid2b`, and `aka-modal-evid3` in the Akan evidence table. 

| expression | force | flavor | can_express	| evidence	| polarity	| syntactically_negated	| full_form	| notes	|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| ɛsɛsɛ	| strong	| epistemic	| 1	| aka-modal-evid1, aka-modal-evid2b, aka-modal-evid3	| positive	| no	| ɛsɛsɛ		|
| ɛsɛsɛ	| weak necessity	| epistemic	| 1	| aka-modal-evid5, aka-modal-evid6	| positive	| no	| ɛsɛsɛ	|
| ɛsɛsɛ	| weak	| epistemic	| ?		|| positive	| no	| ɛsɛsɛ	|

The format of this table follows [The Database of Modal Typology](https://github.com/CLMBRs/modal-typology) (Guo et al. 2022[^2]). The columns contain the following information and possible values: 

- `expression`: transcription of the modal element corresponding to the MOD element in the examples table.
- `force`: the possible force of the interpretation of the modal element with the following possible values.
    - `strong`: necessity interpretation or non-necessity interpretation;
    - `weak`: possibility interpretation or impossibility interpretation;
    - `weak necessity`: weak necessity interpretation;
- `flavor`: the possible flavors of the interpretation of the modal element
- `can_express`: whether the modal element can express the relevant force/flavor combination. The value is `?` if there is no relevant evidence in the evidence table.
- `polarity`: the polarity of the possible interpretation.
    -  `positive`: necessity, weak necessity, and possibility interpretations;
    -  `negative`: impossibility and non-necessity interpretations.
- `syntactically negated`: if the form contains syntactic negation, and if so whether the negation is syntactically higher or lower than the element. 


[^2]: Guo, Qingxia, Nathaniel Imel, Shane Steinert-Threlkeld. 2022. "A Database for Modal Semantic Typology", _Proceedings of the 4th Workshop on Computational Typology and Multilingual NLP (SIGTYP 2022)_, pp 42-51.

## How to cite the data

Uegaki, Wataru, Anne Mucha, James Engels, Ella Hannon and Fred Whibley. to appear. Cross-linguistic dataset of force-flavor combinations in modal elements. _Linguistic Variation_
