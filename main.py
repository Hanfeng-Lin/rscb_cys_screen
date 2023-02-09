from pymol import cmd, stored
import os

cmd.reinitialize()
counter = 0
non_hit = 0
# Loop over all the pdb files in the current directory
for filename in os.listdir():
    if filename.endswith(".pdb"):
        cmd.load(filename)
        counter += 1
        # filter the chemicals containing more than 3 types of elements and 10 atoms in the model
        atoms = cmd.get_model(filename[0:-4] + " and organic")
        res_elem_dict = {}
        res_atom_list = []
        true_ligand_list = []
        for at in atoms.atom:
            if at.chain + "_" + at.resi + "_" + at.resn in res_elem_dict:  # for element count
                res_elem_dict[at.chain + "_" + at.resi + "_" + at.resn].add(at.name[0:1])
            else:
                res_elem_dict[at.chain + "_" + at.resi + "_" + at.resn] = set(at.name[0:1])
            res_atom_list.append(at.chain + "_" + at.resi + "_" + at.resn)  # for atom count
        res_elemNo_dict = {key: len(value) for key, value in res_elem_dict.items()}
        res_atomNo_dict = {item: res_atom_list.count(item) for item in res_atom_list}

        elem3_ligand_id_list = [key for key, value in res_elemNo_dict.items() if value >= 3]
        atom10_ligand_id_list = [key for key, value in res_atomNo_dict.items() if value > 10]

        true_ligand_list = [item for item in elem3_ligand_id_list if item in atom10_ligand_id_list]  # take intersection
        print(filename[0:-4] + " ligand: " + str(true_ligand_list))

        # select the cys within 4A of ligand
        cys_global_set = set()
        for ligand_string in true_ligand_list:
            ligand_id = ligand_string.split("_")
            chain_id, resi, resn = ligand_id[0], ligand_id[1], ligand_id[2]
            cmd.select(filename[0:-4] + " and chain " + chain_id + " and resi " + resi + " and resn " + resn)
            cmd.select("byobj(sele) and byres(resn cys within 4 of sele)")
            cys_local_set = set()
            cmd.iterate("sele", 'cys_local_set.add(chain+"_"+resi+"_"+resn)')
            cmd.show("sticks", "sele")
            cmd.label("sele and name CA", '"%s-%s" % (resn,resi)')
            print(filename[0:-4] + ": cys near " + ligand_string + ":" + str(cys_local_set))
            cys_global_set = cys_global_set | cys_local_set

        if not cys_global_set:
            cmd.delete(filename[0:-4])
            non_hit += 1

print("total_pdb:", counter)
print("hits:", counter-non_hit)
