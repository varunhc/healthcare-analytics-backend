import matplotlib.pyplot as plt
import numpy as np


def plot_patient_history(results):
    plt.figure(figsize=(8, 6))

    unique_count_label = results.groupby(['label'], as_index=False).count()
    unique_count_label.sort_values(by="valuenum", ascending=False, inplace=True)

    for label in unique_count_label["label"][:6]:
      y = results.loc[results['label'] == label]
      unit = [unit for unit in y["unitname"][:1]][0]
      y = y["valuenum"]
      x = [i for i in range(y.shape[0])]
      plt.plot(x, y, linestyle='-', label=f"{label}: {unit}", linewidth=0.5, alpha=0.5)
      window_width = 30
      cumsum_vec = np.cumsum(np.insert(y, 0, 0))
      ma_vec = (cumsum_vec[window_width:] - cumsum_vec[:-window_width]) / window_width
      plt.plot(x[:len(ma_vec)], ma_vec, alpha = 1, linewidth=1.1)

    plt.title('Chart items')
    plt.xlabel('Samples')
    plt.ylabel('Reading')

    legend = plt.legend(loc='upper right', shadow=True, fontsize='small')

    legend.get_frame().set_facecolor('C0')

    plt.grid(True)

    plt.savefig("patient_history_plot.png")
