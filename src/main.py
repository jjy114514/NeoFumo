import pyaudio
import wave

def record_audio(output_filename, duration=5, rate=44100, chunk=1024, input_device_index=None):
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=rate, input=True,
                        input_device_index=input_device_index,
                        frames_per_buffer=chunk)
    print("Recording...")

    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    output_filename = "output.wav"
    input_device_index = 1  # 设置为所需的音频输入设备索引
    record_audio(output_filename, input_device_index=input_device_index)