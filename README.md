# Stego - Hide Secret Message

Stego is a simple Python application built using Tkinter and PIL (Python Imaging Library) that allows users to hide secret messages within image files using the least significant bit (LSB) steganography technique.

## Features

- **Hide Secret Message**: Users can select an image file and input a secret message to hide within the image.
- **Show Hidden Message**: Users can reveal any hidden message from an image file.
- **Save Modified Image**: Modified images containing hidden messages can be saved for later use.

## Requirements

- Python 3.x
- Tkinter
- Pillow (Python Imaging Library)
- stegano

## Installation

1. Clone the repository:

    ```
    https://github.com/AliGohar2151/Image-Steganography-Tool.git
    ```

2. Install the required packages:

    ```
    pip install tkinter pillow stegano
    ```

## Usage

1. Run the `stego.py` script:

    ```
    python stego.py
    ```

2. Click on the "Open Image" button to select an image file.
3. Input your secret message in the provided text box.
4. Click on the "Hide Data" button to hide the message within the image.
5. To reveal a hidden message, click on the "Show Data" button.
6. Modified images with hidden messages can be saved using the "Save Image" button.

## Contributors

- Ali Gohar (https://github.com/AliGohar2151)
