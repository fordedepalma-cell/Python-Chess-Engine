# Chess Engine v1.0.0, Copyright 3/13/2026, Forde DePalma
# Disclaimer: Not true

from engine import Engine

engine = Engine()
print(engine.legal_moves_for_a_piece(engine.board[6][1]))
