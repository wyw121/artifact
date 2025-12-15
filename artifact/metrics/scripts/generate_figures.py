import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

METRICS_DIR = os.path.join(os.path.dirname(__file__), 'data', 'metrics')
FIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'results', 'figures'))

os.makedirs(FIG_DIR, exist_ok=True)

def safe_read_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return pd.read_csv(path)

def main():
    metrics_csv = os.path.join(METRICS_DIR, 'metrics.csv')
    mojofm_csv = os.path.join(METRICS_DIR, 'mojofm.csv')

    metrics = safe_read_csv(metrics_csv)
    mojofm = safe_read_csv(mojofm_csv)

    # Normalize column names
    metrics.columns = [c.strip() for c in metrics.columns]
    mojofm.columns = [c.strip() for c in mojofm.columns]

    # Ensure numeric values
    if 'Static Structural' not in metrics.columns:
        raise KeyError('Static Structural column not found in metrics.csv')
    metrics['Static Structural'] = pd.to_numeric(metrics['Static Structural'], errors='coerce')

    # Boxplot: Static Structural per Tool
    plt.figure(figsize=(10,6))
    sns.boxplot(x='Tool', y='Static Structural', data=metrics)
    plt.xticks(rotation=45, ha='right')
    plt.title('Static Structural (TurboMQ) distribution by Tool')
    out1 = os.path.join(FIG_DIR, 'boxplot_turbomq_by_tool.png')
    plt.tight_layout()
    plt.savefig(out1, dpi=200)
    plt.close()

    # Bar plot: mean Static Structural per Tool
    mean_ts = metrics.groupby('Tool')['Static Structural'].mean().reset_index()
    plt.figure(figsize=(10,6))
    sns.barplot(x='Tool', y='Static Structural', data=mean_ts, palette='muted')
    plt.xticks(rotation=45, ha='right')
    plt.title('Mean Static Structural (TurboMQ) per Tool')
    out2 = os.path.join(FIG_DIR, 'bar_mean_turbomq_per_tool.png')
    plt.tight_layout()
    plt.savefig(out2, dpi=200)
    plt.close()

    # Bar plot: mean MoJoFM per Tool (use column 'Mojo' or 'Mojo' variant)
    mojo_col = None
    for c in mojofm.columns:
        if c.lower().startswith('mojo'):
            mojo_col = c
            break
    if mojo_col is None:
        raise KeyError('Mojo column not found in mojofm.csv')
    mojofm[mojo_col] = pd.to_numeric(mojofm[mojo_col], errors='coerce')

    mean_mojo = mojofm.groupby('Tool')[mojo_col].mean().reset_index()
    plt.figure(figsize=(10,6))
    sns.barplot(x='Tool', y=mojo_col, data=mean_mojo, palette='deep')
    plt.xticks(rotation=45, ha='right')
    plt.title('Mean MoJoFM per Tool')
    out3 = os.path.join(FIG_DIR, 'bar_mean_mojofm_per_tool.png')
    plt.tight_layout()
    plt.savefig(out3, dpi=200)
    plt.close()

    # Scatter: Static Structural vs MoJoFM (merge on Application, Tool, Granularity)
    merge_keys = ['Application', 'Tool', 'Granularity']
    if all(k in metrics.columns for k in merge_keys) and all(k in mojofm.columns for k in merge_keys):
        merged = pd.merge(metrics, mojofm, on=merge_keys, how='inner', suffixes=('_metrics', '_mojo'))
        if 'Static Structural' in merged.columns and mojo_col in merged.columns:
            plt.figure(figsize=(8,6))
            sns.scatterplot(x='Static Structural', y=mojo_col, hue='Tool', data=merged)
            plt.title('Static Structural vs MoJoFM (merged records)')
            out4 = os.path.join(FIG_DIR, 'scatter_turbomq_vs_mojofm.png')
            plt.tight_layout()
            plt.savefig(out4, dpi=200)
            plt.close()

    print('Figures saved to:', FIG_DIR)

if __name__ == '__main__':
    main()
