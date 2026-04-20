from src.agents.extractor_agent import extract_financials
from src.core.validator import calculate_covenant_health
from src.agents.stress_tester import simulate_market_stress
from src.core.evaluator import SystemEvaluator

def run_production_audit(file_path: str):
    evaluator = SystemEvaluator()
    evaluator.start_timer()
    
    # 1. AI Extraction
    with open(file_path, "r") as f:
        content = f.read()
    raw_data = extract_financials(content)
    
    # 2. Risk Calculations
    baseline = calculate_covenant_health(raw_data)
    stressed = simulate_market_stress(raw_data)
    
    latency = evaluator.stop_timer()
    cost = evaluator.estimate_cost("llama-3.3-70b")

    print("\n" + "="*45)
    print("         VIGILANTFLOW PRODUCTION AUDIT         ")
    print("="*45)
    print(f"BASELINE LEVERAGE:  {baseline.leverage_ratio}x ({baseline.alert_level})")
    print(f"STRESSED LEVERAGE:  {stressed.leverage_ratio}x ({stressed.alert_level})")
    print("-" * 45)
    print(f"SYSTEM LATENCY:     {latency}s")
    print(f"ESTIMATED COST:     {cost}")
    print(f"DECISION:           {'HARD REJECT' if not stressed.is_compliant else 'PASS'}")
    print("="*45)

if __name__ == "__main__":
    run_production_audit("data/loan_report.txt")