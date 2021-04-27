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
        output('Story will be continued.')

    def _cancel_chosen(_: UiDialogOkCancel):
        output('Story stops => Nothing will be published.')

    # create the tokens to each phrase

    # LocalizedStrings within other LocalizedStrings
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
