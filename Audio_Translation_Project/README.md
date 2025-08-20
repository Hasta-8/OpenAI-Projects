# Audio Translator

A web application that transcribes audio files and translates them to any language using OpenAI's Whisper and GPT models.

## Features

- **Audio Transcription**: Convert speech to text using OpenAI's Whisper model
- **Multi-language Translation**: Translate transcribed text to any target language
- **Web Interface**: Simple, responsive HTML form for file uploads
- **File Upload**: Support for various audio formats (MP3, WAV, etc.)
- **UTF-8 Support**: Proper handling of non-ASCII characters in translations

## Technologies Used

- **Backend**: Python Flask
- **AI Models**: OpenAI Whisper (transcription) + GPT-3.5-turbo (translation)
- **Frontend**: HTML, CSS (responsive design)
- **Environment**: python-dotenv for configuration

## Prerequisites

- Python 3.7+
- OpenAI API key
- Audio files in supported formats (MP3, WAV, M4A, etc.)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd audio-translator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Create uploads directory**
   ```bash
   mkdir uploads
   ```

## Usage

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   
   Open your browser and go to `http://localhost:8080`

### Using the Web Interface

1. Select an audio file using the file input
2. Enter the target language (e.g., "Spanish", "French", "Japanese")
3. Click "Upload" to process the file
4. The application will return a JSON response with the translated text

### API Response Format

```json
{
  "translated_text": "Translated content here"
}
```

### Demo Script

The project includes `demo.py` for testing transcription with a local audio file:

```bash
# Place your audio file as "Recording.mp3" in the project directory
python demo.py
```

## Project Structure

```
audio-translator/
├── app.py              # Main Flask application
├── demo.py             # Demo script for testing
├── index.html          # Web interface template
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── uploads/           # Directory for uploaded files (create this)
```

## Configuration

The application can be configured through environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Dependencies

- `openai==0.28`: OpenAI API client
- `flask`: Web framework
- `python-dotenv`: Environment variable management

## Error Handling

- File validation ensures only valid files are processed
- UTF-8 encoding ensures proper character support
- Environment variables are validated on startup

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- Keep your OpenAI API key secure and never commit it to version control
- Consider implementing file size limits for production use
- Add proper input validation for production deployments

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- OpenAI for providing Whisper and GPT models
- Flask community for the excellent web framework