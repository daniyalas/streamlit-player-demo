import streamlit as st
from pathlib import Path
from streamlit_player import st_player, _SUPPORTED_EVENTS

st.set_page_config(layout="wide")

"""
# 🎬 Streamlit Player [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/okld/streamlit-player

[pypi_badge]: https://badgen.net/pypi/v/streamlit-player?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-player

---
"""

with st.sidebar:
    "## ⚙️ Parameters"

    options = {
        "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
        "progress_interval": st.slider("Progress refresh interval (ms)", 200, 2000, 500, 1),
        "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
        "playing": st.checkbox("Playing", False),
        "loop": st.checkbox("Loop", False),
        "controls": st.checkbox("Controls", True),
        "muted": st.checkbox("Muted", False),
    }

    """
    ---
    ## ⏯️ Supported players

    * Dailymotion
    * Facebook
    * Local files
    * Mixcloud
    * SoundCloud
    * Streamable
    * Twitch
    * Vimeo
    * Wistia
    * YouTube
    """

c1, c2 = st.beta_columns(2)

with c1:
    url = st.text_input("First URL", "https://youtu.be/CmSKVW1v0xM")
    event = st_player(url, **options, key=1)
    event

with c2:
    url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
    event = st_player(url, **options, key=2)
    event

"---"

with st.beta_expander("Component docstring"):
    st_player

with st.beta_expander("Demo source code"):
    st.code(Path(__file__).read_text())
