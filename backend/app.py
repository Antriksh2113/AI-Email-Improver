from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm import EmailRewriter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rewriter = EmailRewriter()

class RewriteRequest(BaseModel):
    draft: str
    tone: str

@app.post("/rewrite")
def rewrite_email(request: RewriteRequest):
    try:
        rewritten_email = rewriter.rewrite(request.draft, request.tone)
        return {"rewritten_email": rewritten_email}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
