# Tips Analysis Visualization

Analyzes the classic "Tips" dataset to explore relationships between bill amounts, tips, gender, smoking status, day of week, and party size using advanced visualizations.[file:12]

## Dataset
- **Source**: Seaborn's built-in `tips` dataset (244 restaurant bills)
- **Key columns**: `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size`[file:12]
- **File**: `data/tips.csv`

## Key Insights
- **Tip patterns**: Higher bills → higher tips; males tip slightly more on average[file:12]
- **Smoking & time**: Smokers tip less; dinner tips > lunch tips[file:12]
- **Day patterns**: Saturday/Sunday see highest bills and tips[file:12]

## Usage
pip install -r requirements.txt
python src/analyze_tips.py
