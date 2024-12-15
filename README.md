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

which is used in the video comparison scripts.

