from win32com import client

names = ["Raul", "Nisan", "Harry", "Everyone"]
speak = client.Dispatch("SAPI.SpVoice")


for name in names:
    speak.Speak(f"Shout-out to {name}")