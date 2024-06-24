# PubMed-articles-summarizer-

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Web Application Development](#web-application-development)
- [Technologies Used](#technologies-used)
- [License](#license)

## Overview

The objective of this project is to create a web application that can summarize PubMed articles. This project demonstrates skills in web development and text summarization techniques.

## Features

- Upload PubMed articles in text format.
- Generate a summarized version of the article.

- the summarization feature was implemented using LSA (Latent Semantic Analysis) from the sumy library. LSA is an extractive summarization technique that analyzes the relationships between terms and documents to identify the most important sentences for summarization. Here’s a summary of how LSA works in this context:

Initialization:

The text from the uploaded file is parsed and tokenized.
LSA Summarization:

LSA (Latent Semantic Analysis) is applied using the sumy library's LsaSummarizer.
It identifies the most relevant sentences based on the underlying structure and context of the text.
Output:

The summarized text (a few selected sentences) is displayed on the web interface for the user to view.
LSA is an effective method for extractive summarization because it leverages statistical techniques to identify the sentences that best capture the main ideas of the text. It does not generate new sentences but selects and rearranges existing ones to create a concise summary.



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pubmed-article-summarizer.git
    cd pubmed-article-summarizer
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    flask run
    ```

## Usage

1. Navigate to the web application in your browser:
    ```
    http://127.0.0.1:5000
    ```

2. Upload a PubMed article in text format.

3. View the original article and the summarized version.

## Web Application Development

The web application is developed using Flask. Key components include:

- **Templates**: HTML templates for the user interface.
- **Routes**: Flask routes to handle file uploads and text summarization.

## Technologies Used

- **Flask**: Web framework for Python.
- **sumy**: Library for text summarization.
- **HTML/CSS**: For the front-end interface.
- **Python**: Programming language.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
