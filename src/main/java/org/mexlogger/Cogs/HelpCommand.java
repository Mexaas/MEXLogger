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
        ).addComponents(ActionRow.of(Button.danger(" ", "⏹️ Удалить")))
                .queue(message -> {
                    message.editMessageComponents(ActionRow.of(Button.danger(
                            "helpCMD_button_delete:" + event.getAuthor().getId() + ":" + message.getId()
                                    + ":" + event.getChannel().getId(), "⏹️ Удалить")
                    )).queue();
                    message.delete().queueAfter(20, TimeUnit.SECONDS);
                });

    }
}