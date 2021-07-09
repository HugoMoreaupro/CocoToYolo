import json

tailleimage = [640, 480]
# Charge le fichier source : adresse à changer suivant les besoins
with open('Coco.json', 'r') as coco:
    data = json.load(coco)
    coco.close()

# Crée la correspondance entre les id et les images, nettoie aussi les fichiers.
correspondancesImages = {}
for q in data["images"]:
    correspondancesImages[q["id"]] = 'sortie/'+q["file_name"][:7] + 'txt'
    file = open('sortie/'+q["file_name"][:7] + 'txt', "w")
    file.close()


correspondancesObjets = {
    "4": "0"
    # boite est notre seul élément dans l'exemple, il correspond donc à l'indice 0. Le choix de l'ordre importe peu, mais il faut que les items soient notés de 0 à Nombre-1
}

for p in data['annotations']:
    name = correspondancesImages[p["image_id"]]

    xcoco = p["bbox"][0]
    ycoco = p["bbox"][1]
    width = p["bbox"][2]
    height = p["bbox"][3]
    xyolo = (xcoco + (width / 2)) / tailleimage[0]
    yyolo = (ycoco + (height / 2)) / tailleimage[1]
    alpha = width / tailleimage[0]
    beta = height / tailleimage[1]

    yolo = open(str(name), "a")
    yolo.write(
        "{:0.6f}".format(xyolo) + ', ' + "{:0.6f}".format(yyolo) + ', ' + "{:0.6f}".format(alpha) + ', ' + "{:0.6f}".format(
            beta))
    yolo.close()
