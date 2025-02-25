def family_members(**kwargs):
    for relacao, nome in kwargs.items():
        print(f"{relacao}: {nome}")

family_members(pai="Andre", mae="dekinha", irmao="dede", prima="deia")
