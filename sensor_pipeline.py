import numpy as np
from scipy.signal import butter, filtfilt

def butter_lowpass(cutoff, fs, order=4):
    nyq = fs / 2
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def filter_signal(data, cutoff=50, fs=1000):
    b, a = butter_lowpass(cutoff, fs)
    return filtfilt(b, a, data)

if __name__ == "__main__":
    np.random.seed(42)
    t = np.linspace(0, 1, 1000)
    signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(len(t))
    filtered = filter_signal(signal)
    print(f"Input  — mean: {signal.mean():.4f}, std: {signal.std():.4f}")
    print(f"Filtered — mean: {filtered.mean():.4f}, std: {filtered.std():.4f}")
    print("Pipeline ran successfully inside Docker.")