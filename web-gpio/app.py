from flask import Flask, render_template, request
import gpiod
import atexit

GPIO_LINE = 29

chip = gpiod.Chip("/dev/gpiochip0")

lines = chip.get_line(29)
lines.request(consumer="web-gpio", type=gpiod.LINE_REQ_DIR_OUT)

app = Flask(__name__)

def gpio_on():
    lines.set_value(1)
    print(f"GPIO {GPIO_LINE} HIGH")

def gpio_off():
    lines.set_value(0)
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
    app.run(debug=True)
