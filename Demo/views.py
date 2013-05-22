from django.shortcuts import render_to_response
from Demo.models import WordTotal
from Demo.models import PhraseComponent
from Demo.models import PhraseTotal
from Demo.models import WordAndWordRootId
from Demo.models import WordRoot
from Demo.models import WordAndWordRootSet
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from Demo.models import PhonmeGroupLinkPhonmeRelation
from Demo.models import PhonmeRelation
from Demo.models import PhonmeGroup
from Demo.models import LettersGroup
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

                phrase_list = PhraseComponent.objects.filter(phrase_component=selected_word).values_list("phrase")
                initial_phrase_list = PhraseTotal.objects.filter(phrase__in=phrase_list, class_id__lte=grade)
                ordered_phrase_list = initial_phrase_list.order_by("phrase","class_id")
                word_phrase_list = list(ordered_phrase_list)
                phraseNumber = len(word_phrase_list)


                word_root_id_list = WordAndWordRootId.objects.filter(word=selected_word).values_list("word_root_id")
                word_root_list = WordRoot.objects.filter(word_root_id__in=word_root_id_list)

                post_back_data = Context({'word_letter': selected_word,
                                          'word_root_list':word_root_list,
                                          'phraseNumber':phraseNumber,
                                          'phraseList':word_phrase_list,
                                          'pronunciation': word_pronunciation_1,
                                          'word_totals': word_explains})

                return render_to_response('home/Word_And_Phrase.html',post_back_data)


def SearchWordLists(request,offset):
    word_root_id = offset
    words = WordAndWordRootId.objects.filter(word_root_id=offset).values_list("word")
    word_set_list = WordAndWordRootSet.objects.filter(word__in=words)
    post_back_data = Context({'word_root_id': word_root_id,
                             'word_set_list': word_set_list})

    return render_to_response('home/Word_Set_lists.html',post_back_data)


def SearchWordRoots(request,offset):
    word_root_id_4 = offset[0:4]
    word_root_list = WordRoot.objects.filter(word_root_id__startswith= word_root_id_4).order_by("word_root_sort")

    root_related_phoneme_group_id = PhonmeGroupLinkPhonmeRelation.objects.get(phonme_id=word_root_id_4).phonme_group_id
    phoneme_id_list = PhonmeGroupLinkPhonmeRelation.objects.filter(phonme_group_id=root_related_phoneme_group_id).values_list("phonme_id")
    phoneme_relation_list = PhonmeRelation.objects.filter(phonme_id__in=phoneme_id_list).order_by("phonme_sort")

    letter_group_id =offset[0:1]

    post_back_data = Context({'word_root_id': word_root_id_4,
                              'phoneme_relation_list':phoneme_relation_list,
                              'letter_group_id':letter_group_id,
                              'word_root_list': word_root_list})

    return render_to_response('home/Word_root_lists.html',post_back_data)

def SearchBasicPhoneme(request,offset):
    letter_group_id = offset
    phoneme_group = PhonmeGroup.objects.filter(phonme_group_id__startswith= letter_group_id).order_by("phonme_group_id").values_list("phonme_group_neigbor_relation",flat=True)
    post_back_data = Context({'letter_group_id': letter_group_id,
                              'phoneme_group': phoneme_group})
    return render_to_response('home/BasicMapper.html',post_back_data)

def LetterGroup(request):
    letter_group_list = LettersGroup.objects.all
    post_back_data = Context({'letter_group_list': letter_group_list,
                              })
    return render_to_response('home/LetterGroup.html',post_back_data)















