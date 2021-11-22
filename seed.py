"""Automatically seed into database"""

import os
import json
from random import choice, randint
import crud, model, server

os.system('dropdb photocards')
os.system('createdb photocards')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/photocards.json') as f:
    pc_data = json.loads(f.read())

photocards_db = []
for photocard in pc_data:
    pc_name, pc_group, pc_album, pc_version, pc_img = photocard["pc_name"], photocard["pc_group"], photocard["pc_album"], photocard["pc_version"], photocard["pc_img"]

    photocards_to_add = crud.create_photocard(pc_name, pc_group, pc_album, pc_version, pc_img)
    photocards_db.append(photocards_to_add)

for n in range(3):
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

    for number in range(5):
        #what i want to do: get a random number from the length of the templates and photocards
        #taking that random number, and put it into create_pc_picked
        all_temps = crud.all_templates()
        random_temp = choice(all_temps)
        all_pcs = crud.all_photocards()
        random_pc = choice(all_pcs)


        crud.create_pc_picked(random_temp.template_id, random_pc.photocard_id)