from django.shortcuts import render_to_response
from Demo.models import WordTotal
from Demo.models import PhraseComponent
from Demo.models import PhraseTotal
from Demo.models import WordAndWordRootId
from Demo.models import WordRoot
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context

def Demo_index(request):
    # main page
    return render_to_response('home/Demo_index.html')

@csrf_exempt
def SearchWordAndPhrase(request):
    selected_grade = request.POST['grade_selected']
    selected_word = request.POST['word']
    grade = int(selected_grade)
    word_explains = list(WordTotal.objects.filter(word=selected_word,class_id__lte=grade))
    wordExist = len( word_explains)
    if wordExist == 0:
                return  HttpResponse("no words, please change another word to try")
    else:
                word_pronunciation = word_explains[0].pronunciation
                word_pronunciation_1 = word_pronunciation.strip('[]')
                #change context to requestcontext can make @csrf_exempt redunant.

                phrase_list = list(PhraseComponent.objects.filter(phrase_component=selected_word).values("phrase"))
                word_phrase_list = list(PhraseTotal.objects.filter(word=selected_word).filter(phrase_in=phrase_list))
                phraseNumber = len( word_phrase_list)



                post_back_data = Context({'word_letter': selected_word,
                                          'phraseNumber':phraseNumber,
                                          'phraseList':word_phrase_list,
                                          'pronunciation': word_pronunciation_1,
                                          'word_totals': word_explains})









                return render_to_response('home/Word_And_Phrase.html',post_back_data)


'''
def SearchWordAndPhrase(request):
    # return searched word's explains..
    selected_grade = request.GET['grade_selected']
    selected_word = request.GET['word']
    word_explains = WordTotal.objects.filter(word=selected_word,class_id=selected_grade)

    phrase_list = PhraseComponent.objects.filter(phrase_component=selected_word).values("phrase")
    word_phrase_list = list( PhraseTotal.objects.filter(word =selected_word).filter(phrase_in = phrase_list))
    #  word_phrase_list = PhraseTotal.objects.filter(word =selected_word).extra(where =['phrase IN phrase_list '])

    word_root_id_list = WordAndWordRootId.filter(word = selected_word).values("word_root_id")
    word_root_list =list(WordRoot.filter(word_root_id_in = word_root_id_list ).values("word_root"))
'''













