package org.mexlogger.Cogs;

import net.dv8tion.jda.api.components.label.Label;
import net.dv8tion.jda.api.components.textinput.TextInput;
import net.dv8tion.jda.api.components.textinput.TextInputStyle;
import net.dv8tion.jda.api.modals.Modal;

public class HelpModalWindow {
    public static Modal create() {
        TextInput name = TextInput.create("name", TextInputStyle.SHORT)
                .setPlaceholder("Андрей").setMinLength(2).setMaxLength(30)
                .setRequired(true).build();
        TextInput description = TextInput.create("description", TextInputStyle.PARAGRAPH)
                .setPlaceholder("Меня зовут Андрей, мне 17. Психолог").setMinLength(2).setMaxLength(200)
                .setRequired(true).build();

        return Modal.create("helpCMD_modal", "Обратная связь").addComponents(
                Label.of("Ваше имя", name), Label.of("Расскажите о себе", description))
                .build();
    }
}