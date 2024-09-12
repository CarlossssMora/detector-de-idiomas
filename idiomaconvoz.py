import speech_recognition as sr

# Configura el reconocimiento de voz
recognizer = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

        try:
            # Convierte el audio en texto
            text = recognizer.recognize_google(audio, language='es-ES')
            print("Texto reconocido:", text)

            with open("transcripcion.txt", "a") as file:
                file.write(text + "\n")

        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError:
            print("No se pudo conectar con el servicio de reconocimiento de voz")

if __name__ == "__main__":
    speech_to_text()
