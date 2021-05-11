# functions for level 7

# ok dialog 
import sims4.commands

from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ui.ui_dialog import UiDialogOk
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog


@sims4.commands.Command('seven_first_dialogue', command_type=sims4.commands.CommandType.Live)
def _7ok1(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(
            _dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                        text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (
            CommonLocalizationUtils.create_localized_string('Actual Story',
                                                            tokens=(CommonSimUtils.get_active_sim_info(),),
                                                            text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'Warehouses',
            # this is where the headline is written -> insert headline here
            'List of Warehouses: \n\n1. Westland Warehouse\nLocation: 700 Manufactures DR, Westland, MI 48186, USA\nRun by: Francois Caron\nBuilt: 15.02.2020\n\n2. Boston Warehouse\nLocation: 23400 Bell Rd, New Bostoon, MI 48164, USA\nRun by:Michal Bruz\nBuilt:27.12.2019\n\n3. New York WarehounLocation: 253-01 Rockaway Blvd, Rosedale, NY 11422, USA\nRun by: Juan Mortez\nBuilt: 01.02.2021',
            # this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Close List',
                                                                               text_color=CommonLocalizedStringColor.GREEN)
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog',
                                             exception=ex)  # falls error -> log
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')


# notification
