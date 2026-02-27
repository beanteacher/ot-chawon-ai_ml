from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ot-chawon-size-api", version="0.1.0")


class SizePredictRequest(BaseModel):
    height_cm: float
    weight_kg: float
    gender: str
    chest_cm: float | None = None
    waist_cm: float | None = None
    hip_cm: float | None = None


class SizePredictResponse(BaseModel):
    recommended_size: str
    confidence: float
    reason: list[str]


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/size/predict', response_model=SizePredictResponse)
def size_predict(payload: SizePredictRequest) -> SizePredictResponse:
    size = 'M' if payload.height_cm < 175 else 'L'
    return SizePredictResponse(
        recommended_size=size,
        confidence=0.6,
        reason=['rule-based baseline v0']
    )
