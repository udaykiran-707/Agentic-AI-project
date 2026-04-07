import json
import os
from datetime import datetime

MEMORY_FILE = "data/memory.json"

class Memory:
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'w') as f:
                json.dump([], f)

    def save_search(self, topic: str, report: dict):
        """Saves a search result to memory."""
        try:
            with open(MEMORY_FILE, 'r') as f:
                history = json.load(f)
            
            entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "topic": topic,
                "summary_preview": report["key_insights"][:200] + "..."
            }
            
            history.insert(0, entry) # Add to beginning
            with open(MEMORY_FILE, 'w') as f:
                json.dump(history, f, indent=4)
        except Exception as e:
            print(f"Error saving to memory: {e}")

    def get_history(self) -> list:
        """Retrieves search history."""
        try:
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return []