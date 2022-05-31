# Introduction
POC of an online collaborative 2048 (original game available [here](https://play.google.com/store/apps/details?id=com.ketchapp.play2048&hl=en_US&gl=US)), using Streamlit and Pandas for the graphical rendering, and pure Python for the game engine.

The result is available [here](https://share.streamlit.io/valentin-laurent/Collaborative-2048/app.py) on Streamlit Cloud. A GitHub workflow pings the app every day to try to keep it up and running, but it doesn't work. I will implement something more elaborated when I have time.

This package also contains the required config files to deploy the game on Heroku.

# About the code
I'm using a hack for the Streamlit part, but I suspect that a much cleaner approach is now possible thanks to Streamlit *Session State* (`app.py` was implemented before its release). This [Streamlit reference repo](https://github.com/gmanchon/streamlit) provides an example [here](https://wagon-data-streamlit.herokuapp.com) of the use of *Session State*.

Regarding the Python game engine, it was not designed to be computationally efficient, or even elegant, but just meant to work 😄 It would be an interesting challenge to rewrite it, either in pure Python, either using librairies like NumPy, with performance or elegance in mind.
