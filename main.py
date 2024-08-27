# from fasthtml.common import *
import fasthtml.common as fc 

app, rt = fc.fast_app(live=True)

@rt('/')
def get():
    return get_list(5)

def get_list(n):
    return fc.Ol(*[fc.Li(f'{x}') for x in range(n)])

# Serve:
fc.serve()