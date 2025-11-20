import main
from datetime import datetime

def test_duplicate_visitor_error():
    with open("visitors.txt", "w") as f:
        f.write(f"John | {datetime.now().isoformat()}\n")
    try:
        main.add_visitor("John")
        raised=False
    except main.DuplicateVisitorError:
        raised=True
    assert raised
