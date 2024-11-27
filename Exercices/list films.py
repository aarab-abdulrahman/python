from datetime import datetime
list_films=[]
def verification_titre(list_films,title):
    if any(x['titre'].lower() == title.lower() for x in list_films):
      return 0
    else:
       return 1

def verification_genre(x):
   if all(not i.isdigit() for i in x): return True
   else: return False

def verification_annee_sortie(x):
   try:
      q=datetime.strptime(x,"%Y-%m-%d")
      return 1
   except:
      return 0

def verification_nombre(x,y):
   if y==1:
      if x.count('.')<=1 and all(i.isdigit() or i=="." for i in x): return 1
      else: return 0
       
   else:
      if x.count('.')<=1 and all(i.isdigit() or i=="." for i in x) and 0<float(x)<=10: return 1
      else: return 0

def creer_list_films(list_films):
    titre=input("entre name film : ").strip()
    if verification_titre(list_films,titre):
       
       genre=input("entre le genre : ").strip()
       if verification_genre(genre):
          
          annee_sortie=input("entrer l'annee de sortie 'Y-M-D' : ").strip()
          if verification_annee_sortie(annee_sortie):
             
            recettes_mondiales=input('entre recettes mondailes : ').strip()
            if verification_nombre(recettes_mondiales,1):
                
                note_moyenne=input("entre note moyenne : ").strip()
                if verification_nombre(note_moyenne,2):
                   
                    list_films.append({
                       "titre":titre,
                       "genre":genre,
                       "annee sortie":annee_sortie,
                       "recettes mondiales":float(recettes_mondiales),
                       "note moyenne":float(note_moyenne)
                    })

                else:
                  print("please entre correct number and between (1-10)")

            else:
               print("please entre correct number ..")
               
          else: 
             print("please entre correct date...")   
       else:
          print('we do not accept numbers...')

    else:
       print('title "{}" exist..'.format(titre))


# calcul le recettes moyennes
def calcul_recettes_moyennes(list_films):
    somme_recettes=sum(map(lambda x : x['recettes mondiales'],list_films))
    return somme_recettes/len(list_films)

# compter les filmes par genre
def compter_filmes_par_genre(list_films):
   name_genre=input("enter nom de genre : ").strip()
   filter_name=filter(lambda i : i['genre'].lower()==name_genre.lower(),list_films)
   return list(filter_name)
    
# enricher les donnees des films
def enricher_donnees_films(list_films):
   les_recettes=list(map(lambda i : i['recettes mondiales'] , list_films))
   for i in range(len(les_recettes)):
      if les_recettes[i] <100:
         categorie="fible"
      elif 100 <= les_recettes[i] <500:
         categorie="moderee"
      elif les_recettes[i] > 500:
         categorie="elevee"
        
      list_films[i]['categorie']=categorie
 
# sorted
def sorted__(films,p):
         sorted_list=sorted(films,key=lambda x:x[p])
         for j in list(sorted_list):
                  print(f"{j}")
      

# sorted reverse
def sorted_reverse__(films,p):
            sorted_list_reverse=sorted(films,key=lambda y : y[p] , reverse= True)
            for y in list(sorted_list_reverse):
                  print(f"{y}")
   
# decreasing and increasing
def dec_inc_reasing(x):
         global list_films
         b=input("chose ('decreasing --> 1' or 'increasing --> 2'): ").strip()
         if b=="1":
            sorted_reverse__(list_films,x)
         elif b=="2":
            sorted__(list_films,x) 

# menu
while True:
   x=input("""
    1---> add filme info
    2 --> show list films
    3 --> calcul le recettes moyennes
    4 --> compter les filmes par genre
    5 --> enricher les donnees des films
    7---> filtrer les filmes selon un critere
    8 --> break
----> """)
   if x=="1": 
      creer_list_films(list_films)
   elif x=="2" : 
    for c in list_films:
        print(c) 
   elif x=="3":
      print(f'{calcul_recettes_moyennes(list_films):.2f}')
   elif x=="4":
      print(compter_filmes_par_genre(list_films))
   elif x=="5":
      enricher_donnees_films(list_films)
   
   elif x=="7":
      chose=input("select one item from this list ('titre' or 'genre' or 'annee sortie' or 'recettes mondiales' or 'note moyenne') : ").strip().lower()

      # chose 1
      if chose =="titre":
            a=input("filter the list by ('alphabetical order --> 1' or 'title lenght --> 2') : ").strip()
            if a=="1":
               sorted__(list_films,'titre')
            elif a=="2":
               ask=input("chose ('decreasing --> 1' or 'increasing --> 2'): ").strip()
               if ask=="1":
                sorted_list_by_lenght=sorted(list_films,key=lambda x: len(x['titre']),reverse=True)
                for j in list(sorted_list_by_lenght):
                  print(f"{j}")
               elif ask=="2":
                sorted__(list_films,x) 
                sorted_list_by_lenght=sorted(list_films,key=lambda x: len(x['titre']))
                for j in list(sorted_list_by_lenght):
                  print(f"{j}")


      # chose 2
      elif chose=="genre":
         compter_filmes_par_genre(list_films)
      

      # chose 3
      elif chose=="annee sortie" or "annee" in chose.split(' '):
         dec_inc_reasing('annee sortie')

      # chose 4
      elif chose=="recettes mondiales" or "recette" in chose.split(' '):
         dec_inc_reasing('recettes mondiales')

      # chose 5
      elif chose=="note moyenne" or "note" in chose.split(' '):
         dec_inc_reasing('note moyenne')


   elif x=="8":
      break