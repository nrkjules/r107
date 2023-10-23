
MinuteEcoule = int(input("Entrez le nombre de minutes ecoulÃ©es."))
heure = (MinuteEcoule //60 ) % 24
jour = (MinuteEcoule // 60) //24
minute = (MinuteEcoule % 60)
print( " La date associÃ©e aux minutes Ã©coulÃ©es est le: " , jour ,"Ã " , heure , "heure" , minute , "minutes")
