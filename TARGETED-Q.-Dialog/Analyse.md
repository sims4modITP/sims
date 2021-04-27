# T.-Q.-Dialog

## Imports: 

Um alle Klassen die wir später brauchen zu verwenden muss man sie aus dem jeweiligen File importieren. Am wichtigsten ist die CommonTargetedQuestionDialog-Klasse, das ist jene Klasse auf der unsere Funktion aufgebaut wird

Wofür wir den Rest brauchen werdet ihr im Zuge dieses Dokuments erfahren

```python
 from sims4communitylib.dialogs.common_targeted_question_dialog import CommonTargetedQuestionDialog
 from sims4communitylib.enums.strings_enum import CommonStringId
 from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
 from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
 from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
 from ui.ui_dialog import UiDialogOkCancel
```
 

## Function

### * Defininere das Command
(Here : question_dialogue) und den Typen. Hier haben wir einen Live-Type => ein Live Type gibt an, dass die Funktion in Game und jetzt ausgeführt werden soll. Andere Typen wären z.B.: Cheats
> @sims4.commands.Command('question_dialogue', command_type=sims4.commands.CommandType.Live)
> 

### * Definition der zu ausführenden Funktion

```python
def _common_testing_show_targeted_question_dialog(_connection: int = None):
    # define two types of Dialogs
    output = sims4.commands.CheatOutput(_connection)

    # All UI Properties are found in ui_dialog.py

    # display a Notification for the sim
    def _ok_chosen(_: UiDialogOkCancel):
        output('Story will be continued.')

    def _cancel_chosen(_: UiDialogOkCancel):
        output('Story stops => Nothing will be published.')
````
common_testing_show_targeted_question_dialog ist die Hauptfunktion => mitgegeben wird ein __connection__ Parameter dieser wird für die kleinen Cheatoutputs verwendet (Für Cheatoutputs braucht man keine Verbindung)

In unserer Hauptfunktion sehen wir zwei kleinere Funktionen, die wir später für einen Output brauchen, der ausgelöst wird, wenn man scih für eine Antwort entscheidet.

### * Texte definieren

Jeder Dialog braucht Texte, diese habe ich mit folgenden Variabeln definiert.

```python
    description_tokens = (
        CommonLocalizationUtils.create_localized_string(
            "Do you want to publish everything that you’ve found and stop this awful business?",
            tokens=(CommonSimUtils.get_active_sim_info(),),
            text_color=CommonLocalizedStringColor.DEFAULT),)
    ok_text = (
        CommonLocalizationUtils.create_localized_string("Yes I do",
                                                        tokens=(CommonSimUtils.get_active_sim_info(),),
                                                        text_color=CommonLocalizedStringColor.GREEN),)

    cancel_text = (
        CommonLocalizationUtils.create_localized_string("No I don't",
                                                        tokens=(CommonSimUtils.get_active_sim_info(),),
                                                        text_color=CommonLocalizedStringColor.RED),)
```
Dafür hab ich eine Class verwendet und deren __create_localized_string___ Methode. Mit dieser Methode kann man alleine Texte bzw. Strings erstellen und diese dann im Game darstellen. Desweiteren hab ich mit der CommonLocalizedStringColor Class die Farbe der Texte angepasst.

Rot => Cancel Option
Grün => Ok Option

### * Dialog Fenster definieren

Für die Definiton unserer Dialoges müssen wir mal die passende Klasse heraussuchen => Hier arbeiten wir mit einem CommontargetedQuestionDialog. Wie in C++ haben Klassen ebenfalls einen Konstruktor, dieser wird (so wie hier) einfach mit dem Klassen-Namen aufgerufen. Innerhalb der Klammern werden dann die  einzelnen Parameter gesetzt. Nicht jeder Parameter ist bedeutend und kann deswegen auch ausgelassen werden.


Folgende sind die Parameter, die notwendig sind um einen CommonTargetedQuestion Dialog zu erstellen.
```python
CommonTargetedQuestionDialog(
        question_text,
        question_tokens=(),
        ok_text_identifier=CommonStringId.OK,
        ok_text_tokens=(),
        cancel_text_identifier=CommonStringId.CANCEL,
        cancel_text_tokens=(),
        mod_identity=None
    )
 ```
 
 Kurze Erklärungen zu den Parametern:
    :param question_text: A decimal identifier of the question text.
    :type question_text: Union[int, str, LocalizedString, CommonStringId]
    :param question_tokens: Tokens to format into the question text.
    :type question_tokens: Iterator[Any], optional
    :param ok_text_identifier: A decimal identifier for the Ok text.
    :type ok_text_identifier: Union[int, str, LocalizedString, CommonStringId], optional
    :param ok_text_tokens: Tokens to format into the Ok text.
    :type ok_text_tokens: Iterator[Any], optional
    :param cancel_text_identifier: A decimal identifier for the Cancel text.
    :type cancel_text_identifier: Union[int, str, LocalizedString, CommonStringId], optional
    :param cancel_text_tokens: Tokens to format into the Cancel text.
    :type cancel_text_tokens: Iterator[Any], optional
    :param mod_identity: The identity of the mod creating the dialog. See :class:`.CommonModIdentity`                          for more information.
    :type mod_identity: CommonModIdentity, optional
    
 
 __Unser CommonTargetedQuestionDialog___
 
Wie man sieht hab ich einfach die von uns vorhin definierten Textteile als Parameter-Werte gesetzt und so den Dialog aufgebaut
 
```python
dialog = CommonTargetedQuestionDialog(
        # Fill the properties of that specific Class
        CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
        # question_tokens  – Tokens to format into the question text.
        question_tokens=description_tokens,
        # ok_text_identifier  – A decimal identifier for the Ok text.
        ok_text_identifier=CommonStringId.TEXT_WITH_GREEN_COLOR,
        ok_text_tokens=ok_text,
        # cancel_text_identifier  – A decimal identifier for the Cancel text.
        cancel_text_identifier=CommonStringId.TEXT_WITH_RED_COLOR,
        cancel_text_tokens=cancel_text
        # red text => this option doesnt get u far
    )
 ```

### * Dialog ausgeben

Um einen Dialog auszugeben brauchen wir mal eine Art Show Function mit bestimmten Parametern die wichtig sind für einen targeted Question Dialog

Die generelle show Funktion sieht so aus: 

```python
    def show(
        sim_info: SimInfo,
        target_sim_info: SimInfo,
        on_ok_selected: Callable[[UiDialogOkCancel], Any]=CommonFunctionUtils.noop,
        on_cancel_selected: Callable[[UiDialogOkCancel], Any]=CommonFunctionUtils.noop
    )
```

Wir brauchen also einen Sim der die Frage stellt und einen Sim an den die Frage gerichtet ist. (Wie man diese 2 Sim bekommt wird später erklärt)

Des weiteren kann man je nach Selektion eine Aktion hervorrufen bzw. eine Funktion aufrufen.

__Unsere Show Function___

Wir rufen dialog.show() auf => dialog ist under davor definierter CommonTargetedQuestionDialog und dieser soll jetzt , mit anderen Dingen, mit hilfe von .show() gezeigt werden.
Hier sieht man jetzt wie ich auf die Sims aus dem Spiel zugreife:
Um den aktiven Sim zu bekommen (Jener Sim auf dessen Fokus das Spiel gerade liegt) verwende ich die CommonSimUtils Klasse und greife auf ihre Methode get_active_sim_info() zu.
Wenn ich auf einen spefifischen anderen Sim zugreifen möchte, so verwende ich die Methode get_sim_info_of_sim_with_name (Vorname: str, Nachname: str) und kann so jeden beliebigen Townie verwenden

Unten sehen wir jetzt die zwei kleinen Output Funktionen die wir oben definiert haben.
ok_chosen wird aufgerufen wenn die Option die OK ist ausgewählt wurde
cancel_chosen wird aufgerufen wenn die Option die nicht OK ist ausgewählt wurde

```python
    dialog.show(
        # .show => show the dialogue and everything in the brackets
        # CommonSimUtils.get_active_sim_info(),
        # tuple(CommonSimUtils.get_sim_info_for_all_sims_generator())[0],
        # sim who answers and got targeted
        sim_info=CommonSimUtils.get_active_sim_info(),
        # sim who asks the question
        # get someone who is a Comp. Scientist

        # Bella Goth bzw Grusel => Is an Agent => suits the story
        target_sim_info=CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"),
        # Travis Scott => is a Tech Guru => Is your Colleague
        # target_sim_info=CommonSimUtils.get_sim_info_of_sim_with_name("Travis", "Scott"),

        # 2 Options of buttons in that Dialogue Windows :

        # Depending on what was chosen => that notification will pop up
        # on_ok_selected – Invoked upon the player clicking the Ok button in the dialog.
        on_ok_selected=_ok_chosen,
        # on_cancel_selected – Invoked upon the player clicking the Cancel button in the dialog.
        on_cancel_selected=_cancel_chosen
    )
```


