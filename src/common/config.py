
import os
from pathlib import Path
from dotenv import load_dotenv

# ────────────────────────────────────────────────────────
# 1) bootstrap paths + env + llm
# ────────────────────────────────────────────────────────
THIS_DIR     = Path(__file__).resolve()
PROJECT_ROOT = THIS_DIR.parent.parent.parent
load_dotenv(PROJECT_ROOT  / "config/env") # expects OCI_ vars in env

#────────────────────────────────────────────────────────
# OCI Security configuration
# ────────────────────────────────────────────────────────
AUTH_TYPE = os.getenv("AUTH_TYPE")
CONFIG_PROFILE = os.getenv("CONFIG_PROFILE")
#────────────────────────────────────────────────────────
# OCI GenAI configuration
# ────────────────────────────────────────────────────────
COMPARTMENT_ID 	 	  	= os.getenv("OCI_COMPARTMENT_ID")
ENDPOINT       			= os.getenv("OCI_GENAI_ENDPOINT")
MODEL_ID       			= os.getenv("OCI_GENAI_MODEL_ID")
MODEL_ID_VISION       	= os.getenv("OCI_GENAI_MODEL_ID_VISION")
PROVIDER       			= os.getenv("PROVIDER")




