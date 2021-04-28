# **Notifications** 

## Imports:

  ```python
  import sims4.commands
  from typing import Any, Union, Iterator, Tuple
  from distributor.shared_messages import IconInfoData
  from protocolbuffers.Localization_pb2 import LocalizedString
  from sims4communitylib.enums.strings_enum import CommonStringId
  import services
  from sims4communitylib.utils.common_resource_utils import CommonResourceUtils
  from sims4.resources import Types
  from sims4communitylib.utils.objects.common_object_utils import CommonObjectUtils
  from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
  from sims4communitylib.modinfo import ModInfo
  from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
  from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
  from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
  from ui.ui_dialog import UiDialogResponse
  from ui.ui_dialog_notification import UiDialogNotification
  ```
Das sind einmal alle imports die ihr benötigt für den Code.
### Und das hier ist der Code:
```python
    @sims4.commands.Command('notif', command_type=sims4.commands.CommandType.Live)
    def _common_testing_show_basic_notification(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    tgt_client = services.client_manager().get(_connection)
    output('first notif')
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",#string id form string table
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )
        dialog = CommonBasicNotification(
            "RUG SALE!!!",
            "XXXX Area\nRug Have a look at this beautiful handwoven rug! It is made of the finest Materials only, wisely chosen by Wayfair. The natural green colour is a perfect       fit for all living rooms!\nMake your house feel like a HOME!\nDetails:Name: XXXX Green Area Rug\nSize: Rectangle 5’ x 8’\nOverall Product Weight: 56 lb.\nFree Shipping on      orders over $35.00\n",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            urgency=UiDialogNotification.UiDialogNotificationUrgency.URGENT
        )
        dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG,16900524886024814375)))
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up', exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')
   ```
## Command:  
Der Command ist ein Live Command, das kennt man zB. wenn man versucht einen Cheat einzugeben.
Dieser Typ von Command ruft die Funktion direkt auf und führt sie aus.
```python
    @sims4.commands.Command('notif', command_type=sims4.commands.CommandType.Live)#command function mit zwei parametern(1. Name vom command,2.Type vom command Live hast dass es sofort aufgerufen wird) 
    def _common_testing_show_basic_notification(_connection: int=None):#Definition
    output = sims4.commands.CheatOutput(_connection)#output der sofort angezeigt wird wenn man den command eingibt
    output('first notif')
```
## Notification Part:
Das hier ist wie eine basic notification ausschaut:
Wir haben hier den **dialog** der aus folgenden Teilen besteht:
  * title_id : Titel der notif
  * description_id : Beschreibung
  * title_tokens: Zusätzlicher Titel den man dann auch in einer anderen Farbe darstellen kann
  * description_tokens: Zusätzliche Beschreibung 
  * urgency: Wichtigkeit(blau=DEFAULT,organge=URGENT)
```python
        dialog = CommonBasicNotification(
            "RUG SALE!!!",#title id 
            "XXXX Area\nRug Have a look at this beautiful handwoven rug! It is made of the finest Materials only, wisely chosen by Wayfair. The natural green colour is a perfect fit for all living rooms!\nMake your house feel like a HOME!\nDetails:Name: XXXX Green Area Rug\nSize: Rectangle 5’ x 8’\nOverall Product Weight: 56 lb.\nFree Shipping on orders over $35.00\n",#description id
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            urgency=UiDialogNotification.UiDialogNotificationUrgency.URGENT#notification ist urgent(orange)
        )
```
Hier sind die Definitionen für beide tokens:
```python
title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                206982752,
                text_color=CommonLocalizedStringColor.GREEN# Text Farbe
            ),
        )
description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                206982752,
                text_color=CommonLocalizedStringColor.RED
            ),
        )
```
Um die Notification anzuzeigen mussen wir die show Funktion aufrufen.
Allgemein sieht die show Funktion so aus: ``show(Icon=None,SecondIcon=None)``
Icons sind optional.
Hier die fertige show Funktion mit einem Teppich als Icon:
 ```python      
                #IconinfoData func um die infos vom Icon zu erhalten damit man diese auch displayen kann
    dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG,16900524886024814375)))#get_resource_key returned die notwendige Info um das Bild darzustellen 
 ```
 Die Parameter von der get_resource_key function verlangen den filetype des Bilds und die Instance ID.
 ## Instance ID
 Für diese Notification hab ich als Icon ein Teppich gewählt damit das auch zur Story passt.
 Um einen Teppich auch als Icon darzustellen braucht man zuerst die Instance ID vom Bild, dafür braucht man das **Sims4 Studio** Programm.
 
 Dort wählt man `Object->wähle overide->Teppich->speicher .package und move es zum Mods Folder->dann Warehouse Tab wählen`
 und es müsste dann so aussehen:
 
 ![image](https://user-images.githubusercontent.com/71192659/116391733-d111f680-a81f-11eb-92d3-fd1117be3f40.png)

Auf der linken Seite wählt man das entsprechende Bild was man als Icon haben will in dem Fall den Teppich:

![image](https://user-images.githubusercontent.com/71192659/116392132-5f867800-a820-11eb-8f58-9fc3b5b8cf75.png)

Dann geht man auf Data und kopiert die Instance,die eine Hexad ist,raus.

![image](https://user-images.githubusercontent.com/71192659/116392302-93619d80-a820-11eb-9692-ea465a35c1a0.png)

Im Tab **Tools** gibt es einen **Hash Generator**. Dort gibt ihr die Hexadecimal Zahl ein und kopiert die Dezimal Zahl die umgerechnet wurde.
**Diese Zahl ist die Instance ID die ihr dann nach Types.PNG eingibt**  `dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG,16900524886024814375)))` 

Wenn ihr das alles gemacht habt sollte die Notification dann so aussehen:

![image](https://user-images.githubusercontent.com/71192659/116393612-28b16180-a822-11eb-918b-5a58e28e1e88.png)

## String ID
Für die String IDs hab ich einfach den Value von CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN geändert und diesen verwendet.

Zuerst öffnet ihr in Sims4 Studio **My Projects** und wählt dann S4CL package.Die erste Zeile der Tabelle links ist der String Table.
Das wählt ihr aus und geht dann auf **Elemente bearbeiten...** 

![image](https://user-images.githubusercontent.com/71192659/116394875-b772ae00-a823-11eb-9eeb-cf52961035d0.png)


Um den Value von **CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN** zu ändern sucht ihr den Eintrag mit **Test Text 0 string**. 
Ändert den Value, kopiert den **Key**,wandelt es in Dezimal um, saved das ganze und schon könnt ihr diese ID einsetzten und verwenden.
