# DALLE Image Generator

A web application that generates AI images from text prompts using OpenAI's DALLE model. Enter any text description and get 5 unique AI-generated images instantly.

## Features

- **Text-to-Image Generation**: Convert text prompts into unique AI-generated images
- **Multiple Image Output**: Generates 5 different variations per prompt
- **Real-time Processing**: Live image generation with loading animation
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Interactive Gallery**: Dynamic image display in a grid layout
- **Simple Interface**: Clean, intuitive web form for easy use

## Technologies Used

- **Backend**: Python Flask
- **AI Model**: OpenAI DALLE (Image Generation)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Environment**: python-dotenv for configuration
- **Image Format**: 256x256 pixel PNG images

## Prerequisites

- Python 3.7+
- OpenAI API key with DALLE access
- Modern web browser

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd dalle-image-generator
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

## Usage

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   
   Open your browser and go to `http://localhost:8080`

### Using the Web Interface

1. Enter a descriptive text prompt in the input field
   - Example: "A futuristic city with flying cars at sunset"
   - Example: "A cute robot playing guitar on Mars"
   
2. Click the "Submit" button

3. Wait for the loading animation to complete

4. View your 5 generated images displayed in a responsive grid

### Example Prompts

- "A majestic dragon flying over a medieval castle"
- "Abstract art with vibrant colors and geometric shapes"
- "A cozy coffee shop in a rainy cyberpunk city"
- "A magical forest with glowing mushrooms and fairies"

## API Endpoints

### `GET /`
Returns the main web interface

### `GET /generateimages/<prompt>`
Generates images based on the provided prompt

**Parameters:**
- `prompt`: URL-encoded text description

**Response:**
```json
{
  "created": 1234567890,
  "data": [
    {
      "url": "https://oaidalleapiprodscus.blob.core.windows.net/..."
    },
    // ... 4 more image objects
  ]
}
```

## Project Structure

```
dalle-image-generator/
├── app.py              # Main Flask application
├── index.html          # Web interface with Bootstrap UI
├── requirements.txt    # Python dependencies
└── .env               # Environment variables (create this)
```

## Configuration

The application uses the following configuration:

- **Image Count**: 5 images per generation
- **Image Size**: 256x256 pixels
- **Server**: Runs on `0.0.0.0:8080`
- **Debug Mode**: Enabled for development

## Dependencies

- `openai==0.28`: OpenAI API client for DALLE access
- `flask`: Lightweight web framework
- `python-dotenv`: Environment variable management

## UI Components

- **Bootstrap 5**: Modern, responsive CSS framework
- **Loading Animation**: SVG-based spinner during image generation
- **Responsive Grid**: Automatic layout adjustment for different screen sizes
- **Form Validation**: Client-side input handling

## Error Handling

- API rate limiting handled by OpenAI client
- Loading states prevent multiple simultaneous requests
- Responsive error handling for network issues

## Development

To run in development mode:

```bash
# The application runs with debug=True by default
python app.py
```

## Cost Considerations

Each image generation request creates 5 images. Be mindful of OpenAI API costs:
- DALLE pricing varies by image size and quantity
- Monitor your API usage through the OpenAI dashboard
- Consider implementing request limits for production use

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Potential Enhancements

- **Image Size Options**: Allow users to select different image dimensions
- **Download Feature**: Enable direct image downloads
- **Prompt History**: Save and reuse previous prompts
- **Style Selection**: Add style modifiers (artistic, photographic, etc.)
- **Batch Processing**: Generate images for multiple prompts
- **User Authentication**: Add user accounts and saved galleries

## Security Notes

- Keep your OpenAI API key secure and never commit it to version control
- Consider implementing rate limiting for production deployments
- Add input sanitization for prompt validation
- Use HTTPS in production environments

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- OpenAI for providing the DALLE API
- Bootstrap team for the responsive framework
- Flask community for the excellent web framework