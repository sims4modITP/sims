def _common_testing_show_targeted_question_dialog(): #Funktionsname => so machen dass das auf bedingung reagiert

    # define two types of Dialogs

    # Alle UI properties sind im ui_dialog.py zu finden

    def _ok_chosen(_: UiDialogOkCancel): # mit hilfe des UI Handlings
        pass

    def _cancel_chosen(_: UiDialogOkCancel):
        pass

    # LocalizedStrings within other LocalizedStrings
    description_tokens = (CommonLocalizationUtils.create_localized_string(CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME, tokens=(CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
    # Definiere welchen Dialog wir haben möchten
    dialog = CommonTargetedQuestionDialog(
        CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
        # question_tokens (Iterator[Any], optional) – Tokens to format into the question text.
        question_tokens=description_tokens,
        # ok_text_identifier (Union[int, str, LocalizedString, CommonStringId], optional) – A decimal identifier for the Ok text.
        ok_text_identifier=CommonLocalizationUtils.create_localized_string(CommonStringId.TESTING_TEST_BUTTON_ONE, text_color=CommonLocalizedStringColor.RED),
        # cancel_text_identifier (Union[int, str, LocalizedString, CommonStringId], optional) – A decimal identifier for the Cancel text.
        cancel_text_identifier=CommonStringId.TESTING_TEST_BUTTON_TWO
    )
    dialog.show(
        # .show => show the dialogue and everything in the brackets
        CommonSimUtils.get_active_sim_info(),
        tuple(CommonSimUtils.get_sim_info_for_all_sims_generator())[0],

        # 2 Options of buttons in that Dialogue Windows :
        # on_ok_selected (Callable[[UiDialogOkCancel], Any], optional) – Invoked upon the player clicking the Ok button in the dialog.
        on_ok_selected=_ok_chosen,
        # on_cancel_selected (Callable[[UiDialogOkCancel], Any], optional) – Invoked upon the player clicking the Cancel button in the dialog.
        on_cancel_selected=_cancel_chosen
    )
