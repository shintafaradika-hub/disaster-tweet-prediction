\
        # visualize.py
        import pandas as pd
        import matplotlib.pyplot as plt
        from collections import Counter


        def plot_label_distribution(csv_path='../data/processed/train_clean.csv'):
            df = pd.read_csv(csv_path)
            if 'target' not in df.columns:
                print('No target column')
                return
            counts = Counter(df['target'])
            plt.bar(['non-disaster','disaster'], [counts.get(0,0), counts.get(1,0)])
            plt.title('Label distribution')
            plt.savefig('./models/label_dist.png')
            print('Saved label distribution to ./models/label_dist.png')

        if __name__ == '__main__':
            plot_label_distribution()
