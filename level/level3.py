# alle imports für einen ok - dialog
import sims4.commands


from ScriptLibrary.sims4communitylib.dialogs.common_input_float_dialog import CommonInputFloatDialog
from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from pprint import pformat
from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ui.ui_dialog import UiDialogOk
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog #die common_ok_dialog klasse wird importiert...
# alle Dialogue für die dritte Stufe


# 1 Input Dialog => (Miriam|Chiara)
@sims4.commands.Command('input_first_level_three', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_input_float_dialog(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test input float dialog.')

    def _on_chosen(choice: float, outcome: CommonChoiceOutcome):
        if choice == 2 or choice == 3:
            output("answer right")
        else:
            output("answer wrong")

        output('Chose {} with result: {}.'.format(pformat(choice), pformat(outcome)))

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string
                        ("You nearly did it!", text_color=CommonLocalizedStringColor.BLUE),)
        description_tokens = (CommonLocalizationUtils.create_localized_string
                              ("Your have nearly made it to the final destination of your work to reach the next hint.\nThere is one more thing you have to solve before you can take a look at it: \n\nWhat might be the Evil behind all that \n(1) Pop-Culture \n(2) Capitalism \n(3) Men ",
                               tokens=(CommonSimUtils.get_active_sim_info(),),
                               text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonInputFloatDialog(
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            0.0,
            title_tokens=title_tokens,
            description_tokens=description_tokens
        )
        dialog.show(on_submit=_on_chosen)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show dialog, please locate your exception log file.')
    output('Done showing.')



# 1 Ok Dialog => Lobna
def _3ok1():
    try:
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                        text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (
            CommonLocalizationUtils.create_localized_string('Actual Story',
                                                            tokens=(CommonSimUtils.get_active_sim_info(),),
                                                            text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'Valenti Remer Gray/Blue Area Rug',
            # this is where the headline is written -> insert headline here
            'Special things stand the test of time. Used look meets modern. This rug cannot be described any better. This style shows the classic counter-reaction to swish designer pieces and is so special that you need to look at least twice. Upcycling is the new trend. Exceptional colours make this small work of art into a real eye catcher with character. Anyone can do boring. The Oeko-Tex 100 certified quality is not only a low price but also durable and dirt-repellent. Of course the fabric used is suitable for use on underfloor heating. Bring a trend setter home, which sets new standards in combination with your furniture.Details:\n\n\nName: Valenti Remer Gray/Blue Area Rug\n\nSize: Rectangle 5’ x 6’\n\nOverall Product Weight: 39.5 lb.\n\nFree Shipping on orders over $35.00\n\n'
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

    
# 2 Input Dialog => (Miriam|Chiara)


# Notification => Lobna
def notif():
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                0,
                text_color=CommonLocalizedStringColor.GREEN
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                0,
                text_color=CommonLocalizedStringColor.RED
            ),
        )
        dialog = CommonBasicNotification(
            # CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            # CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            "",
            "Those names … and the weight. Something is strange here, why are those kept a secret? It doesn’t make any sense. But I do feel like I know these names they sound strangely familiar. Wasn’t there a case of missing children last month that had the name Charlotte Brandt in it? I have to get those police files. I just need to know for sure!",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            urgency=UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                             'Failed to show a basic notification you fucked up', exception=ex)
    return 0

