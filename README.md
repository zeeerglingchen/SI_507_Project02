Program purpose:
This program provides a easy way for users to access the data in the movies_clean.csv file.
The home page shows how many movie records are in the dataset
The route "/movies/ratings/" will randomly show five movies titles and corresponding IDMB ratings
The route "/movies/ratings/<score>" will show the movies that IDMB ratings are higher than the score the user input in the route, which means this route will screen out all the movies that IDBM ratings are lower than the input.
