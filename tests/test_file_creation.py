import os
import main

def test_file_is_created_if_missing():
    if os.path.exists("visitors.txt"):
        os.remove("visitors.txt")
    main.ensure_file()
    assert os.path.exists("visitors.txt")
