from sys import argv
import yaml
import io
import numpy as np
import pandas as pd

folder_loc, project_name, n_PWs = argv[1:]
table = pd.DataFrame([0 for i in range(int(n_PWs))])

for i in range(int(n_PWs)):
    data_loaded = None
    with open("{}/4-PWs/{}_{}_mnpw.yaml".format(folder_loc, project_name, i), 'r') as stream:
        data_loaded = yaml.load(stream)
    for key, subdict in data_loaded.items():
        if 'group' in subdict:
            group = subdict['group']
            if group in table:
                table.set_value(i, group, table.iloc[i][group]+1)
            else:
                table[group] = 0
                table.set_value(i, group, 1)
        if 'label' in subdict:
            label = subdict['label']
            if label in table:
                table.set_value(i, label, table.iloc[i][label]+1)
            else:
                table[label] = 0
                table.set_value(i, label, 1)

table = table.drop(0, axis = 1)
table.reindex_axis(sorted(table.columns), axis=1)

table.to_csv('{}/extracted_stats.csv'.format(folder_loc))

