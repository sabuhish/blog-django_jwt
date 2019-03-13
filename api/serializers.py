from rest_framework import serializers
from blog_app.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

# serilizer authoru la isleyecek jsnon reposneda

# api meqsed odurki yazdigin butun melumatlar, istenilen
# programlasdirma dilinde integrasiya olunsun
# yeni istenilen programlasdirma dilinde yazan bir programci 
# menim bu yazdigim psotlardan istifade eliye bilsin
# menim api  goturur
# ele bil api vermek le siz butun funksiyanligi vermis olursuznu
# avtomatik olaraq yazfiginiz app ikinci bir versiya olur,
# yeni programist ikinci bir app yaratmir
# tutalim javada application yazmisiq qisa olaraq, kiminse yazdigi
# crud istifade eliyib birde backend yazmag ehtoyac olmaz
# proyetin hecneyi olmur, api ile herseyi idare elemeyir
#
# meselen facebook login nedir, facebook bize login vemrese
# facebook bize api verir, meselen bu tokeni bunu gonder usere
# interface acilir, bu app sizin adini emailini istfiade edir,
# raizsiniz? eger razi duymeisni bassaq onda faceboko, useri gmail
# herbiseyi istadfde olunur app terefinde

# api olmasa, backend yazmadan login register post paylasmq olsun
# nece olar? database olmasin, 
# api o xidemti dasiri ki, 
# api 20 programlasdirma dilinde kod yazaq. api ile elaqelednirmek olar
# microserviseler hersey api dir, saytlar api uzeriden qurulur,
# json verirler, user arasinda olan vasitecidir, 
# yeni bir basa data qaytarir 
# servisler verir, html almiriq data aliriq
# egov ozu basdan ayaga api di
# yeni bu qeder serviselerin olmasi, api olmadan isleye bilmez
# tutalim calculator yazmisan c sharpda , python la nece eleaqe dira bilersen en rahat yolu api, servis gonderrirsen , birnov ele bil servis yaziriq, bir app api yazanda o demekdir ki onun geleceyini gururuq o demekdir hemin app iso da ayzmaq olur, androide ve digerlerinede, destkopda olar basqa servislerde olar,
# birdene api yazmaqla bututn serviseler istifade ede bilerik

# meselen bezen gelir facebook ile login ol deyir, eslinde o gedir faccebookdan senin emailini username, parolunu siferein alir
# json data ni gonderir, basanda artiq useri tanimis olurq
# gedir facebooka gelir
class AuthorSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = User
        fields =("first_name", "last_name", "email")



class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model =Article
        fields =("title", "sub_title", "author", "text", "publish_date", "image")