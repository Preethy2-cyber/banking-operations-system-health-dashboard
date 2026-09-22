from data_validation import validate_database
from risk_detection import calculate_alerts
from escalation_workflow import create_escalations
if __name__=="__main__":
    print("Validation:",validate_database())
    print("Alerts:",len(calculate_alerts()))
    print("Escalations:",create_escalations())
