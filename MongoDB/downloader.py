{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "2376dd6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import requests\n",
    "import pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "12b4b34c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://data.colorado.gov/resource/cjkq-q9ih.json?area=13&periodtype=1&indcode=624&%24order=periodyear+desc&%24limit=5\n",
      "{'stateabbrv': 'CO', 'statename': 'Colorado', 'stfips': '8', 'areaname': 'Boulder County', 'areatype': '4', 'areatyname': 'County', 'area': '13', 'periodyear': '2021', 'periodtype': '1', 'period': '0', 'pertypdesc': 'Annual', 'indcodty': '10', 'indcode': '624', 'codetitle': 'Social Assistance', 'ownership': '00', 'ownertitle': 'Aggregate of all types', 'prelim': '0', 'firms': '0', 'estab': '363', 'avgemp': '3814', 'mnth1emp': '0', 'mnth2emp': '0', 'mnth3emp': '0', 'topempav': '0', 'totwage': '125712588', 'avgwkwage': '634', 'taxwage': '0', 'contrib': '0', 'suppress': '0'}\n",
      "\n",
      "Count of Array: 5\n"
     ]
    }
   ],
   "source": [
    "URL =  \"https://data.colorado.gov/resource/cjkq-q9ih.json\"\n",
    "\n",
    "#parameters\n",
    "paramD = dict()\n",
    "paramD[\"area\"] = \"13\"    \n",
    "paramD[\"periodtype\"]=\"1\"\n",
    "paramD[\"indcode\"]=\"624\"\n",
    "#624, 811, 53\n",
    "paramD[\"$order\"] = \"periodyear desc\"\n",
    "paramD[\"$limit\"] = 5\n",
    "\n",
    "# open the URL \n",
    "document = requests.get(URL, paramD)\n",
    "print(document.request.url)\n",
    "\n",
    "js = document.json()\n",
    "        \n",
    "if document.status_code != 200 :\n",
    "     print(\"Error code=\",document.status_code, document.request.url)\n",
    "     js = json.loads(\"{}\")\n",
    "\n",
    "# Output first Record\n",
    "print (js[0])\n",
    "\n",
    "\n",
    "# JSON open and close\n",
    "files = open('social.txt', \"w\")\n",
    "files.write(json.dumps(js).strip())\n",
    "files.close()\n",
    "\n",
    "#Length\n",
    "length = len(js)\n",
    "print (\"\\nCount of Array:\", length)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "d9a790c6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e890383",
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
