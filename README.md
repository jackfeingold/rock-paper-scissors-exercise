# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```
The game will ask that you input "Rock" "Paper" or "Scissors".  
It does not matter if it is capitalized or not, only that it is spelled correctly.

If you do not enter any of the three, the game will give you an error message and ask you to try again.

When the game is over, the program will terminate.  To play again, enter the above command in Terminal.

## Testing

Run tests:

```sh
pytest
```
