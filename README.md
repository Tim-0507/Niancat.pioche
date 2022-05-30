# Niancat.pioche
auteur : Timothee Robin ; Julien Menet 


Notre projet NyanCat a pour objectif de reproduire le célèbre GIF visionné plus de 300 000 000 de fois sur youtube.
L'animal apparaitra dans une interface grphique créée à l'aide de Pyqt. Pour ajouter une touche plus personnelle à notre NyanCat, nous avons décidé d'utiliser le jeu de la vie pour reproduire les étoiles présentes en arrière plan. Ces dernières permettent de donner une impression de mouvement.

L'ensemble apparait sur une grille composée d'un nombre défini de cases. 
La grille est séparée en 2 parties:


  -La première partie correspond à un rectangle dans lequel se trouve le chat. Toutes les 0.1 secondes, un 'clean_grid' est   effectué et le 2ème état du NyanCat apparait, et ainsi de suite. NyanCat possède 4 état répétés en boucle, donnant une impression de mouvement continu.
  
  
  -la seconde partie correspond au reste de la grille. C'est dans cette partie que s'applique le jeu de la vie en continu. Aucun 'clean_grid' n'est effectué.
