import os
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import gpiod
import atexit

GPIO_LINE = 29

chip = gpiod.Chip("/dev/gpiochip0")

lines = chip.get_line(GPIO_LINE)

app = Flask(__name__)
secret_key = os.urandom(32)
app.config['SECRET_KEY'] = secret_key.hex()
csrf = CSRFProtect(app)

def gpio_on():
    lines.request(consumer="web-gpio", type=gpiod.LINE_REQ_DIR_OUT)
    lines.set_value(1)
    lines.release()
    print(f"GPIO {GPIO_LINE} HIGH")

def gpio_off():
    lines.request(consumer="web-gpio", type=gpiod.LINE_REQ_DIR_OUT)
    lines.set_value(0)
    lines.release()
    print(f"GPIO {GPIO_LINE} LOW")

def cleanup():
    lines.release()
    print("GPIO released")

atexit.register(cleanup)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/control', methods=['GET'])
def control():
    state = request.args.get('state')

    if state:
        print(f"Estado selecionado: {state}")

        if state == "ON":
            gpio_on()
        elif state == "OFF":
            gpio_off()
        else:
            print("Erro na API")

        return f"Estado selecionado: {state}", 200
    return "Nenhum estado recebido", 400

if __name__ == '__main__':
    gpio_off()
    app.run(host='0.0.0.0', port=5000, debug=False)
