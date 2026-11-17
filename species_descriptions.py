# species_descriptions.py
# Full species descriptions (6 languages) for the Lithuanian tree identifier.
# Import in streamlit_app.py:
#     from species_descriptions import SPECIES_DESCRIPTIONS, sp_name, sp_desc, sp_feature

SPECIES_DESCRIPTIONS = {
    "Acer platanoides": {
        "n": {"lt": "Paprastasis klevas", "en": "Norway maple", "de": "Spitzahorn",
              "fr": "Érable plane", "es": "Arce real", "uk": "Клен гостролистий"},
        "d": {
            "lt": "Lapai plačiai skiltuoti – paprastai su penkiomis skiltimis, tarsi atversta ranka – rudenį įsiplieskia auksine geltona ir oranžine spalva. Jauna žievė lygi ir žalia, vėliau tamsėja ir išilgai vagėja. Vaisiai – sparnuoti sparnavaisiai, kabantys poromis tarsi maži propeleriukai – vaikams mėgstama pramoga. Dažnas parkuose, skveruose ir derlingesniuose miškuose.",
            "en": "Broadly lobed leaves – usually with five lobes, like an open hand – flare gold and orange in autumn. Young bark is smooth and green, later darkening and furrowing lengthwise. Fruits are paired winged samaras hanging like little propellers – a favourite toy for kids. Common in parks, squares, and fertile woodland.",
            "de": "Breit gelappte Blätter – meist mit fünf Lappen, wie eine offene Hand – leuchten im Herbst gold und orange. Junge Rinde ist glatt und grün, später dunkelt sie nach und wird längs gefurcht. Die Früchte sind paarweise hängende geflügelte Spaltfrüchte wie kleine Propeller – bei Kindern beliebt. Häufig in Parks, auf Plätzen und in fruchtbaren Wäldern.",
            "fr": "Feuilles largement lobées – en général à cinq lobes, comme une main ouverte – qui flamboient d'or et d'orange en automne. L'écorce jeune est lisse et verte, puis fonce et se fissure dans le sens de la longueur. Les fruits sont des samares ailées suspendues par paires comme de petites hélices – un jouet favori des enfants. Commun dans les parcs, les places et les bois fertiles.",
            "es": "Hojas ampliamente lobuladas – normalmente con cinco lóbulos, como una mano abierta – que se encienden de dorado y naranja en otoño. La corteza joven es lisa y verde, luego oscurece y se agrieta longitudinalmente. Los frutos son sámaras aladas colgando en parejas como pequeñas hélices – un juguete favorito de los niños. Común en parques, plazas y bosques fértiles.",
            "uk": "Широко лопатеві листки – зазвичай із п'ятьма лопатями, мов розкрита долоня – восени спалахують золотом та оранжем. Молода кора гладенька й зелена, згодом темніє та вкривається поздовжніми тріщинами. Плоди – крилаті двосім'янки, що звисають парами, наче маленькі пропелери – улюблена забавка дітлахів. Частий у парках, скверах і родючих лісах.",
        },
    },
    "Alnus glutinosa": {
        "n": {"lt": "Juodalksnis", "en": "Black alder", "de": "Schwarz-Erle",
              "fr": "Aulne glutineux", "es": "Aliso negro", "uk": "Вільха чорна"},
        "d": {
            "lt": "Lapai atvirkščiai kiaušiniški, su būdingu įkirptu viršūniu – tarsi kas būtų nukandęs galiuką. Jauni jie lipnūs, vėliau tampa blizgūs, tamsiai žali. Žievė tamsi, giliai sueižėjusi, sena – beveik juoda, todėl ir vadinama juodalksniu. Mėgsta šlapias, pelkėtas vietas prie vandens – ten jaučiasi kaip namie.",
            "en": "Leaves are obovate with a characteristic notched tip – as if someone had nibbled the end. Sticky when young, later becoming glossy dark green. Bark is dark, deeply fissured, almost black when old – hence the name. Loves wet, swampy sites beside water – that's where it feels at home.",
            "de": "Blätter sind verkehrt-eiförmig mit einer typischen eingekerbten Spitze – als hätte jemand hineingebissen. Jung klebrig, später glänzend dunkelgrün. Die Rinde ist dunkel und tief gefurcht, im Alter fast schwarz – daher der Name. Liebt nasse, sumpfige Standorte am Wasser – dort fühlt sie sich zu Hause.",
            "fr": "Feuilles obovales à pointe caractéristique échancrée – comme si quelqu'un avait mordu le bout. Collantes jeunes, puis luisantes et vert foncé. L'écorce est sombre, profondément fissurée, presque noire en vieillissant – d'où son nom. Aime les sols humides et marécageux au bord de l'eau – c'est là qu'il se sent chez lui.",
            "es": "Hojas obovadas con una característica punta escotada – como si alguien le hubiera dado un mordisco. Pegajosas de jóvenes, luego brillantes y de color verde oscuro. La corteza es oscura, profundamente agrietada, casi negra en la vejez – de ahí su nombre. Ama los lugares húmedos y pantanosos junto al agua – allí se siente como en casa.",
            "uk": "Листки обернено-яйцеподібні, з характерною виїмкою на верхівці – наче хтось відкусив кінчик. Молоді – клейкі, згодом стають блискучими, темно-зеленими. Кора темна, глибоко потріскана, у старості майже чорна – звідси й назва. Любить вологі, болотисті місця біля води – там почувається як удома.",
        },
    },
    "Alnus incana": {
        "n": {"lt": "Baltalksnis", "en": "Grey alder", "de": "Grau-Erle",
              "fr": "Aulne blanc", "es": "Aliso gris", "uk": "Вільха сіра"},
        "d": {
            "lt": "Lapai smailūs, plačiai kiaušiniški arba elipsiški, dantyti – jų apatinė pusė pilkai plaukuota, todėl nuo tolo atrodo tarsi sidabrinė. Žievė lygi, šviesiai pilka, todėl lengvai atskiriama nuo tamsios juodalksnio žievės. Auga pakelėse, upių slėniuose, sausringesnėse vietose nei juodalksnis – ištvermingas ir nepretenzingas.",
            "en": "Leaves are pointed, broadly ovate or elliptical, toothed – their underside is grey-hairy, giving the tree a silvery look from afar. Bark is smooth and light grey, easy to tell apart from the dark bark of black alder. Grows along roadsides, in river valleys, and on drier sites than black alder – hardy and undemanding.",
            "de": "Blätter sind zugespitzt, breit eiförmig oder elliptisch, gezähnt – ihre Unterseite ist grau behaart, wodurch der Baum aus der Ferne silbrig wirkt. Die Rinde ist glatt und hellgrau, gut von der dunklen Rinde der Schwarz-Erle zu unterscheiden. Wächst an Straßenrändern, in Flusstälern und auf trockeneren Standorten als die Schwarz-Erle – robust und anspruchslos.",
            "fr": "Feuilles pointues, largement ovales ou elliptiques, dentées – leur dessous est gris-poilu, donnant à l'arbre un aspect argenté de loin. L'écorce est lisse et gris clair, facile à distinguer de celle, sombre, de l'aulne glutineux. Pousse au bord des routes, dans les vallées fluviales et sur des sols plus secs que l'aulne glutineux – rustique et peu exigeant.",
            "es": "Hojas puntiagudas, anchamente ovadas o elípticas, dentadas – su envés es gris-peloso, lo que da al árbol un aspecto plateado de lejos. La corteza es lisa y de color gris claro, fácil de distinguir de la corteza oscura del aliso negro. Crece junto a carreteras, en valles fluviales y en lugares más secos que el aliso negro – rústico y poco exigente.",
            "uk": "Листки загострені, широко-яйцеподібні або еліптичні, зубчасті – їхній низ сіро-опушений, тому здалеку дерево виглядає сріблястим. Кора гладенька, світло-сіра, її легко відрізнити від темної кори вільхи чорної. Росте обабіч доріг, у річкових долинах і на сухіших місцях, ніж вільха чорна – витривала й невибаглива.",
        },
    },
    "Betula pendula": {
        "n": {"lt": "Karpotasis beržas", "en": "Silver birch", "de": "Hänge-Birke",
              "fr": "Bouleau verruqueux", "es": "Abedul común", "uk": "Береза повисла"},
        "d": {
            "lt": "Balta žievė su horizontaliomis juodomis juostelėmis – tarsi kas būtų braukęs anglimi. Jaunos šakelės karpotos, todėl ir vadinamas karpotuoju. Lapai rombiški, smailūs, dvigubai dantyti, rudenį paauksuoja. Jauni medžiai turi gražiai nusvirusias šakeles – iš tolo atrodo tarsi verkiantys.",
            "en": "White bark with horizontal black bands – as if drawn with charcoal. Young twigs are warty, which gives it its name. Leaves are rhombic, pointed, doubly toothed, turning gold in autumn. Young trees have gracefully weeping branches – they look like they're crying from afar.",
            "de": "Weiße Rinde mit waagerechten schwarzen Bändern – als wären sie mit Kohle gezeichnet. Junge Zweige sind warzig, daher der Name. Blätter sind rhombisch, zugespitzt, doppelt gezähnt und werden im Herbst golden. Junge Bäume haben anmutig überhängende Zweige – aus der Ferne wirken sie wie weinend.",
            "fr": "Écorce blanche aux bandes noires horizontales – comme dessinées au fusain. Les jeunes rameaux sont verruqueux, d'où son nom. Feuilles rhombiques, pointues, doublement dentées, dorées en automne. Les jeunes arbres ont des branches gracieusement pleureuses – de loin, on dirait qu'ils pleurent.",
            "es": "Corteza blanca con bandas negras horizontales – como dibujadas con carbón. Las ramillas jóvenes son verrugosas, de ahí su nombre. Hojas rómbicas, puntiagudas, doblemente dentadas, que se vuelven doradas en otoño. Los árboles jóvenes tienen ramas elegantemente lloronas – de lejos parecen estar llorando.",
            "uk": "Біла кора з горизонтальними чорними смугами – наче намальованими вугіллям. Молоді пагони горбкуваті, звідси й назва. Листки ромбічні, загострені, двічі зубчасті, восени золотіють. Молоді дерева мають граційно пониклі гілки – здалеку здається, ніби вони плачуть.",
        },
    },
    "Betula pubescens": {
        "n": {"lt": "Plaukuotasis beržas", "en": "Downy birch", "de": "Moor-Birke",
              "fr": "Bouleau pubescent", "es": "Abedul pubescente", "uk": "Береза пухнаста"},
        "d": {
            "lt": "Labai panašus į karpotąjį beržą – bet jaunos šakelės ir lapai plaukuoti, be karpių, todėl jį atskirti padeda lietimas. Lapai platesni, šiek tiek širdiški, trumpesniais koteliais. Žievė balta, bet žemyn link kamieno dažnai tamsėja. Mėgsta drėgnesnes vietas – pelkes, šlapius miškus, ten kur karpotasis beržas nenori augti.",
            "en": "Very similar to silver birch – but its young twigs and leaves are hairy, without warts, so a gentle touch helps tell them apart. Leaves are broader, somewhat heart-shaped, with shorter petioles. Bark is white but often darkens lower down the trunk. Prefers wetter sites – bogs, wet woodland, places where silver birch won't grow.",
            "de": "Sehr ähnlich der Hänge-Birke – aber junge Zweige und Blätter sind behaart, ohne Warzen, also hilft ein sanftes Anfassen beim Unterscheiden. Blätter breiter, etwas herzförmig, mit kürzeren Stielen. Rinde weiß, wird aber weiter unten am Stamm oft dunkel. Bevorzugt feuchtere Standorte – Moore, nasse Wälder, wo die Hänge-Birke nicht wächst.",
            "fr": "Très semblable au bouleau verruqueux – mais ses jeunes rameaux et ses feuilles sont poilus, sans verrues, un contact léger aide donc à les distinguer. Feuilles plus larges, un peu cordiformes, à pétioles plus courts. L'écorce est blanche mais s'assombrit souvent vers le bas du tronc. Préfère les sites plus humides – tourbières, bois humides, là où le bouleau verruqueux ne pousse pas.",
            "es": "Muy similar al abedul común – pero sus ramillas y hojas jóvenes son peludas, sin verrugas, así que un tacto suave ayuda a distinguirlos. Hojas más anchas, algo acorazonadas, con peciolos más cortos. La corteza es blanca pero a menudo oscurece hacia la base del tronco. Prefiere lugares más húmedos – turberas, bosques húmedos, donde el abedul común no crece.",
            "uk": "Дуже схожа на березу повислу – але молоді пагони й листки пухнасті, без горбиків, тож на дотик їх легко розрізнити. Листки ширші, трохи серцеподібні, з коротшими черешками. Кора біла, але ближче до основи стовбура часто темніє. Любить вологіші місця – болота, вологі ліси, там, де береза повисла не росте.",
        },
    },
    "Carpinus betulus": {
        "n": {"lt": "Paprastasis skroblas", "en": "European hornbeam", "de": "Hainbuche",
              "fr": "Charme", "es": "Carpe blanco", "uk": "Граб звичайний"},
        "d": {
            "lt": "Lapai ovalūs, dantyti, su labai ryškiomis gyslomis – tarsi suraukti. Žievė lygi, pilka, su būdingu „raumenų“ raštu – ja net sunku patikėti, kad tai medis. Vaisiai – smulkūs riešutėliai, kiekvienas su trijų skilčių lapeliu-kapučiu, kuris padeda sklisti vėjui. Auga derlingose, drėgnose dirvose, dažnas mišriuose miškuose.",
            "en": "Leaves are oval, toothed, with very prominent veins – as if wrinkled. Bark is smooth and grey with a characteristic 'muscular' pattern – hard to believe it belongs to a tree. Fruits are small nutlets, each with a three-lobed leafy bract that helps wind dispersal. Grows on fertile, moist soils, common in mixed woodland.",
            "de": "Blätter sind oval, gezähnt, mit sehr ausgeprägten Adern – wie gerunzelt. Die Rinde ist glatt und grau mit einem typischen „muskulösen“ Muster – kaum zu glauben, dass sie zu einem Baum gehört. Die Früchte sind kleine Nüsschen, jedes mit einem dreilappigen Hochblatt, das der Windverbreitung dient. Wächst auf fruchtbaren, feuchten Böden, häufig in Mischwäldern.",
            "fr": "Feuilles ovales, dentées, aux nervures très marquées – comme ridées. L'écorce est lisse et grise, avec un motif «musclé» caractéristique – difficile de croire qu'elle appartient à un arbre. Les fruits sont de petites noisettes, chacune avec une bractée trilobée qui aide à la dispersion par le vent. Pousse sur des sols fertiles et humides, commun dans les bois mixtes.",
            "es": "Hojas ovaladas, dentadas, con nervios muy marcados – como arrugadas. La corteza es lisa y gris con un patrón «musculoso» característico – cuesta creer que sea de un árbol. Los frutos son pequeñas nuececillas, cada una con una bráctea trilobulada que ayuda a la dispersión por el viento. Crece en suelos fértiles y húmedos, común en bosques mixtos.",
            "uk": "Листки овальні, зубчасті, з дуже виразними жилками – наче зморшкуваті. Кора гладенька, сіра, з характерним «мускулястим» візерунком – важко повірити, що вона належить дереву. Плоди – дрібні горішки, кожен із трилопатевою листоподібною обгорткою, що допомагає поширенню вітром. Росте на родючих вологих ґрунтах, частий у мішаних лісах.",
        },
    },
    "Fagus sylvatica": {
        "n": {"lt": "Paprastasis bukas", "en": "European beech", "de": "Rotbuche",
              "fr": "Hêtre", "es": "Haya", "uk": "Бук лісовий"},
        "d": {
            "lt": "Lapai blizgūs, elipsiški, lygiais kraštais – rudenį nusidažo varine ruda spalva, kuri ilgai išlieka ant medžio. Žievė lygi, plona, šviesiai pilka, net sena lieka lygi – ant jos mėgsta raižyti įsimylėjėliai. Riešutai – trikampiai bukučiai, paslėpti dygliuotame gaubte, kuris subrendęs atsiveria į keturias skiltis. Mėgsta derlingas, kalkingas dirvas.",
            "en": "Leaves are glossy, elliptical, with smooth margins – in autumn they turn a copper brown that lingers on the tree. Bark is smooth, thin and pale grey, remaining smooth even on old trees – lovers love to carve on it. Nuts are triangular beechnuts hidden inside a spiny husk that splits into four valves when ripe. Prefers fertile, calcareous soils.",
            "de": "Blätter sind glänzend, elliptisch, ganzrandig – im Herbst färben sie sich kupferbraun und bleiben lange am Baum. Die Rinde ist glatt, dünn und hellgrau, selbst alte Bäume bleiben glatt – Verliebte ritzen gerne Herzen hinein. Die Früchte sind dreikantige Bucheckern in einer stacheligen Hülle, die bei Reife in vier Klappen aufspringt. Bevorzugt fruchtbare, kalkhaltige Böden.",
            "fr": "Feuilles luisantes, elliptiques, à bord lisse – en automne elles prennent un brun cuivré qui persiste longtemps sur l'arbre. L'écorce est lisse, fine et gris pâle, restant lisse même sur les vieux arbres – les amoureux aiment y graver. Les fruits sont des faînes triangulaires cachées dans une cupule épineuse qui s'ouvre en quatre valves à maturité. Préfère les sols fertiles et calcaires.",
            "es": "Hojas brillantes, elípticas, de margen liso – en otoño se tiñen de un marrón cobrizo que permanece mucho tiempo en el árbol. La corteza es lisa, fina y de color gris claro, y sigue lisa incluso en árboles viejos – los enamorados adoran grabarla. Los frutos son hayucos triangulares escondidos en una cúpula espinosa que se abre en cuatro valvas al madurar. Prefiere suelos fértiles y calcáreos.",
            "uk": "Листки блискучі, еліптичні, з рівним краєм – восени набувають мідно-бурого кольору, який довго тримається на дереві. Кора гладенька, тонка, світло-сіра, навіть у старих дерев залишається гладенькою – закохані люблять вирізати на ній серця. Плоди – трикутні горішки, сховані в колючій обгортці, що достигаючи розкривається на чотири стулки. Надає перевагу родючим, вапняним ґрунтам.",
        },
    },
    "Fraxinus excelsior": {
        "n": {"lt": "Paprastasis uosis", "en": "European ash", "de": "Gewöhnliche Esche",
              "fr": "Frêne commun", "es": "Fresno común", "uk": "Ясен звичайний"},
        "d": {
            "lt": "Lapai sudėtiniai, paprastai su 5–9 lapeliais, išsidėstę priešais – tarsi žalių plunksnų poros. Žiemą uosį lengviausia atpažinti iš juodų, aksominių pumpurų – jie tarsi maži juodi kačiukai. Vaisiai – sparnuoti riešutėliai, sukabinti kekėmis ir kabantys žemyn. Auga derlingose, drėgnose dirvose, dažnas slėniuose.",
            "en": "Leaves are pinnately compound, usually with 5–9 leaflets arranged in opposite pairs – like pairs of green feathers. In winter, ash is easiest to recognise by its black, velvety buds – like tiny black kittens. Fruits are winged samaras clustered in hanging bunches. Grows on fertile, moist soils, common in valleys.",
            "de": "Blätter sind gefiedert, meist mit 5–9 gegenständigen Fiederblättchen – wie Paare grüner Federn. Im Winter erkennt man die Esche am leichtesten an ihren schwarzen, samtigen Knospen – wie winzige schwarze Kätzchen. Früchte sind geflügelte Spaltfrüchte in hängenden Büscheln. Wächst auf fruchtbaren, feuchten Böden, häufig in Tälern.",
            "fr": "Feuilles composées pennées, généralement à 5–9 folioles opposées – comme des paires de plumes vertes. En hiver, le frêne se reconnaît le plus facilement à ses bourgeons noirs et veloutés – comme de minuscules chatons noirs. Les fruits sont des samares ailées regroupées en grappes pendantes. Pousse sur des sols fertiles et humides, commun dans les vallées.",
            "es": "Hojas compuestas pinnadas, normalmente con 5–9 foliolos opuestos – como pares de plumas verdes. En invierno, el fresno se reconoce más fácilmente por sus yemas negras y aterciopeladas – como pequeños gatitos negros. Los frutos son sámaras aladas agrupadas en racimos colgantes. Crece en suelos fértiles y húmedos, común en valles.",
            "uk": "Листки складні, пірчасті, зазвичай із 5–9 листочками, розташованими супротивно – наче пари зелених пір'їн. Узимку ясен найлегше впізнати за чорними оксамитовими бруньками – наче маленькі чорні кошенята. Плоди – крилаті двосім'янки, зібрані в пониклі пучки. Росте на родючих вологих ґрунтах, частий у долинах.",
        },
    },
    "Juniperus communis": {
        "n": {"lt": "Paprastasis kadagys", "en": "Common juniper", "de": "Gewöhnlicher Wacholder",
              "fr": "Genévrier commun", "es": "Enebro común", "uk": "Ялівець звичайний"},
        "d": {
            "lt": "Krūmas arba mažas medis, dažnai kūgiškos formos – iš tolo gali atrodyti kaip maža eglutė. Spygliai dygliuoti, 1–2 cm ilgio, išsidėstę po tris ratuose, todėl juos liesdamas tikrai pajusi. Uogų kekės melsvai juodos, apvalios, sunoksta net dvejus metus – tad ant vieno krūmo gali rasti ir žalių, ir prinokusių. Auga sausuose, smėlėtuose arba uolėtuose plotuose.",
            "en": "A shrub or small tree, often conical in form – from afar it may look like a little fir. Needles are prickly, 1–2 cm long, arranged three at a time in whorls – you'll definitely feel them if you touch. Berry-like cones are bluish-black, round, ripening over two years – so one bush can hold both green and ripe ones. Grows in dry, sandy or rocky sites.",
            "de": "Ein Strauch oder kleiner Baum, oft kegelförmig – aus der Ferne wirkt er wie eine kleine Tanne. Nadeln sind stechend, 1–2 cm lang, in Dreierquirlen angeordnet – beim Anfassen spürst du sie garantiert. Beerenzapfen sind bläulich-schwarz, rund und reifen über zwei Jahre – an einem Strauch finden sich also grüne und reife. Wächst an trockenen, sandigen oder felsigen Standorten.",
            "fr": "Un arbuste ou petit arbre, souvent conique – de loin, il peut ressembler à un petit sapin. Les aiguilles sont piquantes, longues de 1–2 cm, disposées par trois en verticilles – vous les sentirez à coup sûr si vous les touchez. Les cônes-berries sont bleu-noir, ronds, et mûrissent sur deux ans – un même buisson peut donc en porter des verts et des mûrs. Pousse dans des sites secs, sablonneux ou rocheux.",
            "es": "Un arbusto o pequeño árbol, a menudo de forma cónica – de lejos puede parecer un pequeño abeto. Las acículas son punzantes, de 1–2 cm, dispuestas de tres en tres en verticilos – seguro que las notas si las tocas. Los conos-baya son de color azul negruzco, redondos, y maduran a lo largo de dos años – así que un mismo arbusto puede tener unos verdes y otros maduros. Crece en lugares secos, arenosos o rocosos.",
            "uk": "Кущ або невелике дерево, часто конічної форми – здалеку може здатися маленькою ялинкою. Голки колючі, 1–2 см завдовжки, розташовані по три в кільцях – ви неодмінно їх відчуєте на дотик. Шишкоягоди синювато-чорні, круглі, достигають аж два роки – тож на одному кущі можна знайти і зелені, і стиглі. Росте на сухих, піщаних або кам'янистих місцях.",
        },
    },
    "Larix decidua": {
        "n": {"lt": "Europinis maumedis", "en": "European larch", "de": "Europäische Lärche",
              "fr": "Mélèze d'Europe", "es": "Alerce europeo", "uk": "Модрина європейська"},
        "d": {
            "lt": "Vienintelis Lietuvoje spyglius numetantis spygliuotis – rudenį spygliai nusidažo aukso geltonumo ir nukrinta, todėl žiemą maumedis stovi plikas. Spygliai minkšti, šviesiai žali, auga kekėmis ant trumpųjų ūglių – liesdamas nesudursi. Kankorėžiai smulkūs, kiaušiniški, 2–4 cm ilgio, subręsta pirmaisiais metais. Auga greitai, mėgsta šviesą ir derlingas dirvas.",
            "en": "The only deciduous conifer in Lithuania – its needles turn golden-yellow in autumn and drop, so in winter the larch stands bare. Needles are soft, light green, growing in tufts on short shoots – no prickles when you touch them. Cones are small, ovoid, 2–4 cm long, ripening in a single year. Grows fast, prefers light and fertile soils.",
            "de": "Der einzige sommergrüne Nadelbaum Litauens – seine Nadeln werden im Herbst goldgelb und fallen ab, im Winter steht die Lärche also kahl. Nadeln sind weich, hellgrün, in Büscheln an Kurztrieben – beim Anfassen pikst nichts. Zapfen sind klein, eiförmig, 2–4 cm lang, reifen in einem Jahr. Wächst schnell, bevorzugt Licht und fruchtbare Böden.",
            "fr": "Le seul conifère caduc de Lituanie – ses aiguilles jaunissent en automne et tombent, le mélèze reste donc nu en hiver. Les aiguilles sont douces, vert clair, en touffes sur des rameaux courts – aucune épine au toucher. Les cônes sont petits, ovoïdes, longs de 2–4 cm, mûrissant en un an. Pousse vite, préfère la lumière et les sols fertiles.",
            "es": "La única conífera caducifolia de Lituania – sus acículas se vuelven de color amarillo dorado en otoño y caen, por lo que en invierno el alerce queda desnudo. Las acículas son suaves, verde claro, en manojos sobre brotes cortos – nada punzante al tacto. Los conos son pequeños, ovoides, de 2–4 cm, madurando en un solo año. Crece rápido, prefiere luz y suelos fértiles.",
            "uk": "Єдина в Литві листопадна хвойна – її голки восени стають золотаво-жовтими й опадають, тож узимку модрина стоїть гола. Голки м'які, світло-зелені, ростуть пучками на коротких пагонах – на дотик не колються. Шишки дрібні, яйцеподібні, 2–4 см завдовжки, достигають за один рік. Росте швидко, любить світло й родючі ґрунти.",
        },
    },
    "Malus sylvestris": {
        "n": {"lt": "Miškinė obelis", "en": "European crab apple", "de": "Holzapfel",
              "fr": "Pommier sauvage", "es": "Manzano silvestre", "uk": "Яблуня лісова"},
        "d": {
            "lt": "Nedidelis medis, dažnai su dygliuotomis šakelėmis – saugokis, kai skinasi kelią pro tankmę. Lapai ovalūs, dantyti, blizgūs. Žiedai balti arba rausvi, kvapnūs, žydi gegužę ir traukia bites iš tolo. Vaisiai – smulkūs, rūgštūs obuoliai, subręsta rugsėjį, bet skanūs tik po šalnų. Auga miškų pakraščiuose ir krūmynuose.",
            "en": "A small tree, often with thorny twigs – watch out when you push through thickets. Leaves are oval, toothed, glossy. Flowers are white or pinkish, fragrant, blooming in May and drawing bees from afar. Fruits are small, sour apples ripening in September, tasty only after the first frost. Grows in woodland edges and thickets.",
            "de": "Ein kleiner Baum, oft mit dornigen Zweigen – Vorsicht beim Durchqueren von Dickichten. Blätter oval, gezähnt, glänzend. Blüten weiß oder rosastichig, duftend, blühen im Mai und locken Bienen von weit her an. Früchte sind kleine, saure Äpfel, die im September reifen und erst nach dem ersten Frost schmecken. Wächst an Waldrändern und in Gebüschen.",
            "fr": "Un petit arbre, souvent à rameaux épineux – attention en traversant les fourrés. Feuilles ovales, dentées, luisantes. Fleurs blanches ou rosées, parfumées, fleurissant en mai et attirant les abeilles de loin. Fruits : petites pommes acides mûrissant en septembre, bonnes seulement après les premières gelées. Pousse en lisière de bois et dans les fourrés.",
            "es": "Un árbol pequeño, a menudo con ramillas espinosas – cuidado al atravesar matorrales. Hojas ovaladas, dentadas, brillantes. Flores blancas o rosadas, fragantes, que florecen en mayo y atraen abejas desde lejos. Los frutos son manzanas pequeñas y ácidas que maduran en septiembre, sabrosas solo tras las primeras heladas. Crece en bordes de bosque y matorrales.",
            "uk": "Невелике дерево, часто з колючими пагонами – обережно, продираючись крізь хащі. Листки овальні, зубчасті, блискучі. Квіти білі або рожевуваті, запашні, цвітуть у травні й приваблюють бджіл здалеку. Плоди – дрібні кислі яблука, достигають у вересні, смачні лише після перших заморозків. Росте на узліссях і в чагарниках.",
        },
    },
    "Picea abies": {
        "n": {"lt": "Paprastoji eglė", "en": "Norway spruce", "de": "Gemeine Fichte",
              "fr": "Épicéa commun", "es": "Picea común", "uk": "Ялина європейська"},
        "d": {
            "lt": "Siaurai piramidinis, simetriškas medis su nusvirusiomis šakomis – klasikinė Kalėdų eglutė. Spygliai tamsiai žali, 1–2,5 cm ilgio, išsidėstę spirališkai aplink šakelę. Kankorėžiai ilgi, cilindriški, kabantys žemyn – jie subręsta ir nukrinta per vieną sezoną. Auga derlingose, drėgnose dirvose, dažna mišriuose miškuose.",
            "en": "A narrowly pyramidal, symmetrical tree with drooping branches – the classic Christmas tree. Needles are dark green, 1–2.5 cm long, spirally arranged around the twig. Cones are long, cylindrical, and hang downwards – they ripen and fall within one season. Grows on fertile, moist soils, common in mixed woodland.",
            "de": "Ein schmal-pyramidaler, symmetrischer Baum mit überhängenden Zweigen – der klassische Weihnachtsbaum. Nadeln sind dunkelgrün, 1–2,5 cm lang, spiralig um den Zweig angeordnet. Zapfen sind lang, zylindrisch und hängen nach unten – sie reifen und fallen in einer Saison. Wächst auf fruchtbaren, feuchten Böden, häufig in Mischwäldern.",
            "fr": "Un arbre étroitement pyramidal et symétrique, aux branches retombantes – le sapin de Noël classique. Aiguilles vert foncé, longues de 1–2,5 cm, disposées en spirale autour du rameau. Cônes longs, cylindriques, pendants – ils mûrissent et tombent en une seule saison. Pousse sur des sols fertiles et humides, commun dans les bois mixtes.",
            "es": "Un árbol estrechamente piramidal y simétrico, con ramas colgantes – el clásico árbol de Navidad. Acículas verde oscuro, de 1–2,5 cm, dispuestas en espiral alrededor de la ramilla. Conos largos, cilíndricos y colgantes – maduran y caen en una sola estación. Crece en suelos fértiles y húmedos, común en bosques mixtos.",
            "uk": "Вузько-пірамідальне, симетричне дерево з пониклими гілками – класична різдвяна ялинка. Голки темно-зелені, 1–2,5 см завдовжки, розташовані спірально навколо пагона. Шишки довгі, циліндричні, звисають донизу – достигають і опадають за один сезон. Росте на родючих вологих ґрунтах, часта в мішаних лісах.",
        },
    },
    "Pinus sylvestris": {
        "n": {"lt": "Paprastoji pušis", "en": "Scots pine", "de": "Waldkiefer",
              "fr": "Pin sylvestre", "es": "Pino silvestre", "uk": "Сосна звичайна"},
        "d": {
            "lt": "Spygliai 4–7 cm ilgio, išsidėstę po du ir šiek tiek susisukę – tarsi mažos žalios žirklės. Viršutinė kamieno žievė oranžiškai rausva, pleiskanojanti plokštelėmis – iš tolo atrodo lyg įdegusi. Kankorėžiai smulkūs, kūgiški, subręsta antraisiais metais. Auga sausuose, smėlėtuose plotuose, dažna pušynuose – ten, kur kiti medžiai sunkiai prigyja.",
            "en": "Needles are 4–7 cm long, arranged in pairs and slightly twisted – like small green scissors. The upper trunk bark is orange-red, flaking in plates – it looks sun-tanned from afar. Cones are small and conical, ripening in the second year. Grows on dry, sandy sites, common in pine forests – places where other trees struggle.",
            "de": "Nadeln sind 4–7 cm lang, paarweise und leicht gedreht – wie kleine grüne Scheren. Die Rinde des oberen Stamms ist orangerot und blättert in Platten ab – sie wirkt aus der Ferne sonnengebräunt. Zapfen sind klein und kegelförmig, reifen im zweiten Jahr. Wächst an trockenen, sandigen Standorten, häufig in Kiefernwäldern – wo andere Bäume kaum gedeihen.",
            "fr": "Aiguilles longues de 4–7 cm, groupées par deux et légèrement torsadées – comme de petits ciseaux verts. L'écorce du haut du tronc est orange-rouge, s'écaillant en plaques – de loin, elle paraît bronzée. Les cônes sont petits et coniques, mûrissant la deuxième année. Pousse dans des sites secs et sablonneux, commun dans les pinèdes – là où les autres arbres ont du mal.",
            "es": "Acículas de 4–7 cm, agrupadas por pares y algo retorcidas – como pequeñas tijeras verdes. La corteza de la parte alta del tronco es de color naranja rojizo y se descama en placas – de lejos parece bronceada. Los conos son pequeños y cónicos, madurando el segundo año. Crece en lugares secos y arenosos, común en pinares – donde otros árboles apenas prosperan.",
            "uk": "Голки 4–7 см завдовжки, зібрані по дві й трохи скручені – наче маленькі зелені ножиці. Кора верхньої частини стовбура оранжево-руда, відшаровується пластинками – здалеку виглядає засмаглою. Шишки дрібні, конічні, достигають на другий рік. Росте на сухих піщаних місцях, часта в соснових лісах – там, де інші дерева ледве виживають.",
        },
    },
    "Populus nigra": {
        "n": {"lt": "Juodoji tuopa", "en": "Black poplar", "de": "Schwarz-Pappel",
              "fr": "Peuplier noir", "es": "Álamo negro", "uk": "Тополя чорна"},
        "d": {
            "lt": "Storas, plačiai išsišakojęs kamienas su tamsia, giliai sueižėjusia žieve – atrodo tarsi raukšlėtas dramblio odos. Lapai trikampiški arba rombiški, smailūs, ilgais koteliais. Auga upių slėniuose, drėgnose, derlingose dirvose – mėgsta, kai po kojomis šlapia. Šiuo metu tai reta, saugoma rūšis, tad pamatęs pasidžiauk.",
            "en": "A thick, widely branching trunk with dark, deeply fissured bark – it looks like wrinkled elephant skin. Leaves are triangular or rhombic, pointed, with long petioles. Grows in river valleys on moist, fertile soils – loves wet feet. It is now a rare, protected species, so be happy if you spot one.",
            "de": "Ein dicker, breit verzweigter Stamm mit dunkler, tief gefurchter Rinde – sie sieht aus wie runzlige Elefantenhaut. Blätter dreieckig oder rhombisch, zugespitzt, mit langen Stielen. Wächst in Flusstälern auf feuchten, fruchtbaren Böden – liebt nasse Füße. Heute eine seltene, geschützte Art – freu dich, wenn du eine siehst.",
            "fr": "Un tronc épais et largement ramifié à l'écorce sombre et profondément fissurée – on dirait une peau d'éléphant ridée. Feuilles triangulaires ou rhombiques, pointues, à longs pétioles. Pousse dans les vallées fluviales sur des sols humides et fertiles – aime avoir les pieds dans l'eau. C'est aujourd'hui une espèce rare et protégée – réjouis-toi si tu en croises un.",
            "es": "Un tronco grueso y muy ramificado, con corteza oscura y profundamente agrietada – parece piel de elefante arrugada. Hojas triangulares o rómbicas, puntiagudas, con pecíolos largos. Crece en valles fluviales sobre suelos húmedos y fértiles – le encanta tener los pies mojados. Hoy es una especie rara y protegida – alégrate si te topas con uno.",
            "uk": "Товстий, широко розгалужений стовбур із темною, глибоко потрісканою корою – наче зморшкувата слоняча шкіра. Листки трикутні або ромбічні, загострені, з довгими черешками. Росте в річкових долинах на вологих родючих ґрунтах – любить мокрі ноги. Нині це рідкісний, охоронюваний вид – тож радій, якщо зустрінеш.",
        },
    },
    "Populus tremula": {
        "n": {"lt": "Drebulė", "en": "Eurasian aspen", "de": "Zitter-Pappel",
              "fr": "Peuplier tremble", "es": "Álamo temblón", "uk": "Осика"},
        "d": {
            "lt": "Lapai apvalūs, ilgais, plokščiais koteliais – todėl jie virpa net lengvame vėjyje, ir medis tarsi „dreba“. Žievė lygi, pilkai žalia, su rombiškomis „akimis“ – jaunystėje ji būna lygi kaip popierius. Rudenį lapai tampa raudoni arba geltoni ir sukuria tikrą spalvų šventę. Auga miškų pakraščiuose, dažnai drėgnose vietose.",
            "en": "Leaves are rounded with long, flattened petioles – so they tremble even in a light breeze, and the tree seems to 'quake'. Bark is smooth, grey-green, with diamond-shaped 'eyes' – when young it's as smooth as paper. In autumn the leaves turn red or yellow, creating a real festival of colour. Grows in woodland edges, often on moist sites.",
            "de": "Blätter rund mit langen, abgeflachten Stielen – sie zittern schon bei leichtem Wind, und der Baum scheint zu 'beben'. Rinde glatt, graugrün, mit rautenförmigen 'Augen' – in jungen Jahren glatt wie Papier. Im Herbst färben sich die Blätter rot oder gelb – ein wahres Farbenfest. Wächst an Waldrändern, oft auf feuchten Standorten.",
            "fr": "Feuilles rondes à longs pétioles aplatis – elles tremblent au moindre souffle de vent, et l'arbre semble 'frémir'. Écorce lisse, gris-vert, avec des 'yeux' en losange – jeune, elle est lisse comme du papier. En automne, les feuilles deviennent rouges ou jaunes, créant une véritable fête des couleurs. Pousse en lisière de bois, souvent sur des sols humides.",
            "es": "Hojas redondeadas con pecíolos largos y aplanados – tiemblan incluso con una brisa ligera, y el árbol parece 'temblar'. Corteza lisa, gris-verde, con 'ojos' rómbicos – de joven es lisa como el papel. En otoño las hojas se vuelven rojas o amarillas, creando una auténtica fiesta de color. Crece en bordes de bosque, a menudo en lugares húmedos.",
            "uk": "Листки округлі, з довгими пласкими черешками – тож тремтять навіть від легкого вітерцю, і здається, ніби дерево 'трясеться'. Кора гладенька, сіро-зелена, з ромбічними 'вічками' – замолоду вона гладенька, як папір. Восени листки стають червоними або жовтими й створюють справжнє свято барв. Росте на узліссях, часто у вологих місцях.",
        },
    },
    "Prunus padus": {
        "n": {"lt": "Paprastoji ieva", "en": "Bird cherry", "de": "Gewöhnliche Traubenkirsche",
              "fr": "Merisier à grappes", "es": "Cerezo de racimo", "uk": "Черемха звичайна"},
        "d": {
            "lt": "Lapai pailgi, smulkiai dantyti, tamsiai žali. Pavasarį ieva pasipuošia ilgomis, kabančiomis, stipriai kvepiančiomis baltų žiedų kekėmis – jų kvapą pajusi dar prieš pamatydamas medį. Vaisiai – smulkios, juodos, kartoko skonio uogos, kurias mėgsta paukščiai. Auga drėgnose, derlingose dirvose, dažna upių slėniuose.",
            "en": "Leaves are oblong, finely toothed, dark green. In spring the bird cherry dresses up with long, drooping, intensely fragrant white flower racemes – you'll smell them before you see the tree. Fruits are small black berries with a slightly bitter taste, loved by birds. Grows on moist, fertile soils, common in river valleys.",
            "de": "Blätter länglich, fein gezähnt, dunkelgrün. Im Frühling schmückt sich die Traubenkirsche mit langen, hängenden, stark duftenden weißen Blütentrauben – du riechst sie, bevor du den Baum siehst. Früchte sind kleine schwarze Beeren mit leicht bitterem Geschmack, bei Vögeln beliebt. Wächst auf feuchten, fruchtbaren Böden, häufig in Flusstälern.",
            "fr": "Feuilles oblongues, finement dentées, vert foncé. Au printemps, le merisier se pare de longues grappes pendantes de fleurs blanches intensément parfumées – vous les sentirez avant de voir l'arbre. Les fruits sont de petites baies noires au goût légèrement amer, appréciées des oiseaux. Pousse sur des sols humides et fertiles, commun dans les vallées fluviales.",
            "es": "Hojas oblongas, finamente dentadas, verde oscuro. En primavera, el cerezo de racimo se engalana con largos racimos colgantes de flores blancas intensamente fragantes – los olerás antes de ver el árbol. Los frutos son pequeñas bayas negras de sabor algo amargo, apreciadas por los pájaros. Crece en suelos húmedos y fértiles, común en valles fluviales.",
            "uk": "Листки довгасті, дрібнозубчасті, темно-зелені. Навесні черемха вдягається в довгі пониклі суцвіття білих квітів із сильним ароматом – ви відчуєте їхній запах ще до того, як побачите дерево. Плоди – дрібні чорні ягоди з гіркуватим смаком, улюблені птахами. Росте на вологих родючих ґрунтах, часта в річкових долинах.",
        },
    },
    "Pyrus pyraster": {
        "n": {"lt": "Miškinė kriaušė", "en": "European wild pear", "de": "Wildbirne",
              "fr": "Poirier sauvage", "es": "Peral silvestre", "uk": "Груша лісова"},
        "d": {
            "lt": "Panaši į miškinę obelį, bet vaisiai kietesni, smulkūs, tikros kriaušės formos. Šakelės su aštriais dygliais – pro ją sunkiai prasiskinsi. Lapai blizgūs, apvaliai kiaušiniški, smulkiai dantyti. Žiedai balti, žydi balandį–gegužę, labai kvapnūs. Auga sausose, kalkingose dirvose, dažna krūmynuose.",
            "en": "Similar to the wild apple but with harder, smaller fruits of true pear shape. Twigs bear sharp thorns – hard to push through. Leaves are glossy, roundly ovate, finely toothed. Flowers are white, blooming April–May, very fragrant. Grows on dry, calcareous soils, common in thickets.",
            "de": "Ähnlich dem Holzapfel, aber mit härteren, kleineren Früchten in echter Birnenform. Zweige mit scharfen Dornen – schwer durchzukommen. Blätter glänzend, rundlich-eiförmig, fein gezähnt. Blüten weiß, Blüte April–Mai, sehr duftend. Wächst auf trockenen, kalkhaltigen Böden, häufig in Gebüschen.",
            "fr": "Semblable au pommier sauvage, mais aux fruits plus durs, plus petits, de vraie forme de poire. Rameaux à épines acérées – difficile de se frayer un chemin. Feuilles luisantes, arrondies-ovales, finement dentées. Fleurs blanches, floraison avril–mai, très parfumées. Pousse sur des sols secs et calcaires, commun dans les fourrés.",
            "es": "Similar al manzano silvestre pero con frutos más duros, pequeños, de auténtica forma de pera. Ramillas con espinas afiladas – difícil abrirse paso. Hojas brillantes, ovalado-redondeadas, finamente dentadas. Flores blancas, florece en abril–mayo, muy fragantes. Crece en suelos secos y calcáreos, común en matorrales.",
            "uk": "Схожа на яблуню лісову, але плоди твердіші, дрібні, справжньої грушоподібної форми. Пагони з гострими колючками – крізь неї важко продертися. Листки блискучі, округло-яйцеподібні, дрібнозубчасті. Квіти білі, цвіте у квітні–травні, дуже запашні. Росте на сухих вапняних ґрунтах, часта в чагарниках.",
        },
    },
    "Quercus petraea": {
        "n": {"lt": "Bekotis ąžuolas", "en": "Sessile oak", "de": "Traubeneiche",
              "fr": "Chêne sessile", "es": "Roble albar", "uk": "Дуб скельний"},
        "d": {
            "lt": "Panašus į paprastąjį ąžuolą, bet lapai turi aiškų kotelį, o gilės – be jo, sėdi tiesiai ant šakelės. Lapų skiltys lygesnės, lapai šiek tiek odiškesni, tarsi nulakuoti. Auga sausesnėse, dažnai kalvotose vietose. Mediena labai vertinama – iš jos statomi laivai, daromi baldai, statomos bažnyčios.",
            "en": "Similar to English oak, but leaves have a clear petiole and acorns sit directly on the twig without a stalk. Leaf lobes are more regular, leaves slightly more leathery, as if varnished. Grows on drier, often hilly sites. Its timber is highly prized – used for ships, furniture and churches.",
            "de": "Ähnlich der Stieleiche, aber die Blätter haben einen deutlichen Stiel und die Eicheln sitzen ohne Stiel direkt am Zweig. Blattlappen regelmäßiger, Blätter etwas lederartig, wie lackiert. Wächst an trockeneren, oft hügeligen Standorten. Ihr Holz ist äußerst begehrt – für Schiffe, Möbel, Kirchen.",
            "fr": "Semblable au chêne pédonculé, mais les feuilles ont un pétiole net et les glands sont sessiles, directement sur le rameau. Lobes foliaires plus réguliers, feuilles légèrement coriaces, comme vernies. Pousse sur des sites plus secs, souvent vallonnés. Son bois est très prisé – pour les navires, les meubles, les églises.",
            "es": "Similar al roble común, pero las hojas tienen un pecíolo claro y las bellotas se sientan directamente sobre la ramilla, sin pedúnculo. Los lóbulos son más regulares, las hojas algo más coriáceas, como barnizadas. Crece en lugares más secos, a menudo colinares. Su madera es muy apreciada – para barcos, muebles, iglesias.",
            "uk": "Схожий на дуб звичайний, але листки мають виразний черешок, а жолуді сидять без нього, прямо на пагоні. Лопаті листків рівніші, листки трохи шкірясті, наче лаковані. Росте на сухіших, часто пагорбистих місцях. Його деревина вельми цінується – для кораблів, меблів, церков.",
        },
    },
    "Quercus robur": {
        "n": {"lt": "Paprastasis ąžuolas", "en": "English oak", "de": "Stieleiche",
              "fr": "Chêne pédonculé", "es": "Roble común", "uk": "Дуб звичайний"},
        "d": {
            "lt": "Lapai su apvaliomis skiltimis, beveik bekociai – tarsi žalios bangos. Žievė giliai sueižėjusi, tamsiai ruda, laikui bėgant tampa tarsi šarvai. Gilės su dubenėliu, išsidėsčiusios ant ilgo kotelio – jas mėgsta šernai, paukščiai ir vaikai. Ilgaamžis milžinas, galintis gyventi 500–1000 metų – tikras miško karalius.",
            "en": "Leaves with rounded lobes, almost sessile – like green waves. Bark deeply fissured, dark brown, becoming like armour over time. Acorns sit in a cup on a long stalk – loved by wild boar, birds and children. A long-lived giant, able to reach 500–1000 years – a true king of the forest.",
            "de": "Blätter mit gerundeten Lappen, fast sitzend – wie grüne Wellen. Rinde tief gefurcht, dunkelbraun, wird mit der Zeit wie eine Rüstung. Eicheln in einem Becher an langem Stiel – beliebt bei Wildschweinen, Vögeln und Kindern. Ein langlebiger Riese, kann 500–1000 Jahre alt werden – ein wahrer König des Waldes.",
            "fr": "Feuilles à lobes arrondis, presque sessiles – comme des vagues vertes. Écorce profondément fissurée, brun foncé, devenant comme une armure avec l'âge. Glands dans une cupule sur un long pédoncule – appréciés des sangliers, des oiseaux et des enfants. Un géant centenaire, pouvant atteindre 500 à 1000 ans – un vrai roi de la forêt.",
            "es": "Hojas con lóbulos redondeados, casi sésiles – como olas verdes. Corteza profundamente agrietada, de color marrón oscuro, que se vuelve como una armadura con la edad. Bellotas en una cúpula sobre un largo pedúnculo – apreciadas por jabalíes, aves y niños. Un gigante longevo, capaz de alcanzar los 500–1000 años – un auténtico rey del bosque.",
            "uk": "Листки з округлими лопатями, майже сидячі – наче зелені хвилі. Кора глибоко потріскана, темно-бура, з часом стає мов броня. Жолуді в плюсці на довгому черешку – їх люблять дикі кабани, птахи й діти. Довговічний велетень, здатний прожити 500–1000 років – справжній король лісу.",
        },
    },
    "Salix alba": {
        "n": {"lt": "Baltasis gluosnis", "en": "White willow", "de": "Silber-Weide",
              "fr": "Saule blanc", "es": "Sauce blanco", "uk": "Верба біла"},
        "d": {
            "lt": "Lapai pailgi, sidabriškai žali, ypač apatinė pusė, su šilkiniais plaukeliais – lyg būtų apibarstyti miltais. Šakelės lanksčios, geltonos arba rausvos – iš jų pindavo krepšius ir tvoras. Auga prie vandens, upių ir ežerų pakrantėse. Dažnai naudojamas kaip dekoratyvus medis parkuose ir prie tvenkinių.",
            "en": "Leaves are long, silvery-green – especially beneath – with silky hairs, as if dusted with flour. Twigs are flexible, yellow or reddish – used for weaving baskets and fences. Grows by water, along rivers and lake shores. Often planted as an ornamental tree in parks and by ponds.",
            "de": "Blätter lang, silbrig-grün – besonders unterseits – mit seidigen Haaren, als wären sie bemehlt. Zweige biegsam, gelb oder rötlich – zum Flechten von Körben und Zäunen. Wächst am Wasser, an Flüssen und Seeufern. Oft als Zierbaum in Parks und an Teichen gepflanzt.",
            "fr": "Feuilles longues, vert argenté – surtout dessous – aux poils soyeux, comme saupoudrées de farine. Rameaux souples, jaunes ou rougeâtres – utilisés pour tresser paniers et clôtures. Pousse au bord de l'eau, le long des rivières et des lacs. Souvent planté comme arbre ornemental dans les parcs et au bord des étangs.",
            "es": "Hojas largas, verde plateado – sobre todo por el envés – con pelos sedosos, como si estuvieran enharinadas. Ramillas flexibles, amarillas o rojizas – usadas para tejer cestas y cercas. Crece junto al agua, en ríos y orillas de lagos. A menudo plantado como árbol ornamental en parques y junto a estanques.",
            "uk": "Листки довгі, сріблясто-зелені – особливо знизу – з шовковистими волосками, наче припудрені борошном. Пагони гнучкі, жовті або червоняві – з них плели кошики й тини. Росте біля води, по берегах річок та озер. Часто висаджують як декоративне дерево в парках і біля ставків.",
        },
    },
    "Salix caprea": {
        "n": {"lt": "Blindė", "en": "Goat willow", "de": "Sal-Weide",
              "fr": "Saule marsault", "es": "Sauce cabruno", "uk": "Верба козяча"},
        "d": {
            "lt": "Stambūs, platūs, apvalūs lapai su raukšlėtu, šiek tiek plaukuotu paviršiumi – tarsi gofruoti. Pavasarį – dideli, pilki, pūkiniai „kačiukai“ (žiedynai), kuriuos mėgsta bitės ir vaikai. Krūmas arba mažas medis. Auga miškų pakraščiuose ir pagrioviuose, vienas pirmųjų pasitinka pavasarį.",
            "en": "Large, broad, rounded leaves with a wrinkled, slightly hairy surface – as if corrugated. In spring it bears large grey, downy catkins, beloved by bees and children. A shrub or small tree. Grows on woodland edges and roadside ditches – one of the first to greet the spring.",
            "de": "Große, breite, runde Blätter mit runzliger, leicht behaarter Oberfläche – wie gewellt. Im Frühling trägt sie große graue, flauschige Kätzchen, geliebt von Bienen und Kindern. Ein Strauch oder kleiner Baum. Wächst an Waldrändern und Straßengräben – eine der ersten, die den Frühling begrüßen.",
            "fr": "Grandes feuilles larges et arrondies à surface ridée et légèrement poilue – comme gaufrées. Au printemps, elle porte de gros chatons gris et duveteux, aimés des abeilles et des enfants. Un arbuste ou petit arbre. Pousse en lisière de bois et dans les fossés – l'un des premiers à saluer le printemps.",
            "es": "Hojas grandes, anchas y redondeadas, con superficie arrugada y algo peluda – como corrugadas. En primavera luce grandes amentos grises y vellosos, amados por abejas y niños. Un arbusto o pequeño árbol. Crece en bordes de bosque y cunetas – uno de los primeros en saludar la primavera.",
            "uk": "Великі, широкі, округлі листки зі зморшкуватою, трохи опушеною поверхнею – наче гофровані. Навесні – великі сірі пухнасті 'котики' (судвіття), які люблять бджоли й діти. Кущ або невелике дерево. Росте на узліссях і в кюветах – один із перших вітає весну.",
        },
    },
    "Salix fragilis": {
        "n": {"lt": "Trapusis gluosnis", "en": "Crack willow", "de": "Bruch-Weide",
              "fr": "Saule fragile", "es": "Mimbrera frágil", "uk": "Верба ламка"},
        "d": {
            "lt": "Labai panašus į baltąjį gluosnį, bet šakelės lengvai lūžta – iš čia ir „trapusis“ vardas, girdisi net garsus spragtelėjimas. Lapai blizgūs, plonesni, ryškiai žali, be šilkinio plaukelio. Auga prie vandens, dažnai šalia baltųjų gluosnių – jie mėgsta augti drauge. Dažnai kryžminasi su baltuoju gluosniu, todėl kartais sunku atskirti.",
            "en": "Very similar to white willow but its twigs snap easily – hence the name, you can even hear a loud crack. Leaves are glossy, thinner, bright green, without silky hairs. Grows by water, often alongside white willows – they like growing together. Frequently hybridises with white willow, which can make them hard to tell apart.",
            "de": "Sehr ähnlich der Silber-Weide, aber ihre Zweige brechen leicht – daher der Name, man hört sogar ein lautes Knacken. Blätter glänzend, dünner, hellgrün, ohne seidige Haare. Wächst am Wasser, oft neben Silber-Weiden – sie wachsen gerne zusammen. Hybridisiert häufig mit der Silber-Weide, was die Unterscheidung erschwert.",
            "fr": "Très semblable au saule blanc, mais ses rameaux cassent facilement – d'où son nom, on entend même un craquement net. Feuilles luisantes, plus fines, vert vif, sans poils soyeux. Pousse au bord de l'eau, souvent aux côtés de saules blancs – ils aiment pousser ensemble. S'hybride fréquemment avec le saule blanc, ce qui les rend parfois difficiles à distinguer.",
            "es": "Muy similar al sauce blanco, pero sus ramillas se rompen con facilidad – de ahí su nombre, incluso se oye un chasquido. Hojas brillantes, más finas, verde brillante, sin pelos sedosos. Crece junto al agua, a menudo junto a sauces blancos – les gusta crecer juntos. Se hibrida con frecuencia con el sauce blanco, lo que a veces los hace difíciles de distinguir.",
            "uk": "Дуже схожа на вербу білу, але її пагони легко ламаються – звідси й назва, чути навіть голосний тріск. Листки блискучі, тонші, яскраво-зелені, без шовковистих волосків. Росте біля води, часто поряд із вербами білими – вони люблять рости разом. Часто гібридизується з вербою білою, що іноді ускладнює розрізнення.",
        },
    },
    "Sorbus aucuparia": {
        "n": {"lt": "Paprastasis šermukšnis", "en": "Rowan", "de": "Vogelbeere",
              "fr": "Sorbier des oiseleurs", "es": "Serbal de los cazadores", "uk": "Горобина звичайна"},
        "d": {
            "lt": "Lapai sudėtiniai, su 11–15 lapelių – atrodo tarsi žalios plunksnos. Žievė lygi, pilka, su skersinėmis žymėmis. Pavasarį žydi baltais žiedais, o rudenį prinoksta oranžinės uogos, sukabintos kekėmis – jų negali nepastebėti. Uogos mėgstamos paukščių, o žmonės iš jų verda sultis ir uogas – bet žalias valgyti negalima.",
            "en": "Leaves are pinnate with 11–15 leaflets – they look like green feathers. Bark is smooth and grey with horizontal lenticels. Flowers are white in spring, and orange berries ripen in autumn in bright clusters – impossible to miss. The berries are loved by birds; people make juice and preserves from them – but don't eat them raw.",
            "de": "Blätter gefiedert mit 11–15 Fiederblättchen – wie grüne Federn. Rinde glatt, grau, mit waagerechten Lentizellen. Blüten weiß im Frühling, im Herbst reifen orange Beeren in leuchtenden Doldentrauben – unübersehbar. Die Beeren sind bei Vögeln beliebt; Menschen machen Saft und Marmelade daraus – roh aber nicht essen.",
            "fr": "Feuilles composées pennées à 11–15 folioles – comme des plumes vertes. Écorce lisse, grise, à lenticelles horizontales. Fleurs blanches au printemps, en automne mûrissent des baies orange en grappes éclatantes – impossibles à manquer. Baies appréciées des oiseaux ; on en fait jus et confitures – mais ne les mangez pas crues.",
            "es": "Hojas compuestas pinnadas con 11–15 foliolos – parecen plumas verdes. Corteza lisa y gris con lenticelas horizontales. Flores blancas en primavera, y en otoño maduran bayas naranjas en vistosos racimos – imposibles de pasar por alto. Las bayas gustan a los pájaros; con ellas se hacen zumos y mermeladas – pero no las comas crudas.",
            "uk": "Листки складні, пірчасті, з 11–15 листочками – наче зелені пера. Кора гладенька, сіра, з поперечними сочевичками. Квіти білі навесні, а восени достигають оранжеві ягоди у яскравих гронах – їх годі не помітити. Ягоди люблять птахи; люди варять із них сік і варення – але сирими не їсти.",
        },
    },
    "Taxus baccata": {
        "n": {"lt": "Europinis kukmedis", "en": "European yew", "de": "Europäische Eibe",
              "fr": "If commun", "es": "Tejo común", "uk": "Тис ягідний"},
        "d": {
            "lt": "Amžinai žalias medis su plokščiais, 2–3 cm spygliukais – apačioje jie turi dvi šviesias juostas. Sėklos – su ryškiai raudonu, minkštu gaubtu, kuris atrodo kaip uoga; pati sėkla labai nuodinga, bet gaubtas – ne. Auga pavėsyje, labai ilgaamžis, gali gyventi net 2000 metų – tikras ilgaamžiškumo rekordininkas.",
            "en": "An evergreen tree with flat needles 2–3 cm long – they have two pale bands on the underside. Seeds sit in a bright red fleshy aril that looks like a berry; the seed itself is highly poisonous, though the aril is not. Grows in shade; extremely long-lived, can reach 2000 years – a true record holder for longevity.",
            "de": "Ein immergrüner Baum mit flachen Nadeln, 2–3 cm lang – unterseits mit zwei hellen Streifen. Samen in einem leuchtend roten fleischigen Arillus, der wie eine Beere aussieht; der Same selbst ist stark giftig, der Arillus nicht. Wächst im Schatten; extrem langlebig, kann 2000 Jahre erreichen – ein echter Rekordhalter.",
            "fr": "Un arbre toujours vert à aiguilles plates de 2–3 cm – avec deux bandes claires dessous. Les graines sont logées dans un arille charnu rouge vif qui ressemble à une baie ; la graine elle-même est très toxique, mais pas l'arille. Pousse à l'ombre ; extrêmement longévif, peut atteindre 2000 ans – un vrai recordman de longévité.",
            "es": "Un árbol perennifolio con acículas planas de 2–3 cm – con dos bandas claras en el envés. Las semillas están envueltas en un arilo carnoso rojo brillante que parece una baya; la semilla en sí es muy venenosa, aunque el arilo no. Crece en la sombra; extremadamente longevo, puede alcanzar los 2000 años – un auténtico récord de longevidad.",
            "uk": "Вічнозелене дерево з плоскими голками 2–3 см завдовжки – знизу вони мають дві світлі смуги. Насіння оточене яскраво-червоним м'ясистим принасінником, схожим на ягоду; саме насіння дуже отруйне, а принасінник – ні. Росте в тіні; надзвичайно довговічне, може сягати 2000 років – справжній рекордсмен довголіття.",
        },
    },
    "Tilia cordata": {
        "n": {"lt": "Mažalapė liepa", "en": "Small-leaved lime", "de": "Winter-Linde",
              "fr": "Tilleul à petites feuilles", "es": "Tilo de hoja pequeña", "uk": "Липа дрібнолиста"},
        "d": {
            "lt": "Lapai širdiški, smulkiai dantyti, su ryškiomis gyslomis, apatinė pusė melsvai žalia – iš tolo atrodo tarsi švelniai aksominiai. Žiedai gelsvi, labai kvapnūs, su lapeliu-priedu – jų kvapas liepą paverčia tikru bičių rojumi. Žydi liepą, medingas. Auga derlingose, drėgnose dirvose, dažna parkuose ir prie namų.",
            "en": "Leaves are heart-shaped, finely toothed, with prominent veins and a bluish-green underside – they look softly velvety from afar. Flowers are pale yellow, very fragrant, with a leafy bract – their scent turns July into a real bee paradise. Blooms in July, highly melliferous. Grows on fertile, moist soils, common in parks and near homes.",
            "de": "Blätter herzförmig, fein gezähnt, mit ausgeprägten Adern und bläulich-grüner Unterseite – sie wirken aus der Ferne samtig. Blüten blassgelb, sehr duftend, mit einem Hochblatt – ihr Duft macht den Juli zum wahren Bienenparadies. Blüht im Juli, stark honiggebend. Wächst auf fruchtbaren, feuchten Böden, häufig in Parks und bei Häusern.",
            "fr": "Feuilles cordiformes, finement dentées, aux nervures marquées et au dessous vert bleuté – elles paraissent doucement veloutées de loin. Fleurs jaune pâle, très parfumées, avec une bractée foliacée – leur parfum transforme juillet en vrai paradis des abeilles. Floraison en juillet, très mellifère. Pousse sur des sols fertiles et humides, commun dans les parcs et près des maisons.",
            "es": "Hojas acorazonadas, finamente dentadas, con nervios marcados y envés verde azulado – de lejos parecen suavemente aterciopeladas. Flores amarillo pálido, muy fragantes, con una bráctea foliácea – su aroma convierte julio en un auténtico paraíso para las abejas. Florece en julio, muy melífera. Crece en suelos fértiles y húmedos, común en parques y cerca de casas.",
            "uk": "Листки серцеподібні, дрібнозубчасті, з виразними жилками й сизувато-зеленим низом – здалеку виглядають ніжно оксамитовими. Квіти блідо-жовті, дуже запашні, з листоподібним приквітком – їхній аромат перетворює липень на справжній бджолиний рай. Цвіте в липні, добрий медонос. Росте на родючих вологих ґрунтах, часта в парках і біля осель.",
        },
    },
    "Ulmus glabra": {
        "n": {"lt": "Kalninė guoba", "en": "Wych elm", "de": "Bergulme",
              "fr": "Orme de montagne", "es": "Olmo de montaña", "uk": "В'яз гірський"},
        "d": {
            "lt": "Dideli, šiurkštūs lapai su nelygiu, dvigubu pamatu – tarsi kas būtų nelygiai įkirpęs. Vaisiai – plokšti, sparnuoti riešutėliai, sukabinti kekėmis, subręsta dar pavasarį. Žievė ilgai lieka lygi, vėliau sueižėja. Auga derlingose, drėgnose dirvose, dažna mišriuose miškuose – mėgsta šešėlį.",
            "en": "Large, rough leaves with an unequal, doubly serrate base – as if unevenly cut. Fruits are flat, winged samaras clustered in bunches, ripening in spring. Bark stays smooth for a long time, later fissuring. Grows on fertile, moist soils, common in mixed woodland – loves shade.",
            "de": "Große, raue Blätter mit ungleicher, doppelt gesägter Basis – als wären sie ungleich eingeschnitten. Früchte sind flache, geflügelte Spaltfrüchte in Büscheln, reifen schon im Frühling. Rinde bleibt lange glatt, später gefurcht. Wächst auf fruchtbaren, feuchten Böden, häufig in Mischwäldern – liebt Schatten.",
            "fr": "Grandes feuilles rugueuses à base inégale et doublement dentée – comme découpées irrégulièrement. Fruits plats et ailés, groupés en bouquets, mûrissant dès le printemps. L'écorce reste longtemps lisse, puis se fissure. Pousse sur des sols fertiles et humides, commun dans les bois mixtes – aime l'ombre.",
            "es": "Hojas grandes y ásperas con base desigual y doblemente aserrada – como cortadas irregularmente. Frutos planos y alados, agrupados en racimos, que maduran ya en primavera. La corteza permanece lisa mucho tiempo, luego se agrieta. Crece en suelos fértiles y húmedos, común en bosques mixtos – le encanta la sombra.",
            "uk": "Великі шорсткі листки з нерівною, двічі пилчастою основою – наче нерівно надрізані. Плоди – плоскі крилаті двосім'янки, зібрані в пучки, достигають уже навесні. Кора довго залишається гладенькою, згодом тріскається. Росте на родючих вологих ґрунтах, частий у мішаних лісах – любить затінок.",
        },
    },
    "Ulmus laevis": {
        "n": {"lt": "Paprastoji vinkšna", "en": "European white elm", "de": "Flatterulme",
              "fr": "Orme lisse", "es": "Olmo temblón", "uk": "В'яз гладкий"},
        "d": {
            "lt": "Panaši į guobą, bet lapai lygesni, mažiau šiurkštūs, pamatas simetriškesnis. Vaisiai – sparnuoti, su blakstienėlėmis palei kraštą, sukabinti ilgais koteliais. Žievė pilkai ruda, sueižėjusi. Auga drėgnose, derlingose dirvose, dažna prie upių – ten kur drėgmė niekada netrūksta.",
            "en": "Similar to wych elm, but leaves are smoother, less rough, with a more symmetrical base. Fruits are winged with ciliate margins, hanging from long stalks. Bark is grey-brown, fissured. Grows in moist, fertile soils, common near rivers – where moisture never runs short.",
            "de": "Ähnlich der Bergulme, aber Blätter glatter, weniger rau, mit symmetrischerer Basis. Früchte geflügelt mit bewimperten Rändern, an langen Stielen. Rinde graubraun, gefurcht. Wächst auf feuchten, fruchtbaren Böden, häufig an Flüssen – wo es nie an Feuchtigkeit mangelt.",
            "fr": "Semblable à l'orme de montagne, mais feuilles plus lisses, moins rugueuses, à base plus symétrique. Fruits ailés à bords ciliés, suspendus à de longs pédoncules. Écorce gris-brun, fissurée. Pousse sur des sols humides et fertiles, commun près des rivières – là où l'humidité ne manque jamais.",
            "es": "Similar al olmo de montaña, pero con hojas más lisas, menos ásperas, de base más simétrica. Frutos alados con márgenes ciliados, colgando de largos pedúnculos. Corteza gris-marrón, agrietada. Crece en suelos húmedos y fértiles, común cerca de ríos – donde la humedad nunca escasea.",
            "uk": "Схожий на в'яз гірський, але листки гладші, менш шорсткі, з симетричнішою основою. Плоди крилаті, з війчастими краями, звисають на довгих ніжках. Кора сіро-бура, потріскана. Росте на вологих родючих ґрунтах, частий біля річок – там, де вологи завжди вдосталь.",
        },
    },
    "Ulmus minor": {
        "n": {"lt": "Paprastasis skirpstas", "en": "Field elm", "de": "Feldulme",
              "fr": "Orme champêtre", "es": "Olmo común", "uk": "В'яз граболистий"},
        "d": {
            "lt": "Smulkesni lapai nei guobos, dažnai su kamštinėmis šakelėmis – jos atrodo tarsi sparnuotos. Vaisiai – sparnuoti, su blakstienėlėmis. Žievė tamsiai ruda, giliai sueižėjusi. Auga sausesnėse, šiltesnėse vietose, dažnas krūmynuose ir pakelėse – jam patinka saulė ir lengvesnė dirva.",
            "en": "Leaves smaller than wych elm, often with corky twigs – they look like they have wings. Fruits are winged, with ciliate margins. Bark is dark brown, deeply fissured. Grows on drier, warmer sites, common in thickets and roadside verges – it likes sun and lighter soils.",
            "de": "Blätter kleiner als bei der Bergulme, oft mit korkigen Zweigen – sie wirken wie geflügelt. Früchte geflügelt, mit bewimperten Rändern. Rinde dunkelbraun, tief gefurcht. Wächst an trockeneren, wärmeren Standorten, häufig in Gebüschen und an Straßenrändern – liebt Sonne und leichtere Böden.",
            "fr": "Feuilles plus petites que celles de l'orme de montagne, souvent à rameaux liégeux – ils semblent ailés. Fruits ailés à bords ciliés. Écorce brun foncé, profondément fissurée. Pousse sur des sites plus secs et plus chauds, commun dans les fourrés et au bord des routes – aime le soleil et les sols légers.",
            "es": "Hojas más pequeñas que las del olmo de montaña, a menudo con ramillas suberosas – parecen aladas. Frutos alados con márgenes ciliados. Corteza marrón oscuro, profundamente agrietada. Crece en lugares más secos y cálidos, común en matorrales y bordes de camino – le gusta el sol y los suelos ligeros.",
            "uk": "Листки дрібніші, ніж у в'яза гірського, часто з корковими пагонами – вони виглядають наче крилаті. Плоди крилаті, з війчастими краями. Кора темно-бура, глибоко потріскана. Росте на сухіших, тепліших місцях, частий у чагарниках і обабіч доріг – любить сонце й легші ґрунти.",
        },
    },
}


def sp_name(latin, lang):
    d = SPECIES_DESCRIPTIONS.get(latin, {})
    n = d.get("n", {})
    return n.get(lang) or n.get("en") or latin


def sp_desc(latin, lang):
    d = SPECIES_DESCRIPTIONS.get(latin, {})
    dd = d.get("d", {})
    return dd.get(lang) or dd.get("en") or ""


def sp_feature(latin, lang):
    d = sp_desc(latin, lang)
    if not d:
        return ""
    parts = d.split(". ", 1)
    return parts[0].rstrip(".") + "."