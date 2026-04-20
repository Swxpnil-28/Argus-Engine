from src.schemas.credit_models import Financials, CovenantStatus
from src.core.validator import calculate_covenant_health

def simulate_market_stress(data: Financials) -> CovenantStatus:
    """Simulates a 20% EBITDA haircut."""
    stressed_data = Financials(
        ebitda=round(data.ebitda * 0.8, 2),
        total_debt=data.total_debt,
        cash_on_hand=data.cash_on_hand,
        confidence_score=data.confidence_score
    )
    return calculate_covenant_health(stressed_data)