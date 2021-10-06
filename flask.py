import sys
import os
from flask import Flask

import website
command = sys.argv[1]
if command in ["atp", "ATP", 'template', '-t']:
    template = """{%extends 'base.html'%}
{%block script1%}{%endblock%}
{%block title%} Homepage {%endblock%}
{%block contents%}
<h1>Homepage Title</h1>
<div class="container">
    <!-- Homepage contents -->
</div>
{%endblock%}

{%block script2%}{%endblock%}
                """
    try:
        filename = sys.argv[2]
    except:
        print("Not enough args\nFilename not given")
        exit(1)
    f = open(f"website/templates/{filename}.html", 'w')
    f.write(template)
    f.close()
elif command in ['av', 'AV', 'view', '-v']:
    try:
        params = str(sys.argv[3])
    except:
        print("Not enough args\nFilename not given")
        exit(1)
    params = params.split(',')
    if len(params) > 0:
        pars = ""
        print(params)
        for i in range(len(params)):
            pars += f"/<{params[i]}>"
    template = f"""
@views.route('/{sys.argv[2]}{pars}')
def {sys.argv[2]}():
    return None """
    try:
        f = open('website/views.py', 'a')
        template = '\n' + template
        f.write(template)
        f.close()
    except:
        print("")
    print("Successfully added view")
