"""Automatically seed into database"""

import os
import json
from random import choice, randint
import crud, model, server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/photocards.json') as f:
    pc_data = json.loads(f.read())

photocards_db = []
for photocard in pc_data:
    pc_name, pc_group, pc_album, pc_img = photocard["pc_name"], photocard["pc_group"], photocard["pc_album"], photocard["pc_img"]

    photocards_to_add = crud.create_photocard(pc_name, pc_group, pc_album, pc_img)
    photocards_db.append(photocards_to_add)

for n in range(1,5):
    email = f'user{n}@test.com'
    password = 'testing'

    user_to_add = crud.create_user(email, password)
    for num in range(3):
        all_users_at_hand=crud.all_users()
        user_temp = choice(all_users_at_hand)

        font_family = ["serif", "times", "arial"]
        font_color = ["blue", "red", "green"]
        bg_color = ["pink", "white", "beige"]

        crud.create_template(choice(font_family), choice(font_color), choice(bg_color), user_temp)

for number in range(10):
    random_temp = randint(1,5)
    random_pc = randint(1,6)
    crud.create_pc_picked(random_temp, random_pc)