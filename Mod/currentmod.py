from typing import Any

# from filters.sim_template import TunableSimTemplate
# from interactions.base.super_interaction import SuperInteraction
# from interactions.interaction_queue import InteractionQueue
from protocolbuffers import Consts_pb2
from server_commands.sim_commands import modify_fund_helper
from sims.sim_info import SimInfo
# rom sims.sim_spawner import SimCreator, SimSpawner
from sims4communitylib.classes.math.common_vector3 import CommonVector3
from sims4communitylib.dialogs.common_choice_outcome import CommonChoiceOutcome
from sims4communitylib.dialogs.common_input_float_dialog import CommonInputFloatDialog
from sims4communitylib.dialogs.common_ok_dialog import CommonOkDialog
from sims4communitylib.dialogs.common_targeted_question_dialog import CommonTargetedQuestionDialog
from sims4communitylib.enums.strings_enum import CommonStringId
from sims4communitylib.events.interaction.common_interaction_event_dispatcher import \
    CommonInteractionEventDispatcherService
from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from sims4communitylib.utils.sims.common_sim_interaction_utils import CommonSimInteractionUtils
from sims4communitylib.utils.sims.common_sim_location_utils import CommonSimLocationUtils
from sims4communitylib.utils.sims.common_sim_spawn_utils import CommonSimSpawnUtils
from ui.ui_dialog import UiDialogOkCancel
from sims4communitylib.utils.sims.common_buff_utils import CommonBuffUtils
from sims4communitylib.utils.sims.common_sim_inventory_utils import CommonSimInventoryUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from distributor.shared_messages import IconInfoData
# from ui.ui_dialog import UiDialogOk
from ui.ui_dialog_notification import UiDialogNotification
from sims4.resources import Types
from sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_resource_utils import CommonResourceUtils
from sims4communitylib.utils.localization.common_localization_utils import CommonLocalizationUtils
from sims4communitylib.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from statistics.skill import Skill
from sims4communitylib.enums.skills_enum import CommonSkillId
from sims4communitylib.utils.sims.common_sim_skill_utils import CommonSimSkillUtils


def run_once(function):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return function(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


class skill1:

    @run_once
    def ok1(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'This is you!',  # this is where the headline is written -> insert headline here
                'You wanted to be a computer scientist your whole life and now, finally, that dream is coming true! '
                'You just received the Letter – you are an employee at Wayfair starting Monday morning. '
                'But let’s be honest you sent too many letters of application to even remember what kind of company Wayfair'
                ' is, right? Let’s check it out!',  # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
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
                "RUG SALE!!!",
                "XXXX Area Rug\nHave a look at this beautiful handwoven rug! It is made of the finest Materials only, wisely chosen by Wayfair. The natural green colour is a perfect fit for all living rooms!\nMake your house feel like a HOME!\nDetails:\nName: XXXX Green Area Rug\nSize: Rectangle 5’ x 8’\nOverall Product Weight: 56 lb.\nFree Shipping on orders over $35.00\n",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show(IconInfoData(CommonResourceUtils.get_resource_key(Types.PNG, 16900524886024814375)))
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up',
                                                 exception=ex)

    @run_once
    def ok2(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'XXXXXX...',  # this is where the headline is written -> insert headline here
                'That really does sound familiar. '
                'Where do I know that name from? '
                'Wasn’t it like a childhood friend or something?',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def common_testing_show_basic_notification2(self):
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
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up',
                                                 exception=ex)

    @run_once
    def common_testing_show_basic_notification3(self):
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
                "Mhmm... ",
                "XXXX is still stuck in my head.\nWhere do I know you from?\n",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)

    @run_once
    def ok3(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'GREEN! Of course!',  # this is where the headline is written -> insert headline here
                'It was their favourite colour! And their Name!? Now I know who XXXX was. They were a good friend from back in school, '
                'but they went missing when we were around 8 years old. How could I have forgotten!! I must have repressed the memories. '
                'I have been really close with them; it was a big shock for me when they suddenly disappeared. Police never found out where they went or what happened with them. '
                'I wish I could have at least said goodbye. But how does this rug end up having the same name as they had? I got to find out more about this.',
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 241020,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(4182591747))


class skill2:
    def ok(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'Whats this??',  # this is where the headline is written -> insert headline here
                'I went through all the files at Wayfair and I think I found something. There is a catalogue that is signed to be for VIP’s only. '
                'But why would a furniture firm like Wayfair have a VIP membership? And why would it be sealed? Isn’t that suspicious? '
                'What is VIP furniture supposed to be and why is it so secret that it has to be sealed away from normal customers? '
                'Wouldn’t a VIP membership be a good seller? So why hide it? Also isn’t a rug just a rug? I need to get access to the data that’s in there. '
                'Let’s see what I can do about it.',
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Lets go!',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    def item(self):
        CommonSimInventoryUtils.add_to_inventory(CommonSimUtils.get_active_sim_info(), 34318, 3)
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 31038,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(2822329173))


class skill3:
    @run_once
    def foo(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (
                CommonLocalizationUtils.create_localized_string(
                    2977195159,
                    text_color=CommonLocalizedStringColor.GREEN
                ),
            )
            description_tokens = (
                CommonLocalizationUtils.create_localized_string(
                    2977195159,
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

    @run_once
    def ok(self):
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

    @run_once
    def three_third_dialogue(self):
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

    @run_once
    def common_testing_show_input_float_dialog(self) -> Any:
        def _on_chosen(choice: float, outcome: CommonChoiceOutcome) -> Any:
            if choice == 2 or choice == 3:
                pass
            else:
                dialog2.show(on_submit=_on_chosen)

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string
                            ("You nearly did it!", text_color=CommonLocalizedStringColor.BLUE),)
            description_tokens = (CommonLocalizationUtils.create_localized_string(
                                      "Your have nearly made it to the final destination of your work to reach the next hint.\nThere is one more thing you have to solve before you can take a look at it: \n\nWhat might be the Evil behind all that \n(1) Pop-Culture \n(2) Capitalism \n(3) Men ",
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

    @run_once
    def ok1(self):
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
                'Special things stand the test of time. Used look meets modern. This rug cannot be described any better. This style shows the classic counter-reaction to swish designer pieces and is so special that you need to look at least twice. Upcycling is the new trend. Exceptional colours make this small work of art into a real eye catcher with character. Anyone can do boring. The Oeko-Tex 100 certified quality is not only a low price but also durable and dirt-repellent. Of course the fabric used is suitable for use on underfloor heating. Bring a trend setter home, which sets new standards in combination with your furniture.Details:\n\n\nName: Valenti Remer Gray/Blue Area Rug\n\nSize: Rectangle 5’ x 6’\n\nOverall Product Weight: 39.5 lb.\n\nFree Shipping on orders over $35.00\n\n',
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


class skill4:
    @run_once
    def notification(self):
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
                "The truth...",
                "There is only one way to find out the truth. I have to hack the police system!\n",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)

    @run_once
    def _ok(_self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'PIC',  # this is where the headline is written -> insert headline here
                'Name: Valenti Remer\n'
                'Gender: Male\n'
                'Age: 5\n'
                'Weight: 39.5 lb\n'
                'Height: 42.5"\n'
                'Missing since: 27.03.2020\n'
                'Last seen in Northville, New York\n'
                'Description:\n'
                'Went missing while playing in a field near his house. Wore a blue jacket, black trousers and sneakers. Last seen by his mother in the kitchen, where he got himself a glass of water.',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def _ok2(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'PIC',  # this is where the headline is written -> insert headline here
                'Name: Connie Peyton\n'
                'Gender: Female\n'
                'Age: 7\n'
                'Weight: 49.5 lb\n'
                'Height: 47.7"\n'
                'Missing since: 15.08.2020\n'
                'Last seen in Boston, Massachusetts\n'
                'Description:\n'
                'Went missing on her way home from school. Wore a blue dress, brown sandals and a bow tie in her hair. Last seen by friends at school at 12:35 o’clock.',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def _ok3(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'PIC',  # this is where the headline is written -> insert headline here
                'Name: Name: Charlotte Brandt\n'
                'Gender: Female\n'
                'Age: 4\n'
                'Weight: 34.0 lb\n'
                'Height: 39.5"\n'
                'Missing since: 11.03.2021\n'
                'Last seen in New York City, New York\n'
                'Description:\n'
                'Went missing in the metro while with her mother. Wore a white jacket. Last seen by said mother while buying a ticket. Reported immediately.',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def notification2(self):

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
                "A MATCH",
                "All ages, dates and even NAMES seem to match?!?! How is that even possible? I wanted to just prove myself wrong and get my overly curious mind some rest, but what am I to do with this now? It’s not enough to actually prove it. Police will never believe me. Its my word against theirs. Besides that, I didn’t exactly get the files the legal way… I am on my own now. But I have to find out what this really is!! \n",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)

    @run_once
    def oklvl5(self):

        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                '',
                'PAll those poor children. And their families. Friends. I remember the day XXXX went missing too well. I was little so I can’t recall all the details, but I remember the feeling. Of loosing someone. Someone important. Like loosing a part of myself.\nI remember we used to go for a swim in his pool. We used to play in the near forest, till our mothers would call us back for dinner. We used to be together. We used to be happy.\nBut then one day a police officer knocked at my door. She wanted to know if I had seen them today in school, and I said no – I thought they were ill. Turned out they were not ill at all. They left the house in the morning, giving their mom a goodbye kiss, but they never arrived at school. It was only after a few hours that someone had noticed. They instantly called their mother and the police. They searched everywhere but they could never find them. And I was just lost and numb. I didn’t know what to do or feel. After that, my Mother insisted on driving me to school for a very long time. As time passed, the pain got a bit easier to handle. Those poor kids.',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('Maybe... ',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)

    @run_once
    def notificationlvl5(self):

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
                "",
                "There seems to be a connection between Wayfair and those missing kids, but I don’t know what it is yet. I guess I got to dig a little deeper. Those kids and their families deserve to know the truth!",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)


class skill6:

    @run_once
    def notification(self):
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

    @run_once
    def common_testing_show_targeted_question_dialog(self):
        # define two types of Dialogs

        # All UI Properties are found in ui_dialog.py

        # display a Notification for the sim
        def _ok_chosen(_: UiDialogOkCancel):
            self.notif2_level_6()

        def _cancel_chosen(_: UiDialogOkCancel):
            self.notif3_level_6()
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

    @run_once
    def notif2_level_6(self):
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
    @run_once
    def notif3_level_6(self):
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


class skill7:

    @run_once
    def _7ok1(self):
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

    @run_once
    def notification(self):
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
                "Warehouses",
                "All the Warehouses are near the places children got missing at!?!?\n\nI need to get access to the Warehouses, maybe I can find prove there. This all is connected somehow!\n\nI feel like I don’t like where this is going ... but its on me to help these children now!",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up',
                                                 exception=ex)

    @run_once
    def notificationlvl8(self):
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
                "",
                "I got in, its all there!! Some dates of the transactions and bills match the dates of the police files! There are incoming deliveries on the 27th of March 2020, the 15th of August 2020, and the 11th of march in 2021 with the exact weight that each of the children had - delivered to the nearest Warehouse. The bill says its “VIP Custom Delivery”. Is this what the VIP list is all about? Selling children? There must be someone responsible for this! Some kind of Boss. Someone to run the business. And if all of these match with Wayfair delivery data – it must be the Boss of Wayfair right?  Well, there is only one problem about the Boss of Wayfair: No one really knows them. So, I have to get the information my way again!",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up',
                                                 exception=ex)


class skill9:

    @run_once
    def notification(self):
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
                "Hooray!",
                "I found the boss’s laptop it was connected to the firm network. So all I got to do now is get it!",
                title_tokens=title_tokens,
                description_tokens=description_tokens,
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(),
                                                 'Failed to show a basic notification you fucked up', exception=ex)

    @run_once
    def ok(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                'Here, I found some Messages that prove the transport of the kids!! ',
                # this is where the headline is written -> insert headline here
                'One of them says, that there has been struggles with the latest delivery and that they can’t seem to shut her down. That must be another child!! Who is she? Poor little thing. But I will safe her! '
                'With this piece of information, I am actually able to prove what’s been happening here over the past year! There is messages and photos. It’s all right there!!\n'
                'But wait what is this? XXXX?? Their name again? No, this cant be?'
                'It says here that the owner of this laptop is XXXX!? Does that mean they are the Boss to all this? What happened after they went missing? My childhood friend – what kind of monster have they become.\n'
                'I feel sick. This is too much. It must be made public! I will stop them!!',
                # this is where the body part is written -> insert tet here
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('LETS GO',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)


class skill10:

    @run_once
    def travel(self):
        CommonSimUtils.get_active_sim_info().send_travel_switch_to_zone_op(326525086965567655)

    @run_once
    def money(self):
        modify_fund_helper(1000, Consts_pb2.TELEMETRY_MONEY_CHEAT, CommonSimUtils.get_active_sim_info())

    @run_once
    def common_testing_show_targeted_question_dialog(self):
        # define two types of Dialogs

        # All UI Properties are found in ui_dialog.py

        # display a Notification for the sim
        def _ok_chosen(_: UiDialogOkCancel):
            self.travel()
            # CommonSimSpawnUtils.spawn_sim_at_active_sim_location(
            # CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"))
            # CommonSimInteractionUtils.cancel_all_queued_or_running_interactions(CommonSimUtils.get_sim_info_of_sim_with_name("Bella","Goth"),"to make sth else")

            """if not CommonSimInteractionUtils.test_super_interaction(CommonSimUtils.get_sim_info_of_sim_with_name("Bella",
                                                                                                              "Goth"),199524,CommonSimUtils.get_active_sim_info()):
                return _ok_chosen
            #CommonSimInteractionUtils.queue_super_interaction(CommonSimUtils.get_sim_info_of_sim_with_name("Bella",
                                                                                                          "Goth"),199524,CommonSimUtils.get_active_sim_info())
            #modify_fund_helper(1000, Consts_pb2.TELEMETRY_MONEY_CHEAT, CommonSimUtils.get_active_sim_info())
            """

        def _cancel_chosen(_: UiDialogOkCancel):
            pass

        # create the tokens to each phrase

        # LocalizedStrings within other LocalizedStrings
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                "Do you want to publish everything that you’ve found and stop this awful business?",
                tokens=(CommonSimUtils.get_active_sim_info(),),
                text_color=CommonLocalizedStringColor.DEFAULT),)
        ok_text = (
            CommonLocalizationUtils.create_localized_string("Yes",
                                                            tokens=(CommonSimUtils.get_active_sim_info(),),
                                                            text_color=CommonLocalizedStringColor.GREEN),)

        cancel_text = (
            CommonLocalizationUtils.create_localized_string("YESSSSS",
                                                            tokens=(CommonSimUtils.get_active_sim_info(),),
                                                            text_color=CommonLocalizedStringColor.GREEN),)
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

    @run_once
    def ok(self):
        try:
            # LocalizedStrings within other LocalizedStrings
            title_tokens = (CommonLocalizationUtils.create_localized_string('Story Headline',
                                                                            text_color=CommonLocalizedStringColor.GREEN),)
            description_tokens = (CommonLocalizationUtils.create_localized_string('Actual Story', tokens=(
                CommonSimUtils.get_active_sim_info(),), text_color=CommonLocalizedStringColor.BLUE),)
            dialog = CommonOkDialog(
                "",
                "You published everything that you found, and the police was able to find all of the ones involved into child traffic including XXXX - they will all be sent to jail. Some of the kids have been found and are now back together with their families and so very thankful to the anonymous human who saved their lives! Police is still searching for the rest of them, but they got an informer that was willing to tell them everything in order to lessen their punishment. After all, almost all kids are back in the life they deserve – surrounded by a loving family. A hashtag started to spread, where families thank you for saving their children and giving them their normal lives back. The word has spread all over the world, in in every newspaper and on every screen. Wayfair got eliminated. You made it!",
                # this is where the body part is written -> insert tet here

                title_tokens=title_tokens,
                description_tokens=description_tokens,
                ok_text_identifier=CommonLocalizationUtils.create_localized_string('LETS GO',
                                                                                   text_color=CommonLocalizedStringColor.RED)
            )
            dialog.show()
        except Exception as ex:
            CommonExceptionHandler.log_exception(ModInfo.get_identity(), 'Failed to show dialog', exception=ex)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Skill, "_show_level_notification")
def _load_skill1(original, self, *args, **kwargs) -> Any:
    simsskill = CommonSimSkillUtils.get_current_skill_level(CommonSimUtils.get_active_sim_info(),
                                                            CommonSkillId.ADULT_MAJOR_PROGRAMMING)

    if simsskill == 1:
        skill1().ok1()
        skill1().common_testing_show_basic_notification()
        skill1().ok2()
        skill1().common_testing_show_basic_notification2()
        skill1().common_testing_show_basic_notification3()
        skill1().ok3()
    return original(self, *args, **kwargs)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Skill, "on_skill_level_up")
def _load_foo(original, self, *args, **kwargs) -> Any:
    simsskill = CommonSimSkillUtils.get_current_skill_level(CommonSimUtils.get_active_sim_info(),
                                                            CommonSkillId.ADULT_MAJOR_PROGRAMMING)
    logicskill = CommonSimSkillUtils.get_current_skill_level(CommonSimUtils.get_active_sim_info(), CommonSkillId.ADULT_MAJOR_LOGIC)

    if simsskill == 2:
        skill2().ok()
        skill2().item()
    elif simsskill == 3 and logicskill == 2:
        skill3().ok1()
        skill3().ok()
        skill3().three_third_dialogue()
        skill3().common_testing_show_input_float_dialog()
        skill3().foo()
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 31038,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(776248071))
    elif simsskill == 4:
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 23910,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(3173404515))
        # CommonSimUtils.get_active_sim_info().send_travel_switch_to_zone_op(326525086965567655)
        if not CommonSimLocationUtils.is_on_current_lot(CommonSimUtils.get_active_sim_info()):
            CommonSimSpawnUtils.spawn_sim(CommonSimUtils.get_active_sim_info())

        skill4().notification()
        skill4()._ok()
        skill4()._ok2()
        skill4()._ok3()
        skill4().notification2()
    elif simsskill == 5 and logicskill == 3:
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 37549,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(19436895))
        skill4().oklvl5()
        skill4().notificationlvl5()
    elif simsskill == 6:
        skill6().notification()
        skill6().common_testing_show_targeted_question_dialog()
    elif simsskill == 7:
        skill7()._7ok1()
        skill7().notification()
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 31038,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(3303543444))
    elif simsskill == 8:
        skill7().notificationlvl8()
    elif simsskill == 9:
        skill9().notification()
        skill9().ok()
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 99269,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(2282594607))
    elif simsskill == 10 and logicskill == 4:
        skill10().common_testing_show_targeted_question_dialog()
        skill10().ok()
        CommonBuffUtils.add_buff(CommonSimUtils.get_active_sim_info(), 37541,
                                 buff_reason=CommonLocalizationUtils.create_localized_string(1277988298))

    return original(self, *args, **kwargs)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfo, "on_loading_screen_animation_finished")
def _common_on_sim_load(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)

    if not CommonSimLocationUtils.is_on_current_lot(
            CommonSimUtils.get_active_sim_info()) and CommonLocationUtils.get_current_zone_id() == 326525086965567655:
        CommonSimSpawnUtils.spawn_sim(CommonSimUtils.get_active_sim_info(), None,
                                      CommonVector3(180.076584, 150.000015, 254.197342))
        CommonSimSpawnUtils.spawn_sim(
            CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"), None,
            CommonVector3(181.677994, 150.000015, 246.188354))  # 181.677994, 150.000015, 246.188354
        CommonSimSpawnUtils.soft_reset(CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"))
        if CommonSimLocationUtils.is_on_current_lot(CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth")):
            CommonSimSpawnUtils.soft_reset(CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"))

            CommonSimInteractionUtils.cancel_all_queued_or_running_interactions(
                CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"), "to make sth else")
            CommonSimInteractionUtils.queue_super_interaction(
                CommonSimUtils.get_sim_info_of_sim_with_name("Bella", "Goth"),
                199524, CommonSimUtils.get_active_sim_info())
        if CommonSimInteractionUtils.has_interaction_running_or_queued(CommonSimUtils.get_active_sim_info(),
                                                                       199524) or CommonSimInteractionUtils.has_interaction_running_or_queued(
            CommonSimUtils.get_active_sim_info(), 112420):
            modify_fund_helper(1000, Consts_pb2.TELEMETRY_MONEY_CHEAT, CommonSimUtils.get_active_sim_info())
    return original(self, *args, **kwargs)



@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), CommonInteractionEventDispatcherService,
                                         "_on_interaction_outcome")
def _common_interaction(original, self, *args, **kwargs) -> Any:
    if CommonSimInteractionUtils.has_interaction_running_or_queued(CommonSimUtils.get_active_sim_info(),
                                                                   199524) or CommonSimInteractionUtils.has_interaction_running_or_queued(
        CommonSimUtils.get_active_sim_info(), 112420) and CommonSimLocationUtils.is_on_current_lot(
        CommonSimUtils.get_sim_info_of_sim_with_name("Bella",
                                                     "Goth")) and CommonLocationUtils.get_current_zone_id() == 326525086965567655 and CommonSimSkillUtils.get_current_skill_level(
        CommonSimUtils.get_active_sim_info(),
        CommonSkillId.ADULT_MAJOR_PROGRAMMING):
        skill10().money()

    return original(self, *args, **kwargs)
