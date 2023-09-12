{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e3cde501",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requisitos para ser una persona normal 2015\n",
      "Good Ol' Boy 2015\n",
      "The Snake Brothers 2015\n",
      "Miss India America 2015\n",
      "Annie 2014\n",
      "Afterlife 2014\n",
      "Grantham & Rose 2014\n",
      "Saving Christmas 2014\n",
      "Antboy: Revenge of the Red Fury 2014\n",
      "The Pasta Detectives 2014\n",
      "Honig im Kopf 2014\n",
      "Tom and Jerry: The Lost Dragon 2014\n",
      "Ping Pong Summer 2014\n",
      "Night at the Museum: Secret of the Tomb 2014\n",
      "Moomins on the Riviera 2014\n",
      "The Beat Beneath My Feet 2014\n",
      "Postman Pat: The Movie 2014\n",
      "They Are All Dead 2014\n",
      "Alexander and the Terrible, Horrible, No Good, Very Bad Day 2014\n",
      "Paddington 2014\n",
      "The Journey 2014\n",
      "Window Wonderland 2013\n",
      "Zoran, il mio nipote scemo 2013\n",
      "Pecoross' Mother and Her Days 2013\n",
      "Despicable Me 2 2013\n",
      "My Little Pony: Equestria Girls 2013\n",
      "Antboy 2013\n",
      "The Strange Little Cat 2013\n",
      "Cloudy with a Chance of Meatballs 2 2013\n",
      "Min sèsters bèrn i Afrika 2013\n",
      "Ghadi 2013\n",
      "Tio Papi 2013\n",
      "The Giant King 2012\n",
      "OMG: Oh My God! 2012\n",
      "The Lorax 2012\n",
      "Ricky Rapper and Cool Wendy 2012\n",
      "Diary of a Wimpy Kid: Dog Days 2012\n",
      "Cine Hollièdy 2012\n",
      "English Vinglish 2012\n",
      "The Odd Life of Timothy Green 2012\n",
      "Parental Guidance 2012\n",
      "OMG: Oh My God! 2012\n",
      "Frankenweenie 2012\n",
      "Hotel Transylvania 2012\n",
      "Le monde doit m'arriver? 2012\n",
      "Happiness Is a Warm Blanket, Charlie Brown 2011\n",
      "Somebody's Hero 2011\n",
      "Red Dog 2011\n",
      "A Cube of Sugar 2011\n",
      "When Santa Fell to Earth 2011\n",
      "Stanley's Tiffin Box 2011\n",
      "My Grandfather's People 2011\n",
      "Marley & Me: The Puppy Years 2011\n",
      "Sharpay's Fabulous Adventure 2011\n",
      "Diary of a Wimpy Kid: Rodrick Rules 2011\n",
      "Mr. Popper's Penguins 2011\n",
      "The Muppets 2011\n",
      "Judy Moody and the Not Bummer Summer 2011\n",
      "Zookeeper 2011\n",
      "Happy Feet 2 2011\n",
      "Ein Tick anders 2011\n",
      "Anytime, Anywhere 2011\n",
      "Hoodwinked Too! Hood vs. Evil 2011\n",
      "We Bought a Zoo 2011\n",
      "The Chaperone 2011\n",
      "Gnomeo & Juliet 2011\n",
      "A Christmas Wish 2011\n",
      "A Princess for Christmas 2011\n",
      "Foster 2011\n",
      "My Granpa, the Bankrobber 2011\n",
      "Tooth Fairy 2010\n",
      "Hier kommt: Lola 2010\n",
      "Tangled 2010\n",
      "An Invisible Sign 2010\n",
      "Logan 2010\n",
      "Harriet the Spy: Blog Wars 2010\n",
      "Hèroes 2010\n",
      "Camp Rock 2: The Final Jam 2010\n",
      "Cancel Christmas 2010\n",
      "Nanny McPhee Returns 2010\n",
      "Ramona and Beezus 2010\n",
      "The Boy Who Cried Werewolf 2010\n",
      "Jack and the Beanstalk 2010\n",
      "Kooky 2010\n",
      "Khichdi: The Movie 2010\n",
      "You Should Meet My Son! 2010\n",
      "Furry Vengeance 2010\n",
      "Animals United 2010\n",
      "StarStruck 2010\n",
      "Diary of a Wimpy Kid 2010\n",
      "Despicable Me 2010\n",
      "The Spy Next Door 2010\n",
      "Gulliver's Travels 2010\n",
      "Marmaduke 2010\n",
      "Cats & Dogs: The Revenge of Kitty Galore 2010\n",
      "Alvin and the Chipmunks: The Squeakquel 2009\n",
      "Starring Maja 2009\n",
      "Looking for Jackie 2009\n",
      "Knerten 2009\n",
      "Hotel for Dogs 2009\n"
     ]
    }
   ],
   "source": [
    "import pymongo\n",
    "# Replace ###### with data from your connection URI from the Atlas UI\n",
    "mc = pymongo.MongoClient(\"mongodb+srv://hayounam:7S9eXETCpTW68ypX@cluster0.cxxyhrz.mongodb.net/?retryWrites=true&w=majority\")\n",
    "\n",
    "\n",
    "mflix = mc['sample_mflix']\n",
    "\n",
    "# find all movies between 2000 and 2020\n",
    "# uses $ and to filter for 2 genres!\n",
    "filters = { 'year': {'$gte': 2000, '$lt': 2020} , '$and':[ {'genres': 'Comedy' }, {'genres': 'Family' }]}\n",
    "projection = { \"title\": 1, \"year\": 1, \"_id\": 0 }\n",
    "\n",
    "# Sorts descending and limits to only 100 records\n",
    "for movie in mflix.movies.find(filters, projection).sort(\"year\", -1).limit(100) :\n",
    "     print(movie[\"title\"], movie[\"year\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0449bb9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
