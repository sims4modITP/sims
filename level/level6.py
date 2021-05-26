# functions for level 6


# First notification 
@sims4.commands.Command('notif1_level_6', command_type=sims4.commands.CommandType.Live)
def common_testing_show_basic_notification(self):
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
            "FOUND SOMETHING",
            "I think I have found something important ... ",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 16900524886024814375)))
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                             'Failed to show a basic notification you fucked up',
                                             exception=ex)

        
# Targeted Question Dialog aus Level 6 (mit den dazugehörigen imports => Innerer Dialog)
import sims4.commands

# imports for the targeted question
from sims4communitylib.dialogs.common_targeted_question_dialog import CommonTargetedQuestionDialog
from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ui.ui_dialog import UiDialogOkCancel


@sims4.commands.Command('question_dialogue', command_type=sims4.commands.CommandType.Live)
# first value is the function name
def _common_testing_show_targeted_question_dialog(_connection: int = None):
    # define two types of Dialogs
    output = sims4.commands.CheatOutput(_connection)

    # All UI Properties are found in ui_dialog.py

    # display a Notification for the sim
    def _ok_chosen(_: UiDialogOkCancel):
        output('Return => True')

    def _cancel_chosen(_: UiDialogOkCancel):
        output('Return => False')

    # create the tokens to each phrase

    # LocalizedStrings within other LocalizedStrings
    description_tokens = (
        CommonLocalizationUtils.create_localized_string(
            "The name of this file reminds me of something. Could it be some sort of codename? \nWhat is that supposed to mean?",
            tokens=(CommonSimUtils.get_active_sim_info(),),
            text_color=CommonLocalizedStringColor.DEFAULT),)
    ok_text = (
        CommonLocalizationUtils.create_localized_string("That reminds me of my friend XXXX....Weird....",
                                                        tokens=(CommonSimUtils.get_active_sim_info(),),
                                                        text_color=CommonLocalizedStringColor.GREEN),)

    cancel_text = (
        CommonLocalizationUtils.create_localized_string("Hm actually that looks like any other Filename",
                                                        tokens=(CommonSimUtils.get_active_sim_info(),),
                                                        text_color=CommonLocalizedStringColor.RED),)
    # Define the Dialogue
    # => Call the Class

    # define the dialogue
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
    # show => shows a specific param
    # => here shows dialog which we defined before
    dialog.show(
        # .show => show the dialogue and everything in the brackets
        # CommonSimUtils.get_active_sim_info(),
        # tuple(CommonSimUtils.get_sim_info_for_all_sims_generator())[0],
        # sim who answers and got targeted
        sim_info=CommonSimUtils.get_active_sim_info(),
        # sim who asks the question
        # get someone who is a Comp. Scientist

        # Bella Goth bzw Grusel => Is an Agent => suits the story
        target_sim_info=CommonSimUtils.get_active_sim_info(),
        # Travis Scott => is a Tech Guru => Is your Colleague
        # target_sim_info=CommonSimUtils.get_sim_info_of_sim_with_name("Travis", "Scott"),

        # 2 Options of buttons in that Dialogue Windows :

        # Depending on what was chosen => that notification will pop up
        # on_ok_selected – Invoked upon the player clicking the Ok button in the dialog.
        on_ok_selected=_ok_chosen,
        # on_cancel_selected – Invoked upon the player clicking the Cancel button in the dialog.
        on_cancel_selected=_cancel_chosen
    )


# Second notification - right input
@sims4.commands.Command('notif2_level_6', command_type=sims4.commands.CommandType.Live)
def notif2_level_6(_connection: int = None):
    try:
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
            "",
            "XXXX?? What have they to do with all of this? Weren’t they kidnapped themselves? Why did they disappear? "
            "What if they are a part of this? No, I do not want to believe this. I cannot believe this. "
            "If they are responsible for all that has happened to those poor children...\n\n"
            "All the pain that I went through. I cannot let history repeat itself! I will not give up that easily! ",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                             'Failed to show a basic notification you fucked up',
                                             exception=ex)


# Third notification - wrong input
@sims4.commands.Command('notif3_level_6', command_type=sims4.commands.CommandType.Live)
def notif3_level_6(_connection: int = None):
    try:
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
            "",
            "That doesn’t seem to be right, there has to be something bigger to it. "
            "I just cant quite put my finger on what it is. Now focus!!",
            title_tokens=title_tokens,
            description_tokens=description_tokens,
        )
        dialog.show()
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                             'Failed to show a basic notification you fucked up',
                                             exception=ex)


