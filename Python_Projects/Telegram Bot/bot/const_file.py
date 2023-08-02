from Messages_text import Message_text as ms
from flask import Flask, request, Response
from distutils.filelist import findall
from Database import * 
from os import remove
import datetime
import urllib3
import telepot
import logging
import time
import random
import traceback


master_id = "5833709924"
main_group_id = "-1001520098399"
chat_id_group_id = "-1001659027633"
shaps = "🌹👑💍🐶🐭🐹🐰🐼🐣🦋🦄🐓🍀🌿🌱🪴🌾💐🌷🌹🥀🪷🌺🌸🌼🌻🍄🎋🌟💫🌈🔥✨🍎🍌🍉🍇🍓🍒🍑🥤🍷🏀🌡🧪💉🔭🔬🦠🧬🎁🎈🎊🛍🎀📚📖🧡💛💚💙💜🖤🤍🤎"
link_saraha_channel = "https://t.me/+rug82WboqlxjMTM0"
saraha_channel_id = "-1001925803612"
admin_commands = {
    "add_btn": "add a button to the menu",
    "rm_btn": "remove a button from the menu",
    "re_name": "rename a button of the menu",
    "add_mat": "add material to a button of the menu",
    "add_menu": "add a menu to a button of the menu",
    "move_btn": "move button in the menu",
    "start_mult_q": "add a multiple quetions to a button of the menu",
    "cancel": "cancel a command",
    "post": "share a message in the channel"
}
master_commands = {
    "add_admin": "chat_id, channel_id, admin_name",
    "add_sub": "chat_id, sub_name",
    "channel_ids": "return channel ids",
    "admins_ids": "return chat_ids of admins",
    "add_depart":"admin id ,name, channel id, subjects"}
