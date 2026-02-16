# TOPSIS Analysis for Conversational AI Models

This project implements the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) method to rank five different conversational AI models. The goal is to determine the most balanced model by evaluating multiple performance metrics simultaneously.

##  Overview

In this analysis, we compare models that vary in size, speed, and accuracy. TOPSIS allows us to rank these models by calculating their geometric distance from the **Ideal Best** solution and the **Ideal Worst** solution.

### Models Evaluated
* **DialoGPT-medium**
* **BlenderBot-400M**
* **GODEL-base**
* **T5-base**
* **GPT-2-large**

---

##  Evaluation Criteria

The models are judged based on the following weighted criteria:

| Metric | Category | Weight | Description |
| :--- | :--- | :--- | :--- |
| **Perplexity** | Cost (Lower is better) | 0.25 | Measures how well the model predicts a sample. |
| **BLEU Score** | Benefit (Higher is better) | 0.35 | Measures linguistic similarity to human text. |
| **Params (M)** | Cost (Lower is better) | 0.20 | Model size (Memory efficiency). |
| **Inference Time** | Cost (Lower is better) | 0.20 | Latency/Speed of response. |

---

##  Methodology

The script performs the following mathematical steps:
1. **Vector Normalization**: Converts raw data into a normalized scale.
2. **Weighted Normalized Matrix**: Applies the importance weights to each metric.
3. **Ideal Solutions**: 
   - Identifies the $V^+$ (Best values across all models).
   - Identifies the $V^-$ (Worst values across all models).
4. **Distance Calculation**: Computes the Euclidean distance ($D^+$ and $D^-$) for each model.
5. **Performance Score**: Calculates the final TOPSIS score ($S = D^- / (D^+ + D^-)$).



---

##  Results

The execution of the script produces two main outputs:

1. **`conversational_model_ranking.csv`**: A CSV file containing the original data, the calculated TOPSIS scores, and the final rankings.
2. **`result_graph.png`**: A bar chart visualizing the comparison.

### Final Ranking Summary
Based on the provided data, the models are ranked from 1 to 5. A higher TOPSIS score indicates a model that better satisfies the balance between high performance and low resource cost.



---

##  How to Run

1. Ensure you have Python installed with the following libraries:
   ```bash
   pip install numpy pandas matplotlib