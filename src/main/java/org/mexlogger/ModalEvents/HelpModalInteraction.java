package org.mexlogger.ModalEvents;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.entities.channel.concrete.TextChannel;
import net.dv8tion.jda.api.events.interaction.ModalInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.mexlogger.Main;

public class HelpModalInteraction extends ListenerAdapter {
    @Override
    public void onModalInteraction(ModalInteractionEvent event) {
        JDA jda = Main.getJDA();
        if (event.getModalId().equals("helpCMD_modal")) {
            TextChannel adminChannel = jda.getTextChannelById(1469373096132739102L);
            adminChannel.sendMessage(String.format(
                    "# :envelope_with_arrow: Данные от %s\n" +
                    "- Настоящее имя: ` " + event.getValue("name").getAsString() + " `\n" +
                    "- Описание: ` " + event.getValue("description").getAsString() + " `",  event.getUser().getName())
            ).queue();
            event.reply("# :inbox_tray: Запрос отправлен!"
                    + "\n- Ожидайте ` рассмотрения `!").setEphemeral(true).queue();
        }
    }
}
