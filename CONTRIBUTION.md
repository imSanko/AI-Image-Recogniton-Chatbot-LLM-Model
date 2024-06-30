
## Contributing
Contributions are welcome! 
To contribute to this project, please follow these steps:

Fork the repository
Create a new branch for your feature or bug fix (git checkout -b my-new-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin my-new-feature)
Create a new Pull Request

When submitting a Pull Request, please ensure that your code adheres to the project's coding standards and that you have included tests for any new features or bug fixes.

# Image Caption Generator with Streamlit and Transformers

This repository contains a Streamlit application that uses the Transformers library from Hugging Face to generate captions for input images. The application leverages the `VisionEncoderDecoderModel` from the `nlpconnect/vit-gpt2-image-captioning` pre-trained model.

## Contribution Steps

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

### Describe your change:

Fixes #1. There is a bug in the code that doesn't handle the edge case when the insertion of an empty string is done.

* Fix a bug or typo in an existing algorithm?

### Checklist:
ADD [x] = For Availing the point.
Blank [] = For Unselecting.

* [] This pull request is all my own work -- I have not used AI TOOL's, hence it'll be CLOSED.
* [] I know that pull requests will not be merged if they fail the automated tests.
* [] This PR only changes one file. To ease review, please open separate PRs for separate algorithms.
* [] All filenames are in all lowercase characters with no spaces or dashes.
* [] All function parameters and return values are annotated with Python type hints in .py file
* [] If this pull request resolves one or more open issues then the description above includes the issue number(s) with a closing keyword: "Fixes #ISSUE-NUMBER".
* [] I have read CONTRIBUTING.md.
* [] All functions and variable names follow Python naming conventions.
* [] All new algorithms include at least one URL that points to Wikipedia or another similar explanation.
* [] Documentation change?


## Features

- Upload images and generate captions.
- Supports various image formats (JPG, PNG, etc.).
- Utilizes the powerful Transformer architecture for image captioning.

## Requirements

- Python 3.6+
- Streamlit
- Transformers
- PyTorch
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/image-caption-generator.git
