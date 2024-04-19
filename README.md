# Étude Grafical

This repository is part of my fluxus art project **`Étude Grafical`** which was a meditative journey into data visualization.

The project consits of the following parts:

1) The meditation
1) Learning a way to capture the programming process so it can be documented as a video
1) The video created from the work that happened during *the meditation*
1) This repository to give you the tools I used as well as the code that was created during *the meditation*

You can find more description and links about the project [here on my webpage](http://www.fez.world/prj/etude-grafical).

## Setting up

To use the code, create (and use) a virtual environment and the `requirements.txt` provided

```bash
# create venv
python -m venv .venv

# activate your venv (Depends on your OS)
source .venv/bin/active

# install dependencies
pip install -r requirements.txt
```

## Code created during the project

The final result of the main code created during this project is in `meditation.py`.

This code will read `data.json` and render a chart of it into `meditation.png`

## Additional code to create timelapse video

Part of the project was also "filming" myself while creating the final outcome. To do so, I created two scripts located in the `tools` directory.

```bash
# Run this script in background to caputre your current state of work every 10s
python tools/keep_history.py
```

```bash
# To convert all snapshot python scripts into 1080x1920 PNGs run
python tools/render_code_to_png.py

# This script may take quite some tweaking in the scaling part depending on your code
# But luckily for mine it worked without having to scale anything
```

Now that you have run the second script, the history directory will contain 3 image series you can use in your video tool:

* `xxxxxx_meditation.png` is the evolution of your main scripts outcome
* `xxxxxx_meditation.py.png` is the evoultion of your script "as seen in the IDE" - on a 1080x1920 background. Ready to be used in your video tool
* `xxxxxx_meditation.py_tmp.png` the raw renderings of your code
