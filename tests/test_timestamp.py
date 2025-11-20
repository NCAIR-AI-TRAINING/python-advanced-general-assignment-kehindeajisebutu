import main
from datetime import datetime

def test_timestamp_is_added():
    with open("visitors.txt", "w") as f:
        f.write("Jane | 2020-01-01T00:00:00\n")
    main.add_visitor("Mary")
    with open("visitors.txt") as f:
        last = f.readlines()[-1]
    assert last.startswith("Mary | ")
