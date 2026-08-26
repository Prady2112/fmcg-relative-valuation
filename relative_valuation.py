import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_valuation_analysis():
    print("=== FMCG Sector Relative Valuation Analysis ===")
    
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "fmcg_valuation_summary.csv")
    
    if not os.path.exists(data_path):
        print("Data file not found. Please run fetch_data.py first.")
        return
        
    df = pd.read_csv(data_path)
    
    print("\n--- Summary Data ---")
    print(df.to_string())
    
    # Calculate Industry Averages
    avg_pe = df['P/E Ratio'].mean()
    avg_ev_ebitda = df['EV/EBITDA'].mean()
    
    print(f"\n--- Industry Averages ---")
    print(f"Average P/E Ratio:   {avg_pe:.2f}")
    print(f"Average EV/EBITDA:   {avg_ev_ebitda:.2f}")
    
    print("\n--- Britannia Analysis ---")
    britannia = df[df['Ticker'] == 'BRITANNIA.NS'].iloc[0]
    print(f"Britannia P/E: {britannia['P/E Ratio']:.2f} (Industry Avg: {avg_pe:.2f})")
    print(f"Britannia EV/EBITDA: {britannia['EV/EBITDA']:.2f} (Industry Avg: {avg_ev_ebitda:.2f})")
    
    # Optional: Generate plots
    sns.set_theme(style="whitegrid")
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='P/E Ratio', y='Company', data=df.sort_values('P/E Ratio', ascending=False), palette='Blues_d')
    plt.title('P/E Ratio Comparison - FMCG Sector')
    plt.axvline(avg_pe, color='red', linestyle='--', label='Industry Average')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), "..", "data", "pe_comparison.png"))
    print("\nSaved P/E comparison chart to data/pe_comparison.png")
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='EV/EBITDA', y='Company', data=df.sort_values('EV/EBITDA', ascending=False), palette='Greens_d')
    plt.title('EV/EBITDA Comparison - FMCG Sector')
    plt.axvline(avg_ev_ebitda, color='red', linestyle='--', label='Industry Average')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), "..", "data", "ev_ebitda_comparison.png"))
    print("Saved EV/EBITDA comparison chart to data/ev_ebitda_comparison.png")

if __name__ == "__main__":
    run_valuation_analysis()
