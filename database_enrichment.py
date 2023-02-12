import gseapy
from gseapy import barplot, dotplot

# Define your protein list with UniProt accession numbers
protein_list = ["ADORA2A", "ABL1", "ACVR1", "ADH5", "ADK", "ADRB2", "GLA", "AKR1B10", "AKR1C3", "AKT1", "ALDH1A1",
                "ALDH3A1", "AKR1B1", "ALK", "PRMT1", "PRMT5", "PRMT6", "MAOA", "MAOB", "AURKA", "BACE1", "BCAT1",
                "BCAT2", "BCL6", "GLB1", "BIRC2", "BLVRB", "BMP1", "BRAF", "BRD1", "BRD2", "BRD4", "BRDT", "BRPF1",
                "BTK", "CYP11B1", "CYP11B2", "CACNA1G", "CARM1", "CASP1", "CASP3", "CTSK", "CTSL", "CTSS", "CBR1",
                "CCR2", "CDK5", "CDK9", "CECR2", "CETP", "CFD", "CHEK1", "CHEK2", "BCHE", "CMA1", "CNR1", "COMT",
                "CYP17A1", "CYP19A1", "CYP1A1", "CYP1A2", "CYP1B1", "CYP2A6", "CYP2C8", "CYP2C9", "CYP2D6", "CYP3A4",
                "CYP51A1", "CSF1R", "CTBP1", "CXCR4", "AMD1", "DCK", "DCUN1D1", "ODC1", "PDF", "HSD17B1", "SORD",
                "DNMT3B", "DNMT1", "DPP4", "DUSP3", "EIF2AK3", "EIF2AK4", "EDNRB", "EGFR", "EHMT1", "EHMT2", "ELANE",
                "EP300", "EPAS1", "ERBB4", "SQLE", "ERN1", "ESRRG", "ESR1", "EZH2", "FBP1", "PFKFB3", "F10", "F11",
                "F7", "F9", "FABP4", "PTK2", "FDFT1", "FGFR1", "FGFR4", "FLT3", "FNTB", "GAK", "NR3C1", "GNAS", "GSK3B",
                "GSTO1", "HSD17B10", "HDAC2", "HDAC4", "HDAC7", "HDAC8", "HMGCR", "HPGDS", "IDO1", "IDH1", "IGF1R",
                "CHUK", "IKZF1", "ITK", "JAK3", "KDM5A", "KDM5B", "PRKG1", "KHK", "KIT", "KLK5", "KLK7", "KLKB1",
                "KMT2A", "KMT5B", "RPS6KA3", "RPS6KB1", "KSR2", "LGMN", "GLO1", "L3MBTL3", "LSS", "LY96", "MAP3K12",
                "MAP3K14", "MAP3K20", "MAP3K7", "MAP4K1", "MAP4K4", "METAP1", "MAPKAPK2", "MAPKAPK3", "NR3C2", "MELK",
                "MEN1", "MET", "MGLL", "MAPK1", "MAPK10", "MAPK14", "MKNK2", "MAP2K1", "MTOR", "NAAA", "NCOA1", "NEK2",
                "NMT1", "NOS1", "NOS2", "NOS3", "NQO2", "NTRK1", "OGA", "OPRL1", "HCRTR1", "HCRTR2", "DAO", "P2RY1",
                "P2RY12", "PLA2G2A", "PLA2G2E", "PLA2G10", "F2RL1", "PARG", "PCK1", "PTGDR2", "PDE4B", "PDE4D", "PDE5A",
                "PIN1", "PIK3CA", "PLK1", "PLK2", "PLG", "PKMYT1", "PNMT", "PPARA", "PPARD", "PPARG", "PREP", "CTSA",
                "PGR", "PRPF4B", "PSMB7", "PTPN1", "PTPN22", "PTPN9", "PTPRB", "ATIC", "RARA", "ROCK2", "RORC", "RXRB",
                "SLC29A1", "AHCY", "SETD2", "SIRT1", "SIRT2", "SMYD2", "SMYD3", "SPR", "SRC", "SULT1E1", "STK10",
                "STK3", "SUZ12", "TAB1", "TBK1", "VCP", "TGFBR2", "F2", "TEK", "TLR8", "TNIK", "TPH1", "TTBK1", "TTK",
                "TDP2", "TYK2", "TYMS", "USP7", "ULK1", "ULK2", "PLAU", "FLT1", "KDR", "PPIP5K2", "WDR5", "WEE1",
                "XIAP", "ZNF692"]

# Perform PFAM domain enrichment analysis using the 'gseapy' package
pfam_results = gseapy.enrichr(gene_list=protein_list, gene_sets=['InterPro_Domains_2019',  'KEGG_2021_Human', 'GO_Molecular_Function_2021'], outdir="./")


# ax = dotplot(pfam_results.res2d, title='Pfam_Human',cmap='viridis_r', size=10, figsize=(3, 5), ofname="pfam.png")

print(pfam_results.res2d)
ax = dotplot(pfam_results.results,
             column="Adjusted P-value",
             x='Gene_set',  # set x axis, so you could do a multi-sample/library comparsion
             size=10,
             top_term=10,
             figsize=(8, 15),
             title="Ligandable Cys Enrichment (N=255)",
             xticklabels_rot=45,  # rotate xtick labels
             show_ring=False,  # set to False to revmove outer ring
             marker='o',
             ofname="pfam.png"
             )

# Print the top 10 enriched PFAM domains
# for domain in pfam_results.res2d[:10].itertuples():
#    print(domain.Term)
