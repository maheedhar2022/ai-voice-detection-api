import librosa
import numpy as np

def extract_features(path):
    y, sr = librosa.load(path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return mfcc.mean(axis=1)

def predict(path):
    features = extract_features(path)
    prob = np.clip(np.random.rand(), 0, 1)
    return float(prob)
