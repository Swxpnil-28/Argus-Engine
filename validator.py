from src.schemas.credit_models import Financials, CovenantStatus

def calculate_covenant_health(data: Financials, max_leverage: float = 4.0) -> CovenantStatus:
    """Strict math engine. No AI reasoning here."""
    ratio = round(data.total_debt / data.ebitda, 2)
    is_compliant = ratio <= max_leverage
    
    # Define Alert Levels
    if ratio > max_leverage:
        status = "RED"
    elif ratio > (max_leverage * 0.9):
        status = "AMBER"
    else:
        status = "GREEN"
        
    # PM Logic: If it's not GREEN, it's risky and needs eyes [cite: 26]
    return CovenantStatus(
        leverage_ratio=ratio,
        is_compliant=is_compliant,
        alert_level=status,
        requires_human_review=(status != "GREEN")
    )