# Calcul et visualisation duNDVI (indice de végétation) à partir de données Sentinel-2
# Zone : Foret de Fontainebleau - Image du 19 septembre 2026

import rasterio
import matplotlib.pyplot as plt

# Ouverture des deux bandes spectrales nécessaires au calcul du NDVI
#B04 = bande rouge (environ 665nm) et B08 = bande infrarouge / NIR (environ 842nm)
dataset = rasterio.open("data\\2026-09-18-00_00_2026-09-18-23_59_Sentinel-2_L2A_B04_(Raw).tiff", "r")
bande_rouge = dataset.read(1)


dataset_2 = rasterio.open("data\\2026-09-18-00_00_2026-09-18-23_59_Sentinel-2_L2A_B08_(Raw).tiff", "r")
bande_nir = dataset_2.read(1)


# Calcul du NDVI : (NIR - Rouge) / (NIR + Rouge)
# Résultat entre -1 et 1 : proche de 1 = végétation dense, proche de 0 ou négatif = sol nu/eau/bati

ndvi = (bande_nir - bande_rouge)/ (bande_nir + bande_rouge)



# Visualisation : cmap RdYlGn car son dégradé rouge-jaune-vert correspond
# intuitivement à l'absence/présence de végétation

plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label="NDVI")
plt.title("NDVI - Zone Foret de Fontainebleau - Sentinel-2, 19 sept 2026 ")
plt.savefig("ndvi_fontainebleau.png", dpi=150, bbox_inches='tight')
plt.show()