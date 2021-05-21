import streamlit as st
import GameOf2048
import pandas as pd

'''
# Year 2048
'''

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_game():
    possible_moves = GameOf2048.GameOf2048.possible_moves
    game = GameOf2048.GameOf2048(4)
    return (game, possible_moves)

game, possible_moves = load_game()

moves = [st.button('Left'), st.button('Right'), st.button('Up'), st.button('Down')]

if True in moves:
    game.resolve_move(possible_moves[moves.index(True)])

df = pd.DataFrame(game.board)
df.columns = ["2", "0", "4", "8"]
st.write(df.assign(hack='').set_index('hack'))