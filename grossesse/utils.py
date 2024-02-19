from grossesse.models import InfoGrossesse
# import json

# donnees = []

# for semaine in range(1, 44):
#     info =
#     donnees.append(info)

# info_grossesse = InfoGrossesse(data=json.dumps(donnees))
# info_grossesse.save()

info_grossesse = InfoGrossesse(semaine=1, donnees={"image": "image1.jpg", "texte": "Lorem ipsum"})
info_grossesse.save()