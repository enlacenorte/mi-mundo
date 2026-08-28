import json
import generate_exhaustive_atlas

raw_atlas = generate_exhaustive_atlas.ATLAS_177

COUNTRY_EXTRAS = {
  "Afghanistan": {
    "tz": "Asia/Kabul",
    "curr_es": "Afgani afgano (AFN)",
    "curr_en": "Afghan Afghani (AFN)"
  },
  "Albania": {
    "tz": "Europe/Tirane",
    "curr_es": "Lek albanés (ALL)",
    "curr_en": "Albanian Lek (ALL)"
  },
  "Algeria": {
    "tz": "Africa/Algiers",
    "curr_es": "Dinar argelino (DZD)",
    "curr_en": "Algerian Dinar (DZD)"
  },
  "Angola": {
    "tz": "Africa/Luanda",
    "curr_es": "Kwanza angoleño (AOA)",
    "curr_en": "Angolan Kwanza (AOA)"
  },
  "Antarctica": {
    "tz": "Antarctica/McMurdo",
    "curr_es": "Monedas internacionales",
    "curr_en": "International currencies"
  },
  "Argentina": {
    "tz": "America/Argentina/Buenos_Aires",
    "curr_es": "Peso argentino (ARS)",
    "curr_en": "Argentine Peso (ARS)"
  },
  "Armenia": {
    "tz": "Asia/Yerevan",
    "curr_es": "Dram armenio (AMD)",
    "curr_en": "Armenian Dram (AMD)"
  },
  "Australia": {
    "tz": "Australia/Sydney",
    "curr_es": "Dólar australiano (AUD)",
    "curr_en": "Australian Dollar (AUD)"
  },
  "Austria": {
    "tz": "Europe/Vienna",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Azerbaijan": {
    "tz": "Asia/Baku",
    "curr_es": "Manat azerbaiyano (AZN)",
    "curr_en": "Azerbaijani Manat (AZN)"
  },
  "Bahamas": {
    "tz": "America/Nassau",
    "curr_es": "Dólar bahameño (BSD)",
    "curr_en": "Bahamian Dollar (BSD)"
  },
  "Bangladesh": {
    "tz": "Asia/Dhaka",
    "curr_es": "Taka bangladesí (BDT)",
    "curr_en": "Bangladeshi Taka (BDT)"
  },
  "Belarus": {
    "tz": "Europe/Minsk",
    "curr_es": "Rublo bielorruso (BYN)",
    "curr_en": "Belarusian Ruble (BYN)"
  },
  "Belgium": {
    "tz": "Europe/Brussels",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Belize": {
    "tz": "America/Belize",
    "curr_es": "Dólar beliceño (BZD)",
    "curr_en": "Belize Dollar (BZD)"
  },
  "Benin": {
    "tz": "Africa/Porto-Novo",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Bhutan": {
    "tz": "Asia/Thimphu",
    "curr_es": "Ngultrum butanés (BTN)",
    "curr_en": "Bhutanese Ngultrum (BTN)"
  },
  "Bolivia": {
    "tz": "America/La_Paz",
    "curr_es": "Boliviano (BOB)",
    "curr_en": "Bolivian Boliviano (BOB)"
  },
  "Bosnia and Herz.": {
    "tz": "Europe/Sarajevo",
    "curr_es": "Marco convertible (BAM)",
    "curr_en": "Convertible Mark (BAM)"
  },
  "Botswana": {
    "tz": "Africa/Gaborone",
    "curr_es": "Pula de Botsuana (BWP)",
    "curr_en": "Botswana Pula (BWP)"
  },
  "Brazil": {
    "tz": "America/Sao_Paulo",
    "curr_es": "Real brasileño (BRL)",
    "curr_en": "Brazilian Real (BRL)"
  },
  "Brunei": {
    "tz": "Asia/Brunei",
    "curr_es": "Dólar de Brunéi (BND)",
    "curr_en": "Brunei Dollar (BND)"
  },
  "Bulgaria": {
    "tz": "Europe/Sofia",
    "curr_es": "Lev búlgaro (BGN)",
    "curr_en": "Bulgarian Lev (BGN)"
  },
  "Burkina Faso": {
    "tz": "Africa/Ouagadougou",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Burundi": {
    "tz": "Africa/Bujumbura",
    "curr_es": "Franco burundés (BIF)",
    "curr_en": "Burundian Franc (BIF)"
  },
  "Cambodia": {
    "tz": "Asia/Phnom_Penh",
    "curr_es": "Riel camboyano (KHR)",
    "curr_en": "Cambodian Riel (KHR)"
  },
  "Cameroon": {
    "tz": "Africa/Douala",
    "curr_es": "Franco CFA (XAF)",
    "curr_en": "Central African CFA Franc (XAF)"
  },
  "Canada": {
    "tz": "America/Toronto",
    "curr_es": "Dólar canadiense (CAD)",
    "curr_en": "Canadian Dollar (CAD)"
  },
  "Central African Rep.": {
    "tz": "Africa/Bangui",
    "curr_es": "Franco CFA (XAF)",
    "curr_en": "Central African CFA Franc (XAF)"
  },
  "Chad": {
    "tz": "Africa/Ndjamena",
    "curr_es": "Franco CFA (XAF)",
    "curr_en": "Central African CFA Franc (XAF)"
  },
  "Chile": {
    "tz": "America/Santiago",
    "curr_es": "Peso chileno (CLP)",
    "curr_en": "Chilean Peso (CLP)"
  },
  "China": {
    "tz": "Asia/Shanghai",
    "curr_es": "Yuan chino (CNY)",
    "curr_en": "Chinese Yuan (CNY)"
  },
  "Colombia": {
    "tz": "America/Bogota",
    "curr_es": "Peso colombiano (COP)",
    "curr_en": "Colombian Peso (COP)"
  },
  "Congo": {
    "tz": "Africa/Brazzaville",
    "curr_es": "Franco CFA (XAF)",
    "curr_en": "Central African CFA Franc (XAF)"
  },
  "Costa Rica": {
    "tz": "America/Costa_Rica",
    "curr_es": "Colón costarricense (CRC)",
    "curr_en": "Costa Rican Colón (CRC)"
  },
  "Croatia": {
    "tz": "Europe/Zagreb",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Cuba": {
    "tz": "America/Havana",
    "curr_es": "Peso cubano (CUP)",
    "curr_en": "Cuban Peso (CUP)"
  },
  "Cyprus": {
    "tz": "Asia/Nicosia",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Czechia": {
    "tz": "Europe/Prague",
    "curr_es": "Corona checa (CZK)",
    "curr_en": "Czech Koruna (CZK)"
  },
  "Côte d'Ivoire": {
    "tz": "Africa/Abidjan",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Dem. Rep. Congo": {
    "tz": "Africa/Kinshasa",
    "curr_es": "Franco congoleño (CDF)",
    "curr_en": "Congolese Franc (CDF)"
  },
  "Denmark": {
    "tz": "Europe/Copenhagen",
    "curr_es": "Corona danesa (DKK)",
    "curr_en": "Danish Krone (DKK)"
  },
  "Djibouti": {
    "tz": "Africa/Djibouti",
    "curr_es": "Franco yibutiano (DJF)",
    "curr_en": "Djiboutian Franc (DJF)"
  },
  "Dominican Rep.": {
    "tz": "America/Santo_Domingo",
    "curr_es": "Peso dominicano (DOP)",
    "curr_en": "Dominican Peso (DOP)"
  },
  "Ecuador": {
    "tz": "America/Guayaquil",
    "curr_es": "Dólar estadounidense (USD)",
    "curr_en": "United States Dollar (USD)"
  },
  "Egypt": {
    "tz": "Africa/Cairo",
    "curr_es": "Libra egipcia (EGP)",
    "curr_en": "Egyptian Pound (EGP)"
  },
  "El Salvador": {
    "tz": "America/El_Salvador",
    "curr_es": "Dólar estadounidense (USD)",
    "curr_en": "United States Dollar (USD)"
  },
  "Eq. Guinea": {
    "tz": "Africa/Malabo",
    "curr_es": "Franco CFA (XAF)",
    "curr_en": "Central African CFA Franc (XAF)"
  },
  "Eritrea": {
    "tz": "Africa/Asmara",
    "curr_es": "Nakfa eritreo (ERN)",
    "curr_en": "Eritrean Nakfa (ERN)"
  },
  "Estonia": {
    "tz": "Europe/Tallinn",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Eswatini": {
    "tz": "Africa/Mbabane",
    "curr_es": "Lilangeni suazi (SZL)",
    "curr_en": "Swazi Lilangeni (SZL)"
  },
  "Ethiopia": {
    "tz": "Africa/Addis_Ababa",
    "curr_es": "Birr etíope (ETB)",
    "curr_en": "Ethiopian Birr (ETB)"
  },
  "Falkland Is.": {
    "tz": "Atlantic/Stanley",
    "curr_es": "Peso argentino (ARS)",
    "curr_en": "Argentine Peso (ARS)"
  },
  "Fiji": {
    "tz": "Pacific/Fiji",
    "curr_es": "Dólar fiyiano (FJD)",
    "curr_en": "Fijian Dollar (FJD)"
  },
  "Finland": {
    "tz": "Europe/Helsinki",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Fr. S. Antarctic Lands": {
    "tz": "Indian/Kerguelen",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "France": {
    "tz": "Europe/Paris",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Gabon": {
    "tz": "Africa/Libreville",
    "curr_es": "Franco CFA (XAF)",
    "curr_en": "Central African CFA Franc (XAF)"
  },
  "Gambia": {
    "tz": "Africa/Banjul",
    "curr_es": "Dalasi gambiano (GMD)",
    "curr_en": "Gambian Dalasi (GMD)"
  },
  "Georgia": {
    "tz": "Asia/Tbilisi",
    "curr_es": "Lari georgiano (GEL)",
    "curr_en": "Georgian Lari (GEL)"
  },
  "Germany": {
    "tz": "Europe/Berlin",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Ghana": {
    "tz": "Africa/Accra",
    "curr_es": "Cedi ghanés (GHS)",
    "curr_en": "Ghanaian Cedi (GHS)"
  },
  "Greece": {
    "tz": "Europe/Athens",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Greenland": {
    "tz": "America/Nuuk",
    "curr_es": "Corona danesa (DKK)",
    "curr_en": "Danish Krone (DKK)"
  },
  "Guatemala": {
    "tz": "America/Guatemala",
    "curr_es": "Quetzal guatemalteco (GTQ)",
    "curr_en": "Guatemalan Quetzal (GTQ)"
  },
  "Guinea": {
    "tz": "Africa/Conakry",
    "curr_es": "Franco guineano (GNF)",
    "curr_en": "Guinean Franc (GNF)"
  },
  "Guinea-Bissau": {
    "tz": "Africa/Bissau",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Guyana": {
    "tz": "America/Guyana",
    "curr_es": "Dólar guyanés (GYD)",
    "curr_en": "Guyanese Dollar (GYD)"
  },
  "Haiti": {
    "tz": "America/Port-au-Prince",
    "curr_es": "Gourde haitiano (HTG)",
    "curr_en": "Haitian Gourde (HTG)"
  },
  "Honduras": {
    "tz": "America/Tegucigalpa",
    "curr_es": "Lempira hondureña (HNL)",
    "curr_en": "Honduran Lempira (HNL)"
  },
  "Hungary": {
    "tz": "Europe/Budapest",
    "curr_es": "Forinto húngaro (HUF)",
    "curr_en": "Hungarian Forint (HUF)"
  },
  "Iceland": {
    "tz": "Atlantic/Reykjavik",
    "curr_es": "Corona islandesa (ISK)",
    "curr_en": "Icelandic Króna (ISK)"
  },
  "India": {
    "tz": "Asia/Kolkata",
    "curr_es": "Rupia india (INR)",
    "curr_en": "Indian Rupee (INR)"
  },
  "Indonesia": {
    "tz": "Asia/Jakarta",
    "curr_es": "Rupia indonesia (IDR)",
    "curr_en": "Indonesian Rupiah (IDR)"
  },
  "Iran": {
    "tz": "Asia/Tehran",
    "curr_es": "Rial iraní (IRR)",
    "curr_en": "Iranian Rial (IRR)"
  },
  "Iraq": {
    "tz": "Asia/Baghdad",
    "curr_es": "Dinar iraquí (IQD)",
    "curr_en": "Iraqi Dinar (IQD)"
  },
  "Ireland": {
    "tz": "Europe/Dublin",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Israel": {
    "tz": "Asia/Jerusalem",
    "curr_es": "Nuevo séquel israelí (ILS)",
    "curr_en": "Israeli New Shekel (ILS)"
  },
  "Italy": {
    "tz": "Europe/Rome",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Jamaica": {
    "tz": "America/Jamaica",
    "curr_es": "Dólar jamaiquino (JMD)",
    "curr_en": "Jamaican Dollar (JMD)"
  },
  "Japan": {
    "tz": "Asia/Tokyo",
    "curr_es": "Yen japonés (JPY)",
    "curr_en": "Japanese Yen (JPY)"
  },
  "Jordan": {
    "tz": "Asia/Amman",
    "curr_es": "Dinar jordano (JOD)",
    "curr_en": "Jordanian Dinar (JOD)"
  },
  "Kazakhstan": {
    "tz": "Asia/Almaty",
    "curr_es": "Tenge kazajo (KZT)",
    "curr_en": "Kazakhstani Tenge (KZT)"
  },
  "Kenya": {
    "tz": "Africa/Nairobi",
    "curr_es": "Chelín keniano (KES)",
    "curr_en": "Kenyan Shilling (KES)"
  },
  "Kosovo": {
    "tz": "Europe/Belgrade",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Kuwait": {
    "tz": "Asia/Kuwait",
    "curr_es": "Dinar kuwaití (KWD)",
    "curr_en": "Kuwaiti Dinar (KWD)"
  },
  "Kyrgyzstan": {
    "tz": "Asia/Bishkek",
    "curr_es": "Som kirguís (KGS)",
    "curr_en": "Kyrgyzstani Som (KGS)"
  },
  "Laos": {
    "tz": "Asia/Vientiane",
    "curr_es": "Kip laosiano (LAK)",
    "curr_en": "Lao Kip (LAK)"
  },
  "Latvia": {
    "tz": "Europe/Riga",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Lebanon": {
    "tz": "Asia/Beirut",
    "curr_es": "Libra libanesa (LBP)",
    "curr_en": "Lebanese Pound (LBP)"
  },
  "Lesotho": {
    "tz": "Africa/Maseru",
    "curr_es": "Loti de Lesoto (LSL)",
    "curr_en": "Lesotho Loti (LSL)"
  },
  "Liberia": {
    "tz": "Africa/Monrovia",
    "curr_es": "Dólar liberiano (LRD)",
    "curr_en": "Liberian Dollar (LRD)"
  },
  "Libya": {
    "tz": "Africa/Tripoli",
    "curr_es": "Dinar libio (LYD)",
    "curr_en": "Libyan Dinar (LYD)"
  },
  "Lithuania": {
    "tz": "Europe/Vilnius",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Luxembourg": {
    "tz": "Europe/Luxembourg",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Madagascar": {
    "tz": "Indian/Antananarivo",
    "curr_es": "Ariary malgache (MGA)",
    "curr_en": "Malagasy Ariary (MGA)"
  },
  "Malawi": {
    "tz": "Africa/Blantyre",
    "curr_es": "Kwacha malauí (MWK)",
    "curr_en": "Malawian Kwacha (MWK)"
  },
  "Malaysia": {
    "tz": "Asia/Kuala_Lumpur",
    "curr_es": "Ringgit malasio (MYR)",
    "curr_en": "Malaysian Ringgit (MYR)"
  },
  "Mali": {
    "tz": "Africa/Bamako",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Mauritania": {
    "tz": "Africa/Nouakchott",
    "curr_es": "Uguiya mauritana (MRU)",
    "curr_en": "Mauritanian Ouguiya (MRU)"
  },
  "Mexico": {
    "tz": "America/Mexico_City",
    "curr_es": "Peso mexicano (MXN)",
    "curr_en": "Mexican Peso (MXN)"
  },
  "Moldova": {
    "tz": "Europe/Chisinau",
    "curr_es": "Leu moldavo (MDL)",
    "curr_en": "Moldovan Leu (MDL)"
  },
  "Mongolia": {
    "tz": "Asia/Ulaanbaatar",
    "curr_es": "Tugrik mongol (MNT)",
    "curr_en": "Mongolian Tögrög (MNT)"
  },
  "Montenegro": {
    "tz": "Europe/Podgorica",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Morocco": {
    "tz": "Africa/Casablanca",
    "curr_es": "Dírham marroquí (MAD)",
    "curr_en": "Moroccan Dirham (MAD)"
  },
  "Mozambique": {
    "tz": "Africa/Maputo",
    "curr_es": "Metical mozambiqueño (MZN)",
    "curr_en": "Mozambican Metical (MZN)"
  },
  "Myanmar": {
    "tz": "Asia/Yangon",
    "curr_es": "Kyat birmano (MMK)",
    "curr_en": "Myanmar Kyat (MMK)"
  },
  "N. Cyprus": {
    "tz": "Asia/Nicosia",
    "curr_es": "Lira turca (TRY)",
    "curr_en": "Turkish Lira (TRY)"
  },
  "Namibia": {
    "tz": "Africa/Windhoek",
    "curr_es": "Dólar namibio (NAD)",
    "curr_en": "Namibian Dollar (NAD)"
  },
  "Nepal": {
    "tz": "Asia/Kathmandu",
    "curr_es": "Rupia nepalí (NPR)",
    "curr_en": "Nepalese Rupee (NPR)"
  },
  "Netherlands": {
    "tz": "Europe/Amsterdam",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "New Caledonia": {
    "tz": "Pacific/Noumea",
    "curr_es": "Franco CFP (XPF)",
    "curr_en": "CFP Franc (XPF)"
  },
  "New Zealand": {
    "tz": "Pacific/Auckland",
    "curr_es": "Dólar neozelandés (NZD)",
    "curr_en": "New Zealand Dollar (NZD)"
  },
  "Nicaragua": {
    "tz": "America/Managua",
    "curr_es": "Córdoba nicaragüense (NIO)",
    "curr_en": "Nicaraguan Córdoba (NIO)"
  },
  "Niger": {
    "tz": "Africa/Niamey",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Nigeria": {
    "tz": "Africa/Lagos",
    "curr_es": "Naira nigeriana (NGN)",
    "curr_en": "Nigerian Naira (NGN)"
  },
  "North Korea": {
    "tz": "Asia/Pyongyang",
    "curr_es": "Won norcoreano (KPW)",
    "curr_en": "North Korean Won (KPW)"
  },
  "North Macedonia": {
    "tz": "Europe/Skopje",
    "curr_es": "Denar macedonio (MKD)",
    "curr_en": "Macedonian Denar (MKD)"
  },
  "Norway": {
    "tz": "Europe/Oslo",
    "curr_es": "Corona noruega (NOK)",
    "curr_en": "Norwegian Krone (NOK)"
  },
  "Oman": {
    "tz": "Asia/Muscat",
    "curr_es": "Rial omaní (OMR)",
    "curr_en": "Omani Rial (OMR)"
  },
  "Pakistan": {
    "tz": "Asia/Karachi",
    "curr_es": "Rupia pakistaní (PKR)",
    "curr_en": "Pakistani Rupee (PKR)"
  },
  "Palestine": {
    "tz": "Asia/Gaza",
    "curr_es": "Shekel / Dinar",
    "curr_en": "Shekel / Dinar"
  },
  "Panama": {
    "tz": "America/Panama",
    "curr_es": "Balboa panameño (PAB)",
    "curr_en": "Panamanian Balboa (PAB)"
  },
  "Papua New Guinea": {
    "tz": "Pacific/Port_Moresby",
    "curr_es": "Kina de Papúa Nueva Guinea (PGK)",
    "curr_en": "Papua New Guinean Kina (PGK)"
  },
  "Paraguay": {
    "tz": "America/Asuncion",
    "curr_es": "Guaraní paraguayo (PYG)",
    "curr_en": "Paraguayan Guaraní (PYG)"
  },
  "Peru": {
    "tz": "America/Lima",
    "curr_es": "Sol peruano (PEN)",
    "curr_en": "Peruvian Sol (PEN)"
  },
  "Philippines": {
    "tz": "Asia/Manila",
    "curr_es": "Peso filipino (PHP)",
    "curr_en": "Philippine Peso (PHP)"
  },
  "Poland": {
    "tz": "Europe/Warsaw",
    "curr_es": "Zloty polaco (PLN)",
    "curr_en": "Polish Zloty (PLN)"
  },
  "Portugal": {
    "tz": "Europe/Lisbon",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Puerto Rico": {
    "tz": "America/Puerto_Rico",
    "curr_es": "Dólar estadounidense (USD)",
    "curr_en": "United States Dollar (USD)"
  },
  "Qatar": {
    "tz": "Asia/Qatar",
    "curr_es": "Riyal catarí (QAR)",
    "curr_en": "Qatari Riyal (QAR)"
  },
  "Romania": {
    "tz": "Europe/Bucharest",
    "curr_es": "Leu rumano (RON)",
    "curr_en": "Romanian Leu (RON)"
  },
  "Russia": {
    "tz": "Europe/Moscow",
    "curr_es": "Rublo ruso (RUB)",
    "curr_en": "Russian Ruble (RUB)"
  },
  "Rwanda": {
    "tz": "Africa/Kigali",
    "curr_es": "Franco ruandés (RWF)",
    "curr_en": "Rwandan Franc (RWF)"
  },
  "Saudi Arabia": {
    "tz": "Asia/Riyadh",
    "curr_es": "Riyal saudí (SAR)",
    "curr_en": "Saudi Riyal (SAR)"
  },
  "Senegal": {
    "tz": "Africa/Dakar",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Serbia": {
    "tz": "Europe/Belgrade",
    "curr_es": "Dinar serbio (RSD)",
    "curr_en": "Serbian Dinar (RSD)"
  },
  "Sierra Leone": {
    "tz": "Africa/Freetown",
    "curr_es": "Leone de Sierra Leona (SLE)",
    "curr_en": "Sierra Leonean Leone (SLE)"
  },
  "Slovakia": {
    "tz": "Europe/Bratislava",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Slovenia": {
    "tz": "Europe/Ljubljana",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Solomon Is.": {
    "tz": "Pacific/Guadalcanal",
    "curr_es": "Dólar de las Islas Salomón (SBD)",
    "curr_en": "Solomon Islands Dollar (SBD)"
  },
  "Somalia": {
    "tz": "Africa/Mogadishu",
    "curr_es": "Chelín somalí (SOS)",
    "curr_en": "Somali Shilling (SOS)"
  },
  "Somaliland": {
    "tz": "Africa/Mogadishu",
    "curr_es": "Chelín de Somalilandia",
    "curr_en": "Somaliland Shilling"
  },
  "South Africa": {
    "tz": "Africa/Johannesburg",
    "curr_es": "Rand sudafricano (ZAR)",
    "curr_en": "South African Rand (ZAR)"
  },
  "South Korea": {
    "tz": "Asia/Seoul",
    "curr_es": "Won surcoreano (KRW)",
    "curr_en": "South Korean Won (KRW)"
  },
  "South Sudan": {
    "tz": "Africa/Juba",
    "curr_es": "Libra sursudanesa (SSP)",
    "curr_en": "South Sudanese Pound (SSP)"
  },
  "Spain": {
    "tz": "Europe/Madrid",
    "curr_es": "Euro (EUR)",
    "curr_en": "Euro (EUR)"
  },
  "Sri Lanka": {
    "tz": "Asia/Colombo",
    "curr_es": "Rupia de Sri Lanka (LKR)",
    "curr_en": "Sri Lankan Rupee (LKR)"
  },
  "Sudan": {
    "tz": "Africa/Khartoum",
    "curr_es": "Libra sudanesa (SDG)",
    "curr_en": "Sudanese Pound (SDG)"
  },
  "Suriname": {
    "tz": "America/Paramaribo",
    "curr_es": "Dólar surinamés (SRD)",
    "curr_en": "Surinamese Dollar (SRD)"
  },
  "Sweden": {
    "tz": "Europe/Stockholm",
    "curr_es": "Corona sueca (SEK)",
    "curr_en": "Swedish Krona (SEK)"
  },
  "Switzerland": {
    "tz": "Europe/Zurich",
    "curr_es": "Franco suizo (CHF)",
    "curr_en": "Swiss Franc (CHF)"
  },
  "Syria": {
    "tz": "Asia/Damascus",
    "curr_es": "Libra siria (SYP)",
    "curr_en": "Syrian Pound (SYP)"
  },
  "Taiwan": {
    "tz": "Asia/Taipei",
    "curr_es": "Nuevo dólar taiwanés (TWD)",
    "curr_en": "New Taiwan Dollar (TWD)"
  },
  "Tajikistan": {
    "tz": "Asia/Dushanbe",
    "curr_es": "Somoni tayiko (TJS)",
    "curr_en": "Tajikistani Somoni (TJS)"
  },
  "Tanzania": {
    "tz": "Africa/Dar_es_Salaam",
    "curr_es": "Chelín tanzano (TZS)",
    "curr_en": "Tanzanian Shilling (TZS)"
  },
  "Thailand": {
    "tz": "Asia/Bangkok",
    "curr_es": "Baht tailandés (THB)",
    "curr_en": "Thai Baht (THB)"
  },
  "Timor-Leste": {
    "tz": "Asia/Dili",
    "curr_es": "Dólar estadounidense (USD)",
    "curr_en": "United States Dollar (USD)"
  },
  "Togo": {
    "tz": "Africa/Lome",
    "curr_es": "Franco CFA (XOF)",
    "curr_en": "West African CFA Franc (XOF)"
  },
  "Trinidad and Tobago": {
    "tz": "America/Port_of_Spain",
    "curr_es": "Dólar de Trinidad y Tobago (TTD)",
    "curr_en": "Trinidad and Tobago Dollar (TTD)"
  },
  "Tunisia": {
    "tz": "Africa/Tunis",
    "curr_es": "Dinar tunecino (TND)",
    "curr_en": "Tunisian Dinar (TND)"
  },
  "Turkey": {
    "tz": "Europe/Istanbul",
    "curr_es": "Lira turca (TRY)",
    "curr_en": "Turkish Lira (TRY)"
  },
  "Turkmenistan": {
    "tz": "Asia/Ashgabat",
    "curr_es": "Manat turcomano (TMT)",
    "curr_en": "Turkmenistani Manat (TMT)"
  },
  "Uganda": {
    "tz": "Africa/Kampala",
    "curr_es": "Chelín ugandés (UGX)",
    "curr_en": "Ugandan Shilling (UGX)"
  },
  "Ukraine": {
    "tz": "Europe/Kyiv",
    "curr_es": "Grivna ucraniana (UAH)",
    "curr_en": "Ukrainian Hryvnia (UAH)"
  },
  "United Arab Emirates": {
    "tz": "Asia/Dubai",
    "curr_es": "Dírham de los EAU (AED)",
    "curr_en": "United Arab Emirates Dirham (AED)"
  },
  "United Kingdom": {
    "tz": "Europe/London",
    "curr_es": "Libra esterlina (GBP)",
    "curr_en": "Pound Sterling (GBP)"
  },
  "United States of America": {
    "tz": "America/New_York",
    "curr_es": "Dólar estadounidense (USD)",
    "curr_en": "United States Dollar (USD)"
  },
  "Uruguay": {
    "tz": "America/Montevideo",
    "curr_es": "Peso uruguayo (UYU)",
    "curr_en": "Uruguayan Peso (UYU)"
  },
  "Uzbekistan": {
    "tz": "Asia/Tashkent",
    "curr_es": "Som uzbeko (UZS)",
    "curr_en": "Uzbekistani Som (UZS)"
  },
  "Vanuatu": {
    "tz": "Pacific/Efate",
    "curr_es": "Vatu vanuatuense (VUV)",
    "curr_en": "Vanuatu Vatu (VUV)"
  },
  "Venezuela": {
    "tz": "America/Caracas",
    "curr_es": "Bolívar digital (VES)",
    "curr_en": "Venezuelan Bolívar (VES)"
  },
  "Vietnam": {
    "tz": "Asia/Ho_Chi_Minh",
    "curr_es": "Dong vietnamita (VND)",
    "curr_en": "Vietnamese Dong (VND)"
  },
  "W. Sahara": {
    "tz": "Africa/El_Aaiun",
    "curr_es": "Dírham marroquí (MAD)",
    "curr_en": "Moroccan Dirham (MAD)"
  },
  "Yemen": {
    "tz": "Asia/Aden",
    "curr_es": "Rial yemení (YER)",
    "curr_en": "Yemeni Rial (YER)"
  },
  "Zambia": {
    "tz": "Africa/Lusaka",
    "curr_es": "Kwacha zambiano (ZMW)",
    "curr_en": "Zambian Kwacha (ZMW)"
  },
  "Zimbabwe": {
    "tz": "Africa/Harare",
    "curr_es": "ZiG / Dólar de Zimbabue",
    "curr_en": "Zimbabwe Gold (ZiG) / USD"
  }
}

OCEANS_AND_SEAS = [
  {
    "id": "caribbean_sea",
    "name_es": "Mar Caribe",
    "name_en": "Caribbean Sea",
    "name_ja": "カリブ海",
    "name_zh": "加勒比海",
    "name_ar": "البحر الكاريبي",
    "icon": "🏝️",
    "priority": 1,
    "radiusDeg": 7.0,
    "centroid": [
      -75.0,
      15.0
    ],
    "bounds": {
      "minLon": -88.0,
      "maxLon": -60.0,
      "minLat": 9.0,
      "maxLat": 22.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~2.75M km²",
      "depth": "Fosa de Caimán (7.686 m)",
      "fact": "Famoso por sus aguas turquesas, arrecifes de coral y más de 7.000 islas paradisíacas."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~2.75M km²",
      "depth": "Cayman Trench (7,686 m)",
      "fact": "Famous for turquoise waters, coral reefs, and over 7,000 tropical islands."
    },
    "ja": {
      "type": "付属海 / 縁海",
      "area": "約275万 km²",
      "depth": "ケイマン海溝 (7,686 m)",
      "fact": "エメラルドグリーンの美しい海、珊瑚礁、7,000以上の島々で世界的に有名です。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约275万 km²",
      "depth": "开曼海沟 (7,686 m)",
      "fact": "以清澈的绿松石色海水、壮丽珊瑚礁及7000多座热带岛屿闻名于世。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~2.75 مليون كم²",
      "depth": "خندق كايمان (7,686 م)",
      "fact": "يشتهر بمياهه الفيروزية الساحرة وشعابه المرجانية وأكثر من 7000 جزيرة استوائية."
    }
  },
  {
    "id": "mediterranean_sea",
    "name_es": "Mar Mediterráneo",
    "name_en": "Mediterranean Sea",
    "name_ja": "地中海",
    "name_zh": "地中海",
    "name_ar": "البحر الأبيض المتوسط",
    "icon": "🏛️",
    "priority": 1,
    "radiusDeg": 8.0,
    "centroid": [
      18.0,
      35.0
    ],
    "bounds": {
      "minLon": -5.0,
      "maxLon": 36.0,
      "minLat": 30.0,
      "maxLat": 45.0
    },
    "es": {
      "type": "Mar Interior",
      "area": "~2.5M km²",
      "depth": "Fosa de Matapán (5.267 m)",
      "fact": "Cuna de civilizaciones occidentales milenarias: Egipto, Grecia, Roma y Fenicia."
    },
    "en": {
      "type": "Inland Sea",
      "area": "~2.5M km²",
      "depth": "Calypso Deep (5,267 m)",
      "fact": "Cradle of ancient Western civilizations: Egypt, Greece, Rome, and Phoenicia."
    },
    "ja": {
      "type": "地中海 / 内海",
      "area": "約250万 km²",
      "depth": "カリプソ海淵 (5,267 m)",
      "fact": "古代エジプト、ギリシャ、ローマ、フェニキアなど西洋文明発祥のゆりかごです。"
    },
    "zh": {
      "type": "陆间海 / 内海",
      "area": "约250万 km²",
      "depth": "卡吕普索海渊 (5,267 m)",
      "fact": "古埃及、古希腊、古罗马和腓尼基等古代西方文明的发祥摇篮。"
    },
    "ar": {
      "type": "بحر داخلي",
      "area": "~2.5 مليون كم²",
      "depth": "منخفض كاليبسو (5,267 م)",
      "fact": "مهد الحضارات الغربية القديمة العريقة: مصر، اليونان، روما، وفينيقيا."
    }
  },
  {
    "id": "red_sea",
    "name_es": "Mar Rojo",
    "name_en": "Red Sea",
    "name_ja": "紅海",
    "name_zh": "红海",
    "name_ar": "البحر الأحمر",
    "icon": "🐠",
    "priority": 1,
    "radiusDeg": 5.0,
    "centroid": [
      38.0,
      22.0
    ],
    "bounds": {
      "minLon": 32.0,
      "maxLon": 44.0,
      "minLat": 12.0,
      "maxLat": 30.0
    },
    "es": {
      "type": "Golfo / Mar Interior",
      "area": "~438.000 km²",
      "depth": "Fosa de Suakin (3.040 m)",
      "fact": "Uno de los mares más salinos y cálidos del mundo, con una biodiversidad marina única."
    },
    "en": {
      "type": "Inland Sea",
      "area": "~438,000 km²",
      "depth": "Suakin Deep (3,040 m)",
      "fact": "One of the saltiest and warmest seas on Earth, with extraordinary marine life."
    },
    "ja": {
      "type": "内海 / 地溝海",
      "area": "約43.8万 km²",
      "depth": "スアキン海淵 (3,040 m)",
      "fact": "世界で最も塩分濃度が高く温かい海の一つで、独自の海洋生態系を誇ります。"
    },
    "zh": {
      "type": "陆间海",
      "area": "约43.8万 km²",
      "depth": "萨瓦金海渊 (3,040 m)",
      "fact": "世界上盐度最高、水温最暖的海洋之一，拥有极其丰富的独特海洋生物。"
    },
    "ar": {
      "type": "بحر داخلي",
      "area": "~438 ألف كم²",
      "depth": "خندق سواكن (3,040 م)",
      "fact": "من أكثر بحار العالم ملوحة ودفئاً، ويضم تنوعاً بيولوجياً بحرياً استثنائياً."
    }
  },
  {
    "id": "black_sea",
    "name_es": "Mar Negro",
    "name_en": "Black Sea",
    "name_ja": "黒海",
    "name_zh": "黑海",
    "name_ar": "البحر الأسود",
    "icon": "🌊",
    "priority": 1,
    "radiusDeg": 5.0,
    "centroid": [
      34.0,
      43.5
    ],
    "bounds": {
      "minLon": 27.0,
      "maxLon": 42.0,
      "minLat": 40.5,
      "maxLat": 47.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~436.000 km²",
      "depth": "Cuenca del Mar Negro (2.212 m)",
      "fact": "Posee la mayor masa de agua anóxica (sin oxígeno) del mundo en sus profundidades."
    },
    "en": {
      "type": "Inland Sea",
      "area": "~436,000 km²",
      "depth": "Euxine Abyssal (2,212 m)",
      "fact": "Contains the largest body of anoxic (oxygen-depleted) water in the world."
    },
    "ja": {
      "type": "内海",
      "area": "約43.6万 km²",
      "depth": "黒海海盆 (2,212 m)",
      "fact": "深海層に酸素がほとんど含まれない「無酸素水域」としては世界最大です。"
    },
    "zh": {
      "type": "内海",
      "area": "约43.6万 km²",
      "depth": "黑海海盆 (2,212 m)",
      "fact": "拥有全球面积最大、深水层几乎完全缺氧的特异水体构造。"
    },
    "ar": {
      "type": "بحر داخلي",
      "area": "~436 ألف كم²",
      "depth": "حوض البحر الأسود (2,212 م)",
      "fact": "يحتوي على أكبر مسطح مائي محروم من الأكسجين في أعماقه على مستوى العالم."
    }
  },
  {
    "id": "baltic_sea",
    "name_es": "Mar Báltico",
    "name_en": "Baltic Sea",
    "name_ja": "バルト海",
    "name_zh": "波罗的海",
    "name_ar": "بحر البلطيق",
    "icon": "⚓",
    "priority": 1,
    "radiusDeg": 5.0,
    "centroid": [
      20.0,
      58.0
    ],
    "bounds": {
      "minLon": 9.5,
      "maxLon": 30.0,
      "minLat": 53.0,
      "maxLat": 66.0
    },
    "es": {
      "type": "Mar Interior Salobre",
      "area": "~377.000 km²",
      "depth": "Fosa de Landsort (459 m)",
      "fact": "Es la mayor masa de agua salobre (baja salinidad) del planeta."
    },
    "en": {
      "type": "Brackish Sea",
      "area": "~377,000 km²",
      "depth": "Landsort Deep (459 m)",
      "fact": "The largest body of brackish water (low salinity) in the world."
    },
    "ja": {
      "type": "汽水海 / 内海",
      "area": "約37.7万 km²",
      "depth": "ランツオルト海淵 (459 m)",
      "fact": "塩分濃度が非常に低い「汽水域」として世界最大級の広さを誇ります。"
    },
    "zh": {
      "type": "半咸水内海",
      "area": "约37.7万 km²",
      "depth": "兰斯奥特海渊 (459 m)",
      "fact": "世界上盐度极低的半咸水水域中面积最大的海域。"
    },
    "ar": {
      "type": "بحر قليل الملوحة",
      "area": "~377 ألف كم²",
      "depth": "منخفض لاندسورت (459 م)",
      "fact": "أكبر مسطح مائي معتدل الملوحة (شبه عذب) في كوكب الأرض."
    }
  },
  {
    "id": "north_sea",
    "name_es": "Mar del Norte",
    "name_en": "North Sea",
    "name_ja": "北海",
    "name_zh": "北海",
    "name_ar": "بحر الشمال",
    "icon": "⚓",
    "priority": 1,
    "radiusDeg": 4.5,
    "centroid": [
      3.0,
      56.0
    ],
    "bounds": {
      "minLon": -4.0,
      "maxLon": 9.0,
      "minLat": 51.0,
      "maxLat": 61.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~575.000 km²",
      "depth": "Fosa Noruega (700 m)",
      "fact": "Rico en reservas de petróleo y gas, y crucial vía comercial de Europa."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~575,000 km²",
      "depth": "Norwegian Trench (700 m)",
      "fact": "Rich in oil, natural gas reserves, and a major European trade route."
    },
    "ja": {
      "type": "縁海",
      "area": "約57.5万 km²",
      "depth": "ノルウェー海溝 (700 m)",
      "fact": "豊富な海底石油・天然ガス田を有し、欧州の重要航路となっています。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约57.5万 km²",
      "depth": "挪威海沟 (700 m)",
      "fact": "蕴藏丰富的海底石油和天然气，是欧洲最繁忙的核心航道之一。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~575 ألف كم²",
      "depth": "الخندق النرويجي (700 م)",
      "fact": "غني باحتياطيات النفط والغاز الطبيعي وممر تجاري حيوي لأوروبا."
    }
  },
  {
    "id": "caspian_sea",
    "name_es": "Mar Caspio",
    "name_en": "Caspian Sea",
    "name_ja": "カスピ海",
    "name_zh": "里海",
    "name_ar": "بحر قزوين",
    "icon": "🌊",
    "priority": 1,
    "radiusDeg": 5.0,
    "centroid": [
      51.0,
      42.0
    ],
    "bounds": {
      "minLon": 46.5,
      "maxLon": 55.0,
      "minLat": 36.5,
      "maxLat": 47.0
    },
    "es": {
      "type": "Lago Endorreico / Mar Cerrado",
      "area": "~371.000 km²",
      "depth": "Cuenca Sur (1.025 m)",
      "fact": "Es el cuerpo de agua interior cerrado más grande del planeta."
    },
    "en": {
      "type": "Endorheic Lake / Inland Sea",
      "area": "~371,000 km²",
      "depth": "South Caspian Depression (1,025 m)",
      "fact": "The largest enclosed inland body of water on Earth."
    },
    "ja": {
      "type": "内陸湖 / 内海",
      "area": "約37.1万 km²",
      "depth": "南カスピ海盆 (1,025 m)",
      "fact": "世界最大の閉鎖性内陸水域であり、チョウザメの生息地としても有名です。"
    },
    "zh": {
      "type": "内陆湖 / 咸水海",
      "area": "约37.1万 km²",
      "depth": "南里海海盆 (1,025 m)",
      "fact": "地球上面积最大的封闭内陆水体，也是顶级鱼子酱的主产地。"
    },
    "ar": {
      "type": "بحيرة حبيسة / بحر مغلق",
      "area": "~371 ألف كم²",
      "depth": "منخفض قزوين الجنوبي (1,025 م)",
      "fact": "أكبر مسطح مائي داخلي مغلق على كوكب الأرض وموطن لأفخر أنواع الكافيار."
    }
  },
  {
    "id": "persian_gulf",
    "name_es": "Golfo Pérsico / Arábigo",
    "name_en": "Persian Gulf",
    "name_ja": "ペルシャ湾",
    "name_zh": "波斯湾",
    "name_ar": "الخليج العربي",
    "icon": "🛢️",
    "priority": 2,
    "radiusDeg": 4.5,
    "centroid": [
      52.0,
      26.5
    ],
    "bounds": {
      "minLon": 48.0,
      "maxLon": 56.5,
      "minLat": 24.0,
      "maxLat": 30.0
    },
    "es": {
      "type": "Golfo Marino",
      "area": "~251.000 km²",
      "depth": "Estrecho de Ormuz (90 m)",
      "fact": "Concentra las mayores reservas de hidrocarburos del planeta."
    },
    "en": {
      "type": "Mediterranean Sea Basin",
      "area": "~251,000 km²",
      "depth": "Strait of Hormuz (90 m)",
      "fact": "Holds the world's largest concentration of crude oil reserves."
    },
    "ja": {
      "type": "湾 / 浅海",
      "area": "約25.1万 km²",
      "depth": "ホルムズ海峡 (90 m)",
      "fact": "地球上で最も原油・天然ガス埋蔵量が集中する地政学的重要水域です。"
    },
    "zh": {
      "type": "海湾",
      "area": "约25.1万 km²",
      "depth": "霍尔木兹海峡 (90 m)",
      "fact": "汇聚了全球最密集的石油储量，霍尔木兹海峡是能源咽喉。"
    },
    "ar": {
      "type": "خليج بحري",
      "area": "~251 ألف كم²",
      "depth": "مضيق هرمز (90 م)",
      "fact": "يحتضن أكبر تركيز لاحتياطيات النفط والغاز الطبيعي في العالم."
    }
  },
  {
    "id": "gulf_of_mexico",
    "name_es": "Golfo de México",
    "name_en": "Gulf of Mexico",
    "name_ja": "メキシコ湾",
    "name_zh": "墨西哥湾",
    "name_ar": "خليج المكسيك",
    "icon": "🏝️",
    "priority": 2,
    "radiusDeg": 6.5,
    "centroid": [
      -90.0,
      25.0
    ],
    "bounds": {
      "minLon": -98.0,
      "maxLon": -81.0,
      "minLat": 18.0,
      "maxLat": 30.5
    },
    "es": {
      "type": "Golfo Oceánico",
      "area": "~1.6M km²",
      "depth": "Sima de Sigsbee (4.384 m)",
      "fact": "Origina la corriente del Golfo, que lleva calor hacia el norte de Europa."
    },
    "en": {
      "type": "Oceanic Gulf",
      "area": "~1.6M km²",
      "depth": "Sigsbee Deep (4,384 m)",
      "fact": "Origin of the Gulf Stream, carrying warmth to northern Europe."
    },
    "ja": {
      "type": "大洋湾",
      "area": "約160万 km²",
      "depth": "シグスビー海淵 (4,384 m)",
      "fact": "欧州に温暖な気候をもたらす巨大海流「メキシコ湾流」の源です。"
    },
    "zh": {
      "type": "洋湾",
      "area": "约160万 km²",
      "depth": "席格斯比深海平原 (4,384 m)",
      "fact": "北大西洋暖流的发源地，深刻调节着欧洲大陆的气候温和度。"
    },
    "ar": {
      "type": "خليج محيطي",
      "area": "~1.6 مليون كم²",
      "depth": "منخفض سيغسبي (4,384 م)",
      "fact": "منبع تيار الخليج الدافئ الذي ينقل الحرارة إلى شمال القارة الأوروبية."
    }
  },
  {
    "id": "sea_of_japan",
    "name_es": "Mar del Japón / Mar del Este",
    "name_en": "Sea of Japan",
    "name_ja": "日本海",
    "name_zh": "日本海",
    "name_ar": "بحر اليابان",
    "icon": "🌊",
    "priority": 2,
    "radiusDeg": 6.0,
    "centroid": [
      134.0,
      40.0
    ],
    "bounds": {
      "minLon": 127.0,
      "maxLon": 142.0,
      "minLat": 35.0,
      "maxLat": 52.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~978.000 km²",
      "depth": "Cuenca de Japón (3.742 m)",
      "fact": "Casi cerrado por el archipiélago japonés y la península coreana."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~978,000 km²",
      "depth": "Japan Basin (3,742 m)",
      "fact": "Nearly enclosed by the Japanese archipelago and Korean peninsula."
    },
    "ja": {
      "type": "縁海",
      "area": "約97.8万 km²",
      "depth": "日本海盆 (3,742 m)",
      "fact": "日本列島とユーラシア大陸に囲まれた豊かな水産資源の海です。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约97.8万 km²",
      "depth": "日本海盆 (3,742 m)",
      "fact": "被日本列岛、千岛群岛和亚洲大陆近乎封闭包围的边缘海。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~978 ألف كم²",
      "depth": "حوض اليابان (3,742 م)",
      "fact": "مسطح مائي شبه مغلق بأرخبيل الجزر اليابانية وشبه الجزيرة الكورية."
    }
  },
  {
    "id": "coral_sea",
    "name_es": "Mar del Coral",
    "name_en": "Coral Sea",
    "name_ja": "珊瑚海",
    "name_zh": "珊瑚海",
    "name_ar": "بحر المرجان",
    "icon": "🐠",
    "priority": 2,
    "radiusDeg": 8.0,
    "centroid": [
      155.0,
      -18.0
    ],
    "bounds": {
      "minLon": 142.0,
      "maxLon": 170.0,
      "minLat": -30.0,
      "maxLat": -10.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~4.8M km²",
      "depth": "Fosa de las Nuevas Hébridas (7.570 m)",
      "fact": "Alberga la Gran Barrera de Coral, el mayor ser vivo visible desde el espacio."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~4.8M km²",
      "depth": "New Hebrides Trench (7,570 m)",
      "fact": "Home to the Great Barrier Reef, the largest living structure on Earth."
    },
    "ja": {
      "type": "縁海",
      "area": "約480万 km²",
      "depth": "ニューヘブリディーズ海溝 (7,570 m)",
      "fact": "宇宙からも見える地球最大の生命体構造「グレートバリアリーフ」を育みます。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约480万 km²",
      "depth": "新赫布里底海沟 (7,570 m)",
      "fact": "孕育了大堡礁——从太空都能清晰看见的地球最大生物构造。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~4.8 مليون كم²",
      "depth": "خندق نيو هيبريدس (7,570 م)",
      "fact": "موطن الحاجز المرجاني العظيم، أضخم هيكل حي على كوكب الأرض يُرى من الفضاء."
    }
  },
  {
    "id": "arabian_sea",
    "name_es": "Mar Arábigo",
    "name_en": "Arabian Sea",
    "name_ja": "アラビア海",
    "name_zh": "阿拉伯海",
    "name_ar": "بحر العرب",
    "icon": "🌊",
    "priority": 2,
    "radiusDeg": 8.0,
    "centroid": [
      65.0,
      16.0
    ],
    "bounds": {
      "minLon": 50.0,
      "maxLon": 78.0,
      "minLat": 5.0,
      "maxLat": 26.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~3.86M km²",
      "depth": "Cuenca Arábiga (4.652 m)",
      "fact": "Histórica ruta de comercio marítimo de las especias y la seda."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~3.86M km²",
      "depth": "Arabian Basin (4,652 m)",
      "fact": "Historic maritime trade route for spices and silks."
    },
    "ja": {
      "type": "縁海",
      "area": "約386万 km²",
      "depth": "アラビア海盆 (4,652 m)",
      "fact": "古くからシルクロードや香辛料貿易の海上交通の要衝でした。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约386万 km²",
      "depth": "阿拉伯海盆 (4,652 m)",
      "fact": "古代海上丝绸之路与香料贸易至关重要的枢纽水域。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~3.86 مليون كم²",
      "depth": "حوض بحر العرب (4,652 م)",
      "fact": "طريق التجارة البحرية التاريخي الحاسم لتجارة التوابل والحرير."
    }
  },
  {
    "id": "south_china_sea",
    "name_es": "Mar de la China Meridional",
    "name_en": "South China Sea",
    "name_ja": "南シナ海",
    "name_zh": "南海 (南中国海)",
    "name_ar": "بحر الصين الجنوبي",
    "icon": "🌊",
    "priority": 2,
    "radiusDeg": 8.0,
    "centroid": [
      114.0,
      12.0
    ],
    "bounds": {
      "minLon": 102.0,
      "maxLon": 122.0,
      "minLat": 1.0,
      "maxLat": 23.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~3.5M km²",
      "depth": "Fosa de Manila (5.014 m)",
      "fact": "Por aquí transita más de un tercio del comercio marítimo de todo el planeta."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~3.5M km²",
      "depth": "Manila Trench (5,014 m)",
      "fact": "More than one-third of global maritime trade passes through here."
    },
    "ja": {
      "type": "縁海",
      "area": "約350万 km²",
      "depth": "マニラ海溝 (5,014 m)",
      "fact": "世界の海上貿易の3分の1以上が通過する極めて重要な国際航路です。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约350万 km²",
      "depth": "马尼拉海沟 (5,014 m)",
      "fact": "全球超过三分之一的国际海上商船贸易量在此水域穿梭。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~3.5 مليون كم²",
      "depth": "خندق مانيلا (5,014 م)",
      "fact": "يمر عبره أكثر من ثلث إجمالي التجارة البحرية العالمية للشحن الدولي."
    }
  },
  {
    "id": "bering_sea",
    "name_es": "Mar de Bering",
    "name_en": "Bering Sea",
    "name_ja": "ベーリング海",
    "name_zh": "白令海",
    "name_ar": "بحر بيرنغ",
    "icon": "🧊",
    "priority": 2,
    "radiusDeg": 7.0,
    "centroid": [
      -175.0,
      58.0
    ],
    "bounds": {
      "minLon": 160.0,
      "maxLon": -158.0,
      "minLat": 50.0,
      "maxLat": 66.0
    },
    "es": {
      "type": "Mar Marginal",
      "area": "~2.0M km²",
      "depth": "Cuenca Bowers (4.097 m)",
      "fact": "Separa Asia de América a través del histórico Estrecho de Bering."
    },
    "en": {
      "type": "Marginal Sea",
      "area": "~2.0M km²",
      "depth": "Bowers Basin (4,097 m)",
      "fact": "Separates Asia from the Americas via the Bering Strait."
    },
    "ja": {
      "type": "縁海",
      "area": "約200万 km²",
      "depth": "バウワーズ海盆 (4,097 m)",
      "fact": "ベーリング海峡を通じてアジア大陸と北米大陸を隔てる極海です。"
    },
    "zh": {
      "type": "陆缘海",
      "area": "约200万 km²",
      "depth": "鲍尔斯海盆 (4,097 m)",
      "fact": "通过白令海峡将亚洲与北美两大洲紧紧分隔开来。"
    },
    "ar": {
      "type": "بحر هامشي",
      "area": "~2.0 مليون كم²",
      "depth": "حوض باورز (4,097 م)",
      "fact": "يفصل قارة آسيا عن الأمريكتين عبر مضيق بيرنغ التاريخي."
    }
  },
  {
    "id": "great_lakes",
    "name_es": "Grandes Lagos de Norteamérica",
    "name_en": "Great Lakes of North America",
    "name_ja": "北米五大湖",
    "name_zh": "北美五大湖",
    "name_ar": "البحيرات العظمى لأمريكا الشمالية",
    "icon": "🏞️",
    "priority": 2,
    "radiusDeg": 5.0,
    "centroid": [
      -84.0,
      45.0
    ],
    "bounds": {
      "minLon": -92.0,
      "maxLon": -76.0,
      "minLat": 41.0,
      "maxLat": 49.0
    },
    "es": {
      "type": "Sistema de Lagos Glaciares",
      "area": "~244.000 km²",
      "depth": "Lago Superior (406 m)",
      "fact": "Contienen el 21% de toda el agua dulce superficial líquida del planeta Tierra."
    },
    "en": {
      "type": "Glacial Freshwater Lakes",
      "area": "~244,000 km²",
      "depth": "Lake Superior (406 m)",
      "fact": "Contain 21% of the world's surface fresh water."
    },
    "ja": {
      "type": "氷河性淡水湖沼群",
      "area": "約24.4万 km²",
      "depth": "スペリオル湖 (406 m)",
      "fact": "地球上の地表に存在する液体の淡水の約21%を蓄えています。"
    },
    "zh": {
      "type": "冰川淡水湖群",
      "area": "约24.4万 km²",
      "depth": "苏必利尔湖 (406 m)",
      "fact": "蕴藏着全地球地表液态淡水总量的21%。"
    },
    "ar": {
      "type": "بحيرات مياه عذبة جليدية",
      "area": "~244 ألف كم²",
      "depth": "بحيرة سوبيريور (406 م)",
      "fact": "تحتوي على 21% من إجمالي المياه العذبة السطحية السائلة في العالم."
    }
  },
  {
    "id": "sea_of_azov",
    "name_es": "Mar de Azov",
    "name_en": "Sea of Azov",
    "name_ja": "アゾフ海",
    "name_zh": "亚速海",
    "name_ar": "بحر أزوف",
    "icon": "🌊",
    "priority": 2,
    "radiusDeg": 2.5,
    "centroid": [
      36.5,
      46.0
    ],
    "bounds": {
      "minLon": 34.5,
      "maxLon": 39.5,
      "minLat": 45.0,
      "maxLat": 47.5
    },
    "es": {
      "type": "Mar Interior",
      "area": "~39.000 km²",
      "depth": "Máxima de sólo 14 m",
      "fact": "Es el mar más somero (de menor profundidad) del mundo entero."
    },
    "en": {
      "type": "Inland Sea",
      "area": "~39,000 km²",
      "depth": "Maximum depth only 14 m",
      "fact": "The shallowest sea on Earth, connected to the Black Sea."
    },
    "ja": {
      "type": "内海",
      "area": "約3.9万 km²",
      "depth": "最深部わずか 14 m",
      "fact": "地球上で最も水深が浅い海として知られています。"
    },
    "zh": {
      "type": "陆间海",
      "area": "约3.9万 km²",
      "depth": "最深仅 14 m",
      "fact": "全地球平均水深最浅的海洋，通过刻赤海峡连通黑海。"
    },
    "ar": {
      "type": "بحر داخلي",
      "area": "~39 ألف كم²",
      "depth": "أقصى عمق 14 م فقط",
      "fact": "أضحل بحر على الإطلاق في العالم بأسره، متصل بالبحر الأسود."
    }
  },
  {
    "id": "lake_victoria",
    "name_es": "Lago Victoria",
    "name_en": "Lake Victoria",
    "name_ja": "ビクトリア湖",
    "name_zh": "维多利亚湖",
    "name_ar": "بحيرة فيكتوريا",
    "icon": "🏞️",
    "priority": 2,
    "radiusDeg": 3.0,
    "centroid": [
      33.0,
      -1.0
    ],
    "bounds": {
      "minLon": 31.5,
      "maxLon": 34.8,
      "minLat": -3.0,
      "maxLat": 0.5
    },
    "es": {
      "type": "Gran Lago Tropical",
      "area": "~68.800 km²",
      "depth": "Máxima de 84 m",
      "fact": "Es el lago tropical más grande del mundo y principal naciente del río Nilo."
    },
    "en": {
      "type": "Tropical Lake",
      "area": "~68,800 km²",
      "depth": "Max depth 84 m",
      "fact": "Africa's largest lake and the primary reservoir source of the Nile River."
    },
    "ja": {
      "type": "熱帯湖",
      "area": "約6.88万 km²",
      "depth": "最深部 84 m",
      "fact": "アフリカ最大の湖であり、大河ナイル川の源流となっています。"
    },
    "zh": {
      "type": "热带大型湖泊",
      "area": "约6.88万 km²",
      "depth": "最大深度 84 m",
      "fact": "非洲最大的淡水湖，也是世界第一长河尼罗河的主源头。"
    },
    "ar": {
      "type": "بحيرة استوائية عظمى",
      "area": "~68.8 ألف كم²",
      "depth": "أقصى عمق 84 م",
      "fact": "أكبر بحيرة في أفريقيا والمصدر المائي الرئيسي لنهر النيل العظيم."
    }
  },
  {
    "id": "lake_baikal",
    "name_es": "Lago Baikal",
    "name_en": "Lake Baikal",
    "name_ja": "バイカル湖",
    "name_zh": "贝加尔湖",
    "name_ar": "بحيرة بايكال",
    "icon": "🧊",
    "priority": 2,
    "radiusDeg": 3.0,
    "centroid": [
      107.5,
      53.5
    ],
    "bounds": {
      "minLon": 103.5,
      "maxLon": 110.0,
      "minLat": 51.5,
      "maxLat": 56.0
    },
    "es": {
      "type": "Lago de Falla Tectónica",
      "area": "~31.700 km²",
      "depth": "Fosa de Baikal (1.642 m)",
      "fact": "Es el lago más profundo y antiguo (25M de años) del planeta."
    },
    "en": {
      "type": "Rift Lake",
      "area": "~31,700 km²",
      "depth": "Baikal Rift (1,642 m)",
      "fact": "The oldest (25M years) and deepest lake on Earth."
    },
    "ja": {
      "type": "構造湖",
      "area": "約3.17万 km²",
      "depth": "バイカル断層 (1,642 m)",
      "fact": "世界最深かつ最古 (約2,500万年前) の淡水湖です。"
    },
    "zh": {
      "type": "断陷湖",
      "area": "约3.17万 km²",
      "depth": "贝加尔裂谷 (1,642 m)",
      "fact": "世界上最深、最古老 (约2500万年) 且蓄水量最大的淡水湖。"
    },
    "ar": {
      "type": "بحيرة صدعية تكتونية",
      "area": "~31.7 ألف كم²",
      "depth": "صدع بايكال (1,642 م)",
      "fact": "أعمق وأقدم بحيرة على وجه الأرض (عمرها 25 مليون سنة)."
    }
  },
  {
    "id": "pacific_north",
    "name_es": "Océano Pacífico Norte",
    "name_en": "North Pacific Ocean",
    "name_ja": "北太平洋",
    "name_zh": "北太平洋",
    "name_ar": "شمال المحيط الهادئ",
    "icon": "🌊",
    "priority": 3,
    "radiusDeg": 22.0,
    "centroid": [
      -160.0,
      28.0
    ],
    "bounds": {
      "minLon": 115.0,
      "maxLon": -95.0,
      "minLat": 0.0,
      "maxLat": 66.0
    },
    "es": {
      "type": "Océano",
      "area": "~165.2M km² (Total Pacífico)",
      "depth": "Fosa de las Marianas (11.034 m)",
      "fact": "Es el océano más grande y profundo del planeta Tierra."
    },
    "en": {
      "type": "Ocean",
      "area": "~165.2M km² (Total Pacific)",
      "depth": "Mariana Trench (11,034 m)",
      "fact": "The largest and deepest oceanic division on Earth."
    },
    "ja": {
      "type": "大洋",
      "area": "約1億6,520万 km²",
      "depth": "マリアナ海溝 (11,034 m)",
      "fact": "地球上で最も広大かつ最深の海洋区分です。"
    },
    "zh": {
      "type": "大洋",
      "area": "约1.652亿 km²",
      "depth": "马里亚纳海沟 (11,034 m)",
      "fact": "地球上面积最大、平均水深最深的大洋。"
    },
    "ar": {
      "type": "محيط",
      "area": "~165.2 مليون كم²",
      "depth": "خندق ماريانا (11,034 م)",
      "fact": "أكبر وأعمق مسطح محيطي على الإطلاق في كوكب الأرض."
    }
  },
  {
    "id": "pacific_south",
    "name_es": "Océano Pacífico Sur",
    "name_en": "South Pacific Ocean",
    "name_ja": "南太平洋",
    "name_zh": "南太平洋",
    "name_ar": "جنوب المحيط الهادئ",
    "icon": "🌊",
    "priority": 3,
    "radiusDeg": 22.0,
    "centroid": [
      -120.0,
      -28.0
    ],
    "bounds": {
      "minLon": 140.0,
      "maxLon": -70.0,
      "minLat": -60.0,
      "maxLat": 0.0
    },
    "es": {
      "type": "Océano",
      "area": "~165.2M km² (Total Pacífico)",
      "depth": "Fosa de Tonga (10.882 m)",
      "fact": "Contiene el Punto Nemo, el lugar más inaccesible y remoto del planeta."
    },
    "en": {
      "type": "Ocean",
      "area": "~165.2M km² (Total Pacific)",
      "depth": "Tonga Trench (10,882 m)",
      "fact": "Home to Point Nemo, the oceanic pole of inaccessibility."
    },
    "ja": {
      "type": "大洋",
      "area": "約1億6,520万 km²",
      "depth": "トンガ海溝 (10,882 m)",
      "fact": "地球上で最も陸地から遠い絶海の孤点「ポイント・ネモ」が存在します。"
    },
    "zh": {
      "type": "大洋",
      "area": "约1.652亿 km²",
      "depth": "汤加海沟 (10,882 m)",
      "fact": "拥有全球距离陆地最遥远的极点——尼莫点 (Point Nemo)。"
    },
    "ar": {
      "type": "محيط",
      "area": "~165.2 مليون كم²",
      "depth": "خندق تونغا (10,882 م)",
      "fact": "يحتوي على نقطة نيمو، أبعد نقطة بحرية عن أي يابسة في كوكبنا."
    }
  },
  {
    "id": "atlantic_north",
    "name_es": "Océano Atlántico Norte",
    "name_en": "North Atlantic Ocean",
    "name_ja": "北大西洋",
    "name_zh": "北大西洋",
    "name_ar": "شمال المحيط الأطلسي",
    "icon": "🌊",
    "priority": 3,
    "radiusDeg": 18.0,
    "centroid": [
      -40.0,
      32.0
    ],
    "bounds": {
      "minLon": -80.0,
      "maxLon": -5.0,
      "minLat": 0.0,
      "maxLat": 66.0
    },
    "es": {
      "type": "Océano",
      "area": "~106.5M km² (Total Atlántico)",
      "depth": "Fosa de Puerto Rico (8.376 m)",
      "fact": "Es el océano más joven geológicamente y el más salino de los grandes."
    },
    "en": {
      "type": "Ocean",
      "area": "~106.5M km² (Total Atlantic)",
      "depth": "Puerto Rico Trench (8,376 m)",
      "fact": "The saltiest of the major oceans, crossed by the Gulf Stream."
    },
    "ja": {
      "type": "大洋",
      "area": "約1億650万 km²",
      "depth": "プエルトリコ海溝 (8,376 m)",
      "fact": "大洋の中で最も塩分濃度が高く、歴史的な大航海時代の舞台となりました。"
    },
    "zh": {
      "type": "大洋",
      "area": "约1.065亿 km²",
      "depth": "波多黎各海沟 (8,376 m)",
      "fact": "主要大洋中平均盐度最高的洋盆，横跨大西洋暖流。"
    },
    "ar": {
      "type": "محيط",
      "area": "~106.5 مليون كم²",
      "depth": "خندق بورتوريكو (8,376 م)",
      "fact": "أكثر المحيطات الكبرى ملوحة وشهد أعظم رحلات عصر الاستكشاف."
    }
  },
  {
    "id": "atlantic_south",
    "name_es": "Océano Atlántico Sur",
    "name_en": "South Atlantic Ocean",
    "name_ja": "南大西洋",
    "name_zh": "南大西洋",
    "name_ar": "جنوب المحيط الأطلسي",
    "icon": "🌊",
    "priority": 3,
    "radiusDeg": 18.0,
    "centroid": [
      -18.0,
      -28.0
    ],
    "bounds": {
      "minLon": -60.0,
      "maxLon": 20.0,
      "minLat": -60.0,
      "maxLat": 0.0
    },
    "es": {
      "type": "Océano",
      "area": "~106.5M km² (Total Atlántico)",
      "depth": "Fosa de las Sandwich del Sur (8.264 m)",
      "fact": "Atravesado por la Dorsal Mesoatlántica, la cordillera más larga del mundo."
    },
    "en": {
      "type": "Ocean",
      "area": "~106.5M km² (Total Atlantic)",
      "depth": "Meteor Deep (8,264 m)",
      "fact": "Bisected by the Mid-Atlantic Ridge, the world's longest mountain range."
    },
    "ja": {
      "type": "大洋",
      "area": "約1億650万 km²",
      "depth": "メテオ海淵 (8,264 m)",
      "fact": "世界最長の中央海嶺が海底を縦断し、プレート拡大の現場です。"
    },
    "zh": {
      "type": "大洋",
      "area": "约1.065亿 km²",
      "depth": "流星海渊 (8,264 m)",
      "fact": "被世界最长的海底山脉——大西洋中脊纵向贯穿分割。"
    },
    "ar": {
      "type": "محيط",
      "area": "~106.5 مليون كم²",
      "depth": "خندق ميتيور (8,264 م)",
      "fact": "يقطعه حيد وسط الأطلسي، أطول سلسلة جبلية بركانية تحت الماء في العالم."
    }
  },
  {
    "id": "indian_ocean",
    "name_es": "Océano Índico",
    "name_en": "Indian Ocean",
    "name_ja": "インド洋",
    "name_zh": "印度洋",
    "name_ar": "المحيط الهندي",
    "icon": "🌊",
    "priority": 3,
    "radiusDeg": 20.0,
    "centroid": [
      78.0,
      -18.0
    ],
    "bounds": {
      "minLon": 20.0,
      "maxLon": 135.0,
      "minLat": -60.0,
      "maxLat": 30.0
    },
    "es": {
      "type": "Océano",
      "area": "~70.5M km²",
      "depth": "Fosa de Java (7.450 m)",
      "fact": "Es el océano más cálido del mundo y vital ruta de comercio."
    },
    "en": {
      "type": "Ocean",
      "area": "~70.5M km²",
      "depth": "Java Trench (7,450 m)",
      "fact": "The warmest ocean in the world and historic trading route."
    },
    "ja": {
      "type": "大洋",
      "area": "約7,050万 km²",
      "depth": "ジャワ海溝 (7,450 m)",
      "fact": "世界で最も水温が高い大洋であり、季節風 (モンスーン) を生み出します。"
    },
    "zh": {
      "type": "大洋",
      "area": "约7050万 km²",
      "depth": "爪哇海沟 (7,450 m)",
      "fact": "全球平均水温最高的大洋，驱动着亚洲著名的季风气候。"
    },
    "ar": {
      "type": "محيط",
      "area": "~70.5 مليون كم²",
      "depth": "خندق جاوة (7,450 م)",
      "fact": "أدفأ محيط في العالم وشريان تجاري حيوي عبر التاريخ."
    }
  },
  {
    "id": "arctic_ocean",
    "name_es": "Océano Ártico",
    "name_en": "Arctic Ocean",
    "name_ja": "北極海",
    "name_zh": "北冰洋",
    "name_ar": "المحيط المتجمد الشمالي",
    "icon": "🧊",
    "priority": 3,
    "radiusDeg": 16.0,
    "centroid": [
      0.0,
      84.0
    ],
    "bounds": {
      "minLon": -180.0,
      "maxLon": 180.0,
      "minLat": 66.0,
      "maxLat": 90.0
    },
    "es": {
      "type": "Océano Glacial",
      "area": "~14.0M km²",
      "depth": "Fosa de Molloy (5.550 m)",
      "fact": "Rodea el Polo Norte y está cubierto por banquisas polares de hielo."
    },
    "en": {
      "type": "Glacial Ocean",
      "area": "~14.0M km²",
      "depth": "Molloy Deep (5,550 m)",
      "fact": "Surrounds the North Pole and is covered by polar sea ice."
    },
    "ja": {
      "type": "極洋 / 氷海",
      "area": "約1,400万 km²",
      "depth": "モロイ海淵 (5,550 m)",
      "fact": "北極点を中心に広がり、海氷に覆われた最小で最浅の大洋です。"
    },
    "zh": {
      "type": "极地洋",
      "area": "约1400万 km²",
      "depth": "莫洛伊深渊 (5,550 m)",
      "fact": "环绕北极点分布，被大面积极地海冰覆盖的最小大洋。"
    },
    "ar": {
      "type": "محيط متجمد",
      "area": "~14.0 مليون كم²",
      "depth": "خندق مولوي (5,550 م)",
      "fact": "يحيط بالقطب الشمالي وتغطيه طبقات جليدية قطبية عائمة."
    }
  },
  {
    "id": "southern_ocean",
    "name_es": "Océano Antártico",
    "name_en": "Southern Ocean",
    "name_ja": "南極海",
    "name_zh": "南冰洋",
    "name_ar": "المحيط المتجمد الجنوبي",
    "icon": "🧊",
    "priority": 3,
    "radiusDeg": 18.0,
    "centroid": [
      0.0,
      -68.0
    ],
    "bounds": {
      "minLon": -180.0,
      "maxLon": 180.0,
      "minLat": -90.0,
      "maxLat": -58.0
    },
    "es": {
      "type": "Océano Glacial",
      "area": "~20.3M km²",
      "depth": "Fosa de las Sandwich del Sur (7.236 m)",
      "fact": "Rodea la Antártida con la potente corriente circumpolar."
    },
    "en": {
      "type": "Glacial Ocean",
      "area": "~20.3M km²",
      "depth": "South Sandwich Trench (7,236 m)",
      "fact": "Encircles Antarctica with the powerful Circumpolar Current."
    },
    "ja": {
      "type": "極洋",
      "area": "約2,030万 km²",
      "depth": "サウスサンドウィッチ海溝 (7,236 m)",
      "fact": "南極大陸を取り囲み、強力な南極環流が地球の気候を循環させています。"
    },
    "zh": {
      "type": "极地洋",
      "area": "约2030万 km²",
      "depth": "南桑威奇海沟 (7,236 m)",
      "fact": "环绕南极大陆，拥有全球最强大的南极绕极环流。"
    },
    "ar": {
      "type": "محيط متجمد",
      "area": "~20.3 مليون كم²",
      "depth": "خندق ساندويتش الجنوبي (7,236 م)",
      "fact": "يطوق القارة القطبية الجنوبية بتيار دائري قطبي عظيم."
    }
  }
]
