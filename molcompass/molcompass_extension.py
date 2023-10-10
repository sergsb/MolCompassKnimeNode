import logging
import knime_extension as knext
import numpy as np
from molcomplib import MolCompass

LOGGER = logging.getLogger(__name__)

columns_names = ['smiles', 'molecules', 'structures', 'mols', 'smi', 'canonical_smiles', 'canonisized_smiles',
                 'canon_smiles',
                 'can_smiles', 'can_smi']

pharminfo = knext.category(
    path="/community",
    level_id="pharmacoinformatics",
    name="Pharmacoinformatics Research Group (UNIVIE)",
    description="Nodes created by the Pharmacoinformatics Research Group at the University of Vienna members.",
    icon="univie.png",
)

@knext.node(name="MolCompass", node_type=knext.NodeType.MANIPULATOR, icon_path="molcompass.ico", category=pharminfo)
@knext.input_table(name="Molecular Table", description="A dataset with molecular structures")
@knext.output_table(name="Output Data", description="The same datatable, plus X and Y coordinates")
#@knext.output_view(name="Chemical space", description="Showing a seaborn plot of chemical space")

class MolCompassKnimeNode():
    molcompass = MolCompass()
    smiles_column = knext.ColumnParameter(label="SMILES column",description="The SMILES column to use", column_filter=lambda x: (x.name.lower() in columns_names), port_index=0,include_none_column=False )

    def configure(self, configure_context, input_schema_1):
        input_schema_1 = input_schema_1.append(knext.Column(knext.double(), "x"))
        input_schema_1 = input_schema_1.append(knext.Column(knext.double(), "y"))
        return input_schema_1

    def execute(self, exec_context, input_1):
        data = input_1.to_pandas()
        def robust(x):
            try:
                return self.molcompass(x)
            except:
                return np.array([np.NAN, np.NAN], dtype=np.float32)
        if self.smiles_column == None:
            #Info
            LOGGER.info("No smiles column found. Trying to guess one...")
            smiles_column = [x for x in data.columns if x.lower() in columns_names]
            assert len(smiles_column) == 1, "Dataframe should contain ONLY one smiles column, but found: {}".format(smiles_column)
            smiles_column = smiles_column[0]
        else:
            smiles_column = self.smiles_column
        coords = data[smiles_column].apply(robust)
        data['x'] = coords.apply(lambda x: x[0])
        data['y'] = coords.apply(lambda x: x[1])
        return knext.Table.from_pandas(data)


