#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7656304872:AAFCVqpm0bexqREh2Unk3NdtqNuAVTrXOlA")
    API_ID = int(os.environ.get("API_ID", "23551823"))
    API_HASH = os.environ.get("API_HASH", "36727c8db0a63181fe9963f605cc4ef4")
    AUTH_USERS = "1411895712"

