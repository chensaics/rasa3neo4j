from ruamel import yaml
import pandas as pd
import os


def convert_data(currentPath):
    if not os.path.exists(currentPath):
        return
    return


if __name__ == '__main__':
    file = 'Symptoms.txt'
    items = []
    with open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            item = '- {}'.format(line.strip('\n'))
            items.append(item)

    df = pd.DataFrame(items)
    out = 'Symptoms.xlsx'
    df.to_excel(out, index=None)




