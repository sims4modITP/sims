# alle imports für einen ok - dialog
import sims4.commands

from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ui.ui_dialog import UiDialogOk
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog #die common_ok_dialog klasse wird importiert...
# alle Dialogue für die dritte Stufe


# 1 Ok Dialog => Lobna



# 2 Ok Dialog => Chiara
@sims4.commands.Command('three_second_dialogue', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(
            _dialog: UiDialogOk):  # console logs für den rückgabewert des dialoges -> wurde auf ok gedrückt oder einfach geschlossen?
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
            'Connie Peyton Brown Indoor/Outdoor Area Rug',
            # this is where the headline is written -> insert headline here
            '15.08.2020 \n\n Can a rug sturdy enough for both indoor and outdoor use also be chic and attractive? This durable and fade-resistant area rug is ideal for the casual lifestyle and works just as well in covered outdoor locations such as patio or porch as they do in your living room, family room or another favorite spot. Distinguished by their high-low loop pile, this area rug takes a visual cue from hand-carved rugs but is easily affordable and designed to withstand wear. This contemporary collection ranges from linear and geometric to sprightly floral – all enhanced by dimensional pile in today’s most coveted neutral tones. \n Details: \n\n Name: Connie Peyton Brown Indoor/Outdoor Area Rug \n\n Size: Rectangle 6’ x 7’ \n\n Overall Product Weight: 49.5 lb. \n\n Free Shipping on orders over $35.00',
            # this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Show Next Object',
                                                                               text_color=CommonLocalizedStringColor.GREEN)
        )
        # dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 7169552662410693051)))
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog',
                                             exception=ex)  # falls error -> log
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')


# 3 Ok Dialog => Miriam
@sims4.commands.Command('three_third_dialogue', command_type=sims4.commands.CommandType.Live)
def three_third_dialogue(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing testxyz ok dialog.')

    def _on_acknowledged(
            _dialog: UiDialogOk):  # console logs für den rückgabewert des dialoges -> wurde auf ok gedrückt oder einfach geschlossen?
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
            'Charlotte Brandt White/Navy Hallway Runner',
            # this is where the headline is written -> insert headline here
            '11.03.2021 \n\n'
            'Complement your coastal - inspired decor with this breezy indoor / outdoor area rug, featuring a simple quatrefoil design. '
            'It\'s flatwoven in Turkey from water- and fade-resistant polypropylene, so it can easily stand up to tough stains and spills. '
            'The backing is safe to roll out in rooms with floor heating. '
            'And the soft navy blue and white hues work well with any color palette you can dream up. '
            'Plus, it has a low 0.09" pile height that\'s ideal for spaces with high foot traffic like the entryway or '
            'patio, and for homes with little ones and furry friends running around.\n\n'
            'Details:\n\n'
            'Name: Charlotte Brandt White/Navy Hallway Runner\n\n'
            'Size: Rectangle 5’3’’ x 7’3’’\n\n'
            'Overall Product Weight: 34.0 lb.\n\n'
            'Free Shipping on orders over $35.00',

            # this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Close',
                                                                               text_color=CommonLocalizedStringColor.GREEN)
        )
        # dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 7169552662410693051)))
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog',
                                             exception=ex)  # falls error -> log
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')

# Notification => freie Wahl
