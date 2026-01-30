import base64
import io
import numpy as np
import librosa

def extract_audio_features(audio_base64: str):
    # Step 1: Decode Base64
    try:
        audio_bytes = base64.b64decode(audio_base64)
    except Exception:
        raise ValueError("Invalid Base64 audio")

    # Step 2: Load MP3 to waveform
    audio_buffer = io.BytesIO(audio_bytes)
    y, sr = librosa.load(audio_buffer, sr=None, mono=True)

    # Step 3: Resample to 16kHz
    TARGET_SR = 16000
    if sr != TARGET_SR:
        y = librosa.resample(y, orig_sr=sr, target_sr=TARGET_SR)
        sr = TARGET_SR

    # Step 4: Trim silence
    y, _ = librosa.effects.trim(y, top_db=25)

    # Step 5: Validate length
    duration = len(y) / sr
    if duration < 1.0:
        raise ValueError("Audio too short")

    # Step 6: MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfcc_mean = mfcc.mean(axis=1)
    mfcc_std = mfcc.std(axis=1)

    # Step 7: Mel spectrogram features
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64)
    mel_db = librosa.power_to_db(mel)
    mel_mean = mel_db.mean(axis=1)

    # Step 8: Pitch features
    f0, _, _ = librosa.pyin(y, fmin=80, fmax=400)
    pitch_mean = np.nanmean(f0)
    pitch_std = np.nanstd(f0)

    # Step 9: Spectral features
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr).mean()
    spectral_flatness = librosa.feature.spectral_flatness(y=y).mean()

    # Step 10: Combine all features
    features = np.concatenate([
        mfcc_mean,
        mfcc_std,
        mel_mean,
        [pitch_mean, pitch_std, spectral_centroid, spectral_flatness]
    ])

    return features
