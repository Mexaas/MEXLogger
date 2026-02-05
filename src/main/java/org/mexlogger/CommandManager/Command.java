package org.mexlogger.CommandManager;

import net.dv8tion.jda.api.events.message.MessageReceivedEvent;

public interface Command {
    String name();

    void executeCommand(MessageReceivedEvent event);
}
