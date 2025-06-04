#Yes i am still working on it
# risk-gametheory
creating a risk game simulation to define the importance of humanity
---SET OF RULES:
-each entity starts with 20 resources
-each turn each entity recieve n resources, n = (math.floor(number of owned tiles / 3))          need: (import math)
-each turn each entity can position the resources obtained at the start of the turn and position them in any owned tile with now limit on how many resources can be in a tile.
-each turn each entity can attack one non owned tile:
    -the attack can be carried with  n resources where 1 >= x <= 3 as long as the tile from which the attack is being carried has 1 remaning tile at the start of the attack
    -for each attacking/defending resource a 6 face dice is cast the attack wins if  the attack dice > defending dice.
    -the tile is conquered if no remaning resource is left standing , at least 1 resource must be moved into the tile to be conquered

---WIN CONDITIONS:
    -total domination
    
