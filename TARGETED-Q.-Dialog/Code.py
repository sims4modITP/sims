# TARGETED QUESTION DIALOG
# EXAMPLE CODE AND EXPLANATION BELOW
# base :
# Class for our Dialogue-Window
class CommonTargetedQuestionDialog(question_text, question_tokens=(), ok_text_identifier=CommonStringId.OK, ok_text_tokens=(), cancel_text_identifier=CommonStringId.CANCEL, cancel_text_tokens=(), mod_identity=None)

def _common_testing_show_targeted_question_dialog():

    # define two types of Dialogs

    # All UI Properties are found in ui_dialog.py
    def _ok_chosen(_: UiDialogOkCancel):
        pass

    def _cancel_chosen(_: UiDialogOkCancel):
        pass

    # LocalizedStrings within other LocalizedStrings
    description_tokens = (CommonLocalizationUtils.create_localized_string(CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME, tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
    # Define the Dialogue
    # => Call the Class
    dialog = CommonTargetedQuestionDialog(
        # Fill the properties of that specific Class
        CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
        question_text = "Wanna go shopping ?",
        # question_tokens  – Tokens to format into the question text.
        question_tokens=description_tokens,
        # ok_text_identifier  – A decimal identifier for the Ok text.
        ok_text_identifier=CommonLocalizationUtils.create_localized_string(CommonStringId.TESTING_TEST_BUTTON_ONE, text_color=CommonLocalizedStringColor.RED),
        # cancel_text_identifier  – A decimal identifier for the Cancel text.
        cancel_text_identifier=CommonStringId.TESTING_TEST_BUTTON_TWO
    )
    dialog.show(
        # .show => show the dialogue and everything in the brackets
        CommonSimUtils.get_active_sim_info(),
        tuple(CommonSimUtils.get_sim_info_for_all_sims_generator())[0],

        # 2 Options of buttons in that Dialogue Windows :
        # on_ok_selected – Invoked upon the player clicking the Ok button in the dialog.
        on_ok_selected=_ok_chosen,
        # on_cancel_selected – Invoked upon the player clicking the Cancel button in the dialog.
        on_cancel_selected=_cancel_chosen
    )
