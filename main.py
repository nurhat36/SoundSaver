import sounddevice as sd
import numpy as np
import soundfile as sf

# Ses kaydı parametreleri
sampling_frequency = 44100  # Örnekleme frekansı
duration = 5  # Süre (saniye)

# Ses kaydetme
input("Kaydetmeye başlamak için tuşa basın...")  # Kullanıcıdan giriş bekleme
print("Kayda başlandı...")
mydata = sd.rec(int(sampling_frequency * duration), samplerate=sampling_frequency, channels=2, blocking=True)
print("Kayıt tamamlandı.")

# Ses verisini bir dosyaya kaydetme
sf.write('output.wav', mydata, sampling_frequency)
