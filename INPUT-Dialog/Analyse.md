Input-Dialog



Diese Funktion beschreibt einfach den outcome bzw. den input durch den Player.
Und da wir sowieso Rechenaufgaben haben, ist es besser als Template den Float Input zu nehmen, weswegen jetzt auch "choice" also der input ein float ist.
Outcome hierbei ist einfach wofür sich der Spieler entschieden hat.
Vergleich ob richtig:
![image](https://user-images.githubusercontent.com/80634953/116568092-7dc7a300-a908-11eb-850e-bc1719bdca8a.png)


Das sieht man in der common_choice_outcome.py

![image](https://user-images.githubusercontent.com/80634953/116288996-59e25100-a792-11eb-8710-9089584bd0fa.png)

Wird womöglich wichtig sein, da die Klasse ebenso schaut ob es zu einem Error gekommen ist. Aber jetzt grundsätzlich sollte es für den input float dialogue hoffentliich immer nur 1 returned werden -> choice made

"extras":
format - formatiert den string mit den gegeben substitutionen - wird in {} eingesetzt
pformat - formatiert ein python object zu einer schönen lesbaren Repräsentation


Also dann jetzt zum Dialog selbst:
Da wird die common_input_float_dialog.py imported -> enthält die Klasse dafür
Parameter:
  title_identifier: Union[int, str, LocalizedString, CommonStringId]
    identifier für den title des textes
  description_identifier: Union[int, str, LocalizedString, CommonStringId]
    identifier für die description
  initial_value: float
  min_value: optional
  max_value: optional
  title_tokens: Iterator[Any], optional
    tokens um Titel zu formatieren
  description_tokens: Iterator[Any], optional
    selbiges gilt für die description
  mod_identity: optional
    enthält info über den mod - name author etc

Parameter "erstellen":

Da sind derweil bsp für Texte, die man als title/description verwenden kann

![image](https://user-images.githubusercontent.com/80634953/116290593-ed685180-a793-11eb-890d-a829f10ed889.png)

Es gibt da auch die Möglichkeit einfach den Namen des Sims auszugeben mittels

![image](https://user-images.githubusercontent.com/80634953/116290840-33bdb080-a794-11eb-8e73-67d7c31a688d.png)

Jetzt wird der Dialog erstellt

![image](https://user-images.githubusercontent.com/80634953/116291039-71223e00-a794-11eb-8b30-e4b489b6af71.png)

identifiers
0.0 ist dabei der initial value - Wert der angezeigt wird
tokens

"extras":
da kommt die on_chosen funktion ins Spiel - oben erklärt

![image](https://user-images.githubusercontent.com/80634953/116291587-0cb3ae80-a795-11eb-8e77-55443b852156.png)


INFOS FÜR DEN DIALOG DER SO LANGE AUFPOPPT BIS ETWAS RICHTIGES EINGEGEBEN WURDE:
![image](https://user-images.githubusercontent.com/80634958/118989943-bd6f3100-b982-11eb-9052-df746752696f.png)
Hier wird ein zweiter dialog generiert be dem nur der Titel anders ist -> "try again" diesmal in rot damit es auffälliger ist. Beim ersten mal wird dialog.show aufgerufen, bei jedem eiteren Mal wird dann dialog2.show aufgerufen weil man ja die "warning" für den falschen Input ahben will

![image](https://user-images.githubusercontent.com/80634958/118990361-19d25080-b983-11eb-92e0-1303d93e5b70.png)
Hier wird bei der if bedingung ein choice == None hinzugefügt um zu überprüfen ob überhaupt eine choide gemacht wurde -> wenn nicht wurde auf abbrechen geklickt und der dialog verschwindet
Falls eine choice gemacht wurde die falsch ist wird die funktion durch dialog2.show quasi rekurzsiv aufgerufen .. das funktioniert so lange bis entweder die richtige eingabe gemacht wurde oder auf abbrechen geklickt wurde

der rest bleibt eh gleich ^^
