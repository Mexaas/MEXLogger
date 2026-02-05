package org.mexlogger.CommandManager;

import java.util.HashMap;
import java.util.Map;

public class CommandManager {
    public static final String PREFIX = ".";
    private static Map<String, Command> commands = new HashMap<>();

    public static void register(Command command) {
        commands.put(command.name(), command);
    }
    public static Command get(String command) {
        return commands.get(command);
    }
}
