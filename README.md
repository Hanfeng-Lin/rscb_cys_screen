# rscb_cys_screen

## main.py (pymol script)

This script screens any cysteine residue within the 4 angstrom radius of the ligand in a rcsb_pdb structure.

Ligand definition: at least 3 types of elements AND atom number > 10

After getting the pdb code using `print(cmd.get_object_list())`, query in https://www.uniprot.org/id-mapping to get detailed target protein information. But notice that this table includes many proteins co-exist in the pdb file but not the target protein. Further filtering will be done using `mapping_uniprot_pdbchain.py`

## mapping_cys.py (pymol script)

This script generates the `cys residue ID` (chainID_resi_resn) within 4A of ligand, exports as a csv in the current directory.

The output `pdb_cys.csv` contains in each row:
`pdb_id: [chain_id_with_cys, *cys_residue_id]`

## mapping_uniprot_pdbchain.py

The input is the id-mapping xlsx generated from uniprot `ID mapping web service`.

This script will find which chain(s) contains a certain uniprot protein given a pdb id.
An additional column "chainID" will be inserted into the xlsx, yielding `uniprot_IDmapping.xlsx`

## combine_table.py

Mapping the `pdb_cys.csv` to the `uniprot_IDmapping.xlsx`, so that in the `uniprot_IDmapping.xlsx`, the chain_id with cys near the pocket will be added.

## check_chain.py

To check whether the cys-containing chain_id from `pdb_cys.csv` also appears in the uniprot-mapped pdb chains.

For example: pdb `1FM6` has three proteins from `uniprot P19793, P37231, Q15788`, but only `P37231` contains near pocket cys. The purpose of this script is to tell whether each `uniprot_id` contains a near-pocket cys.

After manually remove all the non-cys-containing proteins and non-human proteins, this table contains all the currently available structures with cysteine within the 4A of ligand.

**A.k.a. a ligandable cysteinome list!**

## database_enrichment.py (Linux)

Input: Gene_ID list from non-redundant cysteinome uniprot list.

Output: 

1. Enrichment of Gene_ID in `KEGG pathway database`, `InterPro Domain Database`, `GO Molecular_Function Database` in tabulated format.
2. Bubble plot for 1.