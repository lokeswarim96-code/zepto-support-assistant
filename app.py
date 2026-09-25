from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Zepto Support Assistant",
    description="Customer support assistant API"
)

class AssistantRequest(BaseModel):
    question: str

class AssistantResponse(BaseModel):
    answer: str

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Zepto Support Assistant is running"
    }

@app.post("/ask", response_model=AssistantResponse)
def ask(request: AssistantRequest):
    question = request.question.lower()

    if "hello" in question or "hi" in question:
        answer = "Hello! How can I help you?"

    elif "delivery" in question:
        answer = "Delivery information is available in the support knowledge base."

    elif "cancel" in question:
        answer = "You can request order cancellation through customer support."

    elif "refund" in question:
        answer = "Refund information is available in the support policy."

    elif "return" in question:
        answer = "Return information is available in the support policy."

    else:
        answer = "I could not find a specific answer. Please contact customer support."

    return AssistantResponse(answer=answer)