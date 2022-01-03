from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "name": "sabonete", "price": 5.99},
    {"id": 2, "name": "perfume", "price": 39.90},
    {"id": 3, "name": "tapete", "price": 10.30},
    {"id": 4, "name": "tunica", "price": 19.29},
    {"id": 5, "name": "chuveiro", "price": 119.19},
    {"id": 6, "name": "arroz", "price": 30.10},
    {"id": 7, "name": "oleo de cozinha", "price": 11.15},
    {"id": 8, "name": "carne moida", "price": 39.90},
    {"id": 9, "name": "bola", "price": 25.99},
    {"id": 10, "name": "cantil", "price": 55.99},
    {"id": 11, "name": "copo", "price": 5.99},
    {"id": 12, "name": "panela", "price": 25.99},
    {"id": 13, "name": "prato", "price": 10.99},
    {"id": 14, "name": "açucar", "price": 7.99},
    {"id": 15, "name": "sal", "price": 5.99},
    {"id": 16, "name": "pipoca", "price": 3.14},
    {"id": 17, "name": "sabonete", "price": 5.99},
    {"id": 18, "name": "miojo", "price": 2.39},
    {"id": 19, "name": "alface", "price": 3.99},
    {"id": 20, "name": "tomate", "price": 9.99},
    {"id": 21, "name": "macarrao", "price": 6.40},
    {"id": 22, "name": "mesa", "price": 115.99},
    {"id": 23, "name": "cadeira gamer", "price": 445.99},
    {"id": 24, "name": "mouse gamer", "price": 215.99},
    {"id": 25, "name": "tv", "price": 995.99},
    {"id": 26, "name": "liquidificador", "price": 65.99},
    {"id": 27, "name": "furadeira", "price": 99.15},
    {"id": 28, "name": "ferro de passar", "price": 55.80},
    {"id": 29, "name": "coberta", "price": 55.99},
    {"id": 30, "name": "sofa", "price": 600.15}
]

@app.get("/products")
def list_products():
  
    return jsonify(produtos), 200;

@app.get("/products/<product_id>")
def get(product_id : int):
    number = int(product_id)
    code = 200
    elements = []
    
    for objects in produtos:
        if objects["id"] == number:
            elements = objects

        if elements == []:
           elements = {"messagem": "elemento nao foi encontrado"},
           code = 404

    return jsonify(elements), code;
    


@app.post("/products")
def create():
    objects = dict(request.json)
    response ="item não foi criado"
    code = 401
    if objects.get("name") and objects.get("price"):
        objects["id"]=len(produtos)
        produtos.append(objects)
        response ="item foi criado"
        code = 201   
    return objects,code

@app.patch("/products/<product_id>")
def update(product_id: int):
    number =int(product_id)
    element = dict(request.json)
    response = jsonify({"messagem":"item não encontrado"})
    code = 404
    for obje in produtos:
        if obje["id"] == number:
            obje["name"]= element.get("name")
            obje["price"]= element.get("price")
            response = jsonify()
            code = 204
    return response, code

@app.delete("/products/<product_id>")
def delete(product_id: int):
    code=404
    for item in produtos:
        if int(product_id) == item["id"]:
            conter =item["id"]-1
            produtos.pop(conter)
            code =204
            element = jsonify()
        else:
           element= jsonify({"messagem": "objeto não encontrado"})
     
    return  element, code
    