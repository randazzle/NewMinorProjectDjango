from django.shortcuts import render
from .models import Article
from accounts.models import Profile
from django.http import HttpResponse
import pandas as pd
import numpy as np
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

user_preference_choices = [
    "Adventure",
    "Relaxation" ,
    "Nature",
    "Architecture",
    "Historical",
    "Religious"
]


# Create your views here.
def article_list(request):	# *args, **kwargs
    articles = Article.objects.all().order_by('-date')[0:3]
    cards = Article.objects.all().order_by('-date')[3:6]
    current_user = request.user
    if(current_user.is_authenticated):
        all_articles = Article.objects.all()
        # current_user = request.user.get_profile()
        current_user_profile = Profile.objects.get(user=current_user)
        # all_article_tags = Article.objects.all().values_list('tags', flat=True)
        a_tags =[None] * len(all_articles)
        # print("len of all_artciles:", len(all_articles))
        j=0
        for a in all_articles:
            a_tags[j] = list(a.tags)
            # print(a.tags)
            j = j +1
            # j=0
            # for tag in a.tags:
            #     a_tags = list(tag)
            #     j =j+1
        
        a_tags_converted =[None] * len(a_tags)
        def convert(lst): 
            return ' '.join(lst)

        def get_article_from_index(index):
            return all_articles[index]

        j=0
        for b in a_tags:
            a_tags_converted[j] = convert(a_tags[j])
            j = j +1

        # print("Article tags:",a_tags)
        # print("Converted article tags:",a_tags_converted)

        user_preferences = [None] * 2
        user_preferences[0] = user_preference_choices
        user_preferences[1] = current_user_profile.preferences

        user_preferences_converted =[None] * len(user_preferences)

        j=0
        for b in user_preferences:
            user_preferences_converted[j] = convert(user_preferences[j])
            j = j +1

        # print("User tags:",user_preferences)
        # print("Converted user tags:",user_preferences_converted)

        ucv = CountVectorizer()
        user_count_matrix = ucv.fit_transform(user_preferences_converted)
        # print( "User Feature names: ",ucv.get_feature_names())
        # print("User count matrix to array:", user_count_matrix.toarray())

        acv = CountVectorizer()
        count_matrix = acv.fit_transform(a_tags_converted)
        # print( "Feature names: ",acv.get_feature_names())
        # print("count matrix to array:", count_matrix.toarray())

        i=0
        cosine_sim_list = [None] * len(all_articles)
        for art in count_matrix:
            cosine_sim = cosine_similarity(user_count_matrix[1], count_matrix[i])
            # print("Cosine Similarity: ",i, " : ", cosine_sim)
            cosine_sim_list[i] = cosine_sim
            i = i + 1
        
        similar_destinations = list(enumerate(cosine_sim_list))
        print("Similar destinations:",similar_destinations)

        sorted_similar_destinations= sorted(similar_destinations, key = lambda x : x[1],reverse=True)
        print("Sorted Sim Des:", sorted_similar_destinations)

        # print("Cosine Similarity List:  ",cosine_sim_list)
        Recommended_articles = [None] * 3
        p=0
        for each in sorted_similar_destinations:
            print("Article: ", get_article_from_index(each[0]))
            Recommended_articles[p] = get_article_from_index(each[0])
            p = p + 1
            if(p>2):
                break

        print("Recommended articles:",Recommended_articles)

        # cosine_sim = cosine_similarity(count_matrix[3],count_matrix[1])
        # print("Cosine Similarity: ",cosine_sim)
        
        # count_matrix = cv.fit_transform(all_article_tags)
        # cosine_sim = cosine_similarity(count_matrix)
        # print(all_articles)
        # current_user = request.user
        # cosine_sim = cosine_similarity(all_articles)
        # print(cosine_sim)

        # for articlee in all_articles:
        #     article_tags = articlee.tags
        #     user_preferences = current_user.Profile.preferences
        #     cosine_sim = cosine_similarity(article_tags, user_preferences)


    return render(request, 'articles/article_list.html', context={'articles':articles, 'cards':cards, 'recommend':Recommended_articles})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
