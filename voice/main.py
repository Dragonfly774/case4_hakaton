import queue
import sounddevice as sd
import vosk
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import words

q = queue.Queue()
model = vosk.Model('ru_model_s')
device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def finder():
    pass


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, cv, clf):
    trg = words.triggers.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0], '')
    text_vector = cv.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    print(answer)


def main():
    cv = CountVectorizer()
    vectors = cv.fit_transform(list(words.d_s.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.d_s.values()))

    del words.d_s
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0],
                           dtype="int16", channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, cv, clf)


if __name__ == "__main__":
    main()
