# web-requests-exercise

Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "web-requests-exercise". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/web-requests-exercise.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

cd ~/Desktop/web-requests-exercise

Use your text editor or the command-line to create a file in that repo called "get_data.py", and then place the following contents inside:

# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")

Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.
Environment Setup

Create and activate a new Anaconda virtual environment:

conda create -n requests-env python=3.7 # (first time only)
conda activate requests-env

From within the virtual environment, install the requests package:

pip install requests

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

python get_data.py