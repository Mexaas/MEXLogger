package org.mexlogger;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.events.session.ReadyEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.requests.GatewayIntent;
import org.mexlogger.Cogs.HelpCommand;
import org.mexlogger.CommandManager.Command;
import org.mexlogger.CommandManager.CommandManager;

public class Main extends ListenerAdapter {
    private static JDA jda;

    public static JDA getJDA() {
        return jda;
    }
    static void main(String[] args) throws InterruptedException {
        JDABuilder builder = JDABuilder.createDefault(System.getenv("DISCORD_TOKEN"))
                .setActivity(Activity.customStatus("люблю джаву"))
                .addEventListeners(new Main())
                .enableIntents(
                        GatewayIntent.MESSAGE_CONTENT,
                        GatewayIntent.GUILD_MEMBERS
                );
        jda = builder.build().awaitReady();

        CommandManager.register(new HelpCommand());
    }
    @Override
    public void onReady(ReadyEvent event) {
        System.out.println("Bot is ready");
    }

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {
        String message = event.getMessage().getContentRaw();
        if (event.getAuthor().isBot() || !message.startsWith(CommandManager.PREFIX)) {
            return;
        }
        String[] text = message.substring(1).split(" ");
        Command command = CommandManager.get(text[0].toLowerCase());
        if (command != null) {
            command.executeCommand(event);
        }
    }
}