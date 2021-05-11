# Codes für level 1 und 2 
# Imports 
import sims4.commands

from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ui.ui_dialog import UiDialogOk
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog

# Coding Level 1

@sims4.commands.Command('level1_ok1', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'This is you!', # this is where the headline is written -> insert headline here
            'You wanted to be a computer scientist your whole life and now, finally, that dream is coming true! '
            'You just received the Letter – you are an employee at Wayfair starting Monday morning. '
            'But let’s be honest you sent too many letters of application to even remember what kind of company Wayfair'
            ' is, right? Let’s check it out!', # this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')

    
@sims4.commands.Command('level1_notif1', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_basic_notification(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)


    tgt_client = services.client_manager().get(_connection)
    output('first notif')
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",  # string id form string table
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
            "XXXX Area Rug\nHave a look at this beautiful handwoven rug! It is made of the finest Materials only, wisely chosen by Wayfair. The natural green colour is a perfect fit for all living rooms!\nMake your house feel like a HOME!\nDetails:\nName: XXXX Green Area Rug\nSize: Rectangle 5’ x 8’\nOverall Product Weight: 56 lb.\nFree Shipping on orders over $35.00\n",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 16900524886024814375)))
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up',
                                             exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')
    
    
@sims4.commands.Command('level1_ok2', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'XXXXXX...',# this is where the headline is written -> insert headline here
            'That really does sound familiar. '
            'Where do I know that name from? '
            'Wasn’t it like a childhood friend or something?',# this is where the body part is written -> insert tet here
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')

    
@sims4.commands.Command('level1_notif2', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_basic_notification(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)


    tgt_client = services.client_manager().get(_connection)
    output('first notif')
    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "string id",  # string id form string table
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
            "Hmmmmm...",
            "This really is kind of suss, I cannot seem to get that name out of my head. \nWhere do I know it from? I must find out!",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up',
                                             exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')
    

@sims4.commands.Command('level1_notif3', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_basic_notification(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    tgt_client = services.client_manager().get(_connection)
    output('third notif')
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
            "Mhmm... ",
            "XXXX is still stuck in my head.\nWhere do I know you from?\n",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show a basic notification you fucked up', exception=ex)
        output('Failed to show a basic notification, please locate your exception log file.')
    output('Done showing.')    
    
    
@sims4.commands.Command('level1_ok3', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'GREEN! Of course!', # this is where the headline is written -> insert headline here
            'It was their favourite colour! And their Name!? Now I know who XXXX was. They were a good friend from back in school, '
            'but they went missing when we were around 8 years old. How could I have forgotten!! I must have repressed the memories. '
            'I have been really close with them; it was a big shock for me when they suddenly disappeared. Police never found out where they went or what happened with them. '
            'I wish I could have at least said goodbye. But how does this rug end up having the same name as they had? I got to find out more about this.',
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')

 
# Coding Level 2
@sims4.commands.Command('level2_ok1', command_type=sims4.commands.CommandType.Live)
def _ok(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test ok dialog.')

    def _on_acknowledged(_dialog: UiDialogOk):
        if _dialog.accepted:
            output('Ok option chosen.')
        else:
            output('Dialog closed.')

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline', text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
        dialog = CommonOkDialog(
            'Whats this??', # this is where the headline is written -> insert headline here
            'I went through all the files at Wayfair and I think I found something. There is a catalogue that is signed to be for VIP’s only. '
            'But why would a furniture firm like Wayfair have a VIP membership? And why would it be sealed? Isn’t that suspicious? '
            'What is VIP furniture supposed to be and why is it so secret that it has to be sealed away from normal customers? '
            'Wouldn’t a VIP membership be a good seller? So why hide it? Also isn’t a rug just a rug? I need to get access to the data that’s in there. '
            'Let’s see what I can do about it.',
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!', text_color=CommonLocalizedStringColor.RED)
        )
        dialog.show(on_acknowledged=_on_acknowledged)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show ok dialog, please locate your exception log file.')
    output('Done showing.')

