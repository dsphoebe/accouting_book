# -*- coding: utf-8 -*-
from flask import Flask, render_template

import papaya_card.config
from papaya_card.cache import cache

app = Flask(__name__)
app.config.from_object(papaya_card.config.DevelopmentConfig)

# cache init
cache.init_app(app, config={'CACHE_TYPE': 'memcached'})


@app.route('/')
def index():
    return render_template('index.html')
