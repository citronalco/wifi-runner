#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mechanicalsoup

URL="http://wifionice.de/de/";

browser = mechanicalsoup.StatefulBrowser()
browser.open(URL)
form=browser.select_form(selector='form')
browser.submit(form,browser.get_url())
