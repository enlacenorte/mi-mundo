import json

# Full exhaustive database of all 177 TopoJSON features
# Every single country and territory with Flag, Capital, Continent, Independence/Founding, Population, Language, Distractors
ATLAS_177 = {
  "Afghanistan": {
    "flag": "🇦🇫", "isSovereign": True,
    "es": {"name": "Afganistán", "capital": "Kabul", "continent": "Asia", "indep": "1919 (19 de Agosto)", "pop": "41.1 Millones", "lang": "Pastún, Dari", "distractors": ["Kandahar", "Herat", "Mazar-i-Sharif"]},
    "en": {"name": "Afghanistan", "capital": "Kabul", "continent": "Asia", "indep": "1919 (August 19th)", "pop": "41.1 Million", "lang": "Pashto, Dari", "distractors": ["Kandahar", "Herat", "Mazar-i-Sharif"]}
  },
  "Albania": {
    "flag": "🇦🇱", "isSovereign": True,
    "es": {"name": "Albania", "capital": "Tirana", "continent": "Europa", "indep": "1912 (28 de Noviembre)", "pop": "2.8 Millones", "lang": "Albanés", "distractors": ["Durrës", "Vlorë", "Shkodër"]},
    "en": {"name": "Albania", "capital": "Tirana", "continent": "Europe", "indep": "1912 (November 28th)", "pop": "2.8 Million", "lang": "Albanian", "distractors": ["Durres", "Vlore", "Shkoder"]}
  },
  "Algeria": {
    "flag": "🇩🇿", "isSovereign": True,
    "es": {"name": "Argelia", "capital": "Argel", "continent": "África", "indep": "1962 (5 de Julio)", "pop": "44.9 Millones", "lang": "Árabe, Bereber", "distractors": ["Orán", "Constantina", "Annaba"]},
    "en": {"name": "Algeria", "capital": "Algiers", "continent": "Africa", "indep": "1962 (July 5th)", "pop": "44.9 Million", "lang": "Arabic, Berber", "distractors": ["Oran", "Constantine", "Annaba"]}
  },
  "Angola": {
    "flag": "🇦🇴", "isSovereign": True,
    "es": {"name": "Angola", "capital": "Luanda", "continent": "África", "indep": "1975 (11 de Noviembre)", "pop": "35.6 Millones", "lang": "Portugués", "distractors": ["Huambo", "Lobito", "Benguela"]},
    "en": {"name": "Angola", "capital": "Luanda", "continent": "Africa", "indep": "1975 (November 11th)", "pop": "35.6 Million", "lang": "Portuguese", "distractors": ["Huambo", "Lobito", "Benguela"]}
  },
  "Antarctica": {
    "flag": "🇦🇶", "isSovereign": False,
    "es": {"name": "Antártida", "capital": "Tratado Antártico", "continent": "Antártida", "indep": "Tratado Internacional (1959)", "pop": "1.000 - 5.000 Científicos", "lang": "Multilingüe", "distractors": ["Base Esperanza", "McMurdo", "Marambio"]},
    "en": {"name": "Antarctica", "capital": "Antarctic Treaty", "continent": "Antarctica", "indep": "International Treaty (1959)", "pop": "1,000 - 5,000 Scientists", "lang": "Multilingual", "distractors": ["Esperanza Base", "McMurdo", "Marambio"]}
  },
  "Argentina": {
    "flag": "🇦🇷", "isSovereign": True,
    "es": {"name": "Argentina", "capital": "Buenos Aires", "continent": "América del Sur", "indep": "1816 (9 de Julio)", "pop": "46.2 Millones", "lang": "Español", "distractors": ["Córdoba", "Rosario", "Mendoza"]},
    "en": {"name": "Argentina", "capital": "Buenos Aires", "continent": "South America", "indep": "1816 (July 9th)", "pop": "46.2 Million", "lang": "Spanish", "distractors": ["Cordoba", "Rosario", "Mendoza"]}
  },
  "Armenia": {
    "flag": "🇦🇲", "isSovereign": True,
    "es": {"name": "Armenia", "capital": "Ereván", "continent": "Asia / Europa", "indep": "1991 (21 de Septiembre)", "pop": "2.8 Millones", "lang": "Armenio", "distractors": ["Gyumri", "Vanadzor", "Dilijan"]},
    "en": {"name": "Armenia", "capital": "Yerevan", "continent": "Asia / Europe", "indep": "1991 (September 21st)", "pop": "2.8 Million", "lang": "Armenian", "distractors": ["Gyumri", "Vanadzor", "Dilijan"]}
  },
  "Australia": {
    "flag": "🇦🇺", "isSovereign": True,
    "es": {"name": "Australia", "capital": "Canberra", "continent": "Oceanía", "indep": "1901 (1 de Enero)", "pop": "26.5 Millones", "lang": "Inglés", "distractors": ["Sídney", "Melbourne", "Brisbane"]},
    "en": {"name": "Australia", "capital": "Canberra", "continent": "Oceania", "indep": "1901 (January 1st)", "pop": "26.5 Million", "lang": "English", "distractors": ["Sydney", "Melbourne", "Brisbane"]}
  },
  "Austria": {
    "flag": "🇦🇹", "isSovereign": True,
    "es": {"name": "Austria", "capital": "Viena", "continent": "Europa", "indep": "1156 / 1955", "pop": "9.1 Millones", "lang": "Alemán", "distractors": ["Salzburgo", "Innsbruck", "Graz"]},
    "en": {"name": "Austria", "capital": "Vienna", "continent": "Europe", "indep": "1156 / 1955", "pop": "9.1 Million", "lang": "German", "distractors": ["Salzburg", "Innsbruck", "Graz"]}
  },
  "Azerbaijan": {
    "flag": "🇦🇿", "isSovereign": True,
    "es": {"name": "Azerbaiyán", "capital": "Bakú", "continent": "Asia / Europa", "indep": "1991 (30 de Agosto)", "pop": "10.3 Millones", "lang": "Azerí", "distractors": ["Ganja", "Sumqayit", "Lankaran"]},
    "en": {"name": "Azerbaijan", "capital": "Baku", "continent": "Asia / Europe", "indep": "1991 (August 30th)", "pop": "10.3 Million", "lang": "Azerbaijani", "distractors": ["Ganja", "Sumqayit", "Lankaran"]}
  },
  "Bahamas": {
    "flag": "🇧🇸", "isSovereign": True,
    "es": {"name": "Bahamas", "capital": "Nasáu", "continent": "Caribe", "indep": "1973 (10 de Julio)", "pop": "410 Mil", "lang": "Inglés", "distractors": ["Freeport", "West End", "Marsh Harbour"]},
    "en": {"name": "Bahamas", "capital": "Nassau", "continent": "Caribbean", "indep": "1973 (July 10th)", "pop": "410 Thousand", "lang": "English", "distractors": ["Freeport", "West End", "Marsh Harbour"]}
  },
  "Bangladesh": {
    "flag": "🇧🇩", "isSovereign": True,
    "es": {"name": "Bangladés", "capital": "Daca", "continent": "Asia", "indep": "1971 (26 de Marzo)", "pop": "171.2 Millones", "lang": "Bengalí", "distractors": ["Chittagong", "Khulna", "Sylhet"]},
    "en": {"name": "Bangladesh", "capital": "Dhaka", "continent": "Asia", "indep": "1971 (March 26th)", "pop": "171.2 Million", "lang": "Bengali", "distractors": ["Chittagong", "Khulna", "Sylhet"]}
  },
  "Belarus": {
    "flag": "🇧🇾", "isSovereign": True,
    "es": {"name": "Bielorrusia", "capital": "Minsk", "continent": "Europa", "indep": "1991 (25 de Agosto)", "pop": "9.2 Millones", "lang": "Bielorruso, Ruso", "distractors": ["Brest", "Grodno", "Gómel"]},
    "en": {"name": "Belarus", "capital": "Minsk", "continent": "Europe", "indep": "1991 (August 25th)", "pop": "9.2 Million", "lang": "Belarusian, Russian", "distractors": ["Brest", "Grodno", "Gomel"]}
  },
  "Belgium": {
    "flag": "🇧🇪", "isSovereign": True,
    "es": {"name": "Bélgica", "capital": "Bruselas", "continent": "Europa", "indep": "1830 (4 de Octubre)", "pop": "11.7 Millones", "lang": "Neerlandés, Francés, Alemán", "distractors": ["Brujas", "Amberes", "Gante"]},
    "en": {"name": "Belgium", "capital": "Brussels", "continent": "Europe", "indep": "1830 (October 4th)", "pop": "11.7 Million", "lang": "Dutch, French, German", "distractors": ["Bruges", "Antwerp", "Ghent"]}
  },
  "Belize": {
    "flag": "🇧🇿", "isSovereign": True,
    "es": {"name": "Belice", "capital": "Belmopán", "continent": "América Central", "indep": "1981 (21 de Septiembre)", "pop": "405 Mil", "lang": "Inglés, Español", "distractors": ["Ciudad de Belice", "San Ignacio", "Orange Walk"]},
    "en": {"name": "Belize", "capital": "Belmopan", "continent": "Central America", "indep": "1981 (September 21st)", "pop": "405 Thousand", "lang": "English, Spanish", "distractors": ["Belize City", "San Ignacio", "Orange Walk"]}
  },
  "Benin": {
    "flag": "🇧🇯", "isSovereign": True,
    "es": {"name": "Benín", "capital": "Porto Novo", "continent": "África", "indep": "1960 (1 de Agosto)", "pop": "13.3 Millones", "lang": "Francés", "distractors": ["Cotonú", "Parakou", "Djougou"]},
    "en": {"name": "Benin", "capital": "Porto-Novo", "continent": "Africa", "indep": "1960 (August 1st)", "pop": "13.3 Million", "lang": "French", "distractors": ["Cotonou", "Parakou", "Djougou"]}
  },
  "Bhutan": {
    "flag": "🇧🇹", "isSovereign": True,
    "es": {"name": "Bután", "capital": "Timbu", "continent": "Asia", "indep": "1907 / 1949", "pop": "780 Mil", "lang": "Dzongkha", "distractors": ["Paro", "Punakha", "Phuntsholing"]},
    "en": {"name": "Bhutan", "capital": "Thimphu", "continent": "Asia", "indep": "1907 / 1949", "pop": "780 Thousand", "lang": "Dzongkha", "distractors": ["Paro", "Punakha", "Phuntsholing"]}
  },
  "Bolivia": {
    "flag": "🇧🇴", "isSovereign": True,
    "es": {"name": "Bolivia", "capital": "Sucre", "continent": "América del Sur", "indep": "1825 (6 de Agosto)", "pop": "12.2 Millones", "lang": "Español, Quechua, Aimara", "distractors": ["La Paz", "Santa Cruz", "Cochabamba"]},
    "en": {"name": "Bolivia", "capital": "Sucre", "continent": "South America", "indep": "1825 (August 6th)", "pop": "12.2 Million", "lang": "Spanish, Quechua, Aymara", "distractors": ["La Paz", "Santa Cruz", "Cochabamba"]}
  },
  "Bosnia and Herz.": {
    "flag": "🇧🇦", "isSovereign": True,
    "es": {"name": "Bosnia y Herzegovina", "capital": "Sarajevo", "continent": "Europa", "indep": "1992 (1 de Marzo)", "pop": "3.2 Millones", "lang": "Bosnio, Croata, Serbio", "distractors": ["Mostar", "Bania Luka", "Tuzla"]},
    "en": {"name": "Bosnia and Herzegovina", "capital": "Sarajevo", "continent": "Europe", "indep": "1992 (March 1st)", "pop": "3.2 Million", "lang": "Bosnian, Croatian, Serbian", "distractors": ["Mostar", "Banja Luka", "Tuzla"]}
  },
  "Botswana": {
    "flag": "🇧🇼", "isSovereign": True,
    "es": {"name": "Botsuana", "capital": "Gaborone", "continent": "África", "indep": "1966 (30 de Septiembre)", "pop": "2.6 Millones", "lang": "Inglés, Setsuana", "distractors": ["Francistown", "Maun", "Kasane"]},
    "en": {"name": "Botswana", "capital": "Gaborone", "continent": "Africa", "indep": "1966 (September 30th)", "pop": "2.6 Million", "lang": "English, Setswana", "distractors": ["Francistown", "Maun", "Kasane"]}
  },
  "Brazil": {
    "flag": "🇧🇷", "isSovereign": True,
    "es": {"name": "Brasil", "capital": "Brasilia", "continent": "América del Sur", "indep": "1822 (7 de Septiembre)", "pop": "215.3 Millones", "lang": "Portugués", "distractors": ["Río de Janeiro", "San Pablo", "Salvador"]},
    "en": {"name": "Brazil", "capital": "Brasilia", "continent": "South America", "indep": "1822 (September 7th)", "pop": "215.3 Million", "lang": "Portuguese", "distractors": ["Rio de Janeiro", "Sao Paulo", "Salvador"]}
  },
  "Brunei": {
    "flag": "🇧🇳", "isSovereign": True,
    "es": {"name": "Brunéi", "capital": "Bandar Seri Begawan", "continent": "Asia", "indep": "1984 (1 de Enero)", "pop": "450 Mil", "lang": "Malayo, Inglés", "distractors": ["Kuala Belait", "Seria", "Tutong"]},
    "en": {"name": "Brunei", "capital": "Bandar Seri Begawan", "continent": "Asia", "indep": "1984 (January 1st)", "pop": "450 Thousand", "lang": "Malay, English", "distractors": ["Kuala Belait", "Seria", "Tutong"]}
  },
  "Bulgaria": {
    "flag": "🇧🇬", "isSovereign": True,
    "es": {"name": "Bulgaria", "capital": "Sofía", "continent": "Europa", "indep": "1908 (22 de Septiembre)", "pop": "6.4 Millones", "lang": "Búlgaro", "distractors": ["Plovdiv", "Varna", "Burgas"]},
    "en": {"name": "Bulgaria", "capital": "Sofia", "continent": "Europe", "indep": "1908 (September 22nd)", "pop": "6.4 Million", "lang": "Bulgarian", "distractors": ["Plovdiv", "Varna", "Burgas"]}
  },
  "Burkina Faso": {
    "flag": "🇧🇫", "isSovereign": True,
    "es": {"name": "Burkina Faso", "capital": "Uagadugú", "continent": "África", "indep": "1960 (5 de Agosto)", "pop": "22.6 Millones", "lang": "Francés, Moré", "distractors": ["Bobo-Dioulasso", "Koudougou", "Banfora"]},
    "en": {"name": "Burkina Faso", "capital": "Ouagadougou", "continent": "Africa", "indep": "1960 (August 5th)", "pop": "22.6 Million", "lang": "French, Moore", "distractors": ["Bobo-Dioulasso", "Koudougou", "Banfora"]}
  },
  "Burundi": {
    "flag": "🇧🇮", "isSovereign": True,
    "es": {"name": "Burundi", "capital": "Gitega", "continent": "África", "indep": "1962 (1 de Julio)", "pop": "12.8 Millones", "lang": "Kirundi, Francés", "distractors": ["Buyumbura", "Ngozi", "Rumonge"]},
    "en": {"name": "Burundi", "capital": "Gitega", "continent": "Africa", "indep": "1962 (July 1st)", "pop": "12.8 Million", "lang": "Kirundi, French", "distractors": ["Bujumbura", "Ngozi", "Rumonge"]}
  },
  "Cambodia": {
    "flag": "🇰🇭", "isSovereign": True,
    "es": {"name": "Camboya", "capital": "Nom Pen", "continent": "Asia", "indep": "1953 (9 de Noviembre)", "pop": "16.7 Millones", "lang": "Jemer", "distractors": ["Siem Reap", "Battambang", "Sihanoukville"]},
    "en": {"name": "Cambodia", "capital": "Phnom Penh", "continent": "Asia", "indep": "1953 (November 9th)", "pop": "16.7 Million", "lang": "Khmer", "distractors": ["Siem Reap", "Battambang", "Sihanoukville"]}
  },
  "Cameroon": {
    "flag": "🇨🇲", "isSovereign": True,
    "es": {"name": "Camerún", "capital": "Yaundé", "continent": "África", "indep": "1960 (1 de Enero)", "pop": "27.9 Millones", "lang": "Francés, Inglés", "distractors": ["Duala", "Garua", "Bamenda"]},
    "en": {"name": "Cameroon", "capital": "Yaounde", "continent": "Africa", "indep": "1960 (January 1st)", "pop": "27.9 Million", "lang": "French, English", "distractors": ["Douala", "Garoua", "Bamenda"]}
  },
  "Canada": {
    "flag": "🇨🇦", "isSovereign": True,
    "es": {"name": "Canadá", "capital": "Ottawa", "continent": "América del Norte", "indep": "1867 (1 de Julio)", "pop": "39.5 Millones", "lang": "Inglés, Francés", "distractors": ["Toronto", "Montreal", "Vancouver"]},
    "en": {"name": "Canada", "capital": "Ottawa", "continent": "North America", "indep": "1867 (July 1st)", "pop": "39.5 Million", "lang": "English, French", "distractors": ["Toronto", "Montreal", "Vancouver"]}
  },
  "Central African Rep.": {
    "flag": "🇨🇫", "isSovereign": True,
    "es": {"name": "República Centroafricana", "capital": "Bangui", "continent": "África", "indep": "1960 (13 de Agosto)", "pop": "5.5 Millones", "lang": "Sango, Francés", "distractors": ["Bimbo", "Berbérati", "Carnot"]},
    "en": {"name": "Central African Republic", "capital": "Bangui", "continent": "Africa", "indep": "1960 (August 13th)", "pop": "5.5 Million", "lang": "Sango, French", "distractors": ["Bimbo", "Berberati", "Carnot"]}
  },
  "Chad": {
    "flag": "🇹🇩", "isSovereign": True,
    "es": {"name": "Chad", "capital": "Yamena", "continent": "África", "indep": "1960 (11 de Agosto)", "pop": "17.7 Millones", "lang": "Árabe, Francés", "distractors": ["Moundou", "Sarh", "Abéché"]},
    "en": {"name": "Chad", "capital": "N'Djamena", "continent": "Africa", "indep": "1960 (August 11th)", "pop": "17.7 Million", "lang": "Arabic, French", "distractors": ["Moundou", "Sarh", "Abeche"]}
  },
  "Chile": {
    "flag": "🇨🇱", "isSovereign": True,
    "es": {"name": "Chile", "capital": "Santiago", "continent": "América del Sur", "indep": "1818 (12 de Febrero)", "pop": "19.5 Millones", "lang": "Español", "distractors": ["Valparaíso", "Concepción", "Antofagasta"]},
    "en": {"name": "Chile", "capital": "Santiago", "continent": "South America", "indep": "1818 (February 12th)", "pop": "19.5 Million", "lang": "Spanish", "distractors": ["Valparaiso", "Concepcion", "Antofagasta"]}
  },
  "China": {
    "flag": "🇨🇳", "isSovereign": True,
    "es": {"name": "China", "capital": "Pekín (Beijing)", "continent": "Asia", "indep": "221 a.C. / 1949", "pop": "1.41 Mil Millones", "lang": "Mandarín", "distractors": ["Shanghái", "Cantón", "Shenzhen"]},
    "en": {"name": "China", "capital": "Beijing", "continent": "Asia", "indep": "221 BC / 1949", "pop": "1.41 Billion", "lang": "Mandarin", "distractors": ["Shanghai", "Guangzhou", "Shenzhen"]}
  },
  "Colombia": {
    "flag": "🇨🇴", "isSovereign": True,
    "es": {"name": "Colombia", "capital": "Bogotá", "continent": "América del Sur", "indep": "1810 (20 de Julio)", "pop": "52.1 Millones", "lang": "Español", "distractors": ["Medellín", "Cali", "Barranquilla"]},
    "en": {"name": "Colombia", "capital": "Bogota", "continent": "South America", "indep": "1810 (July 20th)", "pop": "52.1 Million", "lang": "Spanish", "distractors": ["Medellin", "Cali", "Barranquilla"]}
  },
  "Congo": {
    "flag": "🇨🇬", "isSovereign": True,
    "es": {"name": "República del Congo", "capital": "Brazzaville", "continent": "África", "indep": "1960 (15 de Agosto)", "pop": "5.9 Millones", "lang": "Francés, Lingala", "distractors": ["Pointe-Noire", "Dolisie", "Nkayi"]},
    "en": {"name": "Republic of the Congo", "capital": "Brazzaville", "continent": "Africa", "indep": "1960 (August 15th)", "pop": "5.9 Million", "lang": "French, Lingala", "distractors": ["Pointe-Noire", "Dolisie", "Nkayi"]}
  },
  "Costa Rica": {
    "flag": "🇨🇷", "isSovereign": True,
    "es": {"name": "Costa Rica", "capital": "San José", "continent": "América Central", "indep": "1821 (15 de Septiembre)", "pop": "5.2 Millones", "lang": "Español", "distractors": ["Alajuela", "Cartago", "Heredia"]},
    "en": {"name": "Costa Rica", "capital": "San Jose", "continent": "Central America", "indep": "1821 (September 15th)", "pop": "5.2 Million", "lang": "Spanish", "distractors": ["Alajuela", "Cartago", "Heredia"]}
  },
  "Croatia": {
    "flag": "🇭🇷", "isSovereign": True,
    "es": {"name": "Croacia", "capital": "Zagreb", "continent": "Europa", "indep": "1991 (25 de Junio)", "pop": "3.8 Millones", "lang": "Croata", "distractors": ["Split", "Dubrovnik", "Rijeka"]},
    "en": {"name": "Croatia", "capital": "Zagreb", "continent": "Europe", "indep": "1991 (June 25th)", "pop": "3.8 Million", "lang": "Croatian", "distractors": ["Split", "Dubrovnik", "Rijeka"]}
  },
  "Cuba": {
    "flag": "🇨🇺", "isSovereign": True,
    "es": {"name": "Cuba", "capital": "La Habana", "continent": "Caribe", "indep": "1902 (20 de Mayo)", "pop": "11.2 Millones", "lang": "Español", "distractors": ["Santiago de Cuba", "Varadero", "Camagüey"]},
    "en": {"name": "Cuba", "capital": "Havana", "continent": "Caribbean", "indep": "1902 (May 20th)", "pop": "11.2 Million", "lang": "Spanish", "distractors": ["Santiago de Cuba", "Varadero", "Camaguey"]}
  },
  "Cyprus": {
    "flag": "🇨🇾", "isSovereign": True,
    "es": {"name": "Chipre", "capital": "Nicosia", "continent": "Europa / Asia", "indep": "1960 (16 de Agosto)", "pop": "1.2 Millones", "lang": "Griego, Turco", "distractors": ["Limasol", "Lárnaca", "Pafos"]},
    "en": {"name": "Cyprus", "capital": "Nicosia", "continent": "Europe / Asia", "indep": "1960 (August 16th)", "pop": "1.2 Million", "lang": "Greek, Turkish", "distractors": ["Limassol", "Larnaca", "Paphos"]}
  },
  "Czechia": {
    "flag": "🇨🇿", "isSovereign": True,
    "es": {"name": "República Checa", "capital": "Praga", "continent": "Europa", "indep": "1993 (1 de Enero)", "pop": "10.8 Millones", "lang": "Checo", "distractors": ["Brno", "Ostrava", "Plzen"]},
    "en": {"name": "Czech Republic", "capital": "Prague", "continent": "Europe", "indep": "1993 (January 1st)", "pop": "10.8 Million", "lang": "Czech", "distractors": ["Brno", "Ostrava", "Plzen"]}
  },
  "Côte d'Ivoire": {
    "flag": "🇨🇮", "isSovereign": True,
    "es": {"name": "Costa de Marfil", "capital": "Yamusukro", "continent": "África", "indep": "1960 (7 de Agosto)", "pop": "28.1 Millones", "lang": "Francés", "distractors": ["Abiyán", "Bouaké", "San-Pédro"]},
    "en": {"name": "Ivory Coast", "capital": "Yamoussoukro", "continent": "Africa", "indep": "1960 (August 7th)", "pop": "28.1 Million", "lang": "French", "distractors": ["Abidjan", "Bouake", "San-Pedro"]}
  },
  "Dem. Rep. Congo": {
    "flag": "🇨🇩", "isSovereign": True,
    "es": {"name": "R.D. del Congo", "capital": "Kinsasa", "continent": "África", "indep": "1960 (30 de Junio)", "pop": "99.0 Millones", "lang": "Francés, Lingala", "distractors": ["Lubumbashi", "Goma", "Kisangani"]},
    "en": {"name": "DR Congo", "capital": "Kinshasa", "continent": "Africa", "indep": "1960 (June 30th)", "pop": "99.0 Million", "lang": "French, Lingala", "distractors": ["Lubumbashi", "Goma", "Kisangani"]}
  },
  "Denmark": {
    "flag": "🇩🇰", "isSovereign": True,
    "es": {"name": "Dinamarca", "capital": "Copenhague", "continent": "Europa", "indep": "Siglo X", "pop": "5.9 Millones", "lang": "Danés", "distractors": ["Aarhus", "Odense", "Aalborg"]},
    "en": {"name": "Denmark", "capital": "Copenhagen", "continent": "Europe", "indep": "10th Century", "pop": "5.9 Million", "lang": "Danish", "distractors": ["Aarhus", "Odense", "Aalborg"]}
  },
  "Djibouti": {
    "flag": "🇩🇯", "isSovereign": True,
    "es": {"name": "Yibuti", "capital": "Yibuti", "continent": "África", "indep": "1977 (27 de Junio)", "pop": "1.1 Millones", "lang": "Árabe, Francés", "distractors": ["Ali Sabieh", "Tadjoura", "Obock"]},
    "en": {"name": "Djibouti", "capital": "Djibouti City", "continent": "Africa", "indep": "1977 (June 27th)", "pop": "1.1 Million", "lang": "Arabic, French", "distractors": ["Ali Sabieh", "Tadjoura", "Obock"]}
  },
  "Dominican Rep.": {
    "flag": "🇩🇴", "isSovereign": True,
    "es": {"name": "República Dominicana", "capital": "Santo Domingo", "continent": "Caribe", "indep": "1844 (27 de Febrero)", "pop": "11.1 Millones", "lang": "Español", "distractors": ["Santiago", "Punta Cana", "La Romana"]},
    "en": {"name": "Dominican Republic", "capital": "Santo Domingo", "continent": "Caribbean", "indep": "1844 (February 27th)", "pop": "11.1 Million", "lang": "Spanish", "distractors": ["Santiago", "Punta Cana", "La Romana"]}
  },
  "Ecuador": {
    "flag": "🇪🇨", "isSovereign": True,
    "es": {"name": "Ecuador", "capital": "Quito", "continent": "América del Sur", "indep": "1809 (10 de Agosto)", "pop": "18.0 Millones", "lang": "Español, Kichwa", "distractors": ["Guayaquil", "Cuenca", "Manta"]},
    "en": {"name": "Ecuador", "capital": "Quito", "continent": "South America", "indep": "1809 (August 10th)", "pop": "18.0 Million", "lang": "Spanish, Kichwa", "distractors": ["Guayaquil", "Cuenca", "Manta"]}
  },
  "Egypt": {
    "flag": "🇪🇬", "isSovereign": True,
    "es": {"name": "Egipto", "capital": "El Cairo", "continent": "África", "indep": "3100 a.C. / 1922", "pop": "111 Millones", "lang": "Árabe", "distractors": ["Alejandría", "Guiza", "Lúxor"]},
    "en": {"name": "Egypt", "capital": "Cairo", "continent": "Africa", "indep": "3100 BC / 1922", "pop": "111 Million", "lang": "Arabic", "distractors": ["Alexandria", "Giza", "Luxor"]}
  },
  "El Salvador": {
    "flag": "🇸🇻", "isSovereign": True,
    "es": {"name": "El Salvador", "capital": "San Salvador", "continent": "América Central", "indep": "1821 (15 de Septiembre)", "pop": "6.3 Millones", "lang": "Español", "distractors": ["Santa Ana", "San Miguel", "Sonsonate"]},
    "en": {"name": "El Salvador", "capital": "San Salvador", "continent": "Central America", "indep": "1821 (September 15th)", "pop": "6.3 Million", "lang": "Spanish", "distractors": ["Santa Ana", "San Miguel", "Sonsonate"]}
  },
  "Eq. Guinea": {
    "flag": "🇬🇶", "isSovereign": True,
    "es": {"name": "Guinea Ecuatorial", "capital": "Malabo", "continent": "África", "indep": "1968 (12 de Octubre)", "pop": "1.6 Millones", "lang": "Español, Francés", "distractors": ["Bata", "Ciudad de la Paz", "Ebebiyín"]},
    "en": {"name": "Equatorial Guinea", "capital": "Malabo", "continent": "Africa", "indep": "1968 (October 12th)", "pop": "1.6 Million", "lang": "Spanish, French", "distractors": ["Bata", "Ciudad de la Paz", "Ebebiyin"]}
  },
  "Eritrea": {
    "flag": "🇪🇷", "isSovereign": True,
    "es": {"name": "Eritrea", "capital": "Asmara", "continent": "África", "indep": "1993 (24 de Mayo)", "pop": "3.6 Millones", "lang": "Tigriña, Árabe, Inglés", "distractors": ["Keren", "Massawa", "Assab"]},
    "en": {"name": "Eritrea", "capital": "Asmara", "continent": "Africa", "indep": "1993 (May 24th)", "pop": "3.6 Million", "lang": "Tigrinya, Arabic, English", "distractors": ["Keren", "Massawa", "Assab"]}
  },
  "Estonia": {
    "flag": "🇪🇪", "isSovereign": True,
    "es": {"name": "Estonia", "capital": "Tallin", "continent": "Europa", "indep": "1918 / 1991", "pop": "1.3 Millones", "lang": "Estonio", "distractors": ["Tartu", "Narva", "Pärnu"]},
    "en": {"name": "Estonia", "capital": "Tallinn", "continent": "Europe", "indep": "1918 / 1991", "pop": "1.3 Million", "lang": "Estonian", "distractors": ["Tartu", "Narva", "Parnu"]}
  },
  "Ethiopia": {
    "flag": "🇪🇹", "isSovereign": True,
    "es": {"name": "Etiopía", "capital": "Adís Abeba", "continent": "África", "indep": "Estado Milenario", "pop": "123.4 Millones", "lang": "Amhárico", "distractors": ["Dire Dawa", "Gondar", "Mekele"]},
    "en": {"name": "Ethiopia", "capital": "Addis Ababa", "continent": "Africa", "indep": "Ancient Empire", "pop": "123.4 Million", "lang": "Amharic", "distractors": ["Dire Dawa", "Gondar", "Mekelle"]}
  },
  "Falkland Is.": {
    "flag": "🇦🇷", "isSovereign": False,
    "es": {"name": "Islas Malvinas (Argentina)", "capital": "Puerto Argentino", "continent": "América del Sur", "indep": "Territorio Nacional Argentino", "pop": "3.500 Hab.", "lang": "Español", "distractors": ["Puerto Deseado", "Río Gallegos", "Ushuaia"]},
    "en": {"name": "Islas Malvinas (Argentina)", "capital": "Puerto Argentino (Stanley)", "continent": "South America", "indep": "Argentine National Territory", "pop": "3,500 Inh.", "lang": "Spanish, English", "distractors": ["Puerto Deseado", "Rio Gallegos", "Ushuaia"]}
  },
  "Fiji": {
    "flag": "🇫🇯", "isSovereign": True,
    "es": {"name": "Fiyi", "capital": "Suva", "continent": "Oceanía", "indep": "1970 (10 de Octubre)", "pop": "930 Mil", "lang": "Inglés, Fiyiano", "distractors": ["Nadi", "Lautoka", "Labasa"]},
    "en": {"name": "Fiji", "capital": "Suva", "continent": "Oceania", "indep": "1970 (October 10th)", "pop": "930 Thousand", "lang": "English, Fijian", "distractors": ["Nadi", "Lautoka", "Labasa"]}
  },
  "Finland": {
    "flag": "🇫🇮", "isSovereign": True,
    "es": {"name": "Finlandia", "capital": "Helsinki", "continent": "Europa", "indep": "1917 (6 de Diciembre)", "pop": "5.6 Millones", "lang": "Finés, Sueco", "distractors": ["Espoo", "Tampere", "Turku"]},
    "en": {"name": "Finland", "capital": "Helsinki", "continent": "Europe", "indep": "1917 (December 6th)", "pop": "5.6 Million", "lang": "Finnish, Swedish", "distractors": ["Espoo", "Tampere", "Turku"]}
  },
  "Fr. S. Antarctic Lands": {
    "flag": "🇹🇫", "isSovereign": False,
    "es": {"name": "Tierras Australes Francesas", "capital": "Port-aux-Français", "continent": "Océano Índico / Antártida", "indep": "Territorio de Ultramar (Francia)", "pop": "150 Investigadores", "lang": "Francés", "distractors": ["Kerguelen", "Crozet", "Saint-Paul"]},
    "en": {"name": "French Southern Lands", "capital": "Port-aux-Francais", "continent": "Indian Ocean / Antarctica", "indep": "Overseas Territory (France)", "pop": "150 Researchers", "lang": "French", "distractors": ["Kerguelen", "Crozet", "Saint-Paul"]}
  },
  "France": {
    "flag": "🇫🇷", "isSovereign": True,
    "es": {"name": "Francia", "capital": "París", "continent": "Europa", "indep": "843 (Tratado de Verdún)", "pop": "68.0 Millones", "lang": "Francés", "distractors": ["Marsella", "Lyon", "Niza"]},
    "en": {"name": "France", "capital": "Paris", "continent": "Europe", "indep": "843 (Treaty of Verdun)", "pop": "68.0 Million", "lang": "French", "distractors": ["Marseille", "Lyon", "Nice"]}
  },
  "Gabon": {
    "flag": "🇬🇦", "isSovereign": True,
    "es": {"name": "Gabón", "capital": "Libreville", "continent": "África", "indep": "1960 (17 de Agosto)", "pop": "2.4 Millones", "lang": "Francés", "distractors": ["Port-Gentil", "Franceville", "Oyem"]},
    "en": {"name": "Gabon", "capital": "Libreville", "continent": "Africa", "indep": "1960 (August 17th)", "pop": "2.4 Million", "lang": "French", "distractors": ["Port-Gentil", "Franceville", "Oyem"]}
  },
  "Gambia": {
    "flag": "🇬🇲", "isSovereign": True,
    "es": {"name": "Gambia", "capital": "Banjul", "continent": "África", "indep": "1965 (18 de Febrero)", "pop": "2.7 Millones", "lang": "Inglés", "distractors": ["Serekunda", "Brikama", "Bakau"]},
    "en": {"name": "Gambia", "capital": "Banjul", "continent": "Africa", "indep": "1965 (February 18th)", "pop": "2.7 Million", "lang": "English", "distractors": ["Serekunda", "Brikama", "Bakau"]}
  },
  "Georgia": {
    "flag": "🇬🇪", "isSovereign": True,
    "es": {"name": "Georgia", "capital": "Tiflis", "continent": "Europa / Asia", "indep": "1991 (9 de Abril)", "pop": "3.7 Millones", "lang": "Georgiano", "distractors": ["Batumi", "Kutaisi", "Rustavi"]},
    "en": {"name": "Georgia", "capital": "Tbilisi", "continent": "Europe / Asia", "indep": "1991 (April 9th)", "pop": "3.7 Million", "lang": "Georgian", "distractors": ["Batumi", "Kutaisi", "Rustavi"]}
  },
  "Germany": {
    "flag": "🇩🇪", "isSovereign": True,
    "es": {"name": "Alemania", "capital": "Berlín", "continent": "Europa", "indep": "1871 (Imperio Alemán)", "pop": "84.4 Millones", "lang": "Alemán", "distractors": ["Múnich", "Fráncfort", "Hamburgo"]},
    "en": {"name": "Germany", "capital": "Berlin", "continent": "Europe", "indep": "1871 (German Empire)", "pop": "84.4 Million", "lang": "German", "distractors": ["Munich", "Frankfurt", "Hamburg"]}
  },
  "Ghana": {
    "flag": "🇬🇭", "isSovereign": True,
    "es": {"name": "Ghana", "capital": "Acra", "continent": "África", "indep": "1957 (6 de Marzo)", "pop": "33.5 Millones", "lang": "Inglés", "distractors": ["Kumasi", "Tamale", "Sekondi-Takoradi"]},
    "en": {"name": "Ghana", "capital": "Accra", "continent": "Africa", "indep": "1957 (March 6th)", "pop": "33.5 Million", "lang": "English", "distractors": ["Kumasi", "Tamale", "Sekondi-Takoradi"]}
  },
  "Greece": {
    "flag": "🇬🇷", "isSovereign": True,
    "es": {"name": "Grecia", "capital": "Atenas", "continent": "Europa", "indep": "1821 (Revolución Griega)", "pop": "10.4 Millones", "lang": "Griego", "distractors": ["Salónica", "Patras", "Heraclión"]},
    "en": {"name": "Greece", "capital": "Athens", "continent": "Europe", "indep": "1821 (Greek Revolution)", "pop": "10.4 Million", "lang": "Greek", "distractors": ["Thessaloniki", "Patras", "Heraklion"]}
  },
  "Greenland": {
    "flag": "🇬🇱", "isSovereign": False,
    "es": {"name": "Groenlandia", "capital": "Nuuk", "continent": "América del Norte", "indep": "Territorio Autónomo (Dinamarca)", "pop": "56 Mil", "lang": "Groenlandés, Danés", "distractors": ["Ilulissat", "Sisimiut", "Qaqortoq"]},
    "en": {"name": "Greenland", "capital": "Nuuk", "continent": "North America", "indep": "Autonomous Territory (Denmark)", "pop": "56 Thousand", "lang": "Greenlandic, Danish", "distractors": ["Ilulissat", "Sisimiut", "Qaqortoq"]}
  },
  "Guatemala": {
    "flag": "🇬🇹", "isSovereign": True,
    "es": {"name": "Guatemala", "capital": "Ciudad de Guatemala", "continent": "América Central", "indep": "1821 (15 de Septiembre)", "pop": "18.6 Millones", "lang": "Español", "distractors": ["Antigua", "Quetzaltenango", "Escuintla"]},
    "en": {"name": "Guatemala", "capital": "Guatemala City", "continent": "Central America", "indep": "1821 (September 15th)", "pop": "18.6 Million", "lang": "Spanish", "distractors": ["Antigua", "Quetzaltenango", "Escuintla"]}
  },
  "Guinea": {
    "flag": "🇬🇳", "isSovereign": True,
    "es": {"name": "Guinea", "capital": "Conakri", "continent": "África", "indep": "1958 (2 de Octubre)", "pop": "13.9 Millones", "lang": "Francés", "distractors": ["Nzérékoré", "Kankan", "Kindia"]},
    "en": {"name": "Guinea", "capital": "Conakry", "continent": "Africa", "indep": "1958 (October 2nd)", "pop": "13.9 Million", "lang": "French", "distractors": ["Nzerekore", "Kankan", "Kindia"]}
  },
  "Guinea-Bissau": {
    "flag": "🇬🇼", "isSovereign": True,
    "es": {"name": "Guinea-Bisáu", "capital": "Bisáu", "continent": "África", "indep": "1973 (24 de Septiembre)", "pop": "2.1 Millones", "lang": "Portugués", "distractors": ["Bafatá", "Gabú", "Canchungo"]},
    "en": {"name": "Guinea-Bissau", "capital": "Bissau", "continent": "Africa", "indep": "1973 (September 24th)", "pop": "2.1 Million", "lang": "Portuguese", "distractors": ["Bafata", "Gabu", "Canchungo"]}
  },
  "Guyana": {
    "flag": "🇬🇾", "isSovereign": True,
    "es": {"name": "Guyana", "capital": "Georgetown", "continent": "América del Sur", "indep": "1966 (26 de Mayo)", "pop": "800 Mil", "lang": "Inglés", "distractors": ["Linden", "New Amsterdam", "Bartica"]},
    "en": {"name": "Guyana", "capital": "Georgetown", "continent": "South America", "indep": "1966 (May 26th)", "pop": "800 Thousand", "lang": "English", "distractors": ["Linden", "New Amsterdam", "Bartica"]}
  },
  "Haiti": {
    "flag": "🇭🇹", "isSovereign": True,
    "es": {"name": "Haití", "capital": "Puerto Príncipe", "continent": "Caribe", "indep": "1804 (1 de Enero)", "pop": "11.5 Millones", "lang": "Francés, Criollo", "distractors": ["Cabo Haitiano", "Gonaïves", "Les Cayes"]},
    "en": {"name": "Haiti", "capital": "Port-au-Prince", "continent": "Caribbean", "indep": "1804 (January 1st)", "pop": "11.5 Million", "lang": "French, Creole", "distractors": ["Cap-Haitien", "Gonaives", "Les Cayes"]}
  },
  "Honduras": {
    "flag": "🇭🇳", "isSovereign": True,
    "es": {"name": "Honduras", "capital": "Tegucigalpa", "continent": "América Central", "indep": "1821 (15 de Septiembre)", "pop": "10.4 Millones", "lang": "Español", "distractors": ["San Pedro Sula", "La Ceiba", "Choloma"]},
    "en": {"name": "Honduras", "capital": "Tegucigalpa", "continent": "Central America", "indep": "1821 (September 15th)", "pop": "10.4 Million", "lang": "Spanish", "distractors": ["San Pedro Sula", "La Ceiba", "Choloma"]}
  },
  "Hungary": {
    "flag": "🇭🇺", "isSovereign": True,
    "es": {"name": "Hungría", "capital": "Budapest", "continent": "Europa", "indep": "895 / 1000", "pop": "9.7 Millones", "lang": "Húngaro", "distractors": ["Debrecen", "Szeged", "Miskolc"]},
    "en": {"name": "Hungary", "capital": "Budapest", "continent": "Europe", "indep": "895 / 1000", "pop": "9.7 Million", "lang": "Hungarian", "distractors": ["Debrecen", "Szeged", "Miskolc"]}
  },
  "Iceland": {
    "flag": "🇮🇸", "isSovereign": True,
    "es": {"name": "Islandia", "capital": "Reikiavik", "continent": "Europa", "indep": "1944 (17 de Junio)", "pop": "390 Mil", "lang": "Islandés", "distractors": ["Akureyri", "Keflavík", "Hafnarfjörður"]},
    "en": {"name": "Iceland", "capital": "Reykjavik", "continent": "Europe", "indep": "1944 (June 17th)", "pop": "390 Thousand", "lang": "Icelandic", "distractors": ["Akureyri", "Keflavik", "Hafnarfjordur"]}
  },
  "India": {
    "flag": "🇮🇳", "isSovereign": True,
    "es": {"name": "India", "capital": "Nueva Delhi", "continent": "Asia", "indep": "1947 (15 de Agosto)", "pop": "1.43 Mil Millones", "lang": "Hindi, Inglés", "distractors": ["Bombay (Mumbai)", "Calcuta", "Bangalore"]},
    "en": {"name": "India", "capital": "New Delhi", "continent": "Asia", "indep": "1947 (August 15th)", "pop": "1.43 Billion", "lang": "Hindi, English", "distractors": ["Mumbai", "Kolkata", "Bangalore"]}
  },
  "Indonesia": {
    "flag": "🇮🇩", "isSovereign": True,
    "es": {"name": "Indonesia", "capital": "Yakarta", "continent": "Asia / Oceanía", "indep": "1945 (17 de Agosto)", "pop": "277.5 Millones", "lang": "Indonesio", "distractors": ["Surabaya", "Bandung", "Medan"]},
    "en": {"name": "Indonesia", "capital": "Jakarta", "continent": "Asia / Oceania", "indep": "1945 (August 17th)", "pop": "277.5 Million", "lang": "Indonesian", "distractors": ["Surabaya", "Bandung", "Medan"]}
  },
  "Iran": {
    "flag": "🇮🇷", "isSovereign": True,
    "es": {"name": "Irán", "capital": "Teherán", "continent": "Asia", "indep": "550 a.C. / 1979", "pop": "88.5 Millones", "lang": "Persa (Farsi)", "distractors": ["Isfahán", "Mashhad", "Shiraz"]},
    "en": {"name": "Iran", "capital": "Tehran", "continent": "Asia", "indep": "550 BC / 1979", "pop": "88.5 Million", "lang": "Persian (Farsi)", "distractors": ["Isfahan", "Mashhad", "Shiraz"]}
  },
  "Iraq": {
    "flag": "🇮🇶", "isSovereign": True,
    "es": {"name": "Irak", "capital": "Bagdad", "continent": "Asia", "indep": "1932 (3 de Octubre)", "pop": "44.5 Millones", "lang": "Árabe, Kurdo", "distractors": ["Basora", "Mosul", "Erbil"]},
    "en": {"name": "Iraq", "capital": "Baghdad", "continent": "Asia", "indep": "1932 (October 3rd)", "pop": "44.5 Million", "lang": "Arabic, Kurdish", "distractors": ["Basra", "Mosul", "Erbil"]}
  },
  "Ireland": {
    "flag": "🇮🇪", "isSovereign": True,
    "es": {"name": "Irlanda", "capital": "Dublín", "continent": "Europa", "indep": "1922 (6 de Diciembre)", "pop": "5.1 Millones", "lang": "Inglés, Irlandés", "distractors": ["Cork", "Galway", "Limerick"]},
    "en": {"name": "Ireland", "capital": "Dublin", "continent": "Europe", "indep": "1922 (December 6th)", "pop": "5.1 Million", "lang": "English, Irish", "distractors": ["Cork", "Galway", "Limerick"]}
  },
  "Israel": {
    "flag": "🇮🇱", "isSovereign": True,
    "es": {"name": "Israel", "capital": "Jerusalén", "continent": "Asia", "indep": "1948 (14 de Mayo)", "pop": "9.8 Millones", "lang": "Hebreo, Árabe", "distractors": ["Tel Aviv", "Haifa", "Beerseba"]},
    "en": {"name": "Israel", "capital": "Jerusalem", "continent": "Asia", "indep": "1948 (May 14th)", "pop": "9.8 Million", "lang": "Hebrew, Arabic", "distractors": ["Tel Aviv", "Haifa", "Beersheba"]}
  },
  "Italy": {
    "flag": "🇮🇹", "isSovereign": True,
    "es": {"name": "Italia", "capital": "Roma", "continent": "Europa", "indep": "1861 (Unificación)", "pop": "58.9 Millones", "lang": "Italiano", "distractors": ["Milán", "Nápoles", "Florencia"]},
    "en": {"name": "Italy", "capital": "Rome", "continent": "Europe", "indep": "1861 (Unification)", "pop": "58.9 Million", "lang": "Italian", "distractors": ["Milan", "Naples", "Florence"]}
  },
  "Jamaica": {
    "flag": "🇯🇲", "isSovereign": True,
    "es": {"name": "Jamaica", "capital": "Kingston", "continent": "Caribe", "indep": "1962 (6 de Agosto)", "pop": "2.8 Millones", "lang": "Inglés", "distractors": ["Montego Bay", "Spanish Town", "Portmore"]},
    "en": {"name": "Jamaica", "capital": "Kingston", "continent": "Caribbean", "indep": "1962 (August 6th)", "pop": "2.8 Million", "lang": "English", "distractors": ["Montego Bay", "Spanish Town", "Portmore"]}
  },
  "Japan": {
    "flag": "🇯🇵", "isSovereign": True,
    "es": {"name": "Japón", "capital": "Tokio", "continent": "Asia", "indep": "660 a.C.", "pop": "124.5 Millones", "lang": "Japonés", "distractors": ["Kioto", "Osaka", "Yokohama"]},
    "en": {"name": "Japan", "capital": "Tokyo", "continent": "Asia", "indep": "660 BC", "pop": "124.5 Million", "lang": "Japanese", "distractors": ["Kyoto", "Osaka", "Yokohama"]}
  },
  "Jordan": {
    "flag": "🇯🇴", "isSovereign": True,
    "es": {"name": "Jordania", "capital": "Amán", "continent": "Asia", "indep": "1946 (25 de Mayo)", "pop": "11.3 Millones", "lang": "Árabe", "distractors": ["Zarqa", "Irbid", "Áqaba"]},
    "en": {"name": "Jordan", "capital": "Amman", "continent": "Asia", "indep": "1946 (May 25th)", "pop": "11.3 Million", "lang": "Arabic", "distractors": ["Zarqa", "Irbid", "Aqaba"]}
  },
  "Kazakhstan": {
    "flag": "🇰🇿", "isSovereign": True,
    "es": {"name": "Kazajistán", "capital": "Astaná", "continent": "Asia / Europa", "indep": "1991 (16 de Diciembre)", "pop": "19.9 Millones", "lang": "Kazajo, Ruso", "distractors": ["Almatý", "Shymkent", "Karagandá"]},
    "en": {"name": "Kazakhstan", "capital": "Astana", "continent": "Asia / Europe", "indep": "1991 (December 16th)", "pop": "19.9 Million", "lang": "Kazakh, Russian", "distractors": ["Almaty", "Shymkent", "Karaganda"]}
  },
  "Kenya": {
    "flag": "🇰🇪", "isSovereign": True,
    "es": {"name": "Kenia", "capital": "Nairobi", "continent": "África", "indep": "1963 (12 de Diciembre)", "pop": "54.0 Millones", "lang": "Suajili, Inglés", "distractors": ["Mombasa", "Kisumu", "Nakuru"]},
    "en": {"name": "Kenya", "capital": "Nairobi", "continent": "Africa", "indep": "1963 (December 12th)", "pop": "54.0 Million", "lang": "Swahili, English", "distractors": ["Mombasa", "Kisumu", "Nakuru"]}
  },
  "Kosovo": {
    "flag": "🇽🇰", "isSovereign": True,
    "es": {"name": "Kosovo", "capital": "Pristina", "continent": "Europa", "indep": "2008 (17 de Febrero)", "pop": "1.8 Millones", "lang": "Albanés, Serbio", "distractors": ["Prizren", "Peja", "Mitrovica"]},
    "en": {"name": "Kosovo", "capital": "Pristina", "continent": "Europe", "indep": "2008 (February 17th)", "pop": "1.8 Million", "lang": "Albanian, Serbian", "distractors": ["Prizren", "Peja", "Mitrovica"]}
  },
  "Kuwait": {
    "flag": "🇰🇼", "isSovereign": True,
    "es": {"name": "Kuwait", "capital": "Ciudad de Kuwait", "continent": "Asia", "indep": "1961 (19 de Junio)", "pop": "4.3 Millones", "lang": "Árabe", "distractors": ["Al Ahmadi", "Hawalli", "Salmiya"]},
    "en": {"name": "Kuwait", "capital": "Kuwait City", "continent": "Asia", "indep": "1961 (June 19th)", "pop": "4.3 Million", "lang": "Arabic", "distractors": ["Al Ahmadi", "Hawalli", "Salmiya"]}
  },
  "Kyrgyzstan": {
    "flag": "🇰🇬", "isSovereign": True,
    "es": {"name": "Kirguistán", "capital": "Biskek", "continent": "Asia", "indep": "1991 (31 de Agosto)", "pop": "7.0 Millones", "lang": "Kirguís, Ruso", "distractors": ["Osh", "Jalal-Abad", "Karakol"]},
    "en": {"name": "Kyrgyzstan", "capital": "Bishkek", "continent": "Asia", "indep": "1991 (August 31st)", "pop": "7.0 Million", "lang": "Kyrgyz, Russian", "distractors": ["Osh", "Jalal-Abad", "Karakol"]}
  },
  "Laos": {
    "flag": "🇱🇦", "isSovereign": True,
    "es": {"name": "Laos", "capital": "Vientián", "continent": "Asia", "indep": "1953 (22 de Octubre)", "pop": "7.5 Millones", "lang": "Laosiano", "distractors": ["Luang Prabang", "Pakse", "Savannakhet"]},
    "en": {"name": "Laos", "capital": "Vientiane", "continent": "Asia", "indep": "1953 (October 22nd)", "pop": "7.5 Million", "lang": "Lao", "distractors": ["Luang Prabang", "Pakse", "Savannakhet"]}
  },
  "Latvia": {
    "flag": "🇱🇻", "isSovereign": True,
    "es": {"name": "Letonia", "capital": "Riga", "continent": "Europa", "indep": "1918 / 1991", "pop": "1.9 Millones", "lang": "Letón", "distractors": ["Daugavpils", "Liepāja", "Jelgava"]},
    "en": {"name": "Latvia", "capital": "Riga", "continent": "Europe", "indep": "1918 / 1991", "pop": "1.9 Million", "lang": "Latvian", "distractors": ["Daugavpils", "Liepaja", "Jelgava"]}
  },
  "Lebanon": {
    "flag": "🇱🇧", "isSovereign": True,
    "es": {"name": "Líbano", "capital": "Beirut", "continent": "Asia", "indep": "1943 (22 de Noviembre)", "pop": "5.5 Millones", "lang": "Árabe", "distractors": ["Trípoli", "Sidón", "Tiro"]},
    "en": {"name": "Lebanon", "capital": "Beirut", "continent": "Asia", "indep": "1943 (November 22nd)", "pop": "5.5 Million", "lang": "Arabic", "distractors": ["Tripoli", "Sidon", "Tyre"]}
  },
  "Lesotho": {
    "flag": "🇱🇸", "isSovereign": True,
    "es": {"name": "Lesoto", "capital": "Maseru", "continent": "África", "indep": "1966 (4 de Octubre)", "pop": "2.3 Millones", "lang": "Sesoto, Inglés", "distractors": ["Teyateyaneng", "Mafeteng", "Hlotse"]},
    "en": {"name": "Lesotho", "capital": "Maseru", "continent": "Africa", "indep": "1966 (October 4th)", "pop": "2.3 Million", "lang": "Sesotho, English", "distractors": ["Teyateyaneng", "Mafeteng", "Hlotse"]}
  },
  "Liberia": {
    "flag": "🇱🇷", "isSovereign": True,
    "es": {"name": "Liberia", "capital": "Monrovia", "continent": "África", "indep": "1847 (26 de Julio)", "pop": "5.4 Millones", "lang": "Inglés", "distractors": ["Gbarnga", "Buchanan", "Ganta"]},
    "en": {"name": "Liberia", "capital": "Monrovia", "continent": "Africa", "indep": "1847 (July 26th)", "pop": "5.4 Million", "lang": "English", "distractors": ["Gbarnga", "Buchanan", "Ganta"]}
  },
  "Libya": {
    "flag": "🇱🇾", "isSovereign": True,
    "es": {"name": "Libia", "capital": "Trípoli", "continent": "África", "indep": "1951 (24 de Diciembre)", "pop": "6.9 Millones", "lang": "Árabe", "distractors": ["Bengasi", "Misurata", "Tobruk"]},
    "en": {"name": "Libya", "capital": "Tripoli", "continent": "Africa", "indep": "1951 (December 24th)", "pop": "6.9 Million", "lang": "Arabic", "distractors": ["Benghazi", "Misrata", "Tobruk"]}
  },
  "Lithuania": {
    "flag": "🇱🇹", "isSovereign": True,
    "es": {"name": "Lituania", "capital": "Vilna", "continent": "Europa", "indep": "1918 / 1990", "pop": "2.8 Millones", "lang": "Lituano", "distractors": ["Kaunas", "Klaipeda", "Siauliai"]},
    "en": {"name": "Lithuania", "capital": "Vilnius", "continent": "Europe", "indep": "1918 / 1990", "pop": "2.8 Million", "lang": "Lithuanian", "distractors": ["Kaunas", "Klaipeda", "Siauliai"]}
  },
  "Luxembourg": {
    "flag": "🇱🇺", "isSovereign": True,
    "es": {"name": "Luxemburgo", "capital": "Luxemburgo", "continent": "Europa", "indep": "1815 / 1867", "pop": "660 Mil", "lang": "Luxemburgués, Francés, Alemán", "distractors": ["Esch-sur-Alzette", "Differdange", "Dudelange"]},
    "en": {"name": "Luxembourg", "capital": "Luxembourg City", "continent": "Europe", "indep": "1815 / 1867", "pop": "660 Thousand", "lang": "Luxembourgish, French, German", "distractors": ["Esch-sur-Alzette", "Differdange", "Dudelange"]}
  },
  "Macedonia": {
    "flag": "🇲🇰", "isSovereign": True,
    "es": {"name": "Macedonia del Norte", "capital": "Skopie", "continent": "Europa", "indep": "1991 (8 de Septiembre)", "pop": "1.8 Millones", "lang": "Macedonio, Albanés", "distractors": ["Bitola", "Kumanovo", "Ohrid"]},
    "en": {"name": "North Macedonia", "capital": "Skopje", "continent": "Europe", "indep": "1991 (September 8th)", "pop": "1.8 Million", "lang": "Macedonian, Albanian", "distractors": ["Bitola", "Kumanovo", "Ohrid"]}
  },
  "Madagascar": {
    "flag": "🇲🇬", "isSovereign": True,
    "es": {"name": "Madagascar", "capital": "Antananarivo", "continent": "África", "indep": "1960 (26 de Junio)", "pop": "29.6 Millones", "lang": "Malgache, Francés", "distractors": ["Toamasina", "Antsirabe", "Mahajanga"]},
    "en": {"name": "Madagascar", "capital": "Antananarivo", "continent": "Africa", "indep": "1960 (June 26th)", "pop": "29.6 Million", "lang": "Malagasy, French", "distractors": ["Toamasina", "Antsirabe", "Mahajanga"]}
  },
  "Malawi": {
    "flag": "🇲🇼", "isSovereign": True,
    "es": {"name": "Malaui", "capital": "Lilongüe", "continent": "África", "indep": "1964 (6 de Julio)", "pop": "20.4 Millones", "lang": "Chichewa, Inglés", "distractors": ["Blantyre", "Mzuzu", "Zomba"]},
    "en": {"name": "Malawi", "capital": "Lilongwe", "continent": "Africa", "indep": "1964 (July 6th)", "pop": "20.4 Million", "lang": "Chichewa, English", "distractors": ["Blantyre", "Mzuzu", "Zomba"]}
  },
  "Malaysia": {
    "flag": "🇲🇾", "isSovereign": True,
    "es": {"name": "Malasia", "capital": "Kuala Lumpur", "continent": "Asia", "indep": "1957 (31 de Agosto)", "pop": "34.3 Millones", "lang": "Malayo, Inglés", "distractors": ["George Town", "Johor Bahru", "Ipoh"]},
    "en": {"name": "Malaysia", "capital": "Kuala Lumpur", "continent": "Asia", "indep": "1957 (August 31st)", "pop": "34.3 Million", "lang": "Malay, English", "distractors": ["George Town", "Johor Bahru", "Ipoh"]}
  },
  "Mali": {
    "flag": "🇲🇱", "isSovereign": True,
    "es": {"name": "Malí", "capital": "Bamako", "continent": "África", "indep": "1960 (22 de Septiembre)", "pop": "22.6 Millones", "lang": "Francés, Bambara", "distractors": ["Sikasso", "Mopti", "Tombuctú"]},
    "en": {"name": "Mali", "capital": "Bamako", "continent": "Africa", "indep": "1960 (September 22nd)", "pop": "22.6 Million", "lang": "French, Bambara", "distractors": ["Sikasso", "Mopti", "Timbuktu"]}
  },
  "Mauritania": {
    "flag": "🇲🇷", "isSovereign": True,
    "es": {"name": "Mauritania", "capital": "Nuakchot", "continent": "África", "indep": "1960 (28 de Noviembre)", "pop": "4.7 Millones", "lang": "Árabe", "distractors": ["Nuadibú", "Kiffa", "Rosso"]},
    "en": {"name": "Mauritania", "capital": "Nouakchott", "continent": "Africa", "indep": "1960 (November 28th)", "pop": "4.7 Million", "lang": "Arabic", "distractors": ["Nouadhibou", "Kiffa", "Rosso"]}
  },
  "Mexico": {
    "flag": "🇲🇽", "isSovereign": True,
    "es": {"name": "México", "capital": "Ciudad de México", "continent": "América del Norte", "indep": "1810 (16 de Septiembre)", "pop": "128.5 Millones", "lang": "Español", "distractors": ["Guadalajara", "Monterrey", "Puebla"]},
    "en": {"name": "Mexico", "capital": "Mexico City", "continent": "North America", "indep": "1810 (September 16th)", "pop": "128.5 Million", "lang": "Spanish", "distractors": ["Guadalajara", "Monterrey", "Puebla"]}
  },
  "Moldova": {
    "flag": "🇲🇩", "isSovereign": True,
    "es": {"name": "Moldavia", "capital": "Chisináu", "continent": "Europa", "indep": "1991 (27 de Agosto)", "pop": "2.5 Millones", "lang": "Rumano", "distractors": ["Bălți", "Tiraspol", "Bender"]},
    "en": {"name": "Moldova", "capital": "Chisinau", "continent": "Europe", "indep": "1991 (August 27th)", "pop": "2.5 Million", "lang": "Romanian", "distractors": ["Balti", "Tiraspol", "Bender"]}
  },
  "Mongolia": {
    "flag": "🇲🇳", "isSovereign": True,
    "es": {"name": "Mongolia", "capital": "Ulán Bator", "continent": "Asia", "indep": "1911 / 1921", "pop": "3.4 Millones", "lang": "Mongol", "distractors": ["Erdenet", "Darhan", "Choibalsan"]},
    "en": {"name": "Mongolia", "capital": "Ulaanbaatar", "continent": "Asia", "indep": "1911 / 1921", "pop": "3.4 Million", "lang": "Mongolian", "distractors": ["Erdenet", "Darkhan", "Choibalsan"]}
  },
  "Montenegro": {
    "flag": "🇲🇪", "isSovereign": True,
    "es": {"name": "Montenegro", "capital": "Podgorica", "continent": "Europa", "indep": "2006 (3 de Junio)", "pop": "620 Mil", "lang": "Montenegrino", "distractors": ["Nikšić", "Herceg Novi", "Budva"]},
    "en": {"name": "Montenegro", "capital": "Podgorica", "continent": "Europe", "indep": "2006 (June 3rd)", "pop": "620 Thousand", "lang": "Montenegrin", "distractors": ["Niksic", "Herceg Novi", "Budva"]}
  },
  "Morocco": {
    "flag": "🇲🇦", "isSovereign": True,
    "es": {"name": "Marruecos", "capital": "Rabat", "continent": "África", "indep": "1956 (2 de Marzo)", "pop": "37.8 Millones", "lang": "Árabe, Bereber", "distractors": ["Casablanca", "Marrakech", "Fez"]},
    "en": {"name": "Morocco", "capital": "Rabat", "continent": "Africa", "indep": "1956 (March 2nd)", "pop": "37.8 Million", "lang": "Arabic, Berber", "distractors": ["Casablanca", "Marrakech", "Fes"]}
  },
  "Mozambique": {
    "flag": "🇲🇿", "isSovereign": True,
    "es": {"name": "Mozambique", "capital": "Maputo", "continent": "África", "indep": "1975 (25 de Junio)", "pop": "32.4 Millones", "lang": "Portugués", "distractors": ["Matola", "Beira", "Nampula"]},
    "en": {"name": "Mozambique", "capital": "Maputo", "continent": "Africa", "indep": "1975 (June 25th)", "pop": "32.4 Million", "lang": "Portuguese", "distractors": ["Matola", "Beira", "Nampula"]}
  },
  "Myanmar": {
    "flag": "🇲🇲", "isSovereign": True,
    "es": {"name": "Birmania (Myanmar)", "capital": "Naipyidó", "continent": "Asia", "indep": "1948 (4 de Enero)", "pop": "54.2 Millones", "lang": "Birmano", "distractors": ["Rangún (Yangon)", "Mandalay", "Bago"]},
    "en": {"name": "Myanmar (Burma)", "capital": "Naypyidaw", "continent": "Asia", "indep": "1948 (January 4th)", "pop": "54.2 Million", "lang": "Burmese", "distractors": ["Yangon", "Mandalay", "Bago"]}
  },
  "N. Cyprus": {
    "flag": "🇹🇷", "isSovereign": False,
    "es": {"name": "Norte de Chipre", "capital": "Nicosia del Norte", "continent": "Europa / Asia", "indep": "Territorio De Facto (1983)", "pop": "380 Mil", "lang": "Turco", "distractors": ["Famagusta", "Kyrenia", "Morphou"]},
    "en": {"name": "Northern Cyprus", "capital": "North Nicosia", "continent": "Europe / Asia", "indep": "De Facto State (1983)", "pop": "380 Thousand", "lang": "Turkish", "distractors": ["Famagusta", "Kyrenia", "Morphou"]}
  },
  "Namibia": {
    "flag": "🇳🇦", "isSovereign": True,
    "es": {"name": "Namibia", "capital": "Windhoek", "continent": "África", "indep": "1990 (21 de Marzo)", "pop": "2.6 Millones", "lang": "Inglés, Afrikáans, Alemán", "distractors": ["Walvis Bay", "Swakopmund", "Oshakati"]},
    "en": {"name": "Namibia", "capital": "Windhoek", "continent": "Africa", "indep": "1990 (March 21st)", "pop": "2.6 Million", "lang": "English, Afrikaans, German", "distractors": ["Walvis Bay", "Swakopmund", "Oshakati"]}
  },
  "Nepal": {
    "flag": "🇳🇵", "isSovereign": True,
    "es": {"name": "Nepal", "capital": "Katmandú", "continent": "Asia", "indep": "1768 (Unificación)", "pop": "30.5 Millones", "lang": "Nepalí", "distractors": ["Pokhara", "Lalitpur", "Biratnagar"]},
    "en": {"name": "Nepal", "capital": "Kathmandu", "continent": "Asia", "indep": "1768 (Unification)", "pop": "30.5 Million", "lang": "Nepali", "distractors": ["Pokhara", "Lalitpur", "Biratnagar"]}
  },
  "Netherlands": {
    "flag": "🇳🇱", "isSovereign": True,
    "es": {"name": "Países Bajos", "capital": "Ámsterdam", "continent": "Europa", "indep": "1581 (Unión de Utrecht)", "pop": "17.9 Millones", "lang": "Neerlandés", "distractors": ["Róterdam", "La Haya", "Utrecht"]},
    "en": {"name": "Netherlands", "capital": "Amsterdam", "continent": "Europe", "indep": "1581 (Union of Utrecht)", "pop": "17.9 Million", "lang": "Dutch", "distractors": ["Rotterdam", "The Hague", "Utrecht"]}
  },
  "New Caledonia": {
    "flag": "🇳🇨", "isSovereign": False,
    "es": {"name": "Nueva Caledonia", "capital": "Numea", "continent": "Oceanía", "indep": "Colectividad Francesa", "pop": "270 Mil", "lang": "Francés", "distractors": ["Mont-Dore", "Dumbéa", "Païta"]},
    "en": {"name": "New Caledonia", "capital": "Noumea", "continent": "Oceania", "indep": "French Collectivity", "pop": "270 Thousand", "lang": "French", "distractors": ["Mont-Dore", "Dumbea", "Paita"]}
  },
  "New Zealand": {
    "flag": "🇳🇿", "isSovereign": True,
    "es": {"name": "Nueva Zelanda", "capital": "Wellington", "continent": "Oceanía", "indep": "1907 / 1947", "pop": "5.2 Millones", "lang": "Inglés, Maorí", "distractors": ["Auckland", "Christchurch", "Hamilton"]},
    "en": {"name": "New Zealand", "capital": "Wellington", "continent": "Oceania", "indep": "1907 / 1947", "pop": "5.2 Million", "lang": "English, Maori", "distractors": ["Auckland", "Christchurch", "Hamilton"]}
  },
  "Nicaragua": {
    "flag": "🇳🇮", "isSovereign": True,
    "es": {"name": "Nicaragua", "capital": "Managua", "continent": "América Central", "indep": "1821 (15 de Septiembre)", "pop": "6.9 Millones", "lang": "Español", "distractors": ["León", "Granada", "Matagalpa"]},
    "en": {"name": "Nicaragua", "capital": "Managua", "continent": "Central America", "indep": "1821 (September 15th)", "pop": "6.9 Million", "lang": "Spanish", "distractors": ["Leon", "Granada", "Matagalpa"]}
  },
  "Niger": {
    "flag": "🇳🇪", "isSovereign": True,
    "es": {"name": "Níger", "capital": "Niamey", "continent": "África", "indep": "1960 (3 de Agosto)", "pop": "26.2 Millones", "lang": "Francés, Hausa", "distractors": ["Maradi", "Zinder", "Tahoua"]},
    "en": {"name": "Niger", "capital": "Niamey", "continent": "Africa", "indep": "1960 (August 3rd)", "pop": "26.2 Million", "lang": "French, Hausa", "distractors": ["Maradi", "Zinder", "Tahoua"]}
  },
  "Nigeria": {
    "flag": "🇳🇬", "isSovereign": True,
    "es": {"name": "Nigeria", "capital": "Abuya", "continent": "África", "indep": "1960 (1 de Octubre)", "pop": "224 Millones", "lang": "Inglés, Hausa, Yoruba", "distractors": ["Lagos", "Kano", "Ibadan"]},
    "en": {"name": "Nigeria", "capital": "Abuja", "continent": "Africa", "indep": "1960 (October 1st)", "pop": "224 Million", "lang": "English, Hausa, Yoruba", "distractors": ["Lagos", "Kano", "Ibadan"]}
  },
  "North Korea": {
    "flag": "🇰🇵", "isSovereign": True,
    "es": {"name": "Corea del Norte", "capital": "Pionyang", "continent": "Asia", "indep": "1948 (9 de Septiembre)", "pop": "26.0 Millones", "lang": "Coreano", "distractors": ["Hamhung", "Chongjin", "Nampo"]},
    "en": {"name": "North Korea", "capital": "Pyongyang", "continent": "Asia", "indep": "1948 (September 9th)", "pop": "26.0 Million", "lang": "Korean", "distractors": ["Hamhung", "Chongjin", "Nampo"]}
  },
  "Norway": {
    "flag": "🇳🇴", "isSovereign": True,
    "es": {"name": "Noruega", "capital": "Oslo", "continent": "Europa", "indep": "1905 (Disolución de Unión)", "pop": "5.5 Millones", "lang": "Noruego", "distractors": ["Bergen", "Trondheim", "Stavanger"]},
    "en": {"name": "Norway", "capital": "Oslo", "continent": "Europe", "indep": "1905 (Union Dissolution)", "pop": "5.5 Million", "lang": "Norwegian", "distractors": ["Bergen", "Trondheim", "Stavanger"]}
  },
  "Oman": {
    "flag": "🇴🇲", "isSovereign": True,
    "es": {"name": "Omán", "capital": "Mascate", "continent": "Asia", "indep": "1650 (Expulsión Portuguesa)", "pop": "4.6 Millones", "lang": "Árabe", "distractors": ["Salalah", "Sohar", "Nizwa"]},
    "en": {"name": "Oman", "capital": "Muscat", "continent": "Asia", "indep": "1650 (Portuguese Expulsion)", "pop": "4.6 Million", "lang": "Arabic", "distractors": ["Salalah", "Sohar", "Nizwa"]}
  },
  "Pakistan": {
    "flag": "🇵🇰", "isSovereign": True,
    "es": {"name": "Pakistán", "capital": "Islamabad", "continent": "Asia", "indep": "1947 (14 de Agosto)", "pop": "241.5 Millones", "lang": "Urdu, Inglés", "distractors": ["Karachi", "Lahore", "Faisalabad"]},
    "en": {"name": "Pakistan", "capital": "Islamabad", "continent": "Asia", "indep": "1947 (August 14th)", "pop": "241.5 Million", "lang": "Urdu, English", "distractors": ["Karachi", "Lahore", "Faisalabad"]}
  },
  "Palestine": {
    "flag": "🇵🇸", "isSovereign": True,
    "es": {"name": "Palestina", "capital": "Jerusalén Este / Ramala", "continent": "Asia", "indep": "1988 (15 de Noviembre)", "pop": "5.4 Millones", "lang": "Árabe", "distractors": ["Gaza", "Hebrón", "Nablus"]},
    "en": {"name": "Palestine", "capital": "East Jerusalem / Ramallah", "continent": "Asia", "indep": "1988 (November 15th)", "pop": "5.4 Million", "lang": "Arabic", "distractors": ["Gaza", "Hebron", "Nablus"]}
  },
  "Panama": {
    "flag": "🇵🇦", "isSovereign": True,
    "es": {"name": "Panamá", "capital": "Ciudad de Panamá", "continent": "América Central", "indep": "1903 (3 de Noviembre)", "pop": "4.4 Millones", "lang": "Español", "distractors": ["Colón", "David", "Santiago"]},
    "en": {"name": "Panama", "capital": "Panama City", "continent": "Central America", "indep": "1903 (November 3rd)", "pop": "4.4 Million", "lang": "Spanish", "distractors": ["Colon", "David", "Santiago"]}
  },
  "Papua New Guinea": {
    "flag": "🇵🇬", "isSovereign": True,
    "es": {"name": "Papúa Nueva Guinea", "capital": "Puerto Moresby", "continent": "Oceanía", "indep": "1975 (16 de Septiembre)", "pop": "10.1 Millones", "lang": "Inglés, Tok Pisin", "distractors": ["Lae", "Mount Hagen", "Madang"]},
    "en": {"name": "Papua New Guinea", "capital": "Port Moresby", "continent": "Oceania", "indep": "1975 (September 16th)", "pop": "10.1 Million", "lang": "English, Tok Pisin", "distractors": ["Lae", "Mount Hagen", "Madang"]}
  },
  "Paraguay": {
    "flag": "🇵🇾", "isSovereign": True,
    "es": {"name": "Paraguay", "capital": "Asunción", "continent": "América del Sur", "indep": "1811 (14 de Mayo)", "pop": "7.4 Millones", "lang": "Español, Guaraní", "distractors": ["Ciudad del Este", "Encarnación", "Luque"]},
    "en": {"name": "Paraguay", "capital": "Asuncion", "continent": "South America", "indep": "1811 (May 14th)", "pop": "7.4 Million", "lang": "Spanish, Guarani", "distractors": ["Ciudad del Este", "Encarnacion", "Luque"]}
  },
  "Peru": {
    "flag": "🇵🇪", "isSovereign": True,
    "es": {"name": "Perú", "capital": "Lima", "continent": "América del Sur", "indep": "1821 (28 de Julio)", "pop": "34.0 Millones", "lang": "Español, Quechua", "distractors": ["Cusco", "Arequipa", "Trujillo"]},
    "en": {"name": "Peru", "capital": "Lima", "continent": "South America", "indep": "1821 (July 28th)", "pop": "34.0 Million", "lang": "Spanish, Quechua", "distractors": ["Cusco", "Arequipa", "Trujillo"]}
  },
  "Philippines": {
    "flag": "🇵🇭", "isSovereign": True,
    "es": {"name": "Filipinas", "capital": "Manila", "continent": "Asia", "indep": "1898 / 1946", "pop": "115.6 Millones", "lang": "Filipino (Tagalo), Inglés", "distractors": ["Ciudad Quezon", "Cebú", "Dávao"]},
    "en": {"name": "Philippines", "capital": "Manila", "continent": "Asia", "indep": "1898 / 1946", "pop": "115.6 Million", "lang": "Filipino (Tagalog), English", "distractors": ["Quezon City", "Cebu", "Davao"]}
  },
  "Poland": {
    "flag": "🇵🇱", "isSovereign": True,
    "es": {"name": "Polonia", "capital": "Varsovia", "continent": "Europa", "indep": "966 / 1918", "pop": "37.7 Millones", "lang": "Polaco", "distractors": ["Cracovia", "Gdansk", "Wroclaw"]},
    "en": {"name": "Poland", "capital": "Warsaw", "continent": "Europe", "indep": "966 / 1918", "pop": "37.7 Million", "lang": "Polish", "distractors": ["Krakow", "Gdansk", "Wroclaw"]}
  },
  "Portugal": {
    "flag": "🇵🇹", "isSovereign": True,
    "es": {"name": "Portugal", "capital": "Lisboa", "continent": "Europa", "indep": "1143 (Tratado de Zamora)", "pop": "10.4 Millones", "lang": "Portugués", "distractors": ["Oporto", "Coímbra", "Faro"]},
    "en": {"name": "Portugal", "capital": "Lisbon", "continent": "Europe", "indep": "1143 (Treaty of Zamora)", "pop": "10.4 Million", "lang": "Portuguese", "distractors": ["Porto", "Coimbra", "Faro"]}
  },
  "Puerto Rico": {
    "flag": "🇵🇷", "isSovereign": False,
    "es": {"name": "Puerto Rico", "capital": "San Juan", "continent": "Caribe", "indep": "Estado Libre Asociado (EE.UU.)", "pop": "3.2 Millones", "lang": "Español, Inglés", "distractors": ["Ponce", "Mayagüez", "Caguas"]},
    "en": {"name": "Puerto Rico", "capital": "San Juan", "continent": "Caribbean", "indep": "Commonwealth of the US", "pop": "3.2 Million", "lang": "Spanish, English", "distractors": ["Ponce", "Mayaguez", "Caguas"]}
  },
  "Qatar": {
    "flag": "🇶🇦", "isSovereign": True,
    "es": {"name": "Catar", "capital": "Doha", "continent": "Asia", "indep": "1971 (3 de Septiembre)", "pop": "2.7 Millones", "lang": "Árabe", "distractors": ["Al Wakrah", "Al Khor", "Lusail"]},
    "en": {"name": "Qatar", "capital": "Doha", "continent": "Asia", "indep": "1971 (September 3rd)", "pop": "2.7 Million", "lang": "Arabic", "distractors": ["Al Wakrah", "Al Khor", "Lusail"]}
  },
  "Romania": {
    "flag": "🇷🇴", "isSovereign": True,
    "es": {"name": "Rumania", "capital": "Bucarest", "continent": "Europa", "indep": "1877 (9 de Mayo)", "pop": "19.0 Millones", "lang": "Rumano", "distractors": ["Cluj-Napoca", "Timisoara", "Iasi"]},
    "en": {"name": "Romania", "capital": "Bucharest", "continent": "Europe", "indep": "1877 (May 9th)", "pop": "19.0 Million", "lang": "Romanian", "distractors": ["Cluj-Napoca", "Timisoara", "Iasi"]}
  },
  "Russia": {
    "flag": "🇷🇺", "isSovereign": True,
    "es": {"name": "Rusia", "capital": "Moscú", "continent": "Europa / Asia", "indep": "862 / 1991", "pop": "144.2 Millones", "lang": "Ruso", "distractors": ["San Petersburgo", "Novosibirsk", "Kazan"]},
    "en": {"name": "Russia", "capital": "Moscow", "continent": "Europe / Asia", "indep": "862 / 1991", "pop": "144.2 Million", "lang": "Russian", "distractors": ["Saint Petersburg", "Novosibirsk", "Kazan"]}
  },
  "Rwanda": {
    "flag": "🇷🇼", "isSovereign": True,
    "es": {"name": "Ruanda", "capital": "Kigali", "continent": "África", "indep": "1962 (1 de Julio)", "pop": "13.8 Millones", "lang": "Kinyarwanda, Francés, Inglés", "distractors": ["Butare (Huye)", "Gisenyi", "Ruhengeri"]},
    "en": {"name": "Rwanda", "capital": "Kigali", "continent": "Africa", "indep": "1962 (July 1st)", "pop": "13.8 Million", "lang": "Kinyarwanda, French, English", "distractors": ["Butare", "Gisenyi", "Ruhengeri"]}
  },
  "S. Sudan": {
    "flag": "🇸🇸", "isSovereign": True,
    "es": {"name": "Sudán del Sur", "capital": "Yuba", "continent": "África", "indep": "2011 (9 de Julio)", "pop": "11.1 Millones", "lang": "Inglés", "distractors": ["Wau", "Malakal", "Yei"]},
    "en": {"name": "South Sudan", "capital": "Juba", "continent": "Africa", "indep": "2011 (July 9th)", "pop": "11.1 Million", "lang": "English", "distractors": ["Wau", "Malakal", "Yei"]}
  },
  "Saudi Arabia": {
    "flag": "🇸🇦", "isSovereign": True,
    "es": {"name": "Arabia Saudita", "capital": "Riad", "continent": "Asia", "indep": "1932 (23 de Septiembre)", "pop": "36.4 Millones", "lang": "Árabe", "distractors": ["Yeda", "La Meca", "Medina"]},
    "en": {"name": "Saudi Arabia", "capital": "Riyadh", "continent": "Asia", "indep": "1932 (September 23rd)", "pop": "36.4 Million", "lang": "Arabic", "distractors": ["Jeddah", "Mecca", "Medina"]}
  },
  "Senegal": {
    "flag": "🇸🇳", "isSovereign": True,
    "es": {"name": "Senegal", "capital": "Dakar", "continent": "África", "indep": "1960 (4 de Abril)", "pop": "17.3 Millones", "lang": "Francés, Wolof", "distractors": ["Touba", "Thiès", "Saint-Louis"]},
    "en": {"name": "Senegal", "capital": "Dakar", "continent": "Africa", "indep": "1960 (April 4th)", "pop": "17.3 Million", "lang": "French, Wolof", "distractors": ["Touba", "Thies", "Saint-Louis"]}
  },
  "Serbia": {
    "flag": "🇷🇸", "isSovereign": True,
    "es": {"name": "Serbia", "capital": "Belgrado", "continent": "Europa", "indep": "1878 / 2006", "pop": "6.6 Millones", "lang": "Serbio", "distractors": ["Novi Sad", "Nis", "Kragujevac"]},
    "en": {"name": "Serbia", "capital": "Belgrade", "continent": "Europe", "indep": "1878 / 2006", "pop": "6.6 Million", "lang": "Serbian", "distractors": ["Novi Sad", "Nis", "Kragujevac"]}
  },
  "Sierra Leone": {
    "flag": "🇸🇱", "isSovereign": True,
    "es": {"name": "Sierra Leona", "capital": "Freetown", "continent": "África", "indep": "1961 (27 de Abril)", "pop": "8.6 Millones", "lang": "Inglés, Krio", "distractors": ["Bo", "Kenema", "Makeni"]},
    "en": {"name": "Sierra Leone", "capital": "Freetown", "continent": "Africa", "indep": "1961 (April 27th)", "pop": "8.6 Million", "lang": "English, Krio", "distractors": ["Bo", "Kenema", "Makeni"]}
  },
  "Slovakia": {
    "flag": "🇸🇰", "isSovereign": True,
    "es": {"name": "Eslovaquia", "capital": "Bratislava", "continent": "Europa", "indep": "1993 (1 de Enero)", "pop": "5.4 Millones", "lang": "Eslovaco", "distractors": ["Kosice", "Presov", "Zilina"]},
    "en": {"name": "Slovakia", "capital": "Bratislava", "continent": "Europe", "indep": "1993 (January 1st)", "pop": "5.4 Million", "lang": "Slovak", "distractors": ["Kosice", "Presov", "Zilina"]}
  },
  "Slovenia": {
    "flag": "🇸🇮", "isSovereign": True,
    "es": {"name": "Eslovenia", "capital": "Liubliana", "continent": "Europa", "indep": "1991 (25 de Junio)", "pop": "2.1 Millones", "lang": "Esloveno", "distractors": ["Maribor", "Celje", "Kranj"]},
    "en": {"name": "Slovenia", "capital": "Ljubljana", "continent": "Europe", "indep": "1991 (June 25th)", "pop": "2.1 Million", "lang": "Slovene", "distractors": ["Maribor", "Celje", "Kranj"]}
  },
  "Solomon Is.": {
    "flag": "🇸🇧", "isSovereign": True,
    "es": {"name": "Islas Salomón", "capital": "Honiara", "continent": "Oceanía", "indep": "1978 (7 de Julio)", "pop": "720 Mil", "lang": "Inglés, Pijin", "distractors": ["Gizo", "Auki", "Kirakira"]},
    "en": {"name": "Solomon Islands", "capital": "Honiara", "continent": "Oceania", "indep": "1978 (July 7th)", "pop": "720 Thousand", "lang": "English, Pijin", "distractors": ["Gizo", "Auki", "Kirakira"]}
  },
  "Somalia": {
    "flag": "🇸🇴", "isSovereign": True,
    "es": {"name": "Somalia", "capital": "Mogadiscio", "continent": "África", "indep": "1960 (1 de Julio)", "pop": "17.6 Millones", "lang": "Somalí, Árabe", "distractors": ["Hargeisa", "Kismayo", "Bosaso"]},
    "en": {"name": "Somalia", "capital": "Mogadishu", "continent": "Africa", "indep": "1960 (July 1st)", "pop": "17.6 Million", "lang": "Somali, Arabic", "distractors": ["Hargeisa", "Kismayo", "Bosaso"]}
  },
  "Somaliland": {
    "flag": "🇸🇴", "isSovereign": False,
    "es": {"name": "Somalilandia", "capital": "Hargeisa", "continent": "África", "indep": "República Autoproclamada (1991)", "pop": "4.2 Millones", "lang": "Somalí, Árabe", "distractors": ["Berbera", "Burao", "Borama"]},
    "en": {"name": "Somaliland", "capital": "Hargeisa", "continent": "Africa", "indep": "Self-Declared State (1991)", "pop": "4.2 Million", "lang": "Somali, Arabic", "distractors": ["Berbera", "Burao", "Borama"]}
  },
  "South Africa": {
    "flag": "🇿🇦", "isSovereign": True,
    "es": {"name": "Sudáfrica", "capital": "Pretoria", "continent": "África", "indep": "1910 (31 de Mayo)", "pop": "60.4 Millones", "lang": "Zulú, Xhosa, Afrikáans, Inglés", "distractors": ["Ciudad del Cabo", "Johannesburgo", "Durban"]},
    "en": {"name": "South Africa", "capital": "Pretoria", "continent": "Africa", "indep": "1910 (May 31st)", "pop": "60.4 Million", "lang": "Zulu, Xhosa, Afrikaans, English", "distractors": ["Cape Town", "Johannesburg", "Durban"]}
  },
  "South Korea": {
    "flag": "🇰🇷", "isSovereign": True,
    "es": {"name": "Corea del Sur", "capital": "Seúl", "continent": "Asia", "indep": "1948 (15 de Agosto)", "pop": "51.7 Millones", "lang": "Coreano", "distractors": ["Busan", "Incheon", "Daegu"]},
    "en": {"name": "South Korea", "capital": "Seoul", "continent": "Asia", "indep": "1948 (August 15th)", "pop": "51.7 Million", "lang": "Korean", "distractors": ["Busan", "Incheon", "Daegu"]}
  },
  "Spain": {
    "flag": "🇪🇸", "isSovereign": True,
    "es": {"name": "España", "capital": "Madrid", "continent": "Europa", "indep": "1492 (Unificación)", "pop": "47.8 Millones", "lang": "Español", "distractors": ["Barcelona", "Valencia", "Sevilla"]},
    "en": {"name": "Spain", "capital": "Madrid", "continent": "Europe", "indep": "1492 (Unification)", "pop": "47.8 Million", "lang": "Spanish", "distractors": ["Barcelona", "Valencia", "Seville"]}
  },
  "Sri Lanka": {
    "flag": "🇱🇰", "isSovereign": True,
    "es": {"name": "Sri Lanka", "capital": "Sri Jayawardenepura Kotte", "continent": "Asia", "indep": "1948 (4 de Febrero)", "pop": "22.2 Millones", "lang": "Cingalés, Tamil", "distractors": ["Colombo", "Kandy", "Galle"]},
    "en": {"name": "Sri Lanka", "capital": "Sri Jayawardenepura Kotte", "continent": "Asia", "indep": "1948 (February 4th)", "pop": "22.2 Million", "lang": "Sinhala, Tamil", "distractors": ["Colombo", "Kandy", "Galle"]}
  },
  "Sudan": {
    "flag": "🇸🇩", "isSovereign": True,
    "es": {"name": "Sudán", "capital": "Jartum", "continent": "África", "indep": "1956 (1 de Enero)", "pop": "48.1 Millones", "lang": "Árabe, Inglés", "distractors": ["Omdurmán", "Port Sudan", "Kassala"]},
    "en": {"name": "Sudan", "capital": "Khartoum", "continent": "Africa", "indep": "1956 (January 1st)", "pop": "48.1 Million", "lang": "Arabic, English", "distractors": ["Omdurman", "Port Sudan", "Kassala"]}
  },
  "Suriname": {
    "flag": "🇸🇷", "isSovereign": True,
    "es": {"name": "Surinam", "capital": "Paramaribo", "continent": "América del Sur", "indep": "1975 (25 de Noviembre)", "pop": "618 Mil", "lang": "Neerlandés", "distractors": ["Lelydorp", "Nieuw Nickerie", "Moengo"]},
    "en": {"name": "Suriname", "capital": "Paramaribo", "continent": "South America", "indep": "1975 (November 25th)", "pop": "618 Thousand", "lang": "Dutch", "distractors": ["Lelydorp", "Nieuw Nickerie", "Moengo"]}
  },
  "Sweden": {
    "flag": "🇸🇪", "isSovereign": True,
    "es": {"name": "Suecia", "capital": "Estocolmo", "continent": "Europa", "indep": "1523 (Gustav Vasa)", "pop": "10.5 Millones", "lang": "Sueco", "distractors": ["Gotemburgo", "Malmö", "Uppsala"]},
    "en": {"name": "Sweden", "capital": "Stockholm", "continent": "Europe", "indep": "1523 (Gustav Vasa)", "pop": "10.5 Million", "lang": "Swedish", "distractors": ["Gothenburg", "Malmo", "Uppsala"]}
  },
  "Switzerland": {
    "flag": "🇨🇭", "isSovereign": True,
    "es": {"name": "Suiza", "capital": "Berna", "continent": "Europa", "indep": "1291 (Pacto Federal)", "pop": "8.9 Millones", "lang": "Alemán, Francés, Italiano", "distractors": ["Zúrich", "Ginebra", "Basilea"]},
    "en": {"name": "Switzerland", "capital": "Bern", "continent": "Europe", "indep": "1291 (Federal Charter)", "pop": "8.9 Million", "lang": "German, French, Italian", "distractors": ["Zurich", "Geneva", "Basel"]}
  },
  "Syria": {
    "flag": "🇸🇾", "isSovereign": True,
    "es": {"name": "Siria", "capital": "Damasco", "continent": "Asia", "indep": "1946 (17 de Abril)", "pop": "22.1 Millones", "lang": "Árabe", "distractors": ["Alepo", "Homs", "Latakia"]},
    "en": {"name": "Syria", "capital": "Damascus", "continent": "Asia", "indep": "1946 (April 17th)", "pop": "22.1 Million", "lang": "Arabic", "distractors": ["Aleppo", "Homs", "Latakia"]}
  },
  "Taiwan": {
    "flag": "🇹🇼", "isSovereign": True,
    "es": {"name": "Taiwán", "capital": "Taipéi", "continent": "Asia", "indep": "1912 / 1949", "pop": "23.9 Millones", "lang": "Mandarín", "distractors": ["Kaohsiung", "Taichung", "Tainan"]},
    "en": {"name": "Taiwan", "capital": "Taipei", "continent": "Asia", "indep": "1912 / 1949", "pop": "23.9 Million", "lang": "Mandarin", "distractors": ["Kaohsiung", "Taichung", "Tainan"]}
  },
  "Tajikistan": {
    "flag": "🇹🇯", "isSovereign": True,
    "es": {"name": "Tayikistán", "capital": "Dusambé", "continent": "Asia", "indep": "1991 (9 de Septiembre)", "pop": "10.1 Millones", "lang": "Tayiko, Ruso", "distractors": ["Khujand", "Kulob", "Bokhtar"]},
    "en": {"name": "Tajikistan", "capital": "Dushanbe", "continent": "Asia", "indep": "1991 (September 9th)", "pop": "10.1 Million", "lang": "Tajik, Russian", "distractors": ["Khujand", "Kulob", "Bokhtar"]}
  },
  "Tanzania": {
    "flag": "🇹🇿", "isSovereign": True,
    "es": {"name": "Tanzania", "capital": "Dodoma", "continent": "África", "indep": "1961 / 1964", "pop": "65.5 Millones", "lang": "Suajili, Inglés", "distractors": ["Dar es Salaam", "Mwanza", "Arusha"]},
    "en": {"name": "Tanzania", "capital": "Dodoma", "continent": "Africa", "indep": "1961 / 1964", "pop": "65.5 Million", "lang": "Swahili, English", "distractors": ["Dar es Salaam", "Mwanza", "Arusha"]}
  },
  "Thailand": {
    "flag": "🇹🇭", "isSovereign": True,
    "es": {"name": "Tailandia", "capital": "Bangkok", "continent": "Asia", "indep": "1238 (Reino de Sujotai)", "pop": "71.8 Millones", "lang": "Tailandés", "distractors": ["Chiang Mai", "Phuket", "Pattaya"]},
    "en": {"name": "Thailand", "capital": "Bangkok", "continent": "Asia", "indep": "1238 (Sukhothai Kingdom)", "pop": "71.8 Million", "lang": "Thai", "distractors": ["Chiang Mai", "Phuket", "Pattaya"]}
  },
  "Timor-Leste": {
    "flag": "🇹🇱", "isSovereign": True,
    "es": {"name": "Timor Oriental", "capital": "Dili", "continent": "Asia / Oceanía", "indep": "2002 (20 de Mayo)", "pop": "1.3 Millones", "lang": "Tetun, Portugués", "distractors": ["Baucau", "Maliana", "Suai"]},
    "en": {"name": "East Timor", "capital": "Dili", "continent": "Asia / Oceania", "indep": "2002 (May 20th)", "pop": "1.3 Million", "lang": "Tetum, Portuguese", "distractors": ["Baucau", "Maliana", "Suai"]}
  },
  "Togo": {
    "flag": "🇹🇬", "isSovereign": True,
    "es": {"name": "Togo", "capital": "Lomé", "continent": "África", "indep": "1960 (27 de Abril)", "pop": "8.8 Millones", "lang": "Francés, Ewé", "distractors": ["Sokodé", "Kara", "Kpalimé"]},
    "en": {"name": "Togo", "capital": "Lome", "continent": "Africa", "indep": "1960 (April 27th)", "pop": "8.8 Million", "lang": "French, Ewe", "distractors": ["Sokode", "Kara", "Kpalime"]}
  },
  "Trinidad and Tobago": {
    "flag": "🇹🇹", "isSovereign": True,
    "es": {"name": "Trinidad y Tobago", "capital": "Puerto España", "continent": "Caribe", "indep": "1962 (31 de Agosto)", "pop": "1.4 Millones", "lang": "Inglés", "distractors": ["San Fernando", "Chaguanas", "Arima"]},
    "en": {"name": "Trinidad and Tobago", "capital": "Port of Spain", "continent": "Caribbean", "indep": "1962 (August 31st)", "pop": "1.4 Million", "lang": "English", "distractors": ["San Fernando", "Chaguanas", "Arima"]}
  },
  "Tunisia": {
    "flag": "🇹🇳", "isSovereign": True,
    "es": {"name": "Túnez", "capital": "Túnez", "continent": "África", "indep": "1956 (20 de Marzo)", "pop": "12.4 Millones", "lang": "Árabe", "distractors": ["Sfax", "Sousse", "Kairouan"]},
    "en": {"name": "Tunisia", "capital": "Tunis", "continent": "Africa", "indep": "1956 (March 20th)", "pop": "12.4 Million", "lang": "Arabic", "distractors": ["Sfax", "Sousse", "Kairouan"]}
  },
  "Turkey": {
    "flag": "🇹🇷", "isSovereign": True,
    "es": {"name": "Turquía", "capital": "Ankara", "continent": "Europa / Asia", "indep": "1923 (29 de Octubre)", "pop": "85.3 Millones", "lang": "Turco", "distractors": ["Estambul", "Esmirna", "Antalya"]},
    "en": {"name": "Turkey", "capital": "Ankara", "continent": "Europe / Asia", "indep": "1923 (October 29th)", "pop": "85.3 Million", "lang": "Turkish", "distractors": ["Istanbul", "Izmir", "Antalya"]}
  },
  "Turkmenistan": {
    "flag": "🇹🇲", "isSovereign": True,
    "es": {"name": "Turkmenistán", "capital": "Asjabad", "continent": "Asia", "indep": "1991 (27 de Octubre)", "pop": "6.5 Millones", "lang": "Turcomano, Ruso", "distractors": ["Turkmenabat", "Dasoguz", "Mary"]},
    "en": {"name": "Turkmenistan", "capital": "Ashgabat", "continent": "Asia", "indep": "1991 (October 27th)", "pop": "6.5 Million", "lang": "Turkmen, Russian", "distractors": ["Turkmenabat", "Dasoguz", "Mary"]}
  },
  "Uganda": {
    "flag": "🇺🇬", "isSovereign": True,
    "es": {"name": "Uganda", "capital": "Kampala", "continent": "África", "indep": "1962 (9 de Octubre)", "pop": "47.2 Millones", "lang": "Inglés, Suajili", "distractors": ["Entebbe", "Jinja", "Gulu"]},
    "en": {"name": "Uganda", "capital": "Kampala", "continent": "Africa", "indep": "1962 (October 9th)", "pop": "47.2 Million", "lang": "English, Swahili", "distractors": ["Entebbe", "Jinja", "Gulu"]}
  },
  "Ukraine": {
    "flag": "🇺🇦", "isSovereign": True,
    "es": {"name": "Ucrania", "capital": "Kiev", "continent": "Europa", "indep": "1991 (24 de Agosto)", "pop": "38.0 Millones", "lang": "Ucraniano", "distractors": ["Járkov", "Odesa", "Leópolis (Lviv)"]},
    "en": {"name": "Ukraine", "capital": "Kyiv", "continent": "Europe", "indep": "1991 (August 24th)", "pop": "38.0 Million", "lang": "Ukrainian", "distractors": ["Kharkiv", "Odesa", "Lviv"]}
  },
  "United Arab Emirates": {
    "flag": "🇦🇪", "isSovereign": True,
    "es": {"name": "Emiratos Árabes Unidos", "capital": "Abu Dabi", "continent": "Asia", "indep": "1971 (2 de Diciembre)", "pop": "9.5 Millones", "lang": "Árabe", "distractors": ["Dubái", "Sharjah", "Ajman"]},
    "en": {"name": "United Arab Emirates", "capital": "Abu Dhabi", "continent": "Asia", "indep": "1971 (December 2nd)", "pop": "9.5 Million", "lang": "Arabic", "distractors": ["Dubai", "Sharjah", "Ajman"]}
  },
  "United Kingdom": {
    "flag": "🇬🇧", "isSovereign": True,
    "es": {"name": "Reino Unido", "capital": "Londres", "continent": "Europa", "indep": "1707 (Acta de Unión)", "pop": "67.7 Millones", "lang": "Inglés", "distractors": ["Mánchester", "Edimburgo", "Birmingham"]},
    "en": {"name": "United Kingdom", "capital": "London", "continent": "Europe", "indep": "1707 (Acts of Union)", "pop": "67.7 Million", "lang": "English", "distractors": ["Manchester", "Edinburgh", "Birmingham"]}
  },
  "United States of America": {
    "flag": "🇺🇸", "isSovereign": True,
    "es": {"name": "Estados Unidos (y Alaska)", "capital": "Washington D.C.", "continent": "América del Norte", "indep": "1776 (4 de Julio)", "pop": "335 Millones", "lang": "Inglés", "distractors": ["Nueva York", "Los Ángeles", "Chicago"]},
    "en": {"name": "United States (and Alaska)", "capital": "Washington D.C.", "continent": "North America", "indep": "1776 (July 4th)", "pop": "335 Million", "lang": "English", "distractors": ["New York", "Los Angeles", "Chicago"]}
  },
  "Uruguay": {
    "flag": "🇺🇾", "isSovereign": True,
    "es": {"name": "Uruguay", "capital": "Montevideo", "continent": "América del Sur", "indep": "1825 (25 de Agosto)", "pop": "3.5 Millones", "lang": "Español", "distractors": ["Punta del Este", "Salto", "Colonia"]},
    "en": {"name": "Uruguay", "capital": "Montevideo", "continent": "South America", "indep": "1825 (August 25th)", "pop": "3.5 Million", "lang": "Spanish", "distractors": ["Punta del Este", "Salto", "Colonia"]}
  },
  "Uzbekistan": {
    "flag": "🇺🇿", "isSovereign": True,
    "es": {"name": "Uzbekistán", "capital": "Taskent", "continent": "Asia", "indep": "1991 (1 de Septiembre)", "pop": "36.0 Millones", "lang": "Uzbeko, Ruso", "distractors": ["Samarcanda", "Bujará", "Namangán"]},
    "en": {"name": "Uzbekistan", "capital": "Tashkent", "continent": "Asia", "indep": "1991 (September 1st)", "pop": "36.0 Million", "lang": "Uzbek, Russian", "distractors": ["Samarkand", "Bukhara", "Namangan"]}
  },
  "Vanuatu": {
    "flag": "🇻🇺", "isSovereign": True,
    "es": {"name": "Vanuatu", "capital": "Port Vila", "continent": "Oceanía", "indep": "1980 (30 de Julio)", "pop": "320 Mil", "lang": "Bislama, Francés, Inglés", "distractors": ["Luganville", "Norsup", "Isangel"]},
    "en": {"name": "Vanuatu", "capital": "Port Vila", "continent": "Oceania", "indep": "1980 (July 30th)", "pop": "320 Thousand", "lang": "Bislama, French, English", "distractors": ["Luganville", "Norsup", "Isangel"]}
  },
  "Venezuela": {
    "flag": "🇻🇪", "isSovereign": True,
    "es": {"name": "Venezuela", "capital": "Caracas", "continent": "América del Sur", "indep": "1811 (5 de Julio)", "pop": "28.8 Millones", "lang": "Español", "distractors": ["Maracaibo", "Valencia", "Barquisimeto"]},
    "en": {"name": "Venezuela", "capital": "Caracas", "continent": "South America", "indep": "1811 (July 5th)", "pop": "28.8 Million", "lang": "Spanish", "distractors": ["Maracaibo", "Valencia", "Barquisimeto"]}
  },
  "Vietnam": {
    "flag": "🇻🇳", "isSovereign": True,
    "es": {"name": "Vietnam", "capital": "Hanói", "continent": "Asia", "indep": "1945 (2 de Septiembre)", "pop": "98.9 Millones", "lang": "Vietnamita", "distractors": ["Ciudad Ho Chi Minh", "Da Nang", "Hai Phong"]},
    "en": {"name": "Vietnam", "capital": "Hanoi", "continent": "Asia", "indep": "1945 (September 2nd)", "pop": "98.9 Million", "lang": "Vietnamese", "distractors": ["Ho Chi Minh City", "Da Nang", "Hai Phong"]}
  },
  "W. Sahara": {
    "flag": "🇪🇭", "isSovereign": False,
    "es": {"name": "Sáhara Occidental", "capital": "El Aaiún", "continent": "África", "indep": "Territorio No Autónomo", "pop": "580 Mil", "lang": "Árabe, Español", "distractors": ["Dajla", "Smara", "Cabo Bojador"]},
    "en": {"name": "Western Sahara", "capital": "El Aaiun", "continent": "Africa", "indep": "Non-Self-Governing Territory", "pop": "580 Thousand", "lang": "Arabic, Spanish", "distractors": ["Dakhla", "Smara", "Cape Bojador"]}
  },
  "Yemen": {
    "flag": "🇾🇪", "isSovereign": True,
    "es": {"name": "Yemen", "capital": "Saná", "continent": "Asia", "indep": "1918 / 1990", "pop": "33.7 Millones", "lang": "Árabe", "distractors": ["Adén", "Taiz", "Al Hudaydah"]},
    "en": {"name": "Yemen", "capital": "Sanaa", "continent": "Asia", "indep": "1918 / 1990", "pop": "33.7 Million", "lang": "Arabic", "distractors": ["Aden", "Taiz", "Al Hudaydah"]}
  },
  "Zambia": {
    "flag": "🇿🇲", "isSovereign": True,
    "es": {"name": "Zambia", "capital": "Lusaka", "continent": "África", "indep": "1964 (24 de Octubre)", "pop": "20.0 Millones", "lang": "Inglés", "distractors": ["Kitwe", "Ndola", "Livingstone"]},
    "en": {"name": "Zambia", "capital": "Lusaka", "continent": "Africa", "indep": "1964 (October 24th)", "pop": "20.0 Million", "lang": "English", "distractors": ["Kitwe", "Ndola", "Livingstone"]}
  },
  "Zimbabwe": {
    "flag": "🇿🇼", "isSovereign": True,
    "es": {"name": "Zimbabue", "capital": "Harare", "continent": "África", "indep": "1980 (18 de Abril)", "pop": "16.3 Millones", "lang": "Inglés, Shona, Ndebele", "distractors": ["Bulawayo", "Chitungwiza", "Mutare"]},
    "en": {"name": "Zimbabwe", "capital": "Harare", "continent": "Africa", "indep": "1980 (April 18th)", "pop": "16.3 Million", "lang": "English, Shona, Ndebele", "distractors": ["Bulawayo", "Chitungwiza", "Mutare"]}
  },
  "eSwatini": {
    "flag": "🇸🇿", "isSovereign": True,
    "es": {"name": "Esuatini (Suazilandia)", "capital": "Mbabane", "continent": "África", "indep": "1968 (6 de Septiembre)", "pop": "1.2 Millones", "lang": "Suazi, Inglés", "distractors": ["Manzini", "Lobamba", "Big Bend"]},
    "en": {"name": "Eswatini (Swaziland)", "capital": "Mbabane", "continent": "Africa", "indep": "1968 (September 6th)", "pop": "1.2 Million", "lang": "Swazi, English", "distractors": ["Manzini", "Lobamba", "Big Bend"]}
  }
}

with open("atlas_177.json", "w", encoding="utf-8") as f:
    json.dump(ATLAS_177, f, indent=2, ensure_ascii=False)

print(f"Generated complete atlas for all {len(ATLAS_177)} countries/territories!")
