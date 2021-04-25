import sims4.commands

from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ui.ui_dialog import UiDialogOk
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog #die common_ok_dialog klasse wird importiert...


@sims4.commands.Command('ok', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(_dialog: UiDialogOk): #console logs für den rückgabewert des dialoges -> wurde auf ok gedrückt oder einfach geschlossen?
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),) #textfarben für felder bestimmen
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog( #objekt der commonOkDialog klasse wird erstellt und im constructor werden die nötigen texte mitgegeben
            'This is the headline', #this is where the headline is written -> insert headline here
            'This is the actual story part, enjoy! :D', #this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Got it, thank you', text_color=CommonLocalizedStringColor.RED) #this is what the ok-button is gonna say
        )
        dialog.show(on_acknowledged=_on_acknowledged) #dialog wird geteigt
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex) #falls error -> log
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')
