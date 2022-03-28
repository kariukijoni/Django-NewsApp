from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def Index(request):
     newsapi=NewsApiClient(api_key='2f077343583e43f489d3dbb0e8665fd8')
     topheadlines=newsapi.get_top_headlines(sources='al-jazeera-english')
     articles=topheadlines['articles']
     
     desc=[]
     news=[]
     img=[]
     
     for i in range(len(articles)):
         myarticles=articles[i]
         news.append(myarticles['title'])
         desc.append(myarticles['description'])
         img.append(myarticles['urlToImage'])
         
         
     mylist=zip(desc,news,img)
     return render(request, 'index.html',context={'mylist':mylist})
    