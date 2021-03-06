import pandas as pd

res_list = ['extra_trees.csv', 'xgb_cate_comb.csv', 'xgb_rf_feat.csv'] # ensemble1
res_list = ['extra_trees.csv', 'xgb_cate_comb.csv', 'xgb_delimiter.csv'] # ensemble2
res_list = ['extra_trees.csv', 'xgb_cate_comb.csv'] # ensemble3
res_list = ['extra_trees.csv', 'xgb_cate_comb.csv', 'addNNLinearFt.csv'] # ensemble4

ext_df = pd.read_csv(res_list[0]) 
xgb_df = pd.read_csv(res_list[1]) 
nn_df = pd.read_csv(res_list[2]) 
ids = ext_df['ID'].values

res_pred = 0.3 * nn_df.PredictedProb + 0.5 * ext_df.PredictedProb  + 0.2 * xgb_df.PredictedProb 

'''
df = pd.read_csv(res_list[0])
res_pred = df['PredictedProb']
ids = df['ID'].values

for f in res_list[1:]:
    df = pd.read_csv(f)
    res_pred = res_pred + df['PredictedProb']

res_pred /= len(res_list)
'''

preds_out = pd.DataFrame({"ID": ids, "PredictedProb": res_pred.values})
preds_out = preds_out.set_index('ID')
preds_out.to_csv('ensemble10.csv')
print 'finish'



