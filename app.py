from fasthtml.common import *
import random

app,rt = fast_app()

@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

@rt('/change')

def get(): 
    texts = ['Nice to be here!', 'Hello World!', 'It\'s so random!']
    return Div(P(random.choice(texts)), hx_get="/change")

serve()