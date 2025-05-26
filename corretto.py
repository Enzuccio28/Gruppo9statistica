def lettura(file):
    lista = []

    tabella = open(file,"r",encoding="utf-8")
    tabella1 = tabella.readline()

    for line in tabella:
        elementi = line.strip().split(",")
        informazioni_cron = elementi[0]
        età = elementi[1]
        paese = elementi[2]
        zona = elementi[3]
        grandezza = elementi[4]
        importanzaamb = elementi[5]
        genere = elementi[6]
        occupazione = elementi[7]
        preferirepagr = elementi[8]
        pagareconcarta = elementi[9]
        pagarecontante = elementi[10]
        quantitàprelievi = elementi[11]
        lontananzapuntoprelievo = elementi[12]
        mezzo = elementi[13]
        animaled = elementi[14]
        amiviaggiare = elementi[15]
        sport = elementi[16]
        tipospart = elementi[17]
        preferenza_luogo = elementi[18]

        lista.append({"informazioni cronologiche":informazioni_cron,"Quanti anni hai":età,"dove vivi":paese,"parte in cui vivi":zona,"Quanto è grande il comune in cui vivi":grandezza,"Quanto reputi importante la cura dell'ambiente":importanzaamb,"Genere":genere,"Occupazione":occupazione,"Come preferisic pagare":preferirepagr,"Se preferisci pagare via carta,perchè":pagareconcarta,"Preferenza contante":pagarecontante,"Quante volte prelevi denaro":quantitàprelievi,"Quanto è lontano il punto in cui prelievi":lontananzapuntoprelievo,"Che mezzo usi per andare a prelevare":mezzo,"Possiedi un animale domestico":animaled,"Ami viaggiare":amiviaggiare,"Pratichi o praticavi uno sport":sport,"Che sport":tipospart,"Weekend fuori porta, cosa preferisci?":preferenza_luogo})

    tabella.close()
    return lista

def media_età(tabella):
    
    senior = 0
    adultoaff = 0
    adulto = 0
    giovaneadul = 0
    giovane = 0
    adolescenza = 0
    totale = 0
    voti_numerici = []

    fascia_media = {
        "14-18(Adolescenza)": 16,
        "18-25(Giovane)": 21.5,
        "25-35(Giovane Adulto)": 30,
        "35-50(Adulto)": 42.5,
        "50-65(Adulto Affermato)": 57.5,
        "65+(Senior)": 75
    }

    for domanda in tabella:
        età = domanda["Quanti anni hai"]
        if età in fascia_media:
            totale += 1
            voti_numerici.append(fascia_media[età])

            if età == "14-18(Adolescenza)":
                adolescenza += 1
            elif età == "18-25(Giovane)":
                giovane += 1
            elif età == "25-35(Giovane Adulto)":
                giovaneadul += 1
            elif età == "35-50(Adulto)":
                adulto += 1
            elif età == "50-65(Adulto Affermato)":
                adultoaff += 1
            elif età == "65+(Senior)":
                senior += 1

    votanti = round((totale / len(tabella)) * 100, 2)
    non_votanti = round(100 - votanti, 2)

    # Calcolo percentuali
    def perc(x): return round((x / totale) * 100, 2) if totale > 0 else 0

    perc_adolescenza = perc(adolescenza)
    perc_giovane = perc(giovane)
    perc_giovaneadul = perc(giovaneadul)
    perc_adulto = perc(adulto)
    perc_adultoaff = perc(adultoaff)
    perc_senior = perc(senior)

    # Stampa ordinata
    print(f"👥 Votanti: {votanti}% - Non votanti: {non_votanti}%\n")

    print("📊 Distribuzione per fascia d'età:")
    print(f"Adolescenza (14-18): {perc_adolescenza}%")
    print(f"Giovani (18-25): {perc_giovane}%")
    print(f"Giovani adulti (25-35): {perc_giovaneadul}%")
    print(f"Adulti (35-50): {perc_adulto}%")
    print(f"Adulti affermati (50-65): {perc_adultoaff}%")
    print(f"Senior (65+): {perc_senior}%\n")

    # Moda
    conteggi = {
        "Adolescenza": adolescenza,
        "Giovane": giovane,
        "Giovane adulto": giovaneadul,
        "Adulto": adulto,
        "Adulto affermato": adultoaff,
        "Senior": senior
    }
    moda = max(conteggi, key=conteggi.get)

    # Mediana (approssimata come la fascia con frequenza mediana)
    mediana_fascia = sorted(conteggi.items(), key=lambda x: x[1])[len(conteggi)//2][0]

    print(f"📌 Moda: {moda}")
    print(f"📍 Mediana: {mediana_fascia}")

    # Media età
    media = round(sum(voti_numerici) / len(voti_numerici), 2)
    print(f"📈 Media età: {media} anni")

    # Varianza e Deviazione standard
    varianza = round(sum((x - media) ** 2 for x in voti_numerici) / len(tabella), 2)
    dev_standard = round(varianza ** 0.5, 2)
    print(f"📏 Varianza: {varianza} anni²")
    print(f"📉 Deviazione standard: {dev_standard} anni")

    # Coefficiente di variazione
    if media != 0:
        coeff_variazione = round((dev_standard / media) * 100, 2)
        print(f"📊 Coefficiente di variazione: {coeff_variazione}%")
    else:
        print("⚠️ Impossibile calcolare il coefficiente di variazione (media = 0)")


def percentuale_pagamento(tabella):
    Sempre = 0
    spesso = 0
    abitualmente = 0
    talvolta = 0
    raramente = 0
    sempre_contante = 0
    totale = 0
    voti_numerici = []

    for domanda in tabella:
        risposta = domanda["Come preferisic pagare"]

        if risposta != "":
            totale += 1

            if risposta == "Sempre con carta(≈ 100% delle volte)":
                Sempre += 1
                voti_numerici.append(100)
            elif risposta == "Spesso con carta(≈80% delle volte)":
                spesso += 1
                voti_numerici.append(80)
            elif risposta == "Abitualmente con carta(≈60% delle volte)":
                abitualmente += 1
                voti_numerici.append(60)
            elif risposta == "Talvolta con carta(≈40% delle volte)":
                talvolta += 1
                voti_numerici.append(40)
            elif risposta == "Raramente con carta(≈20% delle volte)":
                raramente += 1
                voti_numerici.append(20)
            else:
                sempre_contante += 1
                voti_numerici.append(0)

    votanti = round((totale / len(tabella)) * 100, 2)
    non_votanti = round(100 - votanti, 2)

    def perc(x): return round((x / totale) * 100, 2) if totale > 0 else 0

    # Percentuali
    perc_sempre = perc(Sempre)
    perc_spesso = perc(spesso)
    perc_abit = perc(abitualmente)
    perc_talvolta = perc(talvolta)
    perc_raramente = perc(raramente)
    perc_contante = perc(sempre_contante)

    # Print ordinato
    print(f"👥 Votanti: {votanti}% - Non votanti: {non_votanti}%\n")

    print("📊 Distribuzione delle preferenze di pagamento:")
    print(f"Sempre con carta (100% delle volte): {perc_sempre}%")
    print(f"Spesso con carta (≈80% delle volte): {perc_spesso}%")
    print(f"Abitualmente con carta (≈60% delle volte): {perc_abit}%")
    print(f"Talvolta con carta (≈40% delle volte): {perc_talvolta}%")
    print(f"Raramente con carta (≈20% delle volte): {perc_raramente}%")
    print(f"Sempre contanti (0% con carta): {perc_contante}%\n")

    # Moda
    conteggi = {
        "100%": Sempre,
        "80%": spesso,
        "60%": abitualmente,
        "40%": talvolta,
        "20%": raramente,
        "0% (Solo contante)": sempre_contante
    }
    moda = max(conteggi, key=conteggi.get)
    mediana_fascia = sorted(conteggi.items(), key=lambda x: x[1])[len(conteggi) // 2][0]

    print(f"📌 Moda: {moda}")
    print(f"📍 Mediana: {mediana_fascia}")

    # Media
    media = round(sum(voti_numerici) / len(voti_numerici), 2)
    print(f"📈 Media: {media} (dove 100 = sempre con carta, 0 = solo contanti)")

    # Deviazione standard e varianza
    varianza = round(sum((x - media) ** 2 for x in voti_numerici) / totale, 2)
    dev_standard = round(varianza ** 0.5, 2)

    print(f"📏 Varianza: {varianza}")
    print(f"📉 Deviazione standard: {dev_standard}")

    # Coefficiente di variazione
    if media != 0:
        coeff_variazione = round((dev_standard / media) * 100, 2)
        print(f"📊 Coefficiente di variazione: {coeff_variazione}%")
    else:
        print("⚠️ Impossibile calcolare il coefficiente di variazione (media = 0)")



def mediana_comune(tabella):

    # Variabili di conteggio
    paese = 0
    cittadina = 0
    città = 0
    Grande_città = 0
    metropoli = 0
    totale = 0
    dimensioni_valori = []

    # Mapping da testo a numero stimato di abitanti
    dimensioni_numeriche = {
        "Paese(<10.000 abitanti)": 5000,
        "Cittadina(10.000-50.000 abitanti)": 30000,
        "Città (50.000-300.000 abitanti)": 175000,
        "Grande Città (300.000 - 1.000.000 abitanti)": 650000,
        "Metropoli (1.000.000 di abitanti o più)": 1500000
    }

    # Ordine logico per calcolo mediana testuale
    ordine_logico = [
        "Paese(<10.000 abitanti)",
        "Cittadina(10.000-50.000 abitanti)",
        "Città (50.000-300.000 abitanti)",
        "Grande Città (300.000 - 1.000.000 abitanti)",
        "Metropoli (1.000.000 di abitanti o più)"
    ]

    categorie_lista = []  # per mediana testuale

    for domanda in tabella:
        città_ = domanda.get("Quanto è grande il comune in cui vivi", "")

        if città_ in dimensioni_numeriche:
            totale += 1
            dimensioni_valori.append(dimensioni_numeriche[città_])
            categorie_lista.append(città_)

            # Conteggi
            if città_ == "Paese(<10.000 abitanti)":
                paese += 1
            elif città_ == "Cittadina(10.000-50.000 abitanti)":
                cittadina += 1
            elif città_ == "Città (50.000-300.000 abitanti)":
                città += 1
            elif città_ == "Grande Città (300.000 - 1.000.000 abitanti)":
                Grande_città += 1
            elif città_ == "Metropoli (1.000.000 di abitanti o più)":
                metropoli += 1

    if not dimensioni_valori:
        print("⚠️ Nessun dato disponibile.")
        return

    # 📊 Media
    media = round(sum(dimensioni_valori) / totale, 2)
    print(f"📊 Media della dimensione del comune: {int(media)} abitanti")

    # 🔹 Mediana (numerica)
    dimensioni_valori.sort()
    n = len(dimensioni_valori)
    if n % 2 == 1:
        mediana_val = dimensioni_valori[n // 2]
    else:
        mediana_val = (dimensioni_valori[n // 2 - 1] + dimensioni_valori[n // 2]) / 2

    # 🔸 Mediana (testuale/categoria)
    categorie_lista.sort(key=lambda x: ordine_logico.index(x))
    if n % 2 == 1:
        mediana_cat = categorie_lista[n // 2]
    else:
        mediana_cat = categorie_lista[n // 2 - 1]  # o media tra due, ma in categoria prendiamo una

    print(f"🔸 Mediana (categoria): {mediana_cat}")

    # 🟫 Moda
    lista_moda = {
        "Paese": paese,
        "Cittadina": cittadina,
        "Città": città,
        "Grande Città": Grande_città,
        "Metropoli": metropoli
    }

    moda = max(lista_moda, key=lista_moda.get)
    print(f"🟫 Moda (categoria più frequente): {moda}")

    # 📉 Ordinamento crescente
    ordinato = dict(sorted(lista_moda.items(), key=lambda x: x[1]))
    print(f"📉 Ordine crescente di scelta: {ordinato}")
            

    return

def media_genere(tabella):
    maschio = 0
    femmina = 0
    non_specif = 0
    totale = 0
    voti_numerici = []

    for domanda in tabella:
        genere = domanda["Genere"]

        if genere != "":
            totale += 1
            if genere == "Maschile":
                maschio += 1
                voti_numerici.append(1)
            elif genere == "Femminile":
                femmina += 1
                voti_numerici.append(2)
            else:
                non_specif += 1
                voti_numerici.append(0)

    votanti = round((totale / len(tabella)) * 100, 2)
    non_votanti = round(100 - votanti, 2)

    def perc(x): return round((x / totale) * 100, 2) if totale > 0 else 0

    perc_maschi = perc(maschio)
    perc_femmine = perc(femmina)
    perc_non_spec = perc(non_specif)

    # Output ordinato
    print(f"👥 Votanti: {votanti}% - Non votanti: {non_votanti}%\n")

    print("📊 Distribuzione per genere:")
    print(f"Maschi: {perc_maschi}%")
    print(f"Femmine: {perc_femmine}%")
    print(f"Preferisco non specificare: {perc_non_spec}%\n")

    # Fascia con più risposte
    fasce = {
        "Maschile": perc_maschi,
        "Femminile": perc_femmine,
        "Preferisco non specificare": perc_non_spec
    }
    fascia_max = max(fasce, key=fasce.get)
    print(f"🏆 Genere con più risposte: {fascia_max}\n")

    # Moda e mediana
    conteggi = {"Maschi": maschio, "Femmine": femmina, "Non specificato": non_specif}
    moda = max(conteggi, key=conteggi.get)
    mediana = dict(sorted(conteggi.items(), key=lambda x: x[1]))  # solo per vedere la distribuzione

    print(f"📌 Moda: {moda}")
    print(f"📍 Mediana: {mediana}")

    # Media
    media = round(sum(voti_numerici) / totale, 2)
    print(f"📈 Media: {media} (dove 0 = non specificato, 1 = maschio, 2 = femmina)")

    # Varianza e deviazione standard
    varianza = round(sum((x - media) ** 2 for x in voti_numerici) / totale, 2)
    dev_standard = round(varianza ** 0.5, 2)

    print(f"📏 Varianza: {varianza}")
    print(f"📉 Deviazione standard: {dev_standard}")

    # Coefficiente di variazione
    if media != 0:
        coeff_variazione = round((dev_standard / media) * 100, 2)
        print(f"📊 Coefficiente di variazione: {coeff_variazione}%")
    else:
        print("⚠️ Impossibile calcolare il coefficiente di variazione (media = 0)")


def covarianza_età_pagamento(tabella):
    età_mapping = {"14-18(Adolescenza)": 16,
        "18-25(Giovane)": 21.5,
        "25-35(Giovane Adulto)": 
        30,"35-50(Adulto)": 42.5
        ,"50-65(Adulto Affermato)": 57.5,
        "65+(Senior)": 70
    }
    pagamento_mapping = {
        "Sempre con carta(≈ 100% delle volte)": 100,
        "Spesso con carta(≈80% delle volte)": 80,
        "Abitualmente con carta(≈60% delle volte)": 60,
        "Talvolta con carta(≈40% delle volte)": 40,
        "Raramente con carta(≈20% delle volte)": 20,
        "Sempre contante!": 0
    }

    età_valori = []
    pagamento_valori = []

    for riga in tabella:
        e = età_mapping.get(riga["Quanti anni hai"])
        p = pagamento_mapping.get(riga["Come preferisic pagare"])
        if e is not None and p is not None:
            età_valori.append(e)
            pagamento_valori.append(p)

    if not età_valori or not pagamento_valori:
        print("Dati insufficienti.")
        return None
    
    print("[DEBUG] Valori età:", età_valori)
    print("[DEBUG] Valori pagamento:", pagamento_valori)
    print("[DEBUG] Numero valori validi:", len(età_valori))


    n = len(età_valori)
    media_età = 39.55
    media_pag = 63.88

    cov = sum((e - media_età) * (p - media_pag) for e, p in zip(età_valori, pagamento_valori)) / n
    print(f"✅ Covarianza calcolata correttamente: {cov:.2f} ")
    

    scarto_X = 17.72
    Scarto_Y = 30.29

    m =round(cov/ (scarto_X**2),2)
    q = round(media_pag -( m * media_età),2)

    coef_correlazionel = round(cov/(scarto_X * Scarto_Y),2)

    print(f'La retta di regressione lineare è: {m}X + {q}')

    print(f'Il coefficente di correlazione lineare è: {coef_correlazionel}')

    print(f"La covarianza ({cov:.2f}) misura la direzione della relazione tra età e preferenza di pagamento. "
      "Il valore negativo indica che quando aumenta l’età, tende a diminuire la frequenza di pagamento con carta.")

    print(f"""Il coefficiente di correlazione ({coef_correlazionel:.2f}) va da -1 a +1:
    +1 = correlazione perfettamente positiva
    -1 = perfettamente negativa
    0  = nessuna correlazione

    Il valore {coef_correlazionel:.2f} è molto vicino a zero, il che significa:
    ❗ Quasi nessuna correlazione lineare tra età e modalità di pagamento.
    In altre parole: le persone giovani o anziane non mostrano differenze forti nel modo in cui preferiscono pagare (almeno nei dati raccolti).
    """)

    print(f"📈 y = {m:.2f}x + {q:.2f} è l’equazione che stima la percentuale di pagamento con carta in funzione dell’età x.")
    print("La pendenza negativa indica che ogni anno in più porta a una leggera diminuzione attesa nel pagamento con carta.")

    return cov


def parte_incuivivi(tabella):
    Sud_italia = 0
    Centro_italia = 0
    Nord_italia = 0
    totale = 0
    voti_numerici = []

    for domanda in tabella:
        zona = domanda["parte in cui vivi"]

        if zona != "":
            totale += 1
            if zona == "Centro Italia":
                Centro_italia += 1
                voti_numerici.append(1)
            elif zona == "Nord Italia":
                Nord_italia += 1
                voti_numerici.append(2)
            else:
                Sud_italia += 1
                voti_numerici.append(0)

    votanti = round((totale / len(tabella)) * 100, 2)
    non_votanti = round(100 - votanti, 2)

    def perc(x): return round((x / totale) * 100, 2) if totale > 0 else 0

    perc_sud = perc(Sud_italia)
    perc_centro = perc(Centro_italia)
    perc_nord = perc(Nord_italia)

    # Output ordinato
    print(f"👥 Votanti: {votanti}% - Non votanti: {non_votanti}%\n")

    print("📍 Distribuzione per area geografica:")
    print(f"Sud Italia: {perc_sud}%")
    print(f"Centro Italia: {perc_centro}%")
    print(f"Nord Italia: {perc_nord}%\n")

    # Area più rappresentata
    fasce = {
        "Sud Italia": perc_sud,
        "Centro Italia": perc_centro,
        "Nord Italia": perc_nord
    }
    fascia_max = max(fasce, key=fasce.get)
    print(f"🏆 Area più rappresentata: {fascia_max}\n")

    # Moda e mediana
    conteggi = {"Sud Italia": Sud_italia, "Centro Italia": Centro_italia, "Nord Italia": Nord_italia}
    moda = max(conteggi, key=conteggi.get)
    mediana = dict(sorted(conteggi.items(), key=lambda x: x[1]))

    print(f"📌 Moda: {moda}")
    print(f"📍 Mediana: {mediana}")

    # Media
    media = round(sum(voti_numerici) / totale, 2)
    print(f"📈 Media: {media} (dove 0 = Sud, 1 = Centro, 2 = Nord)")

    # Varianza e deviazione standard
    varianza = round(sum((x - media) ** 2 for x in voti_numerici) / totale, 2)
    dev_standard = round(varianza ** 0.5, 2)

    print(f"📏 Varianza: {varianza}")
    print(f"📉 Deviazione standard: {dev_standard}")

    # Coefficiente di variazione
    if media != 0:
        coeff_variazione = round((dev_standard / media) * 100, 2)
        print(f"📊 Coefficiente di variazione: {coeff_variazione}%")
    else:
        print("⚠️ Impossibile calcolare il coefficiente di variazione (media = 0)")


def prelievo_mese(tabella):
    mapping = {
        "ogni 2/3 giorni (circa 10 volte al mese)": 0,
        "settimanalmente": 1,
        "bisettimanalmente": 2,
        "mensilmente": 3,
        "meno di una volta al mese": 4
    }

    contatori = [0, 0, 0, 0, 0]  # indice 0-4 corrisponde alle categorie
    voti_numerici = []
    totale = 0
    risposte_non_riconosciute = []

    for domanda in tabella:
        risposta = domanda.get("Quante volte prelevi denaro", "").strip().lower()

        if risposta == "":
            continue

        trovato = False
        for chiave, valore in mapping.items():
            if risposta == chiave:
                contatori[valore] += 1
                voti_numerici.append(valore)
                totale += 1
                trovato = True
                break

        if not trovato:
            risposte_non_riconosciute.append(risposta)
            contatori[4] += 1  # fallback: meno di una volta al mese
            voti_numerici.append(4)
            totale += 1

    if totale == 0:
        print("⚠️ Nessuna risposta valida trovata.")
        return

    votanti = round(totale / len(tabella) * 100, 2)
    non_votanti = round(100 - votanti, 2)

    print(f"\n👥 Votanti: {votanti}% - Non votanti: {non_votanti}%\n")

    categorie = [
        "Ogni 2/3 giorni (≈10 volte al mese)",
        "Settimanalmente",
        "Bisettimanalmente",
        "Mensilmente",
        "Meno di una volta al mese"
    ]
    percentuali = [round(c / totale * 100, 2) for c in contatori]

    print("💸 Frequenza di prelievo mensile:")
    for cat, perc in zip(categorie, percentuali):
        print(f"{cat}: {perc}%")
    
    print("")

    # Moda
    moda_idx = contatori.index(max(contatori))
    moda = categorie[moda_idx]

    # Mediana
    voti_numerici.sort()
    n = len(voti_numerici)
    if n % 2 == 0:
        mediana = (voti_numerici[n // 2 - 1] + voti_numerici[n // 2]) / 2
    else:
        mediana = voti_numerici[n // 2]

    # Media
    media = round(sum(voti_numerici) / totale, 2)

    # Deviazione standard e varianza
    varianza = round(sum((x - media) ** 2 for x in voti_numerici) / totale, 2)
    dev_std = round(varianza ** 0.5, 2)

    # Coefficiente di variazione
    if media != 0:
        coeff_variazione = round((dev_std / media) * 100, 2)
        coeff_text = f"{coeff_variazione}%"
    else:
        coeff_text = "⚠️ Non definito (media = 0)"

    # Output statistico
    print("📊 Statistiche descrittive:")
    print(f"📌 Moda: {moda}")
    print(f"📍 Mediana: {mediana}")
    print(f"📈 Media: {media} (dove 0 = più frequente, 4 = meno frequente)")
    print(f"📏 Varianza: {varianza}")
    print(f"📉 Deviazione standard: {dev_std}")
    print(f"📊 Coefficiente di variazione: {coeff_text}\n")

    return {
        "media": media,
        "dev_std": dev_std,
        "varianza": varianza,
        "cv": coeff_variazione if media != 0 else None,
        "mediana": mediana,
        "moda": moda,
        "percentuali": percentuali
    }


def lontanaza_punto(tabella):
    mapping = {
        "<500 metri": 0,
        "500-1000 metri": 1,
        "1000-2000 metri": 2,
        "2000 metri o più": 3,
        "più di 2000 metri": 3,
        "più di 2 km": 3,
        ">2000 metri": 3,
        "oltre 2 km": 3,
        "oltre 2000 metri": 3,
        "2000 metri o oltre": 3
    }

    etichette = [
        "<500 metri",
        "500-1000 metri",
        "1000-2000 metri",
        ">2000 metri"
    ]

    contatori = [0, 0, 0, 0]
    voti_numerici = []
    totale = 0
    risposte_non_riconosciute = []

    for riga in tabella:
        risposta = riga.get("Quanto è lontano il punto in cui prelievi", "").strip().lower()
        if risposta:
            trovato = False
            for chiave, indice in mapping.items():
                if risposta == chiave.lower():
                    contatori[indice] += 1
                    voti_numerici.append(indice)
                    totale += 1
                    trovato = True
                    break
            if not trovato:
                risposte_non_riconosciute.append(risposta)

    votanti = round(totale / len(tabella) * 100, 2) if len(tabella) > 0 else 0
    non_votanti = round(100 - votanti, 2)

    print(f"👥 Votanti: {votanti}% - Non votanti: {non_votanti}%\n")

    print("📍 Distribuzione per distanza dal punto di prelievo:")
    for i, etichetta in enumerate(etichette):
        perc = round(contatori[i] / totale * 100, 2) if totale > 0 else 0
        print(f"{etichetta}: {perc}%")
    print("")

    moda_idx = contatori.index(max(contatori))
    print(f"🏆 Distanza più comune: {etichette[moda_idx]}")

    voti_numerici.sort()
    n = len(voti_numerici)
    if n == 0:
        print("⚠️ Nessun dato per calcolare mediana, media, varianza.")
        return

    if n % 2 == 0:
        mediana_val = (voti_numerici[n // 2 - 1] + voti_numerici[n // 2]) / 2
    else:
        mediana_val = voti_numerici[n // 2]
    print(f"📍 Mediana: {etichette[round(mediana_val)]}")

    media = sum(voti_numerici) / totale
    print(f"📈 Media: {round(media, 2)} (dove 0 = <500, 1 = 500-1000, 2 = 1000-2000, 3 = >2000)")

    varianza = sum((x - media) ** 2 for x in voti_numerici) / totale
    dev_standard = round(varianza ** 0.5, 2)

    print(f"📏 Varianza: {round(varianza, 2)}")
    print(f"📉 Deviazione standard: {dev_standard}")

    if media != 0:
        coeff_variazione = round((dev_standard / media) * 100, 2)
        print(f"📊 Coefficiente di variazione: {coeff_variazione}%")
    else:
        print("⚠️ Impossibile calcolare il coefficiente di variazione (media = 0)")


def main():
    file = "File.csv"
    tabella = lettura(file)

    print("\n" + "="*40)
    print("SEZIONE: ANALISI ETÀ")
    print("="*40)
    mediaet = media_età(tabella)

    print("\n" + "="*40)
    print("SEZIONE: ANALISI TIPOLOGIA PAGAMENTO")
    print("="*40)
    tipologia_pag = percentuale_pagamento(tabella)

    print("\n"+ "="*40)
    print("SEZIONE: GENERE")
    print("="*40)
    genere = media_genere(tabella)

    print("\n"+ "="*40)
    print("SEZIONE: PARTE IN CUI VIVI")
    print("="*40)
    vivi = parte_incuivivi(tabella)

    print("\n"+ "="*40)
    print("SEZIONE: FREQUENZA PRELIEVO")
    print("="*40)
    prelievo = prelievo_mese(tabella)

    print("\n"+ "="*40)
    print("SEZIONE: LONTANANZA PRELIEVO")
    print("="*40)
    lontananza = lontanaza_punto(tabella)

    print("\n"+ "="*40)
    print("SEZIONE: MEDIANA COMUNE")
    print("="*40)
    mediana = mediana_comune(tabella)

    print("\n"+ "="*40)
    print("SEZIONE: COVARIANZA ETà/PAG")
    print("="*40)
    covarianza = covarianza_età_pagamento(tabella)


main()