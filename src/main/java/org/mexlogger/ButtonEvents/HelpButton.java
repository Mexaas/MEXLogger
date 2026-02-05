package org.mexlogger.ButtonEvents;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.entities.channel.concrete.TextChannel;
import net.dv8tion.jda.api.events.interaction.component.ButtonInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.mexlogger.Main;

import java.util.concurrent.TimeUnit;

public class HelpButton extends ListenerAdapter {
    @Override
    public void onButtonInteraction(ButtonInteractionEvent event) {
        JDA jda = Main.getJDA();
        if (event.getComponentId().startsWith("helpCMD_button_delete:")) {
            String[] data = event.getComponentId().split(":");
            long authorID = Long.parseLong(data[1]); long messageID = Long.parseLong(data[2]);

            if (event.getUser().getIdLong() != authorID) {
                event.reply("# :x: Ошибка!\n- Вы не ` автор ` команды!").setEphemeral(true)
                        .queue();
            } else {
                long channel = Long.parseLong(data[3]);
                TextChannel currentChannel = jda.getTextChannelById(channel);
                if (currentChannel != null) {
                    currentChannel.deleteMessageById(messageID)
                            .queue(_ -> event.reply("# :inbox_tray: Оповещение\n- Сообщение было ` удалено `!")
                                            .setEphemeral(true)
                                            .queue(hook -> hook.deleteOriginal().queueAfter(5, TimeUnit.SECONDS)),
                                    Throwable::printStackTrace
                            );
                }
            }
        }
    }
}
