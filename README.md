# AI Chatbot with Gemini Pro 🤖

[![React](https://img.shields.io/badge/React-19.1-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.9-blue.svg)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688.svg)](https://fastapi.tiangolo.com/)
[![Firebase](https://img.shields.io/badge/Firebase-12.0-orange.svg)](https://firebase.google.com/)
[![Gemini AI](https://img.shields.io/badge/Gemini_AI-2.0-green.svg)](https://deepmind.google/technologies/gemini/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A modern, responsive chatbot application built with React, TypeScript, and FastAPI, powered by Google's Gemini Pro AI model with Firebase integration for real-time data persistence.

![Chatbot Demo](https://via.placeholder.com/800x400?text=Chatbot+Demo)

## ✨ Features

- **Real-time AI Responses** - Powered by Google's Gemini 2.0 Flash model
- **Persistent Chat History** - Firebase Firestore integration for seamless data storage
- **Responsive Design** - Modern UI that works on desktop and mobile devices
- **TypeScript Support** - Fully typed for better development experience
- **Loading States** - Visual feedback during AI response generation
- **Timestamp Display** - Messages show time sent for better context

## 🏗️ Architecture

```
├── Frontend (React + TypeScript)
│   ├── User Interface
│   ├── Firebase Integration
│   └── API Communication
│
└── Backend (FastAPI + Python)
    ├── Gemini AI Integration
    ├── Firebase Integration (optional)
    └── RESTful API Endpoints
```

## 🚀 Quick Start

### Prerequisites

- Node.js 16+ and npm
- Python 3.8+
- Google Gemini AI API key
- Firebase project (optional for enhanced features)

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot.git
   cd ai-chatbot
   ```

2. Create a `.env` file in the project root:
   ```
   # Frontend Firebase configuration
   REACT_APP_FIREBASE_API_KEY=your_firebase_api_key
   REACT_APP_FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
   REACT_APP_FIREBASE_PROJECT_ID=your_firebase_project_id
   REACT_APP_FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
   REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
   REACT_APP_FIREBASE_APP_ID=your_firebase_app_id
   REACT_APP_FIREBASE_MEASUREMENT_ID=your_firebase_measurement_id
   ```

3. For the backend, set your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   ```

### Running the Application

#### Frontend

```bash
npm install
npm start
```

The frontend will be available at [http://localhost:3000](http://localhost:3000)

#### Backend

```bash
cd backend
pip install fastapi uvicorn google-generativeai firebase-admin
python -m uvicorn backend:app --reload --port 8000
```

The backend will be available at [http://localhost:8000](http://localhost:8000)

## 🛠️ Development

### Available Scripts

- `npm start` - Runs the app in development mode
- `npm test` - Launches the test runner
- `npm run build` - Builds the app for production
- `npm run eject` - Ejects from Create React App configuration

## 📚 API Documentation

When running, FastAPI automatically generates interactive API documentation:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧪 Testing

```bash
npm test
```

## 🔒 Security Notes

- Never commit your `.env` file or expose API keys
- Set up proper Firebase security rules for production use
- Consider implementing user authentication for multi-user support

## 🔄 Future Enhancements

- User authentication
- Multiple chat sessions
- Customizable AI parameters
- Message attachments
- Voice input/output

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/ai-chatbot/issues).

---

Built with ❤️ using React, TypeScript, FastAPI, Firebase, and Google's Gemini AI
