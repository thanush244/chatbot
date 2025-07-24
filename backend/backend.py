from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3002"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API key from environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    print("⚠️ Warning: GEMINI_API_KEY environment variable not set")
    # Don't include default key in code
genai.configure(api_key=gemini_api_key)

# Optional Firebase initialization
db = None
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    
    # Check if service account file exists
    service_account_path = "firebase-service-account.json"
    if os.path.exists(service_account_path):
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("✅ Firebase initialized successfully!")
    else:
        print("⚠️ Firebase service account file not found - running without Firebase")
except Exception as e:
    print(f"⚠️ Firebase initialization skipped: {str(e)}")

class ChatMessage(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Backend is working with Gemini API!"}

@app.post("/chat")
async def chat_with_ai(chat: ChatMessage):
    try:
        if not gemini_api_key:
            return {"response": "Error: Gemini API key not configured. Please set GEMINI_API_KEY environment variable."}
            
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response = model.generate_content(chat.message)
        ai_response = response.text
        
        # Save to Firebase if available (optional)
        if db:
            try:
                chat_ref = db.collection("chats").document()
                chat_ref.set({
                    "user_message": chat.message,
                    "ai_response": ai_response,
                    "timestamp": firestore.SERVER_TIMESTAMP
                })
            except Exception as e:
                print(f"Error saving to Firebase: {str(e)}")
                
        return {"response": ai_response}
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        return {"response": error_msg}
