# Amoebe_RWTH_IAM
Hallo!

Das Programm erstellt eine Kopie des Bildes mit dem Namen „result“, bei der die Lage des Massenmittelpunkts mit einem roten Kreuz markiert ist.
Die Koordinaten lauten (1598, 1339) (in Pixel)

Arbeitsprinzip
Das Prinzip ist sehr einfach.
Das Programm prüft zunächst die Farbe jedes Pixels. 
Ist das Pixel „gelblich“ (d.h. liegt der Farbwert im Bereich typischer Werte für Farbe „gelb“) setzt die Funktion cv2.inRange() seine Farbe auf weiß, ansonsten: auf schwarz(bw picture.png). 
Auf diese Weise wird ein Bild erstellt, das viel einfacher zu verarbeiten ist (zumindest mit den Methoden, die ich gefunden habe). 
Das Programm geht dann das Schwarzweißbild durch und prüft auf weiße Pixel. 
Dann berechnet das Programm unter Verwendung jedes weißen Pixels als Körper mit Masse 1 die Koordinaten des Massenmittelpunkts Xj = (Σmi*xij) / (Σmi).

