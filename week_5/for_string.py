#Kirjutage programm, mis käib läbi iga tähe sõnes ja prindib selle välja.

text = "C#"
for i in text:
        print(i)


#Kirjutage programm, mis prindib sõne tagurpidi (viimasest tähemärgist esimese juurde), nii et iga täht kuvatakse eraldi reale.

lenght = len(text)
print(lenght)

text = "Python"
for letter in range(len(text) - 1, -1, -1):
    print(text[letter])