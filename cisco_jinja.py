# template.j2, conf.yaml
# Thanks to jinja2 template, a data in yaml format can be converted to the configuration to be sent to device.  

from flask import Flask, render_template
from jinja2 import Template
import yaml
from jinja2 import Environment, FileSystemLoader

with open('conf.yaml') as f:
    config = yaml.load(f,Loader = yaml.FullLoader)

# load jinja2 template
env = Environment(loader = FileSystemLoader('C:\PATH\PATH\PATH\PATH'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template.j2')

# Render the template with data and print the output
rendered_data = template.render(config)
print(rendered_data)

with open('jinjatemplate.txt', 'w') as f:
    f.write(rendered_data)

#############################

# conf.yaml file

'''
interfaces:
  - interface: lo1
    desc: network to 1
    ip_add: 10.0.1.1
    netmask: 255.255.255.0
  - interface: lo2
    desc: network to 2 
    ip_add: 10.0.2.1
    netmask: 255.255.255.0
  - interface: lo3
    desc: network to 3 updated
    ip_add: 10.0.3.1
    netmask: 255.255.255.0
'''

# template.j2 file

'''
{% for int in interfaces %}
interface {{ int.interface }}
ip address {{ int.ip_add }} {{ int.netmask }}
description {{ int.desc }}
{% endfor %}
'''

#########################
