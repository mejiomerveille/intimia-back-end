from grossesse.models import InfoGrossesse
# import json

# donnees = []

# for semaine in range(1, 44):
#     info = {
#         'semaine': semaine,
#         'image_bebe': 'chemin/vers/image_bebe_semaine{}.jpg'.format(semaine),
#         'image_fruit': 'chemin/vers/image_fruit_semaine{}.jpg'.format(semaine),
#         'image_ventre_mere': 'chemin/vers/image_ventre_mere_semaine{}.jpg'.format(semaine),
#         'conseil_bebe': 'Conseil pour le bébé semaine {}'.format(semaine),
#         'conseil_mere': 'Conseil pour la mère semaine {}'.format(semaine),
#         'conseil_nutrition': 'Conseil sur la nutrition semaine {}'.format(semaine),
#         'recommandation': 'Recommandation semaine {}'.format(semaine)
#     }
#     donnees.append(info)

# info_grossesse = InfoGrossesse(data=json.dumps(donnees))
# info_grossesse.save()

info_grossesse = InfoGrossesse(semaine=1, donnees={"image": "image1.jpg", "texte": "Lorem ipsum"})
info_grossesse.save()