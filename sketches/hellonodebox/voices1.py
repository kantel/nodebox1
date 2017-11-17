# print(voices())
size(800, 1200)

fill(1.0)
font("Times", 20)

julia = u"anna.premium"

juliatext1 = u"""Willst du schon gehn? Der Tag ist ja noch fern.
Es war die Nachtigall und nicht die Lerche,
Die eben jetzt Dein banges Ohr durchdrang;
Sie singt des Nachts auf dem Granatbaum dort.
Glaub, Lieber, mir: Es war die Nachtigall."""

juliatext2 = u"""Trau mir, das Licht ist nicht des Tages Licht,
Die Sonne hauchte dieses Luftbild aus,
Dein Fackelträger diese Nacht zu sein,
Dir auf dem Weg nach Mantua zu leuchten.
Drum bleibe noch; zu gehn ist noch nicht not."""

juliatext3 = u"""Es tagt, es tagt! Auf, eile, fort von hier!
Es ist die Lerche, die so heiser singt
Und falsche Weisen, rauhen Mißton gurgelt.
Man sagt, der Lerche Harmonie sei süß;
Nicht diese: Sie zerreißt die unsre ja.
Die Lerche, sagt man, wechselt mit der Kröte
Die Augen; möchte sie doch auch die Stimme!
Die Stimm ists ja, die Arm aus Arm uns schreckt,
Dich von mir jagt, da sie den Tag erweckt.
Stets hell und heller wirds: wir müssen scheiden."""

romeo = u"markus.premium"

romeotext1 = u"""Die Lerche wars, die Tagverkünderin,
Nicht Philomele; sieh den neidschen Streif,
Der dort im Ost der Frühe Wolken säumt.
Die Nacht hat ihre Kerzen ausgebrannt,
Der muntre Tag erklimmt die dunstgen Höhn;
Nur Eile rettet mich, Verzug ist Tod."""

romeotext2 = u"""Laß sie mich greifen, ja, laß sie mich töten!
Ich gebe gern mich drein, wenn du es willst.
Nein, jenes Grau ist nicht des Morgens Auge,
Der bleiche Abglanz nur von Cynthias Stirn.
Das ist auch nicht die Lerche, deren Schlag
Hoch über uns des Himmels Wölbung trifft.
Ich bleibe gern; zum Gehn bin ich verdrossen.
Willkommen, Tod, hat Julia dich beschlossen! -
Nun, Herz? Noch tagt es nicht, noch plaudern wir."""

background(0.2, 0.2, 0.2)
text(juliatext1, 20, 20, width=600)
text(romeotext1, 20, 180, width=600)
text(juliatext2, 20, 380, width=600)
text(romeotext2, 20, 540, width=600)
text(juliatext3, 20, 820, width=600)


say(juliatext1, julia)
say(romeotext1, romeo)
say(juliatext2, julia)
say(romeotext2, romeo)
say(juliatext3, julia)

