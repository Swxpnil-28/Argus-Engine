from pydantic import BaseModel, Field, field_validator

class Financials(BaseModel):
    ebitda: float
    total_debt: float
    cash_on_hand: float
    # AI PM Metric: Tracking uncertainty to handle model failure [cite: 18]
    confidence_score: float = Field(..., ge=0, le=1.0) 

class CovenantStatus(BaseModel):
    leverage_ratio: float
    is_compliant: bool
    alert_level: str
    # System Guardrail: Flagging for Human-in-the-loop 
    requires_human_review: bool