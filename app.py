from flask import Flask, request, render_template
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Function to summarize text using LSA Summarizer from sumy
def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 10)  # Summarize to 10 sentences
    summary_text = ' '.join([str(sentence) for sentence in summary])
    return summary_text

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    original_text = ""
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            original_text = uploaded_file.read().decode("utf-8")
            summary = summarize_text(original_text)
    return render_template('index.html', original_text=original_text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
