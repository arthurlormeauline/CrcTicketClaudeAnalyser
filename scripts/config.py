from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
ROOT_DIR = SCRIPTS_DIR.parent

INPUT_DIR = ROOT_DIR / 'input'
OUTPUT_DIR = ROOT_DIR / 'output'
TEMP_DIR = ROOT_DIR / 'temp'
BATCHES_DIR = TEMP_DIR / 'batches'
