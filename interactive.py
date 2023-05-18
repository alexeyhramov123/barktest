import bark
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

debug = True


# initialize bark
# low_mem_gpu == True for GPUs with less than 12GB of memory
def initialize_bark(simple: bool = False, low_mem_gpu: bool = True):
    if low_mem_gpu:
        # offload generation to CPU avoiding running out of memory
        setattr(bark.generation, "OFFLOAD_CPU", True)
    if simple:
        preload_models(text_use_small=True, coarse_use_small=True, fine_use_small=True, force_reload=True)
    else:
        preload_models(force_reload=True)


# generate audio from text
# might not work with to long text prompts
# speakers: https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
def text_to_wave(text_prompt: str, filename: str = 'bark_generation', text_temp: float = 0.3,
                 speaker: str = 'v2/en_speaker_6'):
    audio_array = bark.generate_audio(text_prompt, text_temp=text_temp, history_prompt=speaker)
    write_wav(filename + '.wav', SAMPLE_RATE, audio_array)
    return audio_array


# prompt 1: "The blue whale is the largest animal known to humanity."
# prompt 2: "Here's a lighthearted joke for you: Why don't scientists trust atoms? Because they make up everything!"
if __name__ == "__main__":
    initialize_bark()
    print("Bark initialized")
    file_id = 1
    while True:
        text_to_wave(input("Enter text prompt: "), filename='bark_generation' + str(file_id))
        if debug:
            from playsound import playsound

            playsound('bark_generation' + str(file_id) + '.wav')
        file_id += 1
