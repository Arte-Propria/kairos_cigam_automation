import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("KAIROS_API_KEY")

CNPJS = {
    "ARTE_GLOBAL": os.getenv("CNPJ_ARTE_GLOBAL").strip(),
    "ABSTRACT": os.getenv("CNPJ_ABSTRACT").strip(),
    "ARTE_BASEL": os.getenv("CNPJ_ARTE_BASEL").strip(),
    "MALBA": os.getenv("CNPJ_MALBA").strip(),
}