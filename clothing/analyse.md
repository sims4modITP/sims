NPC - Clothing für Bella Goth

Weil sich die Kleidung im Code "umstellen" lässt, muss man zuerst das Kleidungsstück suchen, das der Sim den man bearbeiten will trägt. In diesem Fall ist das Bella Goths rotes Kleid.

![Screenshot 2021-06-20 163631](https://user-images.githubusercontent.com/80634958/122678217-192d1400-d1e6-11eb-8aeb-ec126ffb80a7.png)

Man sucht also in Sims 4 Studio CAS override das gewünschte item und klickt dann auf Texture und exportiert dort jeden Layer (das ist nur das Design nicht die Form der Kleidung) -> am besten einfach nach den layern benennen damit man es dann wiederfindet beim Importieren

![image](https://user-images.githubusercontent.com/80634958/122678313-8fca1180-d1e6-11eb-889b-154fbd63db47.png)

Wenn das geschafft ist, wechselt man zum Meshes Tab und exportiert hier weider jedes LOD Level (0 ist das detaillierteste, es wird geschalten wenn man den sim von nahem ansieht - 3 ist das gröbste .. man sieht es nur von weiter Entfernung)

![image](https://user-images.githubusercontent.com/80634958/122678367-db7cbb00-d1e6-11eb-9beb-275472412464.png)

Dann kann man dieses Kleidungsstück/Projekt schließen - man braucht es nun eine weile nicht mehr.
Dann sucht man sich noch das Kleidungsstück das der Sim stattdessen tragen soll und macht mit dem dasselbe! Wenn man noch die Farbe ändern oder ein neues KLiedungsstück designen will sucht man am besten eines aus, das dem an mähesten kommt das man gerne hätte.

--> für die nächsten Schritte bracuht man das Tool Blender

Jetzt macht man 2 Blender Tabs auf: einen mit dem ursprünglichen Gewand und einem mit dem neuen Kleidungsstück. zuerst betrachtet man die cut number des ursprünglichen (wir nenen es im weiteren hier jetzt einfach Kleid) Kleides die rechts unten zu finden ist. Man muss sich hier genau merken welcher Körperteil welche cut nummer hat weil Sims dann nach genau derselben aufteilung im neuen Kleidungsstück wieder scuhen wird.

![image](https://user-images.githubusercontent.com/80634958/122678524-9442fa00-d1e7-11eb-80ce-dd96f10cc5fe.png)
(man muss das für jede gruppe ("ebene") tun also kann man immer alle anderen ausblenden um nicht durcheinander zu kommen)

Wenn man das gefunden hat ist es am besten so weiterzumachen: Man sucht die cut nummer eines Körperteils und passt dann die des neuen Kleidungsstückes darauf an - die cut nummern sind hier jedoch komplet zufällig gewählt und folgen keiner logik außer strikter nummerierung also man kann sich nicht herlerten welches Teil welche nummer haben wird - man muss also wirklich für jedes Teil extra prüfen!

Außerdem kann es sein, das man mehr Gruppen hat als das Kleid hatte. Dann muss man rausfinden zu welcher cut nummer es gehört hätte (im KLeid - also sprich zu welchem Körperteil es gehört) und alle files die dieselbe cut nummer haben würden zu einem zusammenfassn es darf nämlich KEINE CUT NUMMER DOPPELT GEBEN! Es gibt sonst einen include Fehler und der Sim wird einfach an manchen Stellen durchsichtig!!

![image](https://user-images.githubusercontent.com/80634958/122678844-bb4dfb80-d1e8-11eb-9de6-4406b5513ff5.png)
(rechts sieht man die ausgewählten files - man muss auf das icon klicken dann kommt ein kleiner oranger Kreis rundherum, links muss man dan auf join klicken)

DIE NAMEN DER GRUPPEN SPIELEN DABEI ÜBERHAUPT KEINE ROLLE was wichtig ist ist dang allein die AUFTEILUNG DER GRUPPEN UND DIE CUT NUMMER!!

Das muss man dann für jeden Layer wiederholen und alle neuen kleidungsstück - Layer spichern.

Danach kann man einfach zurück in Sims 4 Studio. Unter Cas override wieder das rote Kleid suchen -> dort bei Texture alle Ebenen inkludieren und bei Meshes alle LOD Levels inlcludieren und spiechern. (Wenn der Sim nicht aussieht wie man das möchte ist ziemlich wahrscheinlich doch noch eine cut nummer falsch - dann also einfach wieder zurück zu Blender und nochmal rumspielen)

Zum Schluss muss man nur noch die .package Datei in den Mod folder von Sims geben :) Fertig!
