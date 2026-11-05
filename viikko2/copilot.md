Viikolla 2 tehtävässä 9 kokeilin ensi kertaa Githubin Copilot -koodausagenttia.  
Koin koodin täydennyksen ehdotukset aika hyödyllisiksi, koodi vaikutti kyllä toimivalta. Esimerkiksi luodessa funktion koodi oli ymmärrettävää ja palautti oikeat asiat sekä yksikkötesteissä noudatti ohjeita siitä, ettei nettiä saa käyttää.  
Copilotin selitys Pylint-varoituksesta piti paikkansa!  
Kuten hieman jo aiemmin mainitsin, agentti teki siis kyllä toimivan ratkaisun ja testit. Luin ne läpi enkä löytänyt mitään korjattavaa. Kaiken pystyi hyväksymään heti.  
Mielestäni viime viikolla tehdyissä testeissä ei ollut paljoakaan eroa koodausagentin tekemiin. Stub oli tietenkin hieman erilainen, sillä en antanut sen muotoon sen erityisemmin ohjeita. Pelaajien nimet olivat vain "Player One" ja "player Two" jne. ja stubissa oli vain 3 pelaajaa, minkä ottaen huomioon voi kiistellä testien luotettavuudesta.  
Pylint ei löytänyt agentin koodista virheitä, mitkä olisivat estäneet committaamisen. Pylint antoi kylläkin koodille arvosanaksi vain 6.91/10, mutta huomautukset olivat enemmänkin luokkaa "src/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
". Ainoa virhe, joka minun piti korjata, oli liian pitkä rivin pituus mutta se oli itse materiaaleissa annettu docstring funktion selitykseksi.  
En sinänsä oppinut mitään uusia taitoja, mutta oli ihan kiinnostava nähdä miten koodausagentti toimii. Se avarsi hieman näkemystäni siitä, miten tällainen koodaaminen toimii esimerkiksi työpaikoilla.
