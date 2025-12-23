"""
Tips Dataset Analysis - Complete Visualization Pipeline
Explores restaurant tipping patterns with professional plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configure plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.dpi'] = 300

def load_data(file_path: str) -> pd.DataFrame:
    """Load the tips dataset and show basic info."""
    df = pd.read_csv(file_path)
    print(f"Dataset: {df.shape[0]} bills from {df['day'].nunique()} days")
    print("\nDataset preview:")
    print(df.head())
    print(f"\nTip percentage stats: {df['tip_pct'].describe():.2f}")
    return df

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add tip percentage and basic cleaning."""
    df['tip_pct'] = df['tip'] / df['total_bill'] * 100
    print(f"\nData prepared with tip_pct column (mean: {df['tip_pct'].mean():.2f}%)")
    return df

def summary_stats(df: pd.DataFrame):
    """Print key summary statistics by category."""
    print("\n=== SUMMARY STATS ===")
    
    # By gender
    gender_stats = df.groupby('sex')[['total_bill', 'tip', 'tip_pct']].mean().round(2)
    print("\nAverage by Gender:")
    print(gender_stats)
    
    # By time of day
    time_stats = df.groupby('time')[['total_bill', 'tip', 'tip_pct']].mean().round(2)
    print("\nAverage by Time:")
    print(time_stats)

def create_visualizations(df: pd.DataFrame):
    """Generate comprehensive set of professional plots."""
    os.makedirs('output', exist_ok=True)
    
    # 1. Scatter plot: Total bill vs Tip (with hue by gender)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='total_bill', y='tip', hue='sex', size='size', alpha=0.7)
    plt.title('Total Bill vs Tip Amount\n(Size = Party Size)', fontsize=14, pad=20)
    plt.xlabel('Total Bill ($)')
    plt.ylabel('Tip ($)')
    plt.tight_layout()
    plt.savefig('output/bill_vs_tip_scatter.png', bbox_inches='tight')
    plt.close()
    
    # 2. Box plot: Tip % by day and time
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='day', y='tip_pct', hue='time', order=['Thur', 'Fri', 'Sat', 'Sun'])
    plt.title('Tip Percentage by Day and Time of Day')
    plt.ylabel('Tip %')
    plt.xlabel('Day of Week')
    plt.tight_layout()
    plt.savefig('output/tip_pct_by_day_time.png', bbox_inches='tight')
    plt.close()
    
    # 3. Violin plot: Bill amount by smoker status and gender
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x='smoker', y='total_bill', hue='sex')
    plt.title('Distribution of Total Bills\nby Smoker Status and Gender')
    plt.ylabel('Total Bill ($)')
    plt.xlabel('Smoker')
    plt.tight_layout()
    plt.savefig('output/bill_distribution_smoker.png', bbox_inches='tight')
    plt.close()
    
    # 4. Pair plot for correlations (subset)
    cols = ['total_bill', 'tip', 'size', 'tip_pct']
    sns.pairplot(df[cols + ['sex']], hue='sex', diag_kind='hist')
    plt.suptitle('Pairwise Relationships in Tips Data', y=1.02)
    plt.savefig('output/pairplot.png', bbox_inches='tight', dpi=200)
    plt.close()
    
    # 5. Heatmap of correlations
    plt.figure(figsize=(8, 6))
    corr = df[['total_bill', 'tip', 'size', 'tip_pct']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, square=True)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('output/correlation_heatmap.png', bbox_inches='tight')
    plt.close()
    
    print("\n✅ All 5 plots saved to 'output/' folder!")

def main():
    """Execute complete analysis and visualization pipeline."""
    print("=== Restaurant Tips Analysis ===\n")
    
    # Load and prepare data
    df = load_data('data/tips.csv')
    df = prepare_data(df)
    
    # Summary statistics
    summary_stats(df)
    
    # Create all visualizations
    create_visualizations(df)
    
    print("\n🎉 Analysis complete! Check 'output/' for publication-ready plots.")

if __name__ == "__main__":
    main()
