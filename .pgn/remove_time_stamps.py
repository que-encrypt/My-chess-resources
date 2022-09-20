from pathlib import Path
import re
txt = Path("chesscom-export-chessfanatic6 - Copy.pgn").read_text()
regex = re.compile("\{.*?\}")
result = re.sub(regex, "",txt)
print(result, file=open("NO_COMMENTS__chesscom-export-chessfanatic6.pgn","r+"))