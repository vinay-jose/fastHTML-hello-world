from fasthtml.common import *
import random

app = FastHTML()

@app.route('/')
def get(): return Div(P('Hello World!'), hx_get="/change", hx_swap="beforebegin")

@app.route('/change')
def get(): 
    texts = ['Nice to be here!', 'Hello World!', 'It\'s so random!']
    return Div(P(random.choice(texts)), hx_get="/change")

serve()