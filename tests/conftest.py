import sys
from pathlib import Path

# Garante que o pacote local `scripts` seja encontrado sem precisar instalar em modo editable.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
