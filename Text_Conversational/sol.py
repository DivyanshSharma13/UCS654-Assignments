import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

models_list = ['DialoGPT-medium', 'BlenderBot-400M', 'GODEL-base', 'T5-base', 'GPT-2-large']

dataset = {
    'Model_Name': models_list,
    'Perplexity': [26.4, 19.1, 23.5, 33.2, 25.1],
    'BLEU_Score': [0.16, 0.29, 0.21, 0.13, 0.19],
    'Params_Millions': [345, 365, 220, 220, 774], 
    'Inference_Time': [115, 145, 105, 175, 135]
}

results_df = pd.DataFrame(dataset)

print("Original Data:")
print(results_df)
print("-" * 30)
metrics = ['Perplexity', 'BLEU_Score', 'Params_Millions', 'Inference_Time']

criteria_weights = [0.25, 0.35, 0.20, 0.20]
is_benefit = [False, True, False, False] 


norm_df = results_df[metrics].copy()

for metric in metrics:
    sq_sum = np.sqrt((results_df[metric]**2).sum())
    norm_df[metric] = results_df[metric] / sq_sum


weighted_data = norm_df.copy()

for i, col_name in enumerate(metrics):
    weighted_data[col_name] = norm_df[col_name] * criteria_weights[i]


ideal_best_values = []
ideal_worst_values = []

for i, col_name in enumerate(metrics):
    if is_benefit[i]:
        best_val = weighted_data[col_name].max()
        worst_val = weighted_data[col_name].min()
    else:
        best_val = weighted_data[col_name].min()
        worst_val = weighted_data[col_name].max()
        
    ideal_best_values.append(best_val)
    ideal_worst_values.append(worst_val)

dist_best = []
dist_worst = []

for i in range(len(weighted_data)):
    row = weighted_data.iloc[i]
    
    d_plus = np.sqrt(np.sum((row - ideal_best_values) ** 2))
    d_minus = np.sqrt(np.sum((row - ideal_worst_values) ** 2))
    
    dist_best.append(d_plus)
    dist_worst.append(d_minus)

performance_score = []

for i in range(len(dist_best)):
    score = dist_worst[i] / (dist_best[i] + dist_worst[i])
    performance_score.append(score)

results_df['Topsis_Score'] = performance_score

results_df['Final_Rank'] = results_df['Topsis_Score'].rank(ascending=False)

print("\nFinal Ranked Results:")
print(results_df.sort_values(by='Final_Rank'))


results_df.to_csv('conversational_model_ranking.csv', index=False)

plt.figure(figsize=(8, 5))
colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'violet']
bars = plt.bar(results_df['Model_Name'], results_df['Topsis_Score'], color=colors)

plt.xlabel('AI Models')
plt.ylabel('TOPSIS Score')
plt.title('Best Text Conversational Model Ranking')
plt.xticks(rotation=15)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 3), ha='center')

plt.tight_layout()
plt.savefig('result_graph.png')
plt.show()