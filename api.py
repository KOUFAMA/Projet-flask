from enum import unique
from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv

from sqlalchemy import delete

load_dotenv()

app = Flask(__name__)

motdepass=quote_plus('db_password')
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:{}@{}t:5432/projet'.format(motdepass)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Livre(db.Model):
           __tablename__='livres'
           id=db.Column(db.Integer,primary_key=True,nullable=False)
           isbn=db.Column(db.String(50),unique=True,nullable=True)
           titre=db.Column(db.String(100),nullable=False)
           date_publication=db.Column(db.Date)
           auteur=db.Column(db.String(150),nullable=False)
           editeur=db.Column(db.String(100),nullable=False)
           categorie_id=db.Column(db.Integer,db.ForeignKey('categories.cat_id'),nullable=False)
           def format(self):
            return{
                'id':self.id,
                'isbn':self.isbn,
                'titre':self.titre,
                'date_publication':self.date_publication,
                'auteur':self.auteur,
                'editeur':self.editeur,
            }

class Categorie(db.Model):
            __tablename__='categories'
            cat_id=db.Column(db.Integer,primary_key=True,nullable=False)
            libelle=db.Column(db.String(100),nullable=False)
            livres=db.relationship('Livre',backref='categories',lazy=True)

            def format(self):
                return{
                    'cat_id':self.cat_id,
                    'libelle':self.libelle,
                }
    
def delete(self):
    db.session.delete(self)
    db.session.commit()
        
def update(self):
    db.session.commit()

db.create_all()


#########################################################################
#
#               Endpoint liste de tous les livres
#
#########################################################################
@app.route('/livres')
def listes_livre():
    livres=Livre.query.all()
    livret = [ et.format() for et in livres]
    return jsonify({
        'Success': True,
        'total': len(livres),
        "livres": livret
    })

#########################################################################
#
#               Endpoint chercher un livre en particulier
#
#########################################################################
@app.route('/livres/<int:id>')
def Selectionner_un_livre(id):
    try:
        livres=Livre.query.get(id)
        if livres is None:
            abort(404)
        else:
            return jsonify({
            'Success': True,
            'Selected_id':id,
            'livres':livres.format() 
        })
    except:
        abort(400)

#########################################################################
#
#               Endpoint listes des livres d'une catégorie
#
#########################################################################
@app.route('/categories/<int:cat_id>/livres')
def liste_livres_cat(cat_id):
    livres=Livre.query.all()
    livret = [ et.format() for et in livres]
    return jsonify({
         'Success': True,
        'Selected_libelle':cat_id,
        'livres':Categorie.format()
    })

#########################################################################
#
#               Endpoint lister une catégorie
#
#########################################################################
@app.route('/categories/<int:id>')
def lister_categorie():
    try:
        categories=Categorie.query.get(id)
        categories = [ et.format() for et in categories]
        return jsonify({
            'Success': True,
            'selected_id': id,
            "categories": categories
        })
    except:
        abort(400)
#########################################################################
#
#               Endpoint Chercher une catégorie
#
#########################################################################
@app.route('/categories/<int:id>')
def liste_categorie(id):
    try:
        categories=Categorie.query.get(id)
        if categories is None:
            abort(404)
        else:
            return jsonify({
            'success': True,
            'selected_id':id,
            'categories':categories.format()
        })
    except:
        abort(400)

#########################################################################
#
#               Endpoint liste de tous les catégories
#
#########################################################################
@app.route('/categories')
def listes_categorie():
    categories=Categorie.query.all()
    cat = [ et.format() for et in categories]
    return jsonify({
        'Success': True,
        'total': len(categories),
        "categories": cat
    })

#########################################################################
#
#               Endpoint supprimer un  livre
#
#########################################################################
@app.route('/livres/<int:id>',methods=['DELETE'])
def delete_livres(id):
    try:
        livres=Livre.query.get(id)
        if livres is None:
            abort(404)
        else:
            livres.delete()
            return jsonify({
                'success':True,
                'id':id,
                'livres':livres.format(),
                'total_livres':Livre.query.count()
            })
    except:
        abort(400)
    finally:
        db.session.close()


#########################################################################
#
#               Endpoint supprimer une catégorie
#
#########################################################################
@app.route('/categories/<int:id>',methods=['DELETE'])
def delete_categories(id):
    try:
        categories=Categorie.query.get(id)
        if categories is None:
            abort(404)
        else:
            categories.delete()
            return jsonify({
                'success':True,
                'id':id,
                'livres':categories.format(),
                'total_categories':Categorie.query.count()
            })
    except:
        abort(400)
    finally:
        db.session.close()


#########################################################################
#
#               Endpoint modifier un livre
#
#########################################################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def modifier_livres(id):
    body=request.get_json()
    livres=Livre.query.get(id)
    if livres is None:
        abort(404)
    else:
        livres.isbn=body.get('isbn')
        livres.titre=body.get('titre')
        livres.date_publication=body.get('date_publication')
        livres.auteur=body.get('auteur')
        livres.editeur=body.get('editeur')
        livres.update()
        return jsonify({
            'success':True,
            'updated_id':id,
            'livres':livres.format()
        })

#########################################################################
#
#               Endpoint modifier une catégorie
#
##########################################################################
@app.route('/categories/libelle',methods=['PATCH'])
def modifier_categories(id):
    body=request.get_json()
    categories=Categorie.query.get(id)
    if categories is None:
        abort(404)
    else:
        categories.libelle=body.get('libelle')
        categories.update()
        return jsonify({
            'success':True,
            'updated_id':id,
            'livres':categories.format()
        })

#########################################################################
#
#               Endpoint design erreur
#
##########################################################################
@app.errorhandler(404)
def not_fond(error):
    return jsonify({
        "success":False,
        "error":404,
        "message":"Not fond"
    }),404
    
@app.errorhandler(500)
def not_fond(error):
    return jsonify({
        "success":False,
        "error":500,
        "message":"Internal server"
    }),500 