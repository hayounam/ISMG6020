{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "a4234899",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymongo\n",
    "\n",
    "# Replace XXXX with your connection URI from the Atlas UI\n",
    "mc = pymongo.MongoClient(\"mongodb+srv://hayounam:7S9eXETCpTW68ypX@cluster0.cxxyhrz.mongodb.net/?retryWrites=true&w=majority\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "d116549c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Newark Athlete 1891\n"
     ]
    }
   ],
   "source": [
    "projection = { \"title\": 1, \"year\": 1, \"_id\": 0 }\n",
    "for movie in movies.find({}, projection).sort(\"year\", 1).limit(1) :\n",
    "     print(movie['title'], movie[\"year\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab97fe69",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f16bdefb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7227ca63",
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
