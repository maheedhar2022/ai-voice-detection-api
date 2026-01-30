# AI Voice Detection API

A basic REST API project to detect whether a given voice sample is AI-generated or human.

⚠️ **This project is in an early development stage. Features and documentation will be updated as development progresses.**

## 🚧 Project Status

* ✅ Initial project setup completed
* ✅ Backend API structure created
* 🔨 Voice detection logic is under development

## 🎯 Overview

This API will analyze audio files and return a prediction on whether the voice is AI-generated or human. The project is currently in its foundational phase with the basic server infrastructure in place.

## 📋 Prerequisites

- Node.js (v18 or higher)
- npm or yarn package manager

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/GitbyDushyanth/ai-voice-detection-api.git
cd ai-voice-detection-api
```

### 2. Install dependencies

```bash
npm install
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your configuration:

```
PORT=3000
# API_KEY=your_api_key_here
```

## 🏃 Running the Application

### Development Mode

Start the server with auto-reload:

```bash
npm run dev
```

### Production Mode

```bash
npm start
```

The server will run on `http://localhost:3000` by default.

## 📡 API Endpoints

### Health Check

Check if the API is running:

```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

**Example using cURL:**
```bash
curl http://localhost:3000/health
```

> 🔨 **Note:** Voice detection endpoints are currently under development and will be added soon.

## 🏗️ Project Structure

```
ai-voice-detection-api/
├── src/                    # Node.js application
│   ├── app.js             # Express app configuration
│   └── server.js          # Server entry point
├── ml_service/            # ML service (in development)
│   ├── app.py            # FastAPI application
│   ├── model.py          # ML model logic
│   └── requirements.txt  # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── package.json         # Node.js dependencies
└── README.md           # This file
```

## 🔧 Tech Stack

- **Node.js** - JavaScript runtime
- **Express.js** - Web framework for building REST APIs

### Planned Technologies

- Python with FastAPI for ML service
- Audio processing libraries (librosa, NumPy)
- Machine learning frameworks for voice detection

## 🚀 Development Roadmap

### Phase 1: Foundation (Current)
- [x] Project initialization
- [x] Basic Express.js server setup
- [x] Health check endpoint
- [x] Environment configuration
- [ ] File upload handling
- [ ] Basic API route structure

### Phase 2: ML Integration (Upcoming)
- [ ] Set up Python ML service
- [ ] Integrate FastAPI with Node.js backend
- [ ] Implement audio feature extraction
- [ ] Build/train voice detection model
- [ ] Connect ML predictions to API

### Phase 3: Enhancement (Future)
- [ ] Multi-language support
- [ ] Authentication and rate limiting
- [ ] Comprehensive error handling
- [ ] API documentation (Swagger)
- [ ] Testing suite
- [ ] Docker containerization

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the ISC License.

## 👤 Author

**GitbyDushyanth**

- GitHub: [@GitbyDushyanth](https://github.com/GitbyDushyanth)

## 🐛 Issues

Found a bug or have a suggestion? Please [open an issue](https://github.com/GitbyDushyanth/ai-voice-detection-api/issues).

## 📞 Support

For questions or support, please open an issue on GitHub.

---

**Note:** This project is actively under development. Check back for updates!