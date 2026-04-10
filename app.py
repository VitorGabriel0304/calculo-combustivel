from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':  

        km = int(request.form['km'])
        kml = float(request.form['kml'])
        preco = float(request.form['preco'])

        #calculo
        litros = km / kml
        total = litros * preco
        por_km = total / km


        if kml < 8:
            classificacao = "Beberrao"
        elif kml <= 15:
            classificacao = "Padrao"
        elif kml <= 18:
            classificacao = "Economico"
        
        else: 
            classificacao = "Super-Economico"


        return render_template(
            'resultado.html',
           litros=litros,
           total=total,
           por_km=por_km,
           classificacao=classificacao
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)