total_expense = 0
    whatsapp_msgs=re.sub("\n","",whatsapp_msgs)
    x=re.findall("\d+",whatsapp_msgs)
    for i in x:
        total_expense=total_expense+int(i)
    return total_expense
s=""
    l=lines.split("\n")
    for i in l[:-1]:
        if len(i)==0:
            s=s+'\n'
            continue
        if i.strip()[0]=='#':
            continue
        else:
            s=s+i+"\n"
    return s