import os
import gtts

mtext=input("Enter Some Text")

language = 'en'
output = gtts.gTTS(text=mtext ,lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")