from django.shortcuts import render
from googletrans import Translator, LANGUAGES
from .forms import TranslateForm

def translate_view(request):
    translated_text = ''
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            dest_lang = form.cleaned_data['dest_lang']
            translator = Translator()
            translated = translator.translate(text, dest=dest_lang)
            translated_text = translated.text
    else:
        form = TranslateForm()

    return render(request, 'index.html', {
        'form': form,
        'translated_text': translated_text,
        'languages': LANGUAGES
    })
