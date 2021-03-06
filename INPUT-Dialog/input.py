# given template
@sims4.commands.Command('s4clib_testing.show_input_float_dialog', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_input_float_dialog(_connection: int=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test input float dialog.')

    def _on_chosen(choice: float, outcome: CommonChoiceOutcome):
        output('Chose {} with result: {}.'.format(pformat(choice), pformat(outcome)))

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string(CommonStringId.TESTING_SOME_TEXT_FOR_TESTING, text_color=CommonLocalizedStringColor.GREEN),)
        description_tokens = (CommonLocalizationUtils.create_localized_string
                              (CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME,
                               tokens=(CommonSimUtils.get_active_sim_info(),),
                               text_color=CommonLocalizedStringColor.BLUE),)
        from sims4communitylib.utils.common_icon_utils import CommonIconUtils
        dialog = CommonInputFloatDialog(
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            2.0,
            title_tokens=title_tokens,
            description_tokens=description_tokens
        )
        dialog.show(on_submit=_on_chosen)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show dialog, please locate your exception log file.')
    output('Done showing.')
  

# edited 

@sims4.commands.Command('input_test', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_input_float_dialog(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test input float dialog.')
    
    def _on_chosen(choice: float, outcome: CommonChoiceOutcome):
        if choice == 6:
            output("answer right")
        else:
            output("answer wrong")

        output('Chose {} with result: {}.'.format(pformat(choice), pformat(outcome)))

    try:
        # LocalizedStrings within other LocalizedStrings
        title_tokens = (CommonLocalizationUtils.create_localized_string
                        ("Solve following task", text_color=CommonLocalizedStringColor.BLUE),)
        description_tokens = (CommonLocalizationUtils.create_localized_string
                              ("what is 3*4/2",
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

    
# input with repeading pop-up as long as answer is incorrect
@sims4.commands.Command('input_first_level_three', command_type=sims4.commands.CommandType.Live)
def _common_testing_show_input_float_dialog(_connection: int = None):
    output = sims4.commands.CheatOutput(_connection)
    output('Showing test input float dialog.')

    def _on_chosen(choice: float, outcome: CommonChoiceOutcome):
        if choice == 2 or choice == 3 or choice == None: 
            output("answer right or dialogue dismissed")
        else:
            output("answer wrong")
            # show dialogue as oftem as needed recoursively while answer is wrong
            dialog2.show(on_submit=_on_chosen)

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
            0,
            title_tokens=title_tokens,
            description_tokens=description_tokens
        )
        # new title -> error message for false input
        title_tokens2 = (CommonLocalizationUtils.create_localized_string
                        ("Think again", text_color=CommonLocalizedStringColor.RED),)
        # in new dialogue -> is to show when input wrong
        dialog2 = CommonInputFloatDialog(
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            0,
            title_tokens=title_tokens2,
            description_tokens=description_tokens
        )
        dialog.show(on_submit=_on_chosen)
    except Exception as ex:
        CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)
        output('Failed to show dialog, please locate your exception log file.')
    output('Done showing.')
