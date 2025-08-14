import openai
import os
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, Response

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        language = request.form['language']
        file = request.files['file']

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Step 1: Transcribe audio
            with open(file_path, "rb") as audio_file:
                transcript = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio_file
                )

            # Step 2: Translate text
            translation = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You will be provided with a sentence, and your task is to translate it into {language}."},
                    {"role": "user", "content": transcript["text"]}
                ],
                temperature=0,
                max_tokens=256
            )

            translated_text = translation["choices"][0]["message"]["content"]

            # Step 3: Return proper UTF-8 JSON
            return Response(
                json.dumps({"translated_text": translated_text}, ensure_ascii=False),
                content_type="application/json; charset=utf-8"
            )

    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
