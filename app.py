from flask import Flask, request, render_template
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Function to summarize text using LSA Summarizer from sumy
def summarize_text(text, summary_length='medium'):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Choose summarization method based on summary_length
    if summary_length == 'short':
        summarizer = LsaSummarizer()
    elif summary_length == 'long':
        summarizer = LexRankSummarizer()
    else:
        summarizer = LsaSummarizer()
    
    # Summarize the text
    summary = summarizer(parser.document, sentences_count=5)  # Default to 5 sentences for LSA
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
            summary_length = request.form['summary_length']  # Get selected summary length/style
            summary = summarize_text(original_text, summary_length)
    
    return render_template('index.html', original_text=original_text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
