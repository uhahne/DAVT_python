# DAVT_python
 A bunch of python scripts used in DAVT lecture

## Prerequisites

First, we need to download and install Python 3 from [python.org](https://www.python.org/downloads/). The recommended
version is `3.10.7` or above. Then, we can use the following terminal command to inspect the currently installed
version:
<table>
<tr>
<th>
Windows
</th>
<th>
MacOS
</th>
</tr>

<tr>

<td>
<pre>
python --version
</pre>
</td>

<td>
<pre>
python3 --version
</pre>
</td>

</tr>
</table>


*Ensure that the terminal and selected interpreter use the correct version.*

## Installation

### Python Virtual Environments

To more easily develop Python code, it is recommended to set up a virtual environment (VENV) in the project root folder.
The following terminal command will create the hidden folder `.venv` in your current project folder:

```shell
python -m venv .venv
```

*Do not forget to use ```python3``` instead of ```python``` on MacOS.*

---

Next, we need to enable the VENV. The VENV will only be active for the current terminal session. Closing the terminal and re-opening it will disable the VENV. So always make sure to enable it before you start developing.

```shell
# For Windows use
.venv\Scripts\Activate.ps1

# For Linux and Mac OS
source .venv/bin/activate
```

Special care is needed when using Windows. Please consult the following [guide][venv-guide] for more information. When the environment is activated, you should see this as a prefix on your terminal.

---

And then install OpenCV with

```pip install opencv-python```

and a Python ffmpeg wrapper with

```pip install ffmpeg-python```

which are used in the video comparison scripts.

For the Lagrange demo you will need to install [matplotlib](https://matplotlib.org/stable/users/getting_started/) with

```pip install matplotlib```

---

Before you can compare videos with the [compare_video_player](./compare_video_player.py) script, you need to download some sample videos, copy them into the [data](./data/) folder and adjust the file names in the script. The idea is to compare videos with the same content but different codecs used for compression. You will find download sources in the data folder. The raw videos are not part of this repository as they are too big.

You can use the [compress_video](./compress_video.py) script in order to compress a video file, but it is recommended to use the command line version of [FFmpeg](https://ffmpeg.org/download.html) which has to be installed before anyway.