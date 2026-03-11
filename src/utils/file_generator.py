import json
from pathlib import Path


def salvar_json(data, filename):

    path = Path("data/processed")
    path.mkdir(parents=True, exist_ok=True)

    with open(path / filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)