# Projet-flask
#### Installation des dépendances

Après avoir installé ou mis à jour python, vous devez installer les dépendances de notre API avec la commande:

```bash
pip install -r requirements.txt
```

Celà installera tous les packages nécéssaires que nous avons précisé dans le fichier `requirements.txt`.

##### Dépendances clés
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) est un micro framework open-source de développement web en Python.
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) est un ORM de python. Nous allons l'utiliser pour mapper nos tables en postgres à nos classes en python.

#### Variables d'environement

Nous vous recommandons de creer vos propres variables d'environnement pour la connextion à la base de donnée postgres. Pour celà créez un fichier `.env` dans lequel vous copierez le code suivant en prenant soins de remplacer 'your_password' par votre mot de passe postgres d'utilisateur,'host' par l'addresse IP de votre serveur et your_database par le nom de la base de donnée que vous auriez préalablement creé

```file
password=votre mot de passe
host=hostname
database=base de donnee
```

## Ouvrir le serveur en local
Pour démarrer l'API sur votre serveur local, vous devez déjà avoir spécifié 'localhost' comme host dans les variables d'environement. Ensuite vous tapez les commandes suivantes dans un terminal:

- Sous linux ou mac

```bash
export FLASK_APP=api.py
export FLASK_ENV=development
flask run
```

- Sous Windows

```bash
set FLASK_APP=api.py
set FLASK_ENV=development
flask run
```

Pour tester tous les endpoints de notre API, vous pouvez le faire depuis le bash en installant [curl](https://curl.se/download.html).
Mais nous vous conseillons de le faire avec l'application [Postman](https://www.postman.com) que vous pouvez télécharger et y importer les requetes qui se trouvent dans le fichier ...

 


## DOCUMENTATION DE L'API


## REFERENCE DE L'API
Cet API a été déployé sur la plateforme Heroku et est disponible sous le lien  https://app-koufamal2c.herokuapp.com

## GESTION DES ERREURS
Les erreurs sont rertournés sous le format JSON dont voici un exemple:
{
    "success":False
    "error": 400
    "message":"Bad request
}

Voici les erreurs possibles que notre API pourrait retourner:
. 400: Bad request
. 500: Internal server error
. 404: Not found


## Endpoints

### GET /livres
    GENERAL:  Cette route retourne la liste des livres dans notre base de donnée, le statut de la requête  et le nombre total des livres.
            Exemple: curl  https://app-koufamal2c.herokuapp.com/livres

           {
    "Success": true,
    "livres": [
        {
            "auteur": "Kip Thorne",
            "date_publication": "Sat, 12 Feb 2011 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 1,
            "isbn": " ISBN : 978-2-0802-6877-8",
            "titre": "Trous noirs et distorsions du temps"
        },
        {
            "auteur": "Olivia Ferrand, Antoine Couly",
            "date_publication": "Wed, 26 Jan 2022 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 2,
            "isbn": " ISBN : 978-2-0802-4564-9",
            "titre": "Tiens-toi droit ! "
        },
        {
            "auteur": "Stanislas Dehaene",
            "date_publication": "Tue, 06 Jul 2021 00:00:00 GMT",
            "editeur": "Odile Jacob ",
            "id": 3,
            "isbn": " ISBN : 978-2-7381-5702-7",
            "titre": "Face à face avec son cerveau"
        },
        {
            "auteur": " Frédéric Srour",
            "date_publication": "Thu, 20 Jan 2022 00:00:00 GMT",
            "editeur": " Pocket ",
            "id": 4,
            "isbn": " ISBN : 978-2-2663-1330-8",
            "titre": "SOS mal de dos! "
        },
        {
            "auteur": "Patrice Lopès, François-Xavier Poudat",
            "date_publication": "Wed, 26 Jan 2022 00:00:00 GMT",
            "editeur": " Elsevier Masson ",
            "id": 5,
            "isbn": " ISBN : 978-2-2947-7438-6",
            "titre": "Manuel de sexologie ! "
        },
        {
            "auteur": "Jordan/tourneux",
            "date_publication": "Fri, 26 Nov 2021 00:00:00 GMT",
            "editeur": "Sauramps Medical",
            "id": 6,
            "isbn": " ISBN :979-1-0303-0308-7",
            "titre": "Réanimation du nouveau-né en salle de naissance"
        },
        {
            "auteur": "Arthur Sonnet",
            "date_publication": "Sun, 03 May 2020 00:00:00 GMT",
            "editeur": "Paperback",
            "id": 7,
            "isbn": " ISBN-13 :979-8642898321",
            "titre": "Arsalus! "
        },
        {
            "auteur": "Anne-Gaëlle Balpe",
            "date_publication": "Sat, 26 Oct 2019 00:00:00 GMT",
            "editeur": "Shalom",
            "id": 8,
            "isbn": " ISBN :9782375542217",
            "titre": "Underlife"
        },
        {
            "auteur": " Chinua Achebe",
            "date_publication": "Fri, 20 Jan 2012 00:00:00 GMT",
            "editeur": "Kioune",
            "id": 9,
            "isbn": " ISBN : 978-2-153-1330-8",
            "titre": "Le monde s'effondre "
        },
        {
            "auteur": "Patrick Wosch",
            "date_publication": "Wed, 26 Jan 2011 00:00:00 GMT",
            "editeur": "Zodiack",
            "id": 10,
            "isbn": " ISBN : 978-2-2947-7148-6",
            "titre": "Alita"
        },
        {
            "auteur": "Taiga",
            "date_publication": "Thu, 26 Nov 2015 00:00:00 GMT",
            "editeur": "Kuroko",
            "id": 11,
            "isbn": " ISBN :929-1-0303-0308-7",
            "titre": "Plume"
        },
        {
            "auteur": "Arthur Sonnet",
            "date_publication": "Sun, 03 May 2020 00:00:00 GMT",
            "editeur": "Paperback",
            "id": 12,
            "isbn": " ISBN-1 :979-86428926-521",
            "titre": "Arsalus! "
        },
        {
            "auteur": "Anne-Gaëlle Balpe",
            "date_publication": "Sat, 26 Oct 2019 00:00:00 GMT",
            "editeur": "Shadom",
            "id": 13,
            "isbn": " ISBN :97823542217",
            "titre": "Underl"
        },
        {
            "auteur": " Chinua Achebe",
            "date_publication": "Sun, 20 Jan 2002 00:00:00 GMT",
            "editeur": "Kioune",
            "id": 14,
            "isbn": " ISBN : 978-2-103-1330-8",
            "titre": "Le monde du bas"
        },
        {
            "auteur": "Patrick Wosch",
            "date_publication": "Fri, 26 Jan 2001 00:00:00 GMT",
            "editeur": "Zoliack",
            "id": 15,
            "isbn": " ISBN : 978-2-2102-7148-6",
            "titre": "Antanka"
        },
        {
            "auteur": "Taiga",
            "date_publication": "Sat, 26 Nov 2005 00:00:00 GMT",
            "editeur": "Kyse",
            "id": 16,
            "isbn": " ISBN :929-1-0453-0308-7",
            "titre": "Plantoyi"
        },
        {
            "auteur": "Arthur Sonnet",
            "date_publication": "Sun, 03 May 2020 00:00:00 GMT",
            "editeur": "Paperback",
            "id": 17,
            "isbn": " ISBN-1 :979-86-8926-521",
            "titre": "Arsalus! "
        },
        {
            "auteur": "Epreuve",
            "date_publication": "Tue, 24 Sep 2019 00:00:00 GMT",
            "editeur": "Schadraom",
            "id": 18,
            "isbn": " ISBN :97-542217",
            "titre": "Le r\"mède mortel"
        },
        {
            "auteur": " Chinua Achebe",
            "date_publication": "Sat, 20 Jan 2007 00:00:00 GMT",
            "editeur": "Kioune",
            "id": 19,
            "isbn": " ISBN : 978-1330-8",
            "titre": "Gamer"
        },
        {
            "auteur": "Alice",
            "date_publication": "Thu, 26 Feb 2009 00:00:00 GMT",
            "editeur": "Wondul",
            "id": 20,
            "isbn": " ISBN : 978-2-21-02-7148-6",
            "titre": "La faucheuse"
        },
        {
            "auteur": "Kaguya",
            "date_publication": "Sat, 26 Nov 2005 00:00:00 GMT",
            "editeur": "Shine",
            "id": 21,
            "isbn": " ISBN :929-1-04-3-0308-7",
            "titre": "Incarceron"
        },
        {
            "auteur": "Jeans Portex",
            "date_publication": "Mon, 13 May 2019 00:00:00 GMT",
            "editeur": "Paperback",
            "id": 22,
            "isbn": " ISBN-1 :79-86-826-521",
            "titre": "Mariage du desert "
        },
        {
            "auteur": "Arthur",
            "date_publication": "Sun, 24 Apr 2016 00:00:00 GMT",
            "editeur": "Schadraom",
            "id": 23,
            "isbn": " ISBN :7-52217",
            "titre": "Escapade au caraibe"
        },
        {
            "auteur": "Gregoire",
            "date_publication": "Sat, 20 Jan 2007 00:00:00 GMT",
            "editeur": "Azur",
            "id": 24,
            "isbn": " ISBN :78-330-8",
            "titre": "Retrouvaille forcé"
        },
        {
            "auteur": "Shella",
            "date_publication": "Tue, 26 Feb 2019 00:00:00 GMT",
            "editeur": "Manbella",
            "id": 25,
            "isbn": " ISBN :78-2-21-02-748-6",
            "titre": "Audace"
        },
        {
            "auteur": "CArol Halston",
            "date_publication": "Sat, 26 Nov 2005 00:00:00 GMT",
            "editeur": "Azur",
            "id": 26,
            "isbn": " ISBN :29-1-04-3-038-7",
            "titre": "L'impossible oubli"
        },
        {
            "auteur": "Laure Manel",
            "date_publication": "Mon, 13 May 2019 00:00:00 GMT",
            "editeur": "Inedit",
            "id": 27,
            "isbn": "ISBN :879-826-524-1",
            "titre": "Histoire d'@ "
        },
        {
            "auteur": "Jean D'arc",
            "date_publication": "Mon, 24 Apr 1916 00:00:00 GMT",
            "editeur": "Histoire",
            "id": 28,
            "isbn": "ISBN :87-5254-21857",
            "titre": "La premiere G.Mondiale"
        },
        {
            "auteur": "Gregoire",
            "date_publication": "Tue, 20 Jan 1807 00:00:00 GMT",
            "editeur": "Azur",
            "id": 29,
            "isbn": "ISBN :878-32-6530-8",
            "titre": "Prehistoire"
        },
        {
            "auteur": "Sharona",
            "date_publication": "Sun, 26 Feb 2012 00:00:00 GMT",
            "editeur": "Manbella",
            "id": 30,
            "isbn": "ISBN :878-212-748-6",
            "titre": "Histoire tem"
        },
        {
            "auteur": "CArol Halston",
            "date_publication": "Sun, 26 Nov 2000 00:00:00 GMT",
            "editeur": "Romains",
            "id": 31,
            "isbn": "ISBN :829-5-104-3708",
            "titre": "Rome antique"
        },
        {
            "auteur": "Laure tanel",
            "date_publication": "Wed, 13 May 2015 00:00:00 GMT",
            "editeur": "Inedit",
            "id": 32,
            "isbn": "ISBN :019-826-524-1",
            "titre": "Comme toi "
        },
        {
            "auteur": "Jean ",
            "date_publication": "Mon, 24 Apr 1916 00:00:00 GMT",
            "editeur": "bebe",
            "id": 33,
            "isbn": "ISBN :046-5254-2185",
            "titre": "Crocmillivre"
        },
        {
            "auteur": "George",
            "date_publication": "Tue, 20 Jan 1807 00:00:00 GMT",
            "editeur": "Azur",
            "id": 34,
            "isbn": "ISBN :098-32-6530-8",
            "titre": "So nice"
        },
        {
            "auteur": "Sharona",
            "date_publication": "Sun, 26 Feb 2017 00:00:00 GMT",
            "editeur": "vanbella",
            "id": 35,
            "isbn": "ISBN :058-212-748-6",
            "titre": "Dolto"
        },
        {
            "auteur": "CArla Halston",
            "date_publication": "Sun, 26 Nov 2000 00:00:00 GMT",
            "editeur": "Meilleurs",
            "id": 36,
            "isbn": "ISBN :029-5-104-3708",
            "titre": "Coco"
        },
        {
            "auteur": "Laure tanel",
            "date_publication": "Tue, 13 May 2003 00:00:00 GMT",
            "editeur": "Inedit",
            "id": 37,
            "isbn": "ISBN :019-8726-524-1",
            "titre": "Glipour "
        },
        {
            "auteur": "Jean ",
            "date_publication": "Mon, 24 Sep 1906 00:00:00 GMT",
            "editeur": "bebe",
            "id": 38,
            "isbn": "ISBN :064-5654-2185",
            "titre": "Dad"
        },
        {
            "auteur": "George",
            "date_publication": "Sun, 20 Jan 1907 00:00:00 GMT",
            "editeur": "Azur",
            "id": 39,
            "isbn": "ISBN :089-32-6530-8",
            "titre": "Les p'tit diables"
        },
        {
            "auteur": "Sharona",
            "date_publication": "Fri, 26 Jul 2013 00:00:00 GMT",
            "editeur": "vanbella",
            "id": 40,
            "isbn": "ISBN :085-212-748-6",
            "titre": "Bine"
        },
        {
            "auteur": "CArla Halston",
            "date_publication": "Fri, 26 Nov 2010 00:00:00 GMT",
            "editeur": "Meilleurs",
            "id": 41,
            "isbn": "ISBN :092-5-104-3708",
            "titre": "Insectes"
        },
        {
            "auteur": "Laurelle",
            "date_publication": "Mon, 13 May 2013 00:00:00 GMT",
            "editeur": "Inedit",
            "id": 42,
            "isbn": "ISBN :9-8726-7524-1",
            "titre": "Cordon bleu "
        },
        {
            "auteur": "Jeanne Duplex ",
            "date_publication": "Mon, 24 Sep 1906 00:00:00 GMT",
            "editeur": "Gourme",
            "id": 43,
            "isbn": "ISBN :4-5654-2185",
            "titre": "Petit plats"
        },
        {
            "auteur": "Georgette",
            "date_publication": "Sun, 20 Jan 1907 00:00:00 GMT",
            "editeur": "Azur",
            "id": 44,
            "isbn": "ISBN :9-3562-6530-8",
            "titre": "Irressistible"
        },
        {
            "auteur": "Sharonne",
            "date_publication": "Fri, 26 Jul 2013 00:00:00 GMT",
            "editeur": "vanbella",
            "id": 45,
            "isbn": "ISBN :5-2120-748-6",
            "titre": "Dine"
        },
        {
            "auteur": "Carlos Valdez",
            "date_publication": "Fri, 26 Nov 2010 00:00:00 GMT",
            "editeur": "Four",
            "id": 46,
            "isbn": "ISBN :2-5-1804-3708",
            "titre": "Custo"
        },
        {
            "auteur": "Dalton",
            "date_publication": "Mon, 13 May 2013 00:00:00 GMT",
            "editeur": "Inedit",
            "id": 47,
            "isbn": "ISBN :987-26-7524-1",
            "titre": "Courage rions"
        },
        {
            "auteur": " Duplex ",
            "date_publication": "Mon, 24 Sep 1906 00:00:00 GMT",
            "editeur": "Ricotte",
            "id": 48,
            "isbn": "ISBN :456-54-2185",
            "titre": "Trucs fun"
        },
        {
            "auteur": "Williams",
            "date_publication": "Sun, 20 Jan 1907 00:00:00 GMT",
            "editeur": "Azur",
            "id": 49,
            "isbn": "ISBN :935-62-6530-8",
            "titre": "Humour sur toute la ligne"
        },
        {
            "auteur": "Sam",
            "date_publication": "Fri, 26 Jul 2013 00:00:00 GMT",
            "editeur": "Dyouck",
            "id": 50,
            "isbn": "ISBN :1254-2-120-748-6",
            "titre": "Héraclès"
        },
        {
            "auteur": "Henry",
            "date_publication": "Fri, 26 Nov 2010 00:00:00 GMT",
            "editeur": "Fire",
            "id": 51,
            "isbn": "ISBN :25-18-04-3708",
            "titre": "L'echo des savanes"
        }
    ],
    "total": 51
}
###  GET/livres(id)
    GENERAL: Cette route vous permet d'avoir un livre à partir de son id si elle existe. Il retourne les informations concernant un livre, le statut de la requête et l'id du livre demandé.
            Exemple: curl  https://app-koufamal2c.herokuapp.com/livres/5

               {
      "Selected_id": 5,
      "Success": true,
      "livres": {
        "auteur": "Patrice Lopès, François-Xavier Poudat",
        "date_publication": "Wed, 26 Jan 2022 00:00:00 GMT",
        "editeur": " Elsevier Masson ",
        "id": 5,
        "isbn": " ISBN : 978-2-2947-7438-6",
        "titre": "Manuel de sexologie ! "
      }
    }

###  GET /categories
    GENERAL: Cette route retourne la liste complète des catégories, le nombre total de categorie et le statut de la requête.

            Exemple: curl  https://app-koufamal2c.herokuapp.com/categories

                 {
        "Success": true,
        "categories": [
          {
            "cat_id": 1,
            "libelle": "Fixion"
          },
          {
            "cat_id": 2,
            "libelle": "Policier"
          },
          {
            "cat_id": 3,
            "libelle": "Conte"
          },
          {
            "cat_id": 4,
            "libelle": "Harlequin"
          },
          {
            "cat_id": 5,
            "libelle": "Science"
          },
          {
            "cat_id": 6,
            "libelle": "Histoire"
          },
          {
            "cat_id": 7,
            "libelle": "Jeunesse"
          },
          {
            "cat_id": 8,
            "libelle": "Cuisine"
          },
          {
            "cat_id": 9,
            "libelle": "Humour"
          },
          {
            "cat_id": 10,
            "libelle": "Bandes dessinés"
          }
        ],
        "total": 10
      }

###  GET/categories(categorie_id)
    GENERAL: Cette route retourne les informations d'une categorie à partir de son id si elle existe, le statut de la requête et l'id de la categorie recherché
            Exemple: curl https://app-koufamal2c.herokuapp.com/categories/1

                 {
        "Selected_cat_id": 1,
        "Success": true,
        "categories": [
          {
            "cat_id": 1,
            "libelle": "Fixion"
          }

###  DELETE/categorie(categorie_id)
    GENERAL: Cette route permet de supprrimer, si elle existe, une categorie dont l'id est passé en paramètre. Il retourne les informations de la categorie modifié, son id et le statut de la requête.

            Exemple: curl - X DELETE https://app-koufamal2c.herokuapp.com/categories/1
            {
                "delete_categories": {
                    "cat_id": 1,
                    "libelle": "Fixion"
                },
                "Success": true,
                "Total": 9
            }


###  DELETE/livres(id)
            GENERAL: Cette route supprime, si elle existe, un livre dont l'id est passé en paramètre. Il retourne les informations concernant le livre supprimé, son id et le statut de la requête.

            Exemple: curl - X DELETE  https://app-koufamal2c.herokuapp.com/livres/25

            {
                "delete_livres": {
                    "auteur": "Shella",
                    "date_publication": "Tue, 26 Feb 2019 00:00:00 GMT",
                    "editeur": "Manbella",
                    "id": 25,
                    "isbn": " ISBN :78-2-21-02-748-6",
                    "titre": "Audace"
                },
                "Success": true,
                "Total": 50
            }


###  GET /categories/(categories_id)/livres
    GENERAL: This endpoint is used to create a new movie. We return the ID of the new movie created, 
    the movie that was created, the list of movies and the number of movies.

            Exemple: curl   https://app-koufamal2c.herokuapp.com/categories/4/livres

                {
    "Selected_cat_id": 4,
    "Success": true,
    "livres": [
        {
            "auteur": "Jeans Portex",
            "date_publication": "Mon, 13 May 2019 00:00:00 GMT",
            "editeur": "Paperback",
            "id": 22,
            "isbn": " ISBN-1 :79-86-826-521",
            "titre": "Mariage du desert "
        },
        {
            "auteur": "Arthur",
            "date_publication": "Sun, 24 Apr 2016 00:00:00 GMT",
            "editeur": "Schadraom",
            "id": 23,
            "isbn": " ISBN :7-52217",
            "titre": "Escapade au caraibe"
        },
        {
            "auteur": "Gregoire",
            "date_publication": "Sat, 20 Jan 2007 00:00:00 GMT",
            "editeur": "Azur",
            "id": 24,
            "isbn": " ISBN :78-330-8",
            "titre": "Retrouvaille forcé"
        },
        {
            "auteur": "Shella",
            "date_publication": "Tue, 26 Feb 2019 00:00:00 GMT",
            "editeur": "Manbella",
            "id": 25,
            "isbn": " ISBN :78-2-21-02-748-6",
            "titre": "Audace"
        },
        {
            "auteur": "CArol Halston",
            "date_publication": "Sat, 26 Nov 2005 00:00:00 GMT",
            "editeur": "Azur",
            "id": 26,
            "isbn": " ISBN :29-1-04-3-038-7",
            "titre": "L'impossible oubli"
        }
    ],
    "total": 5
}

###  PATCH/livres(livre_id)
    GENERAL: Cette route vous permet de modifier les informations d'un livre dont l'id est passé en paramètre. Il retourne les informations du livre modifié, son id et le statut de la requête

            Exemple: curl -X PATCH  https://app-koufamal2c.herokuapp.com/livres/2
            -H "Content-Type:application/json" -d "{"auteur": "Benjamin KOUFAMA","categorie_id": 1,"date_publication": "2015-04-07","editeur": "Les contes des milles et une nuit","isbn": "ISBN :984-123-12-23","titre": "La mort du soldat"}"

                {
                    "Success": true,
                    "modifier_livres": {
                        "auteur": "Benjamin KOUFAMA",
                        "categorie_id": 1,
                        "date_publication": "2015-04-07",
                        "editeur": "Les contes des milles et une nuit",
                        "id": 1,
                        "isbn": "ISBN:984-123-12-23",
                        "titre": "La mort du soldat"
                    },
                    "updated_id": 2
                }


###  PATCH/categories (categorie_id)
    GENERAL: cette route vous permet de modifier les informations d'une catgories dont l'id est passé en paramètre. Il retoune les informations de la categorie modifié, son id et le statut de la requette.

            Exemple: curl -X PATCH https://capstoneapi.herokuapp.com/categories/3 
            -H "Content-Type:application/json" -d "{"libelle":"comédie"}"

                {
                    "Success": true,
                    "modifier_categories": {
                        "cat_id": 3,
                        "libelle": "comédie"
                    },
                    "updated_id": 3
                }
