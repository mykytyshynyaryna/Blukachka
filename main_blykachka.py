import smart_blykachka
levandivka = smart_blykachka.Region("Левандівка")
levandivka.set_description("Левандівка пахне поїздами, мостами, переїздами.")

india = smart_blykachka.Region("Район Індія")
india.set_description("Район, де живуть заможні цигани.")

center = smart_blykachka.Region("Центр")
center.set_description("У центрі грає атмосферна музика, розвіюється запах кави та панує спокійна спокійна атмосфера.")

kryvchytsi = smart_blykachka.Region("Кривчиці")
kryvchytsi.set_description("Можна чудово провести час у 'Шевченківському гаю'.")

sykhiv = smart_blykachka.Region("Сихів")
sykhiv.set_description("Обережно, кримінальна місцевість.")

kryvchytsi.link_room(india, "північ")
levandivka.link_room(center, "схід")
sykhiv.link_room(center, "північ")
india.link_room(center, "південь")
kryvchytsi.link_room(center, "захід")
center.link_room(sykhiv, "південь")
kryvchytsi.link_room(sykhiv, "південь")
center.link_room(india, "північ")
center.link_room(kryvchytsi, "схід")
center.link_room(levandivka, "захід")

zaliznychnyk = smart_blykachka.Enemy("Залізничник", "Злий дядько, адже ти пройшовся по коліях")
zaliznychnyk.set_conversation("Ей, ти! Зараз у мене дістанеш!")
zaliznychnyk.set_weakness("шматок рейси")
levandivka.set_character(zaliznychnyk)

tsyhanka = smart_blykachka.Enemy("Циганка", "Жінка індоарійської етнічної групи")
tsyhanka.set_conversation("Давай ручку позолочу.")
tsyhanka.set_weakness("булка хліба")
india.set_character(tsyhanka)

robitnyk = smart_blykachka.Enemy("Робітник", "Чоловік, який працює на грядці")
robitnyk.set_conversation("Не топчись по моїй моркві!")
robitnyk.set_weakness("лопата")
kryvchytsi.set_character(robitnyk)

# hulihan = smart_blykachka.Enemy("Хуліган", "Хлопчина, що вимагає гроші або інші цінні речі")
# hulihan.set_conversation("Ей, є телефон подзвонити?")
# hulihan.set_weakness("балончик")
# sykhiv.set_character(hulihan)
# ________________________________________________________

student = smart_blykachka.Character("Студент УКУ", "Студент прикладних наук УКУ")
student.set_conversation("Сон для слабаків!")
sykhiv.set_character(student)

reisa = smart_blykachka.Item("шматок рейси")
reisa.set_description("Металевий брусок, який приносить велику біль, коли падає на ногу")
levandivka.set_item(reisa)

hlib = smart_blykachka.Item("булка хліба")
hlib.set_description("Продукт, що може відвернути увагу")
india.set_item(hlib)

# symochka = smart_blykachka.Item("Сумочка")
# symochka.set_description("Торбинка, яка дуже файно може прилетіти в потилицю")
# center.set_item(symochka)

lopata = smart_blykachka.Item("лопата")
lopata.set_description("Предмет для сільського господарства")
kryvchytsi.set_item(lopata)


balonchyk = smart_blykachka.Item("балончик")
balonchyk.set_description("Невелика баночка з отруйним розчином.")
sykhiv.set_item(balonchyk)

current_room = center
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "захід", "схід"]:
        # Рухатися в заданому напрямку
        current_room = current_room.move(command)
    elif command == "говорити":
        # Поговоріть з жителем - перевірте, чи є він!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "битись":
        if isinstance(inhabitant, smart_blykachka.Enemy):
            if inhabitant is not None:
                # Бийтеся з жителем, якщо він є
                print("Що ти обереш для захисту?")
                fight_with = input()
                # Чи є у тебе ця річ?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # Що станеться, якщо ви виграєте?
                        print("Ура, ти переміг негідника!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 2:
                            print("Вітаємо, Ви перемогли ворогів!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Шкода, ти зазнав поразки")
                        print("Гра завершилась!")
                        dead = True
                else:
                    print("У тебе немає " + fight_with)
            else:
                print("Тут нема з ким воювати")
        else:
            print("Тут нема з ким воювати, це мирний житель")
    elif command == "отримати":
        if item is not None:
            print("Ти поклав " + item.get_name() + " у свій шопер")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Тут немає нічогісько!")
    else:
        print("Я не знаю, як пройти до " + command)