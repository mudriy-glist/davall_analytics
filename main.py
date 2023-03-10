import pandas as pd

cost_record = {}

df = pd.read_excel('cost_export.xlsx')

for index, row in df.iterrows():

    if row['WOEstMatCost'] == 0 or row['WORoutSetUpCost'] == 0 or row['WORoutUnitCost'] == 0:
        continue
    
    if row['WONo1'] not in cost_record:
        if row['WORoutOpNo'] == 10:
            cost_record[row['WONo1']] = {
                row['WORoutOpNo']: (row['WOEstMatCost'] / row['WOQty']) + row['WORoutUnitCost']
                + row['WOSubConCostPerItem'] + (row['WORoutSetUpCost'] / row['WOQty'])
                }
    elif row['WORoutOpNo'] > 10:
            prev_record = list(cost_record[row['WONo1']].items())[-1]
            cost_record[row['WONo1']] = { row['WORoutOpNo']: row['WORoutUnitCost'] + prev_record[1] }
print(cost_record)