# rscb_cys_screen

This script screens any cysteine residue within the 4 angstrom radius of the ligand in a rcsb_pdb structure.

Ligand definition: at least 3 types of elements, atom number > 10



After getting the pdb code using

```
print(cmd.get_object_list())
```

, query in https://www.uniprot.org/id-mapping to get detailed target protein information.