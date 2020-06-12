# hash_data.py

titles = {
	'Subject': 0, 
	'From (display)': 1, 
	'From (address)': 2, 
	'To (display)': 3, 
	'To (address)': 4, 
	'Cc (display)': 5, 
	'Cc (address)': 6, 
	'Bcc (display)': 7, 
	'Bcc (address)': 8, 
	'Creator Name': 9, 
	'Importance': 10, 
	'Date Sent': 11, 
	'Date Received': 12, 
	'Size': 13, 
	'Attachment Names': 14
}

people_real_name = {
	# "walter furlan703": "walter furlan",
	# "w.furlan":"walter furlan",
	# "vmbackup542":"vmbackup",
	# "vince hackingteam.it50b":"vincenzetti",
	# "vince":"vincenzetti",
	# "valeriano bedeschice8": "valeriano bedeschice",
	# "vale":"valeriano bedeschice",
	# "v.bedeschi": "valeriano bedeschice",
	# "utente test294": "utente test",
	# "utest" : "utente test",
	# "u.test": "utente test",
	# "simonetta": "simonetta gallucci",
	# "simonetta gallucci569": "simonetta gallucci",
	# "s.gallucci": "simonetta gallucci",
	# "serge woona65": "serge woona",
	# "serge": "serge woona",
	# "supportfe0": "support",
	# "philippe antoine vinci785": "hilippe antoine vinci",
	# "p.vinci":"hilippe antoine vinci",
	# "mostapha maanna4d7": "mostapha maanna",
	# "mauro romeof4d": "mauro romeof",
	# "mauro.romeo hackingteam344": "mauro romeo",
	# "m.luppi": "massimiliano luppi",
	# "massimiliano luppi133": "massimiliano luppi",
	# "lucia rana9cb": "lucia rana",
	# "giancarlo russof7a": "giancarlo russo",
	# "emad shehata450": "emad shehata",
	# "d.vincenzetti": "david vincenzetti",
	# "david vincenzetti7aa": "david vincenzetti",
	# "daniele milan5af": "daniele milan",
	# "daniel maglietta983": "daniel maglietta",
	# "alessandro scarafiled45": "alessandro scarafile",
	# "antonella capaldodc5": "antonella capaldo",
	"f.degiovanni": "fulvio degiovanni",
	"g.fulvio": "fulvio degiovanni",
	"m.valleri": "marco valleri",
	"marco.valleri": "marco valleri",
	"pelliccione": "alberto pelliccione",
	"alberto.pelliccione": "alberto pelliccione",
	"a.pelliccione": "alberto pelliccione",
	"w.furlan": "walterandrea furlan",
	"max": "max luppi",
	"luppi": "max luppi",
	"mluppi": "max luppi",
	"a.lomonaco": "alessandro lomonaco", 
	"alessandro.lomonaco": "alessandro lomonaco",
	"debora": "debora leanza",
	"debora.leanza": "debora leanza",
	"d.leanza": "debora leanza",
	"dleanza": "debora leanza",
	"diego.giubertoni": "diego giubertoni",
	"d.giubertoni": "diego giubertoni",
	"aldo": "aldo scaccabarozzi",
	"a.scaccabarozzi": "aldo scaccabarozzi",
	"mostapha": "mostapha maana",
	"m.maana": "mostapha maana",
	"serge": "serge wood",
	"e.serge": "serge wood",
	"eserge": "serge wood",
	"s.woon": "serge wood",
	"s.yun": "serge yun",
	"d.romualdi": "davide romualdi",
	"romualdi": "davide romualdi",
	"ivan.roattino": "ivan roattino",
	"i.roattino": "ivan roattino",
	"m.fontana": "marco fontana",
	"federico.guerrini": "federico guerrini",
	"f.guerrini": "federico guerrini",
	"guerrini": "federico guerrini",
	"sara": "sara galvagna",
	"sara.galvagna": "sara galvagna",
	"s.galvagna": "sara galvagna",
	"massimiliano.oldani": "massimiliano oldani",
	"m.oldani": "massimiliano oldani",
	" fabio": "fabio busatto",
	"fabio.busatto": "fabio busatto",
	"busatto": "fabio busatto",
	"f.busatto": "fabio busatto",
	"fbusatto": "fabio busatto",
	"eugene": "eugene ho",
	"e.ho ": "eugene ho",
	"d.molteni": "daniele molteni",
	"gianluca": "gianluca piani",
	"gianluca.piani": "gianluca piani",
	"g.piani": "gianluca piani",
	"david": "david vincenzetti",
	"david.vincenzetti": "david vincenzetti",
	"d.vincenzetti": "david vincenzetti",
	"dvincenzetti": "david vincenzetti",
	"vincenzetti": "david vincenzetti",
	"hackingteam t.valentini": "tomas valentini",
	"t.valentini": "tomas valentini", 
	" gianluca.vadruccio": "gianluca vadruccio",
	" g.vadruccio": "gianluca vadruccio",
	"ianluca.vadruccio": "gianluca vadruccio",
	"luca.vadruccio": "gianluca vadruccio",
	" salvatore": "salvatore rumore",
	"salvatore.rumore": "salvatore rumore",
	"s.rumore": "salvatore rumore",
	" simonetta": "simonetta gallucci",
	"simonetta.gallucci": "simonetta gallucci",
	"s.gallucci": "simonetta gallucci",
	"s.galucci": "simonetta gallucci",
	"ss.gallucci ": "simonetta gallucci",
	"marco": "marco bettini",
	"marco.bettini": "marco bettini", 
	"m.bettini": "marco bettini",
	"m..bettini": "marco bettini",
	"mbettini": "marco bettini",
	" bruno": "bruno muschitiello",
	"bruno.muschitiello": "bruno muschitiello", 
	"b.muschitiello": "bruno muschitiello",
	"valeriano.bedeschi": "valeriano bedeschi",
	"valeriano": "valeriano bedeschi",
	"bedeschi": "valeriano bedeschi",
	"m.luppi": "massimiliano luppi",
	"a.mino": "alessandra mino",
	"mino": "alessandra mino",
	"eva": "eva michalikova",
	"e.michalikova": "eva michalikova",
	"michalikova": "eva michalikova",
	"thomas": "thomas valentini",
	"hackingteam t.valentini": "thomas valentini",
	"t.valentini": "thomas valentini",
	"e.pardo": "eduardo pardo",
	"e.pardocarvajal": "eduardo pardo",
	"c.imbrauglio": "constantino imbrauglio",
	"matteo": "matteo oliva",
	"matteo.oliva": "matteo oliva",
	"m.oliva": "matteo oliva", 
	"danilo": "danilo cordoni",
	"danilo.cordoni": "danilo cordoni",
	"d.cordoni": "danilo cordoni",
	"u.test": "utente test",
	"utest": "utente test",
	"utest2": "utente test",
	"alfredo": "alfredo pesoli",
	"a.pesoli": "alfredo pesoli",
	"guido": "guido landi",
	"guido.landi": "guido landi",
	"g.landi": "guido landi",
	"stefania": "stefania iannelli",
	"s.ianelli": "stefania iannelli", 
	"s.iannelli": "stefania iannelli", 
	"s.iannellli": "stefania iannelli", 
	"giancarlo": "giancarlo russo",
	"giancarlo.russo": "giancarlo russo", 
	"g.russo": "giancarlo russo", 
	"grusso": "giancarlo russo", 
	"russo": "giancarlo russo",  
	"russo2": "giancarlo russo", 
	"enrico": "enrico parentini",
	"e.parentini": "enrico parentini",
	"emad": "emad shehata",
	"e.shehata": "emad shehata",
	"e.sheatha": "emad shehata",
	"antonio.mazzeo": "antonio mazzeo",
	"a.mazzeo": "antonio mazzeo",
	"mazzeo": "antonio mazzeo",
	"amazzeo": "antonio mazzeo",
	"alberto": "alberto ornaghi",
	"alberto.ornaghi": "alberto ornaghi",
	" a.ornaghi": "alberto ornaghi",
	" aornaghi": "alberto ornaghi",
	"g.cino": "giovanni cino",
	"giovanni": "giovanni cino",
	"andrea": "andrea cariola",  
	"andrea.cariola": "andrea cariola", 
	"a.cariola": "andrea cariola", 
	"cariola": "andrea cariola",
	"daniel": "daniel maglietta",
	"daniel.maglietta": "daniel maglietta",
	"d.maglietta": "daniel maglietta",
	"fabrizio.cornelli": "fabrizio cornelli",
	"fcornelli": "fabrizio cornelli",
	"cornelli": "fabrizio cornelli",
	"gabriele.parravicini": "gabriele parravicini",
	"gabiele.parravicini": "gabriele parravicini",
	"g.parravicini": "gabriele parravicini",
	"s.bagnasco": "stefano bagnasco", 
	"c.vardaro": "cristian vardaro",
	"vardaro": "cristian vardaro",
	"antonella": "antonella capaldo",
	"antonella.capaldo": "antonella capaldo",
	"antonella.caparldo": "antonella capaldo",
	"a.capaldo": "antonella capaldo",
	"acapaldo": "antonella capaldo",
	"capaldo": "antonella capaldo",
	"s.solis": "sergio solis",
	"s.rodriguez": "sergio rodriguez",
	"annalisa": "annalisa.mangiacavalli",
	"annalisa.mangiacavalli": "annalisa.mangiacavalli",
	"a.mangiacavalli": "annalisa.mangiacavalli",
	"l.guerra": "luca guerra",
	"roby": "roby banfi", 
	"claudio": "claudio agosti",
	"claudio.agosti": "claudio agosti",
	"c.agosti": "claudio agosti",
	"ciceri": "elisabetta ciceri",
	" e.ciceri": "elisabetta ciceri",
	"ivan.speziale": "ivan speziale",
	"i.speziale": "ivan speziale",
	"mauro.romeo": "mauro romeo",
	"m.romeo": "mauro romeo",
	"mromeo": "mauro romeo",
	"d.martinez": "daniel martinez",
	"c.pozzi": "christain pozzi",
	"emanuele": "emanuele placidi",
	"e.placidi": "emanuele placidi",
	"eric": "eric rabe",
	"e.rabe": "eric rabe",
	"eros.marcon": "eros marcon",
	"eros": "eros marcon",
	"e.marcon": "eros marcon",
	"l.invernizzi": "lorenzo invernizzi",
	"alex": "alex velasco",
	"a.velasco": "alex velasco",
	"avelasco": "alex velasco",
	"a.scarafile": "alessio scarafile",
	"marco.catino": "marco catino",
	"m.catino": "marco catino",
	"mcatino": "marco catino",
	"catino": "marco catino",
	"daniele": "daniele milan",
	"daniele.milan": "daniele milan",
	"scarafile": "alessandro scarafile",
	"alessandro.scarafile": "alessandro scarafile",
	"j.doe": "john doe",
	"banfi": "roberto banfi",
	"r.banfi": "roberto banfi",
	"roberto.banfi": "roberto banfi",
	"philippe": "philippe vinci",
	"p.vinci": "philippe vinci",
	"lucia.rana": "lucia rana",
	"lucia": "lucia rana",
	"l.rana": "lucia rana",
	"lrana": "lucia rana",
	"rana": "lucia rana",
	"luca": "luca filippi",
	"luca.filippi": "luca filippi",
	"l.filippi": "luca filippi",
	"enrico.luzzani": "enrico luzzani",
	"mostapha.maanna": "mostapha maanna",
	"m.maanna": "mostapha maanna",
	" a.citino": "antonella citino",
	"massimo.chiodini": "massimo chiodini",
	"m.chiodini": "massimo chiodini",
	"chiodini": "massimo chiodini",
	"imo.chiodini": "massimo chiodini",
	"simo.chiodini": "massimo chiodini",
}

key_words = {
	"payment",
	"maglietta",
	"partenza",
	"mobile",
	"alessandro",
	"hw",
	"pasticcini",
	"solution",
	"failed",
	"update",
	# "subject",
	"draft",
	"sample",
	"android",
	"itinerary",
	"ht-",
	"symbian",
	"issue",
	"linux",
	"trip",
	"request",
	"security",
	"license",
	"0day",
	"visa",
	"iss",
	# "[confluence]",
	"problem",
	"srl",
	"invitation",
	"arrivederci",
	"daniele",
	"rcs",
	"webinar",
	"upgrade",
	"schedule",
	"e-ticket",
	"team",
	"conference",
	"delete",
	# "[warning:virus/worm]",
	"kazakstan",
	"opportunity",
	"delivery",
	"offer",
	"phone",
	"ht",
	"mac",
	"contract",
	"cyber",
	"windows",
	"support",
	"ddos",
	"exploit",
	"training",
	"calendar",
	"hotel",
	"report",
	"scarafile",
	"pranzo",
	"meeting",
	"error",
	# "[bulk]",
	"test",
	"ios",
	"botnet",
	"anons",
	"installation",
	"customer",
	"it",
	"hacking",
	"delta",
	"blackberry",
	"biglietti",
	# "[success]",
	"urgent",
	"assignment",
	"aerei",
	"azerbaijan",
	"milan",
	"info",
	"ticket",
	"proposal",
	"demo",
	"global",
	"gift",
	"new",
	"release",
	"torta",
	"file",
	"system",
	"malware",
	"confirmation",
	"max",
	"status",
	"gioved",
}

content_class = {
	"业务":{
		"Windows":"Windows",
		"windows":"Windows",
		"Linux":"Linux",
		"Mac":"Mac",
		"iOS":"iOS",
		"IOS":"iOS",
		"Symbian":"Symbian",
		"BlackBerry":"BlackBerry",
		"Android":"Android",
		"android":"Android",
		"Exploit":"Exploit",
		"exploit":"Exploit",
		"RCS":"RCS",
		"Botnet":"Botnet",
		"Malware":"Malware",
		"malware":"Malware",
		"0day":"0day",
		"DDOS":"DDOS",
	},
	"广告":{
		"Biglietti":"Biglietti",
		"Itinerary":"Itinerary",
		"itinerary":"Itinerary",
		"aerei":"aerei",
		"Delta":"Delta",
		"delta":"Delta",
		"Pasticcini":"Pasticcini",
		"Hotel":"Hotel",
		"hotel":"Hotel",
		"anons":"Anons",
		"Anons":"Anons",
		"Pranzo":"Pranzo",
		"pranzo":"Pranzo",
		"Gift":"Gift",
		"Maglietta":"Maglietta",
		"ticket":"Ticket",
		"Ticket":"Ticket",
		"E-Ticket":"E-Ticket",
		"torta":"torta",
		"Visa":"Visa",
	},
}

work_content_class = {
	"操作系统": {
		"Windows",
		"Linux",
		"Mac",
		"iOS",
		"Symbian",
		"BlackBerry",
		"Android",
	} ,
	"攻击":{
		"Exploit",
		"RCS",
		"Botnet",
		"Malware",
		"0day",
		"DDOS",
	}
}