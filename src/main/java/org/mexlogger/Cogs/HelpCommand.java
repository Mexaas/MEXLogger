package org.mexlogger.Cogs;

import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import org.mexlogger.CommandManager.Command;

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
        ).queue();
    }
}