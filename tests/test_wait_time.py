import main
from datetime import datetime, timedelta

def test_wait_time_enforced():
    last_time = datetime.now() - timedelta(minutes=3)
    with open("visitors.txt","w") as f:
        f.write(f"Ada | {last_time.isoformat()}\n")
    try:
        main.add_visitor("Chinedu")
        raised=False
    except Exception:
        raised=True
    assert raised
