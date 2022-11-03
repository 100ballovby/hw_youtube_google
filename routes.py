from app import app
from forms import SearchForm
from flask import render_template, redirect


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/youtube-search', methods=['GET', 'POST'])
def yt():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
        url = f'https://www.youtube.com/results?search_query={query}'
        return redirect(url)
    return render_template('youtube.html', form=form, heading='YouTube')


@app.route('/google-search', methods=['GET', 'POST'])
def goo():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
        url = f'https://google.com/search?q={query}'
        return redirect(url)
    return render_template('google.html', form=form, heading='Google')

