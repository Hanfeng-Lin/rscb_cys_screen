from lxml import etree
import requests
import pandas as pd


def mapping_uniprot_pdbchain(uniprot_id, pdb_id):
    # Get the XML content from the URL
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.xml"
    response = requests.get(url)
    xml_string = response.content

    # Parse the XML content
    parsed_xml = etree.fromstring(xml_string)  # parsed_xml = etree.parse("P29466.xml")
    namespaces = {'ns': 'http://uniprot.org/uniprot'}

    # Find the chains value for the given PDB ID
    xpath = f"//ns:dbReference[@type='PDB' and @id='{pdb_id}']/ns:property[@type='chains']"
    property_content = parsed_xml.xpath(xpath, namespaces=namespaces)

    if property_content:
        chains = property_content[0].get("value")
        print(f"Chains for PDB ID {pdb_id}: {chains}")
        return chains
    else:
        print(f"No chains value found for PDB ID {pdb_id}")
        return None


df = pd.read_excel('uniprot_IDmapping.xlsx')

# Extract the first two columns without the header
pdb_uniprot_list = df.iloc[:, :2].values.tolist()

# Do your processing here...
pdb_uniprot: list
chain_id = []
for pdb_uniprot in pdb_uniprot_list:
    chain_id.append(mapping_uniprot_pdbchain(pdb_uniprot[1], pdb_uniprot[0]))

# Insert the processed data as a new column
df.insert(2, "chainID", chain_id, True)

# Save the updated DataFrame to an Excel file
df.to_excel("uniprot_IDmapping.xlsx", index=False)
