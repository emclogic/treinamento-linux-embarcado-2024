from flask import Flask, render_template, request
import hardware

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/control', methods=['GET'])
def control():
    state = request.args.get('state')

    if state:
        print(f"Estado selecionado: {state}")

        if state == "ON":
            hardware.gpio_on()
        elif state == "OFF":
            hardware.gpio_off()
        else:
            print("Erro na API")

        return f"Estado selecionado: {state}", 200
    return "Nenhum estado recebido", 400

if __name__ == '__main__':
    app.run(debug=True)