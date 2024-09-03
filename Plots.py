import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew


class Plots:
    def __init__(self, predicted, y_test):
        self.predicted = predicted
        self.y_test = y_test

    def daily_stats(self):
        predicted_daily = np.mean(self.predicted, axis=1)
        predicted_stats = {
            'mean': predicted_daily.mean(),
            'std': predicted_daily.std(),
            'skewness': skew(predicted_daily)
        }

        real_stats = {
            'mean': self.y_test.mean(),
            'std': self.y_test.std(),
            'skewness': skew(self.y_test)
        }

        return predicted_stats, real_stats


    def DailyPlot(self):
        predicted_stats, real_stats = self.daily_stats(self.predicted, self.y_test)

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        # Real Daily Means Plot
        axes[0].hist(self.y_test, color='skyblue', edgecolor='black', alpha=0.7, bins=10)
        axes[0].tick_params(axis='y', labelsize=14)
        axes[0].tick_params(axis='x', labelsize=14)
        axes[0].axvline(real_stats['mean'][0], color='black', linestyle='dashed', linewidth=2, label=f"Mean: {real_stats['mean'][0]:.2f}")
        axes[0].axvline(real_stats['std'][0], color='orange', linestyle='dashed', linewidth=2, label=f"STD: {real_stats['std'][0]:.2f}")
        axes[0].axvline(real_stats['skewness'][0], color='green', linestyle='dashed', linewidth=2, label=f"Skewness: {real_stats['skewness'][0]:.2f}")
        axes[0].set_title('Expected Daily Distribution of Avg. Temperature',fontsize=14)
        axes[0].set_xlabel('Value [$\degree C$ ]',fontsize=14)
        axes[0].set_ylabel('Frequency',fontsize=14)
        axes[0].legend(fontsize=14)
        axes[0].grid(True)

        # Predicted Daily Means Plot
        axes[1].hist(self.predicted, color='red', edgecolor='black', alpha=0.7, bins=10)
        axes[1].tick_params(axis='y', labelsize=14)
        axes[1].tick_params(axis='x', labelsize=14)
        axes[1].axvline(predicted_stats['mean'], color='black', linestyle='dashed', linewidth=2, label=f"Mean: {predicted_stats['mean']:.2f}")
        axes[1].axvline(predicted_stats['std'], color='orange', linestyle='dashed', linewidth=2, label=f"STD: {predicted_stats['std']:.2f}")
        axes[1].axvline(predicted_stats['skewness'], color='green', linestyle='dashed', linewidth=2, label=f"Skewness: {predicted_stats['skewness']:.2f}")
        axes[1].set_title('Computed Daily Distribution of Avg. Temperature',fontsize=14)
        axes[1].set_xlabel('Value [$\degree C$ ]',fontsize=14)
        axes[1].set_ylabel('Frequency',fontsize=14)
        axes[1].legend(fontsize=14)
        axes[1].grid(True)



        plt.tight_layout()
        plt.show()
