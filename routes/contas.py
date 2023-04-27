from flask import Blueprint, session, request, render_template, redirect, url_for, flash
from ..extentions.database import mongo
from datetime import date, datetime
import socket
from bson.objectid import ObjectId
import uuid

conta = Blueprint("conta", __name__)

@conta.route("/list")
def listContas():
    if "username" in session:
        contas = mongo.db.produtos.find()
        return render_template("contas/list.html", contas=contas)
    else:
        return redirect(url_for("usuario.index"))


@conta.route('/insert', methods=['GET', "POST"])
def insertContas():
    if request.method =='GET':
        return render_template("contas/insert.html")
    else:
        nome=request.form.get('nome')
        quantidade=request.form.get('quantidade')
        preco=request.form.get('preco')
        categoria=request.form.get('categoria')
        estoque=request.form.get('estoque')

        if not nome or len(nome)>50:
            flash("Campo Obrigatorio")
        elif not quantidade or not quantidade.isdigit() or int(quantidade)<=0:
            flash("Quantidade incorreto")
        elif not preco:
            flash("Valor Obrigatório ")
        elif not categoria:
            flash("Categoria Obrigatório ")
        elif not estoque:
            flash("Estoque Obrigatório ")
        else:
            insert =  mongo.db.produtos.insert_one({
                "produto":nome,
                "quantidade":quantidade,
                "preco":preco,
                "categoria":categoria,
                "estoque":estoque,
                "valor_total":round((float(quantidade)*float(preco)),2)
            })

            mongo.db.logs.insert_one(
                {
                    "timestamp": datetime.today(),
                    "usuario": session["username"],
                    "tag": f"cadastro: {insert.inserted_id}",
                    "endereco": socket.gethostbyname(socket.gethostname()),
                    "sessionId": session["sessionId"]

                }
            )

            flash("Cadastrado Com Sucesso!!")
        return redirect(url_for("conta.listContas"))


@conta.route('/edit')
def editContas():
    if request.method=='GET':
        idocntas=request.values.get("idocntas")

        if not idocntas:
            flash('Campo idproduto é obrigatório!')
            return redirect(url_for("contas.listContas"))
        else:
            idcont=mongo.db.produtos.find({"_id": ObjectId(idocntas)})
            conta=[cta for cta in idcont ]
            estoques=set()
    return  'edit'

@conta.route('/delete')
def deleteContas():
    return  'delete'