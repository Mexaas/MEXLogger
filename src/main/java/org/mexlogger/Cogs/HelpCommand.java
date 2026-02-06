package org.mexlogger.Cogs;

import net.dv8tion.jda.api.components.actionrow.ActionRow;
import net.dv8tion.jda.api.components.buttons.Button;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import org.mexlogger.CommandManager.Command;
import java.util.concurrent.TimeUnit;

public class HelpCommand implements Command {
    @Override
    public String name() {
        return "help";
    }
    @Override
    public void executeCommand(MessageReceivedEvent event) {
        event.getChannel().sendMessage(
                """
                # :raccoon: Помощь по командам\n
                - Пока-что ` пусто... `
                """
        ).addComponents(ActionRow.of(Button.danger(" ", "⏹️ Удалить")), ActionRow.of(Button.secondary("  ", "⏹️ Заполнить")))
                .queue(message -> {
                    message.editMessageComponents(
                            ActionRow.of(Button.danger(
                            "DELETE_BUTTON_HELP:" + event.getAuthor().getId() + ":" + message.getId()
                                    + ":" + event.getChannel().getId(), "⏹️ Удалить")),
                            ActionRow.of(Button.secondary(
                                    "MODAL_BUTTON_HELP:" + event.getAuthor().getId(), "⏹️ Заполнить"))).queue();
                    message.delete().queueAfter(20, TimeUnit.SECONDS);
                });

    }
}