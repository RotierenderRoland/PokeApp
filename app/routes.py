from flask import render_template
from app import app
from app.forms import SearchForm
from app.connector import Pokemon, api_connector


@app.route('/',methods=["GET","POST"])
@app.route('/index',methods=["GET","POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        if api_connector.status("https://pokeapi.co/api/v2/pokemon/{}".format(form.pokemon.data.lower())) is False:
            return "error"
        else:
            return display_result(form.pokemon.data)
    return render_template("home.html", title="Home", form=form)

@app.route("/pokemon/<int:pokemon_id>/" ,methods=["GET","POST"])
def display_result(pokemon_id):
    form=SearchForm()
    ### this code block calls it self.
    #if form.validate_on_submit():
    #    if api_connector.status("https://pokeapi.co/api/v2/pokemon/{}".format(form.pokemon.data.lower())) is False:
    #        return "error"
    #    else:
    #        return display_result(form.pokemon.data)
    ### RecursionError: maximum recursion depth exceeded while calling a Python object
    url="https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_id.lower())
    connector=api_connector.connect(url)
    pokemon=Pokemon(connector)
    return render_template("results.html",form=form,name=pokemon.name,id=pokemon.id,portrait=pokemon.portrait, abilities=pokemon.abilities,height=pokemon.height,base_exp=pokemon.base_experience,weight=pokemon.weight,types=pokemon.types)
