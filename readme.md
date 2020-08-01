## Quickstart
Simple OCR with [tesseract](https://github.com/tesseract-ocr/tesseract) and OpenCV on python 3.

- Intall Tesseract on your machine.
- Clone the repo. Create a virtualenv. [Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)
- Install  the packages using `pip install -r requirements.txt`
- For a simple test, run this `python ocr.py --image="./noisy_text_image.png"`
- With noisier images, try using a preprocessor: `python ocr.py --image="./noisy_text_image.png" --preprocess blur`.


## WIP
`pdftxt` - Working on PDF2TXT using OCR, extract text from images embedded inside PDF and convert to text using OCR with single pipeline flow.