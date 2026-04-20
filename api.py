import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agents.extractor_agent import extract_financials
from src.core.validator import calculate_covenant_health
from src.agents.stress_tester import simulate_market_stress

app = FastAPI(title="VigilantFlow: Institutional Decision Engine")

class AuditRequest(BaseModel):
    report_text: str

@app.get("/")
async def root(): return {"status": "online"}

@app.post("/audit")
async def perform_audit(request: AuditRequest):
    start_time = time.perf_counter()
    try:
        # 1. AI Extraction
        raw_data = extract_financials(request.report_text)
        
        # 2. Risk Modeling
        baseline = calculate_covenant_health(raw_data)
        stressed = simulate_market_stress(raw_data)
        
        # 3. Decision Logic: High-level guardrail [cite: 29]
        # Flag review if AI is unsure OR if math shows risk
        human_review = (raw_data.confidence_score < 0.85) or (not stressed.is_compliant)

        return {
            "verdict": {
                "recommendation": "HARD REJECT" if not baseline.is_compliant else "PROCEED",
                "human_review_required": human_review
            },
            "metrics": {
                "leverage": f"{baseline.leverage_ratio}x",
                "stressed_leverage": f"{stressed.leverage_ratio}x",
                "ai_confidence": f"{round(raw_data.confidence_score * 100, 1)}%"
            },
            "performance": {
                "latency": f"{round(time.perf_counter() - start_time, 3)}s",
                "unit_cost": f"${(500/1000) * 0.00079:.6f}"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Autonomous Engine Failure: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)