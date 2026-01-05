import os, random
from moviepy.editor import *
from TTS.api import TTS
from moviepy.editor import TextClip, CompositeVideoClip

tts = TTS(model_name="tts_models/en/vctk/vits")

def generate_video(script_text, bg_dir, out_path):
    audio_path = "temp.wav"
    tts.tts_to_file(text=script_text, file_path=audio_path)

    bg = VideoFileClip(os.path.join(bg_dir, random.choice(os.listdir(bg_dir)))).subclip(0, 45)
    audio = AudioFileClip(audio_path)

    final = bg.set_audio(audio).resize((1080, 1920))
    final.write_videofile(out_path, fps=24)

    os.remove(audio_path)
    subtitle = TextClip(
        script_text,
        fontsize=48,
        color="white",
        size=(1000, None),
        method="caption"
    ).set_position(("center", "bottom")).set_duration(final.duration)

    final = CompositeVideoClip([final, subtitle])
