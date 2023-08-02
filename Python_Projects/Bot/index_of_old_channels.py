    file = r

    entitis = file['message']['entities']
    text = file['message']['text']
    new_entitis = []
    for entiti in entitis:
        entiti['url'] = entiti['url'].replace('Natural_Sc','c/1825638032')
        new_entitis.append(entiti)



    bot.sendMessage(master_id,text,entities=new_entitis)
